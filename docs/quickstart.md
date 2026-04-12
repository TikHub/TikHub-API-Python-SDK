# Quickstart

A 5-minute tour of the `tikhub` SDK.

## Install

```bash
pip install tikhub
```

Requires Python 3.9+.

## Authenticate

Set your API key as an environment variable (recommended):

```bash
export TIKHUB_API_KEY="YOUR_API_KEY"
```

Or pass it explicitly:

```python
from tikhub import TikHub
client = TikHub(api_key="YOUR_API_KEY")
```

## Your first call

```python
from tikhub import TikHub

with TikHub() as client:
    health = client.health_check.check()
    print(health)
```

If your API key works, you'll see a JSON dict with `code: 200`.

## Calling a real endpoint

The SDK is mechanically derived from the TikHub OpenAPI spec. Every method
matches an endpoint exactly.

```python
with TikHub() as client:
    # GET /api/v1/douyin/web/fetch_one_video
    video = client.douyin_web.fetch_one_video(aweme_id="7251234567890123456")
    print(video)

    # GET /api/v1/tiktok/app/v3/handler_user_profile
    user = client.tiktok_app_v3.handler_user_profile(sec_user_id="MS4wLjA...")

    # POST /api/v1/douyin/search/fetch_video_search_v2
    results = client.douyin_search.fetch_video_search_v2(keyword="cats")
```

The two rules to remember:

1. **Resource attribute** = OpenAPI tag, lowercased, dashes → underscores, `-API` stripped.
2. **Method name** = the last segment of the path, verbatim.
3. **Parameter names** = the OpenAPI parameter names, verbatim.

If you can read the [TikHub API docs](https://docs.tikhub.io), you already know how to use the SDK.

## Async

Identical surface, just `await` everything:

```python
import asyncio
from tikhub import AsyncTikHub

async def main():
    async with AsyncTikHub() as client:
        video = await client.douyin_web.fetch_one_video(aweme_id="...")
        print(video)

asyncio.run(main())
```

## Errors

Every HTTP failure becomes a typed exception:

```python
from tikhub import TikHub, TikHubNotFoundError, TikHubRateLimitError

with TikHub() as client:
    try:
        client.douyin_web.fetch_one_video(aweme_id="invalid")
    except TikHubNotFoundError as exc:
        print("Not found:", exc.url, exc.response_body)
    except TikHubRateLimitError as exc:
        print(f"Slow down — retry after {exc.retry_after}s")
```

The full hierarchy is documented in [errors.md](errors.md).

## Pagination

List endpoints return a paginator. Iterate, take the first N, or drive
page-by-page:

```python
with TikHub() as client:
    pager = client.tiktok_app_v3.fetch_user_post_videos(sec_uid="MS4wLjA...")

    # iterate every video lazily
    for video in pager:
        print(video["aweme_id"])

    # or just the first 100
    first_100 = pager.first(100)
```

## Configuration

The constructor takes only the things you actually need:

```python
TikHub(
    api_key=None,         # str | None — defaults to $TIKHUB_API_KEY
    timeout=30,           # float | None — total request timeout in seconds
    base_url=None,        # str | None — only override for a private mirror
    max_retries=3,
    proxy=None,
    user_agent=None,
    parse_response=True,  # set False to receive raw dicts
    http_client=None,     # bring your own httpx.Client
    transport=None,       # bring your own httpx.BaseTransport (e.g. for tests)
)
```

That's the entire surface. There is no separate `ClientConfig` object.
