"""Retry-policy tests."""

from __future__ import annotations

import json
from itertools import count

import httpx
import pytest

from tikhub import (
    TikHub,
    TikHubBadRequestError,
    TikHubRateLimitError,
    TikHubServerError,
)
from tikhub._retries import RetryPolicy


def test_retry_policy_should_retry_5xx():
    pol = RetryPolicy(max_retries=3)
    exc = TikHubServerError("boom", status_code=500, method="GET", url="x")
    assert pol.should_retry(exc, attempt=1)
    assert pol.should_retry(exc, attempt=2)
    assert not pol.should_retry(exc, attempt=3)


def test_retry_policy_uses_retry_after_when_present():
    pol = RetryPolicy(max_retries=3, jitter=0)
    exc = TikHubRateLimitError(
        "rate limited", status_code=429, method="GET", url="x", retry_after=12.0
    )
    assert pol.sleep_for(exc, attempt=1) == 12.0


def test_retry_policy_exponential_backoff():
    pol = RetryPolicy(max_retries=5, backoff_base=1.0, backoff_max=100.0, jitter=0)
    exc = TikHubServerError("boom", status_code=500, method="GET", url="x")
    assert pol.sleep_for(exc, attempt=1) == 1.0
    assert pol.sleep_for(exc, attempt=2) == 2.0
    assert pol.sleep_for(exc, attempt=3) == 4.0


def test_retry_policy_caps_at_backoff_max():
    pol = RetryPolicy(max_retries=10, backoff_base=1.0, backoff_max=5.0, jitter=0)
    exc = TikHubServerError("boom", status_code=500, method="GET", url="x")
    assert pol.sleep_for(exc, attempt=10) == 5.0


def test_client_retries_on_5xx_then_succeeds(monkeypatch: pytest.MonkeyPatch):
    """Two 500s, then 200 — the call should succeed after two retries."""
    # Skip the actual sleeping so the test runs in milliseconds.
    import tikhub._base_client as base_client

    monkeypatch.setattr(base_client.time, "sleep", lambda _s: None)

    counter = count(1)

    def handler(request: httpx.Request) -> httpx.Response:
        n = next(counter)
        if n < 3:
            return httpx.Response(500, json={"error": "down"})
        return httpx.Response(200, content=json.dumps({"ok": True}).encode())

    with TikHub(
        api_key="sk-test",
        transport=httpx.MockTransport(handler),
        max_retries=5,
    ) as client:
        result = client.health_check.check()

    assert result == {"ok": True}


def test_client_does_not_retry_on_400(monkeypatch: pytest.MonkeyPatch):
    import tikhub._base_client as base_client

    monkeypatch.setattr(base_client.time, "sleep", lambda _s: None)

    call_count = count(0)

    def handler(request: httpx.Request) -> httpx.Response:
        next(call_count)
        return httpx.Response(400, json={"error": "bad"})

    with TikHub(
        api_key="sk-test",
        transport=httpx.MockTransport(handler),
        max_retries=5,
    ) as client:
        with pytest.raises(TikHubBadRequestError):
            client.health_check.check()

    # Should have been called exactly once — no retries on a 400.
    # `count(0)` was advanced once by the handler, so its next value is 1.
    assert next(call_count) == 1
