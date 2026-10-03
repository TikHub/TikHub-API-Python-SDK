# Examples

Runnable example scripts for every resource in the SDK.

## Quickstart

Set your API key and run any example:

```bash
export TIKHUB_API_KEY="YOUR_API_KEY"

python examples/health_check.py        # smallest possible call
python examples/quickstart.py          # 4 useful endpoints, hand-written
python examples/douyin_web.py          # all 55 Douyin web endpoints
python examples/tiktok_app_v3.py       # all 58 TikTok app endpoints
```

Every script is **fully self-contained** — you can copy any one file out of
the repo and run it with just `pip install tikhub`.

## What's in each file

Every per-resource file:

1. Imports `TikHub` and `TikHubError`.
2. Defines a tiny `demo()` helper that calls one endpoint, prints a
   truncated JSON response, and continues on error.
3. Calls every endpoint on that resource using the example values from
   `spec/openapi.json`.

```python
# excerpt from examples/douyin_web.py
def main() -> None:
    with TikHub() as client:  # reads $TIKHUB_API_KEY

        # GET /api/v1/douyin/web/fetch_one_video
        # 获取单个作品数据/Get single video data
        demo("fetch_one_video", lambda: client.douyin_web.fetch_one_video(aweme_id="..."))

        # POST /api/v1/douyin/web/fetch_multi_video
        # 批量获取视频信息/Batch Get Video Information
        demo("fetch_multi_video", lambda: client.douyin_web.fetch_multi_video(body=[]))

        # ... and 66 more
```

## Resource files (51)

All names match the SDK attribute on `client.*`. Endpoint counts in parentheses.

| Platform | File(s) |
|---|---|
| **Douyin** | [`douyin_web.py`](douyin_web.py) (55) · [`douyin_app_v3.py`](douyin_app_v3.py) (38) · [`douyin_search.py`](douyin_search.py) (23) · [`douyin_billboard.py`](douyin_billboard.py) (31) · [`douyin_creator.py`](douyin_creator.py) (17) · [`douyin_creator_v2.py`](douyin_creator_v2.py) (14) · [`douyin_xingtu.py`](douyin_xingtu.py) (23) · [`douyin_xingtu_v2.py`](douyin_xingtu_v2.py) (50) · [`douyin_index.py`](douyin_index.py) (51) · [`douyin_douplus.py`](douyin_douplus.py) (17) |
| **TikTok** | [`tiktok_web.py`](tiktok_web.py) (58) · [`tiktok_app_v3.py`](tiktok_app_v3.py) (58) · [`tiktok_creator.py`](tiktok_creator.py) (14) · [`tiktok_analytics.py`](tiktok_analytics.py) (4) · [`tiktok_ads.py`](tiktok_ads.py) (16) · [`tiktok_shop_web.py`](tiktok_shop_web.py) (12) |
| **Xiaohongshu** | [`xiaohongshu_web_v3.py`](xiaohongshu_web_v3.py) (5) · [`xiaohongshu_app_v2.py`](xiaohongshu_app_v2.py) (20) · [`xiaohongshu_pgy.py`](xiaohongshu_pgy.py) (20) |
| **Bilibili** | [`bilibili_web.py`](bilibili_web.py) (31) · [`bilibili_app.py`](bilibili_app.py) (11) · [`bilibili_huahuo.py`](bilibili_huahuo.py) (45) |
| **Kuaishou** | [`kuaishou_web.py`](kuaishou_web.py) (12) · [`kuaishou_app.py`](kuaishou_app.py) (26) |
| **Weibo** | [`weibo_web_v2.py`](weibo_web_v2.py) (33) · [`weibo_app.py`](weibo_app.py) (23) |
| **WeChat** | [`wechat_channels_v2.py`](wechat_channels_v2.py) (12) · [`wechat_media_platform_v2.py`](wechat_media_platform_v2.py) (11) · [`wechat_search_v2.py`](wechat_search_v2.py) (2) |
| **Zhihu** | [`zhihu_web.py`](zhihu_web.py) (41) |
| **Toutiao** | [`toutiao_web.py`](toutiao_web.py) (2) · [`toutiao_app.py`](toutiao_app.py) (5) |
| **Xigua** | [`xigua_app_v2.py`](xigua_app_v2.py) (7) |
| **PiPiXia** | [`pipixia_app.py`](pipixia_app.py) (17) |
| **Lemon8** | [`lemon8_app.py`](lemon8_app.py) (16) |
| **Instagram** | [`instagram_v1.py`](instagram_v1.py) (29) · [`instagram_v2.py`](instagram_v2.py) (27) · [`instagram_v3.py`](instagram_v3.py) (37) |
| **YouTube** | [`youtube_web.py`](youtube_web.py) (8) · [`youtube_web_v2.py`](youtube_web_v2.py) (26) |
| **Twitter / X** | [`twitter_web.py`](twitter_web.py) (25) |
| **Threads** | [`threads_web.py`](threads_web.py) (12) |
| **Reddit** | [`reddit_app.py`](reddit_app.py) (28) |
| **LinkedIn** | [`linkedin_web_v2.py`](linkedin_web_v2.py) (8) |
| **Telegram** | [`telegram_web.py`](telegram_web.py) (7) |
| **Utility** | [`hybrid_parsing.py`](hybrid_parsing.py) (1) · [`tikhub_user.py`](tikhub_user.py) (6) · [`tikhub_downloader.py`](tikhub_downloader.py) (2) · [`ios_shortcut.py`](ios_shortcut.py) (1) · [`health_check.py`](health_check.py) (2) · [`demo.py`](demo.py) (9) |

**Total:** 51 resource files, 1048 demo calls.

## What's NOT in here

- **Deprecated endpoints** — operations marked `deprecated` in the upstream spec are not exposed by the SDK, so they have no examples either.

## Heads up

- Many calls will return **HTTP 400 with "Request failed. Please retry"** — that's TikHub's generic upstream error when the spec's `example` value (e.g. an aweme_id, note_id, share URL) has gone stale on the upstream platform. The SDK is wired correctly; the example value just no longer points at a real piece of content. Replace the value in the call with a real one and try again.
- Each demo call **costs API quota**. The largest file (`tiktok_app_v3.py`) makes 75 calls; the smallest makes 1.
- The `demo()` helper truncates responses to 600 chars. To see the full payload, replace `demo(...)` with a direct `client.<resource>.<method>(...)` call.

## Regenerating

If TikHub publishes a new spec version, refresh everything in three commands:

```bash
python scripts/refresh_spec.py        # pulls latest openapi.json
python scripts/generate_resources.py  # rewrites src/tikhub/resources/*.py
python scripts/generate_examples.py   # rewrites this directory
```
