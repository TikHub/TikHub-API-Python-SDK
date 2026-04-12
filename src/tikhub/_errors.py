"""Exception hierarchy for the TikHub SDK.

See PLAN_V3.md §10. Every HTTP failure becomes a typed exception that carries
enough context (URL, params, body, request id) to debug without re-running
the request.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

import httpx

__all__ = [
    "TikHubAuthError",
    "TikHubBadRequestError",
    "TikHubConfigError",
    "TikHubConnectionError",
    "TikHubError",
    "TikHubFeatureRemovedError",
    "TikHubHTTPError",
    "TikHubNotFoundError",
    "TikHubPermissionError",
    "TikHubProxyError",
    "TikHubRateLimitError",
    "TikHubServerError",
    "TikHubTimeoutError",
    "TikHubUpstreamError",
    "TikHubValidationError",
]


_REDACT = "***"


def _redact_headers(headers: Mapping[str, str] | None) -> dict[str, str]:
    if not headers:
        return {}
    return {
        k: (_REDACT if k.lower() == "authorization" else v) for k, v in headers.items()
    }


class TikHubError(Exception):
    """Base class for every error raised by the SDK."""


class TikHubConfigError(TikHubError):
    """Configuration is invalid (missing API key, bad base URL, etc.)."""


class TikHubConnectionError(TikHubError):
    """Network failure before any HTTP response was received."""

    def __init__(self, message: str, *, cause: BaseException | None = None) -> None:
        super().__init__(message)
        self.__cause__ = cause


class TikHubTimeoutError(TikHubConnectionError):
    """Timed out waiting for a response."""


class TikHubProxyError(TikHubConnectionError):
    """Proxy could not be contacted or rejected the request."""


class TikHubHTTPError(TikHubError):
    """The server returned a non-2xx response.

    Carries everything you need to debug a failed request without re-running it.
    """

    def __init__(
        self,
        message: str,
        *,
        status_code: int,
        method: str,
        url: str,
        params: Mapping[str, Any] | None = None,
        request_body: Any = None,
        response_body: Any = None,
        request_id: str | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.method = method
        self.url = url
        self.params: dict[str, Any] = dict(params) if params else {}
        self.request_body = request_body
        self.response_body = response_body
        self.request_id = request_id
        self.headers: dict[str, str] = _redact_headers(headers)

    def __str__(self) -> str:
        rid = f" request_id={self.request_id}" if self.request_id else ""
        return f"{self.status_code} {self.method} {self.url}{rid}: {self.args[0]}"

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}("
            f"status_code={self.status_code}, "
            f"method={self.method!r}, "
            f"url={self.url!r}, "
            f"params={self.params!r}, "
            f"request_body={self.request_body!r}, "
            f"response_body={self.response_body!r}, "
            f"request_id={self.request_id!r}, "
            f"headers={self.headers!r}"
            ")"
        )


class TikHubBadRequestError(TikHubHTTPError):
    """400 / 422 — caller sent something the API rejected."""


class TikHubAuthError(TikHubHTTPError):
    """401 — missing, malformed, or invalid API key."""


class TikHubPermissionError(TikHubHTTPError):
    """403 — authenticated but not allowed (out of quota, scope missing, etc.)."""


class TikHubNotFoundError(TikHubHTTPError):
    """404 — endpoint or resource doesn't exist."""


class TikHubRateLimitError(TikHubHTTPError):
    """429 — rate limited. ``retry_after`` is the suggested sleep in seconds."""

    def __init__(self, *args: Any, retry_after: float | None = None, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.retry_after = retry_after


class TikHubServerError(TikHubHTTPError):
    """5xx — TikHub had an internal failure."""


class TikHubUpstreamError(TikHubHTTPError):
    """502 / 503 / 504 indicating TikHub couldn't reach the underlying platform."""


class TikHubValidationError(TikHubError):
    """The response payload could not be parsed into the expected model."""

    def __init__(self, message: str, *, raw: Any = None, cause: BaseException | None = None) -> None:
        super().__init__(message)
        self.raw = raw
        if cause is not None:
            self.__cause__ = cause


class TikHubFeatureRemovedError(TikHubError):
    """Caller invoked a method whose backing endpoint has been removed from the spec."""


# ---------------------------------------------------------------------------
# Mapping helpers
# ---------------------------------------------------------------------------

_STATUS_MAP: dict[int, type[TikHubHTTPError]] = {
    400: TikHubBadRequestError,
    401: TikHubAuthError,
    403: TikHubPermissionError,
    404: TikHubNotFoundError,
    422: TikHubBadRequestError,
    429: TikHubRateLimitError,
}


def http_error_for_status(status: int) -> type[TikHubHTTPError]:
    """Return the exception subclass best matching ``status``."""
    if status in _STATUS_MAP:
        return _STATUS_MAP[status]
    if status in (502, 503, 504):
        return TikHubUpstreamError
    if 500 <= status < 600:
        return TikHubServerError
    return TikHubHTTPError


def from_httpx_request_error(exc: httpx.RequestError) -> TikHubConnectionError:
    """Translate an :mod:`httpx` low-level error into a SDK exception."""
    if isinstance(exc, httpx.TimeoutException):
        return TikHubTimeoutError(str(exc) or "Request timed out", cause=exc)
    if isinstance(exc, httpx.ProxyError):
        return TikHubProxyError(str(exc) or "Proxy error", cause=exc)
    return TikHubConnectionError(str(exc) or "Connection error", cause=exc)
