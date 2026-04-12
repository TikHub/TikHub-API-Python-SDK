# Async

The SDK is async-first. `AsyncTikHub` has the **same API surface** as `TikHub`, just with `await` in front of every method call.

## Basic use

```python
import asyncio
from tikhub import AsyncTikHub

async def main():
    async with AsyncTikHub(api_key="YOUR_API_KEY") as client:
        video = await client.douyin_web.fetch_one_video(aweme_id="7251...")
        print(video)

asyncio.run(main())
```

The async client **must** be used as a context manager (`async with`) so the underlying `httpx.AsyncClient` shuts down cleanly.

## Concurrent requests

The whole point of async is fanning out — fetch many endpoints in parallel:

```python
import asyncio
from tikhub import AsyncTikHub

async def main():
    async with AsyncTikHub() as client:
        ids = ["7251...", "7252...", "7253...", "7254..."]
        videos = await asyncio.gather(*[
            client.douyin_web.fetch_one_video(aweme_id=i) for i in ids
        ])
        for v in videos:
            print(v)

asyncio.run(main())
```

`httpx` pools connections automatically — there's no extra setup.

## Mixing sync code in an async context

If you accidentally call the sync `TikHub` inside an `async def`, the SDK detects the running loop and raises a clear error pointing you at `AsyncTikHub`. To use the synchronous client from inside an async function, run it in a thread:

```python
import anyio
from tikhub import TikHub

async def main():
    sync_client = TikHub(api_key="sk-...")
    video = await anyio.to_thread.run_sync(
        lambda: sync_client.douyin_web.fetch_one_video(aweme_id="...")
    )
```

But the cleaner choice is just to use `AsyncTikHub`.

## Lifecycle

| | Sync | Async |
|---|---|---|
| Construct | `TikHub(api_key=...)` | `AsyncTikHub(api_key=...)` |
| Recommended | `with TikHub() as c:` | `async with AsyncTikHub() as c:` |
| Explicit close | `client.close()` | `await client.aclose()` |
