"""Status-code → exception class mapping tests."""

from __future__ import annotations

import json

import httpx
import pytest

from tikhub import (
    TikHub,
    TikHubAuthError,
    TikHubBadRequestError,
    TikHubError,
    TikHubHTTPError,
    TikHubNotFoundError,
    TikHubPermissionError,
    TikHubRateLimitError,
    TikHubServerError,
    TikHubUpstreamError,
)
from tikhub._errors import http_error_for_status


def _client_returning(status: int, *, body: object = None, headers: dict[str, str] | None = None) -> TikHub:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            status,
            content=json.dumps(body or {"error": "boom"}).encode(),
            headers={**{"content-type": "application/json"}, **(headers or {})},
        )

    return TikHub(
        api_key="sk-test",
        transport=httpx.MockTransport(handler),
        max_retries=0,
    )


@pytest.mark.parametrize(
    "status,exc_cls",
    [
        (400, TikHubBadRequestError),
        (401, TikHubAuthError),
        (403, TikHubPermissionError),
        (404, TikHubNotFoundError),
        (422, TikHubBadRequestError),
        (429, TikHubRateLimitError),
        (500, TikHubServerError),
        (502, TikHubUpstreamError),
        (503, TikHubUpstreamError),
        (504, TikHubUpstreamError),
        (599, TikHubServerError),
    ],
)
def test_status_maps_to_exception(status: int, exc_cls: type[TikHubHTTPError]):
    assert http_error_for_status(status) is exc_cls


def test_400_raises_with_url_and_body():
    with _client_returning(400, body={"message": "bad aweme_id"}) as client:
        with pytest.raises(TikHubBadRequestError) as ei:
            client.health_check.check()
    exc = ei.value
    assert exc.status_code == 400
    assert exc.method == "GET"
    assert exc.url.endswith("/api/v1/health/check")
    assert exc.response_body == {"message": "bad aweme_id"}
    assert "bad aweme_id" in str(exc)


def test_401_raises_auth_error():
    with _client_returning(401) as client:
        with pytest.raises(TikHubAuthError):
            client.health_check.check()


def test_429_carries_retry_after():
    with _client_returning(429, headers={"retry-after": "7"}) as client:
        with pytest.raises(TikHubRateLimitError) as ei:
            client.health_check.check()
    assert ei.value.retry_after == 7.0


def test_authorization_header_redacted_in_exception():
    with _client_returning(500) as client:
        with pytest.raises(TikHubServerError) as ei:
            client.health_check.check()
    # The auth header is added by httpx auth flow, so the exception's headers
    # come from the *response* — it just shouldn't ever leak a Bearer token.
    for k, v in ei.value.headers.items():
        if k.lower() == "authorization":
            assert v == "***"
    assert "sk-test" not in repr(ei.value)


def test_all_specific_errors_inherit_from_base():
    for cls in (
        TikHubAuthError,
        TikHubBadRequestError,
        TikHubNotFoundError,
        TikHubPermissionError,
        TikHubRateLimitError,
        TikHubServerError,
        TikHubUpstreamError,
    ):
        assert issubclass(cls, TikHubHTTPError)
        assert issubclass(cls, TikHubError)
