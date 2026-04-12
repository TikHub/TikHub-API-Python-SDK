"""Sync and async base clients.

These hold the httpx client and own the single ``_request`` method that
every resource calls. Resource methods never touch httpx directly.

The two classes are deliberate near-mirrors of each other. PLAN_V3.md §14
calls for an "async is source of truth" architecture with a generated sync
facade — that codegen lives in Phase 1. For Phase 0 we accept ~80 lines of
parallel code so the foundation is dead simple to read.
"""

from __future__ import annotations

import os
import time
from collections.abc import Mapping
from typing import Any, TypeVar

import anyio
import httpx

from tikhub._errors import (
    TikHubConfigError,
    TikHubError,
    TikHubHTTPError,
    TikHubRateLimitError,
    from_httpx_request_error,
    http_error_for_status,
)
from tikhub._logging import rate_limit_logger, requests_logger, retries_logger
from tikhub._rate_limit import parse_retry_after
from tikhub._retries import RetryPolicy
from tikhub._version import __version__

DEFAULT_BASE_URL = "https://api.tikhub.io"
DEFAULT_TIMEOUT = 30.0

_SyncSelf = TypeVar("_SyncSelf", bound="BaseClient")
_AsyncSelf = TypeVar("_AsyncSelf", bound="AsyncBaseClient")


def _resolve_api_key(explicit: str | None) -> str:
    if explicit:
        return explicit
    env = os.environ.get("TIKHUB_API_KEY")
    if env:
        return env
    raise TikHubConfigError(
        "No API key provided. Pass api_key= to TikHub(...) or set $TIKHUB_API_KEY."
    )


def _resolve_base_url(explicit: str | None) -> str:
    return (explicit or DEFAULT_BASE_URL).rstrip("/")


def _build_user_agent(explicit: str | None) -> str:
    if explicit:
        return explicit
    return f"tikhub-py/{__version__}"


def _raise_for_status(
    response: httpx.Response,
    *,
    method: str,
    url: str,
    params: Mapping[str, Any] | None,
    request_body: Any,
) -> None:
    """Translate a non-2xx response into the right :class:`TikHubHTTPError`."""
    if 200 <= response.status_code < 300:
        return

    # Decode the response body the same way for the exception as we would for
    # the success path, so users can inspect ``exc.response_body`` directly.
    try:
        body: Any = response.json()
    except Exception:
        body = response.text

    request_id = response.headers.get("x-request-id")
    exc_cls = http_error_for_status(response.status_code)

    kwargs: dict[str, Any] = {
        "status_code": response.status_code,
        "method": method,
        "url": url,
        "params": params,
        "request_body": request_body,
        "response_body": body,
        "request_id": request_id,
        "headers": dict(response.headers),
    }

    if exc_cls is TikHubRateLimitError:
        kwargs["retry_after"] = parse_retry_after(response.headers)

    raise exc_cls(_format_error_message(response, body), **kwargs)


def _format_error_message(response: httpx.Response, body: Any) -> str:
    if isinstance(body, dict):
        for key in ("message", "error", "detail", "msg"):
            value = body.get(key)
            if isinstance(value, str) and value:
                return value
    if isinstance(body, str) and body:
        return body[:500]
    return f"HTTP {response.status_code}"


# ---------------------------------------------------------------------------
# Sync
# ---------------------------------------------------------------------------


class BaseClient:
    """Synchronous base client. ``TikHub`` subclasses this and adds resources."""

    def __init__(
        self,
        api_key: str | None = None,
        *,
        timeout: float | None = DEFAULT_TIMEOUT,
        base_url: str | None = None,
        max_retries: int = 3,
        proxy: str | None = None,
        user_agent: str | None = None,
        parse_response: bool = True,
        http_client: httpx.Client | None = None,
        transport: httpx.BaseTransport | None = None,
    ) -> None:
        if http_client is not None and transport is not None:
            raise TikHubConfigError("Pass either http_client or transport, not both.")

        self._api_key = _resolve_api_key(api_key)
        self._base_url = _resolve_base_url(base_url)
        self._parse_response = parse_response
        self._retry_policy = RetryPolicy(max_retries=max_retries)
        self._auth_header = f"Bearer {self._api_key}"

        self._owns_client = http_client is None
        if http_client is not None:
            self._client = http_client
        else:
            self._client = httpx.Client(
                base_url=self._base_url,
                timeout=timeout,
                proxy=proxy,
                transport=transport,
                headers={
                    "User-Agent": _build_user_agent(user_agent),
                    "Accept": "application/json",
                },
            )

    # -- HTTP --

    def _request(
        self,
        method: str,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        json: Any = None,
        files: Mapping[str, Any] | None = None,
    ) -> Any:
        url = self._join(path)
        attempt = 0
        headers = {"Authorization": self._auth_header}
        while True:
            attempt += 1
            try:
                started = time.perf_counter()
                response = self._client.request(
                    method,
                    path,
                    params=params,
                    json=json if files is None else None,
                    files=files,
                    headers=headers,
                )
                duration = time.perf_counter() - started
                requests_logger.debug(
                    "%s %s -> %s (%.0f ms, request_id=%s)",
                    method,
                    url,
                    response.status_code,
                    duration * 1000,
                    response.headers.get("x-request-id"),
                )
                _raise_for_status(
                    response,
                    method=method,
                    url=url,
                    params=params,
                    request_body=json,
                )
                return self._decode(response)
            except httpx.RequestError as exc:
                error: TikHubError = from_httpx_request_error(exc)
            except TikHubHTTPError as exc:
                error = exc

            if not self._retry_policy.should_retry(error, attempt):
                raise error

            sleep = self._retry_policy.sleep_for(error, attempt)
            if isinstance(error, TikHubRateLimitError):
                rate_limit_logger.warning(
                    "Rate limited on %s %s — sleeping %.2fs (attempt %d/%d)",
                    method,
                    url,
                    sleep,
                    attempt,
                    self._retry_policy.max_retries,
                )
            else:
                retries_logger.info(
                    "Retrying %s %s in %.2fs (attempt %d/%d, reason: %s)",
                    method,
                    url,
                    sleep,
                    attempt,
                    self._retry_policy.max_retries,
                    type(error).__name__,
                )
            time.sleep(sleep)

    # -- helpers --

    def _join(self, path: str) -> str:
        if path.startswith(("http://", "https://")):
            return path
        if not path.startswith("/"):
            path = "/" + path
        return self._base_url + path

    def _decode(self, response: httpx.Response) -> Any:
        if not self._parse_response:
            return _safe_json(response)
        # Phase 0: pydantic models for individual resources are added per-tag.
        # The base client returns the parsed JSON; resource methods may further
        # convert into a typed model.
        return _safe_json(response)

    # -- lifecycle --

    def close(self) -> None:
        if self._owns_client and not self._client.is_closed:
            self._client.close()

    def __enter__(self: _SyncSelf) -> _SyncSelf:
        return self

    def __exit__(self, *exc: Any) -> None:
        self.close()


