"""Smoke tests for the generated resource layer.

These tests prove the codegen produces a working SDK without making any
real network calls. They use ``httpx.MockTransport`` to capture each
outgoing request and assert that the right method, path, params, and
JSON body are produced.
"""

from __future__ import annotations

import json

import httpx
import pytest

from tikhub import AsyncTikHub, TikHub

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _capture_handler() -> tuple[list[httpx.Request], httpx.MockTransport]:
    captured: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        captured.append(request)
        return httpx.Response(200, json={"code": 200, "data": {}})

    return captured, httpx.MockTransport(handler)


def _async_capture_handler() -> tuple[list[httpx.Request], httpx.MockTransport]:
    captured: list[httpx.Request] = []

    async def handler(request: httpx.Request) -> httpx.Response:
        captured.append(request)
        return httpx.Response(200, json={"code": 200, "data": {}})

    return captured, httpx.MockTransport(handler)


# ---------------------------------------------------------------------------
# Resource attribute presence
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "attr",
    [
        "douyin_web",
        "douyin_app_v3",
        "douyin_search",
        "douyin_billboard",
        "douyin_creator",
        "douyin_creator_v2",
        "douyin_xingtu",
        "douyin_xingtu_v2",
        "tiktok_web",
        "tiktok_app_v3",
        "tiktok_creator",
        "tiktok_analytics",
        "tiktok_ads",
        "tiktok_shop_web",
        "tiktok_interaction",
        "xiaohongshu_web",
        "xiaohongshu_web_v2",
        "xiaohongshu_web_v3",
        "xiaohongshu_app",
        "xiaohongshu_app_v2",
        "lemon8_app",
        "bilibili_web",
        "bilibili_app",
        "sora2",
        "kuaishou_web",
        "kuaishou_app",
        "pipixia_app",
        "weibo_web",
        "weibo_web_v2",
        "weibo_app",
        "wechat_channels",
        "wechat_media_platform_web",
        "instagram_v1",
        "instagram_v2",
        "instagram_v3",
        "youtube_web",
        "youtube_web_v2",
        "twitter_web",
        "threads_web",
        "reddit_app",
        "linkedin_web",
        "zhihu_web",
        "toutiao_web",
        "toutiao_app",
        "xigua_app_v2",
        "hybrid_parsing",
        "tikhub_user",
        "tikhub_downloader",
        "temp_mail",
        "ios_shortcut",
        "health_check",
        "demo",
    ],
)
def test_resource_attribute_present(attr: str):
    """Every OpenAPI tag is exposed as a flat client attribute."""
    with TikHub(api_key="sk-test") as client:
        assert hasattr(client, attr), f"Missing resource: {attr}"


def test_total_endpoint_count():
    """We expose exactly 1010 callable methods across all resources."""
    with TikHub(api_key="sk-test") as client:
        total = 0
        for attr in dir(client):
            if attr.startswith("_"):
                continue
            obj = getattr(client, attr)
            if obj is client or not hasattr(obj, "__class__"):
                continue
            for name in dir(obj):
                if name.startswith("_"):
                    continue
                if callable(getattr(obj, name, None)):
                    total += 1
    assert total == 1010, f"expected 1010, got {total}"


# ---------------------------------------------------------------------------
# Method dispatch — verifies the codegen wires up the right HTTP call
# ---------------------------------------------------------------------------


def test_get_with_query_params_drops_none():
    captured, transport = _capture_handler()
    with TikHub(api_key="sk-test", transport=transport) as client:
        client.douyin_web.fetch_one_video(aweme_id="123")
    req = captured[0]
    assert req.method == "GET"
    assert req.url.path == "/api/v1/douyin/web/fetch_one_video"
    # need_anchor_info defaulted to None — should not be in the query string
    assert dict(req.url.params) == {"aweme_id": "123"}


def test_get_with_optional_param_included_when_set():
    captured, transport = _capture_handler()
    with TikHub(api_key="sk-test", transport=transport) as client:
        client.douyin_web.fetch_one_video(aweme_id="123", need_anchor_info=True)
    req = captured[0]
    assert dict(req.url.params) == {"aweme_id": "123", "need_anchor_info": "true"}


def test_post_with_json_body_props():
    captured, transport = _capture_handler()
    with TikHub(api_key="sk-test", transport=transport) as client:
        client.douyin_search.fetch_video_search_v2(keyword="cats", cursor=20)
    req = captured[0]
    assert req.method == "POST"
    assert req.url.path == "/api/v1/douyin/search/fetch_video_search_v2"
    body = json.loads(req.content.decode())
    assert body == {"keyword": "cats", "cursor": 20}  # publish_time/etc dropped


def test_post_with_array_body():
    captured, transport = _capture_handler()
    with TikHub(api_key="sk-test", transport=transport) as client:
        client.douyin_web.fetch_multi_video(body=["7251", "7252", "7253"])
    req = captured[0]
    assert req.method == "POST"
    assert req.url.path == "/api/v1/douyin/web/fetch_multi_video"
    assert json.loads(req.content.decode()) == ["7251", "7252", "7253"]


def test_authorization_header_on_every_call():
    captured, transport = _capture_handler()
    with TikHub(api_key="sk-test-12345", transport=transport) as client:
        client.health_check.check()
        client.douyin_web.fetch_one_video(aweme_id="x")
        client.tiktok_web.fetch_user_profile(uniqueId="charlidamelio")
    for req in captured:
        assert req.headers["authorization"] == "Bearer sk-test-12345"


# ---------------------------------------------------------------------------
# Async surface
# ---------------------------------------------------------------------------


async def test_async_get_with_query_params():
    captured, transport = _async_capture_handler()
    async with AsyncTikHub(api_key="sk-test", transport=transport) as client:
        await client.douyin_web.fetch_one_video(aweme_id="abc", need_anchor_info=False)
    req = captured[0]
    assert req.method == "GET"
    assert dict(req.url.params) == {"aweme_id": "abc", "need_anchor_info": "false"}


async def test_async_post_with_json_body():
    captured, transport = _async_capture_handler()
    async with AsyncTikHub(api_key="sk-test", transport=transport) as client:
        await client.douyin_search.fetch_general_search_v2(keyword="taylor swift")
    req = captured[0]
    assert req.method == "POST"
    body = json.loads(req.content.decode())
    assert body["keyword"] == "taylor swift"


async def test_async_method_signatures_match_sync():
    """Sync and async clients must expose the same resources, each with the
    same method names. The only legitimate divergence is the lifecycle pair
    ``close`` (sync) vs ``aclose`` (async), which lives on the client itself.
    """
    sync_client = TikHub(api_key="sk-test")
    async_client = AsyncTikHub(api_key="sk-test")
    try:
        client_only = {"close", "aclose"}
        for attr in dir(sync_client):
            if attr.startswith("_") or attr in client_only:
                continue
            sync_obj = getattr(sync_client, attr)
            # Skip plain methods on the client itself; we only care about resources.
            if not hasattr(sync_obj, "_client"):
                continue
            async_obj = getattr(async_client, attr, None)
            assert async_obj is not None, f"Async client missing resource {attr}"
            sync_methods = {
                m for m in dir(sync_obj)
                if not m.startswith("_") and callable(getattr(sync_obj, m, None))
            }
            async_methods = {
                m for m in dir(async_obj)
                if not m.startswith("_") and callable(getattr(async_obj, m, None))
            }
            assert sync_methods == async_methods, (
                f"{attr}: signature drift\n  sync only: {sync_methods - async_methods}\n  async only: {async_methods - sync_methods}"
            )
    finally:
        sync_client.close()
        await async_client.aclose()
