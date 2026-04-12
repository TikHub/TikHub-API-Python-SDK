# Pagination

The SDK ships three paginator classes that cover every list-style endpoint in the spec:

| Pattern | Class | Used by |
|---|---|---|
| `cursor` / `max_cursor` + `has_more` | `CursorPaginator` | Most Douyin and TikTok user-content listings |
| `page` + `count` | `PagePaginator` | TikTok web search, Bilibili comments |
| `offset` + `limit` | `OffsetPaginator` | Some Instagram and Reddit feeds |

All three implement both **sync iteration** and **async iteration** with the same surface.

## Iterating

```python
from tikhub import TikHub

with TikHub() as client:
    pager = client.tiktok_app_v3.fetch_user_post_videos(sec_uid="MS4wLjA...")

    # Lazy iteration — fetches pages on demand.
    for video in pager:
        print(video["aweme_id"])
```

## Limiting how much you fetch

```python
first_50 = pager.first(50)              # eager, capped at 50 items
```

## Page-by-page

```python
pager = client.tiktok_app_v3.fetch_user_post_videos(sec_uid="MS4wLjA...")
page = pager.next_page()
print(pager.cursor, pager.has_more)
```

## Async

```python
import asyncio
from tikhub import AsyncTikHub

async def main():
    async with AsyncTikHub() as client:
        pager = client.tiktok_app_v3.fetch_user_post_videos(sec_uid="...")

        async for video in pager:
            print(video["aweme_id"])

        first_100 = await pager.afirst(100)

asyncio.run(main())
```

## How the SDK detects paginated endpoints

The codegen marks any endpoint whose query parameters include `cursor`, `max_cursor`, `page`, or `offset` AND whose summary suggests a list. The wrapper paginator inspects the upstream response keys (`has_more`, `next_cursor`, etc.) automatically.

If you hit an endpoint that the SDK didn't detect as paginated but should be, please [open an issue](https://github.com/TikHub/TikHub-API-Python-SDK-V2/issues) — we'll add it.