# ---------------------------------------------------------------------------
# Async
# ---------------------------------------------------------------------------


class AsyncBaseClient:
    """Asynchronous base client. ``AsyncTikHub`` subclasses this and adds resources."""

    def __init__(
        self,
        api_key: str | None = None,
        *,
        timeout: float | None = DEFAULT_TIMEOUT,
        base_url: str | None = None,
        max_retries: int = 3,
        proxy: str | None = None,
        user_agent: str | None = None,
        parse_response: bool = True,
        http_client: httpx.AsyncClient | None = None,
        transport: httpx.AsyncBaseTransport | None = None,
    ) -> None:
        if http_client is not None and transport is not None:
            raise TikHubConfigError("Pass either http_client or transport, not both.")

        self._api_key = _resolve_api_key(api_key)
        self._base_url = _resolve_base_url(base_url)
        self._parse_response = parse_response
        self._retry_policy = RetryPolicy(max_retries=max_retries)
        self._auth_header = f"Bearer {self._api_key}"

        self._owns_client = http_client is None
        if http_client is not None:
            self._client = http_client
        else:
            self._client = httpx.AsyncClient(
                base_url=self._base_url,
                timeout=timeout,
                proxy=proxy,
                transport=transport,
                headers={
                    "User-Agent": _build_user_agent(user_agent),
                    "Accept": "application/json",
                },
            )

    async def _request(
        self,
        method: str,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        json: Any = None,
        files: Mapping[str, Any] | None = None,
    ) -> Any:
        url = self._join(path)
        attempt = 0
        headers = {"Authorization": self._auth_header}
        while True:
            attempt += 1
            try:
                started = time.perf_counter()
                response = await self._client.request(
                    method,
                    path,
                    params=params,
                    json=json if files is None else None,
                    files=files,
                    headers=headers,
                )
                duration = time.perf_counter() - started
                requests_logger.debug(
                    "%s %s -> %s (%.0f ms, request_id=%s)",
                    method,
                    url,
                    response.status_code,
                    duration * 1000,
                    response.headers.get("x-request-id"),
                )
                _raise_for_status(
                    response,
                    method=method,
                    url=url,
                    params=params,
                    request_body=json,
                )
                return self._decode(response)
            except httpx.RequestError as exc:
                error: TikHubError = from_httpx_request_error(exc)
            except TikHubHTTPError as exc:
                error = exc

            if not self._retry_policy.should_retry(error, attempt):
                raise error

            sleep = self._retry_policy.sleep_for(error, attempt)
            if isinstance(error, TikHubRateLimitError):
                rate_limit_logger.warning(
                    "Rate limited on %s %s — sleeping %.2fs (attempt %d/%d)",
                    method,
                    url,
                    sleep,
                    attempt,
                    self._retry_policy.max_retries,
                )
            else:
                retries_logger.info(
                    "Retrying %s %s in %.2fs (attempt %d/%d, reason: %s)",
                    method,
                    url,
                    sleep,
                    attempt,
                    self._retry_policy.max_retries,
                    type(error).__name__,
                )
            await anyio.sleep(sleep)

    def _join(self, path: str) -> str:
        if path.startswith(("http://", "https://")):
            return path
        if not path.startswith("/"):
            path = "/" + path
        return self._base_url + path

    def _decode(self, response: httpx.Response) -> Any:
        if not self._parse_response:
            return _safe_json(response)
        return _safe_json(response)

    async def aclose(self) -> None:
        if self._owns_client and not self._client.is_closed:
            await self._client.aclose()

    async def __aenter__(self: _AsyncSelf) -> _AsyncSelf:
        return self

    async def __aexit__(self, *exc: Any) -> None:
        await self.aclose()


# ---------------------------------------------------------------------------

def _safe_json(response: httpx.Response) -> Any:
    """Decode JSON, falling back to text if the body isn't valid JSON."""
    try:
        return response.json()
    except Exception:
        return response.text


__all__ = [
    "DEFAULT_BASE_URL",
    "DEFAULT_TIMEOUT",
    "AsyncBaseClient",
    "BaseClient",
]
