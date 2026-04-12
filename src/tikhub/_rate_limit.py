"""Helpers for parsing TikHub rate-limit headers."""

from __future__ import annotations

import time
from collections.abc import Mapping


def parse_retry_after(headers: Mapping[str, str]) -> float | None:
    """Return the recommended sleep duration from rate-limit headers.

    Inspects ``Retry-After`` (per RFC 7231) and ``X-RateLimit-Reset``. Returns
    ``None`` if neither header is present or parseable.

    ``Retry-After`` may be an integer (seconds) or an HTTP date — we only
    handle the integer form, which is what TikHub sends in practice. For HTTP
    dates we fall back to ``None``.
    """
    retry_after = headers.get("retry-after") or headers.get("Retry-After")
    if retry_after:
        try:
            return max(0.0, float(retry_after))
        except (TypeError, ValueError):
            pass

    reset = headers.get("x-ratelimit-reset") or headers.get("X-RateLimit-Reset")
    if reset:
        try:
            reset_value = float(reset)
        except (TypeError, ValueError):
            return None
        # Heuristic: small values are "seconds from now", large values are unix
        # timestamps. The boundary at 10**9 is fine for any date after 2001.
        if reset_value > 10**9:
            return max(0.0, reset_value - time.time())
        return max(0.0, reset_value)

    return None
