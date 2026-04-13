# TikHub API Python SDK

English | [中文](README_CN.md)

The official Python SDK for the [TikHub](https://tikhub.io) social media data API — a unified REST API that provides real-time access to **16+ social media platforms** including TikTok, Douyin, Instagram, YouTube, Twitter/X, Xiaohongshu (Red Note), Bilibili, Weibo, Threads, LinkedIn, Reddit, Kuaishou, WeChat, Lemon8, Zhihu, and more.

Built for developers, data scientists, and AI engineers who need structured social media data at scale — for **AI training**, **influencer analytics**, **trend monitoring**, **sentiment analysis**, **market research**, and **competitive intelligence**.

## Why TikHub?

- **1000+ endpoints** across 16 platforms through a single API key
- **Real-time data** — video details, user profiles, comments, search results, live streams, trending content, and e-commerce analytics
- **RESTful & OpenAPI-native** — every endpoint is documented in the [OpenAPI spec](https://api.tikhub.io/openapi.json) and testable via [Swagger UI](https://api.tikhub.io)
- **MCP integration** — connect AI agents (Claude, LangChain, Coze, n8n) directly to social media data via [Model Context Protocol](https://tikhub.io)
- **Datasets available** — 1B+ pre-collected, structured records for training and research

## Why This SDK?

- **100% endpoint coverage** — 1010 / 1010 endpoints from OpenAPI spec V5.3.2, mechanically generated and verified
- **Sync + async** — `TikHub` and `AsyncTikHub` clients with identical APIs
- **Production-ready** — automatic retries with exponential backoff, rate-limit handling, structured error hierarchy with full debugging context
- **Type-safe** — `mypy --strict` clean, built on `httpx` + `pydantic v2`
- **Zero config** — flat kwargs, no config objects; set one env var and go

> **Version:** `2.1.1` — Requires Python 3.9+

## Supported Platforms

| Platform | Resource | Endpoints |
|---|---|---|
| TikTok | `tiktok_web`, `tiktok_app_v3`, `tiktok_creator`, `tiktok_analytics`, `tiktok_ads`, `tiktok_shop_web` | 200+ |
| Douyin | `douyin_web`, `douyin_app_v3`, `douyin_search`, `douyin_billboard`, `douyin_creator`, `douyin_xingtu` | 400+ |
| Instagram | `instagram_v1`, `instagram_v2`, `instagram_v3` | 80+ |
| YouTube | `youtube_web`, `youtube_web_v2` | 50+ |
| Twitter / X | `twitter_web` | 13+ |
| Xiaohongshu (Red Note) | `xiaohongshu_web`, `xiaohongshu_app` (+ v2/v3 variants) | 80+ |
| Bilibili | `bilibili_web`, `bilibili_app` | 40+ |
| Weibo | `weibo_web`, `weibo_web_v2`, `weibo_app` | 30+ |
| Threads | `threads_web` | 10+ |
| LinkedIn | `linkedin_web` | 10+ |
| Reddit | `reddit_app` | 10+ |
| Kuaishou | `kuaishou_web`, `kuaishou_app` | 20+ |
| WeChat | `wechat_channels`, `wechat_media_platform_web` | 20+ |
| Lemon8 | `lemon8_app` | 10+ |
| Zhihu | `zhihu_web` | 30+ |
| Others | `toutiao_web`, `toutiao_app`, `xigua_app_v2`, `pipixia_app`, `sora2` | 30+ |

## Install

```bash
pip install tikhub
```

Requires Python 3.9+.

### From source

```bash
git clone https://github.com/TikHub/TikHub-API-Python-SDK.git
cd TikHub-API-Python-SDK
pip install -e ".[dev]"
pytest -q
```

## Get your API Key

1. Go to [https://user.tikhub.io/login](https://user.tikhub.io/login) and sign up / log in.
2. Copy your API key from the dashboard.
3. Set it as an environment variable or pass it directly:

```bash
export TIKHUB_API_KEY="YOUR_API_KEY"
```

## Quickstart

```python
from tikhub import TikHub

client = TikHub(api_key="YOUR_API_KEY")

# 1:1 with the OpenAPI spec — resource = tag, method = path basename
video = client.douyin_web.fetch_one_video(aweme_id="7251234567890123456")
print(video.aweme_detail.desc)

client.close()
```

Or with the recommended context manager:

```python
with TikHub(api_key="YOUR_API_KEY") as client:
    health = client.health_check.check()
    print(health.status)
```

## Async

```python
import asyncio
from tikhub import AsyncTikHub

async def main():
    async with AsyncTikHub(api_key="YOUR_API_KEY") as client:
        video = await client.douyin_web.fetch_one_video(aweme_id="...")
        print(video.aweme_detail.desc)

asyncio.run(main())
```

## Configuration

The constructor takes one required argument and a small handful of optional kwargs:

```python
TikHub(
    api_key=None,        # str | None — defaults to $TIKHUB_API_KEY
    timeout=30,          # float | None — total request timeout in seconds
    base_url=None,       # str | None — only override for a private mirror

    # Advanced (rare):
    max_retries=3,
    proxy=None,
    user_agent=None,
    parse_response=True,
    http_client=None,    # bring your own httpx.Client
)
```

That's the entire configuration surface. There is no `ClientConfig` object — knobs are flat kwargs.

## Naming rules

The SDK is mechanically derived from the TikHub OpenAPI spec. Two rules:

1. **Resource attribute** = OpenAPI tag, lowercased, dashes → underscores, `-API` stripped.
   `Douyin-Web-API` → `client.douyin_web`. `TikTok-App-V3-API` → `client.tiktok_app_v3`.
2. **Method name** = the **last segment of the API path, verbatim**.
   `/api/v1/douyin/web/fetch_one_video` → `client.douyin_web.fetch_one_video(...)`.

Parameter names match the OpenAPI spec verbatim. If you can read the TikHub API docs, you already know how to use the SDK.

## Status

**100% endpoint coverage** against TikHub OpenAPI spec V5.3.2.

| | |
|---|---|
| Resources | **52** (one per OpenAPI tag) |
| Endpoints | **1010 / 1010** |
| Tests | 110 passing |
| Type-check | mypy `--strict` clean across 71 source files |
| Lint | ruff clean |

| Phase | Scope | State |
|---|---|---|
| 0 | Foundation: client, transport, errors, retries, pagination | ✅ done |
| 1 | Codegen pipeline (`scripts/refresh_spec.py`, `generate_resources.py`, `verify_coverage.py`) | ✅ done |
| 2 | Douyin + TikTok core (412 endpoints) | ✅ done |
| 3 | Other Chinese platforms (302 endpoints) | ✅ done |
| 4 | International platforms (234 endpoints) | ✅ done |
| 5 | TikTok specialty + utilities (94 endpoints) | ✅ done |
| 6 | Docs site, CLI, migration guide, release workflow | ✅ done |

The resource layer is **mechanically generated** from `spec/openapi.json`. To refresh after a TikHub spec update:

```bash
python scripts/refresh_spec.py        # pulls latest openapi.json, prints diff
python scripts/generate_resources.py  # regenerates all 52 resource files + clients
python scripts/generate_docs.py       # regenerates docs/reference.md
python scripts/verify_coverage.py     # asserts 100% coverage
pytest -q                             # 110 tests
```

## CLI

A small console wrapper ships in the `cli` extra:

```bash
pip install "tikhub[cli]"
export TIKHUB_API_KEY="YOUR_API_KEY"

tikhub health                                 # ping the API
tikhub fetch https://v.douyin.com/abc/        # universal video URL parser
tikhub user info                              # plan + quota
tikhub user usage                             # today's request count
```

Every command prints JSON to stdout — pipe to `jq` or any other formatter.

## Documentation

Full docs (mkdocs-material): authentication, async, errors, pagination, retries, logging, CLI, migration guide, naming rules, and the auto-generated reference for all 1010 endpoints.

```bash
pip install -e ".[docs]"
mkdocs serve            # http://127.0.0.1:8000
```

## License

MIT.
