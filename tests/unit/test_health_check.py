"""End-to-end test of the foundation: ``client.health_check.check()``.

Uses ``httpx.MockTransport`` to fake the network — no real HTTP, no recorded
cassettes. The point is to prove the wiring (auth → request → decode →
return) works for both sync and async clients.
"""

from __future__ import annotations

import json

import httpx

from tikhub import AsyncTikHub, TikHub


def _ok_handler(request: httpx.Request) -> httpx.Response:
    assert request.method == "GET"
    assert request.url.path == "/api/v1/health/check"
    assert request.headers["authorization"] == "Bearer sk-test"
    return httpx.Response(
        200,
        content=json.dumps({"code": 200, "data": {"status": "ok"}}).encode(),
        headers={"content-type": "application/json", "x-request-id": "req-123"},
    )


def test_sync_health_check():
    with TikHub(
        api_key="sk-test", transport=httpx.MockTransport(_ok_handler)
    ) as client:
        result = client.health_check.check()
    assert result == {"code": 200, "data": {"status": "ok"}}


async def test_async_health_check():
    async with AsyncTikHub(
        api_key="sk-test", transport=httpx.MockTransport(_ok_handler)
    ) as client:
        result = await client.health_check.check()
    assert result == {"code": 200, "data": {"status": "ok"}}


def test_user_agent_header_set_by_default():
    seen: dict[str, str] = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["user-agent"] = request.headers.get("user-agent", "")
        return httpx.Response(200, json={"ok": True})

    with TikHub(api_key="sk-test", transport=httpx.MockTransport(handler)) as client:
        client.health_check.check()
    assert seen["user-agent"].startswith("tikhub-py/")


def test_custom_user_agent():
    seen: dict[str, str] = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["user-agent"] = request.headers.get("user-agent", "")
        return httpx.Response(200, json={"ok": True})

    with TikHub(
        api_key="sk-test",
        user_agent="my-app/1.2.3",
        transport=httpx.MockTransport(handler),
    ) as client:
        client.health_check.check()
    assert seen["user-agent"] == "my-app/1.2.3"
