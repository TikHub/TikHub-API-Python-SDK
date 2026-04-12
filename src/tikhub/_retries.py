"""Retry policy.

We retry on transient failures only:

- ``TikHubConnectionError`` (network errors, timeouts, proxy issues)
- ``TikHubServerError`` / ``TikHubUpstreamError`` (5xx)
- ``TikHubRateLimitError`` (429) — sleeps for ``retry_after`` if available

We do **not** retry on 4xx (other than 429), validation errors, or anything
the user explicitly aborted.
"""

from __future__ import annotations

import random
from dataclasses import dataclass

from tikhub._errors import (
    TikHubConnectionError,
    TikHubError,
    TikHubRateLimitError,
    TikHubServerError,
    TikHubUpstreamError,
)


@dataclass(frozen=True)
class RetryPolicy:
    """Exponential-backoff retry policy.

    Sleep before attempt ``n`` (1-indexed) is::

        min(backoff_max, backoff_base * 2**(n - 1)) * jitter
    """

    max_retries: int = 3
    backoff_base: float = 0.5
    backoff_max: float = 30.0
    jitter: float = 0.25
    """Multiplicative jitter — actual sleep is multiplied by ``[1 - j, 1 + j]``."""

    def should_retry(self, exc: BaseException, attempt: int) -> bool:
        """Return ``True`` if ``exc`` is retryable and we have attempts left."""
        if attempt >= self.max_retries:
            return False
        return isinstance(
            exc,
            (
                TikHubConnectionError,
                TikHubServerError,
                TikHubUpstreamError,
                TikHubRateLimitError,
            ),
        )

    def sleep_for(self, exc: BaseException, attempt: int) -> float:
        """Compute the sleep duration before the next retry.

        Honours ``retry_after`` from rate-limit errors when present.
        """
        if isinstance(exc, TikHubRateLimitError) and exc.retry_after is not None:
            return max(0.0, exc.retry_after)
        if not isinstance(exc, TikHubError):
            return 0.0
        raw_delay: float = self.backoff_base * (2 ** (attempt - 1))
        delay: float = min(self.backoff_max, raw_delay)
        if self.jitter:
            spread = self.jitter * delay
            delay = delay + float(random.uniform(-spread, spread))
        return max(0.0, delay)
