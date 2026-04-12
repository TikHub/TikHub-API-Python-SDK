# tikhub

> Modern Python SDK for the [TikHub](https://tikhub.io) social-media data API.

`tikhub` is a hand-architected, async-first Python SDK that mirrors the **entire** TikHub OpenAPI spec — every method name and every parameter matches the API exactly. There is no translation layer.

```python
from tikhub import TikHub

with TikHub(api_key="YOUR_API_KEY") as client:
    video = client.douyin_web.fetch_one_video(aweme_id="7251234567890123456")
    print(video)
```

## At a glance

- :material-check-circle: **100% endpoint coverage** — 1010 / 1010 endpoints from spec V5.3.2
- :material-check-circle: **52 resources** — one per OpenAPI tag, flat namespace
- :material-check-circle: **Async-first** with a parallel sync surface
- :material-check-circle: **Typed exceptions** with status-code mapping and request-id
- :material-check-circle: **Built-in retries** with exponential backoff and `Retry-After` honouring
- :material-check-circle: **Pagination helpers** for cursor / page / offset patterns
- :material-check-circle: **Mechanical codegen** — refresh from `openapi.json` in one command

## Naming rules

The SDK is mechanically derived from the TikHub OpenAPI spec. Two rules govern everything:

1. **Resource attribute** = OpenAPI tag, lowercased, dashes → underscores, `-API` stripped.
   `Douyin-Web-API` → `client.douyin_web`. `TikTok-App-V3-API` → `client.tiktok_app_v3`.
2. **Method name** = the **last segment of the path, verbatim**.
   `/api/v1/douyin/web/fetch_one_video` → `client.douyin_web.fetch_one_video(...)`.
   `/api/v1/douyin/web/handler_user_profile` → `client.douyin_web.handler_user_profile(...)`.

Parameter names also match the OpenAPI spec verbatim. If you can read the [TikHub API docs](https://docs.tikhub.io), you already know how to use the SDK.

See the [API reference](reference.md) for the complete catalogue of resources and methods.

## Install

The package isn't on PyPI yet. Install directly from GitHub:

```bash
# Latest from the v2.1.0 branch
pip install "git+https://github.com/TikHub/TikHub-API-Python-SDK-V2.git@v2.1.0"

# With the optional CLI extra
pip install "tikhub[cli] @ git+https://github.com/TikHub/TikHub-API-Python-SDK-V2.git@v2.1.0"

# Pin to a specific commit (recommended for production)
pip install "git+https://github.com/TikHub/TikHub-API-Python-SDK-V2.git@<commit-sha>"
```

Once merged to `main` you can drop the `@v2.1.0` ref. Once published to PyPI you'll be able to use plain `pip install tikhub`.

Requires Python 3.9+.

## Next steps

- [Quickstart](quickstart.md) — 5-minute runnable tour
- [Authentication](authentication.md)
- [API reference](reference.md) — all 1010 endpoints
- [Migrating from V2](migrating-from-v2.md)
