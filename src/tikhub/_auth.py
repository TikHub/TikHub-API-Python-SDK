"""Bearer-token authentication for the TikHub API."""

from __future__ import annotations

from collections.abc import Generator

import httpx


class BearerAuth(httpx.Auth):
    """Adds ``Authorization: Bearer <token>`` to every request.

    Implemented as an :class:`httpx.Auth` subclass so it composes naturally with
    everything else httpx does (retries, redirects, custom transports).
    """

    requires_request_body = False
    requires_response_body = False

    def __init__(self, token: str) -> None:
        if not token:
            raise ValueError("Bearer token must be a non-empty string.")
        self._token = token

    def auth_flow(
        self, request: httpx.Request
    ) -> Generator[httpx.Request, httpx.Response, None]:
        request.headers["Authorization"] = f"Bearer {self._token}"
        yield request
