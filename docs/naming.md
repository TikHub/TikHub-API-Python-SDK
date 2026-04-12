# Naming rules

The SDK is mechanically derived from the TikHub OpenAPI spec. There are exactly **two rules** that determine every name in the SDK.

## Rule 1: Resource attribute = OpenAPI tag

Lowercased, dashes → underscores, `-API` suffix stripped.

| OpenAPI tag | SDK attribute |
|---|---|
| `Douyin-Web-API` | `client.douyin_web` |
| `Douyin-App-V3-API` | `client.douyin_app_v3` |
| `TikTok-Shop-Web-API` | `client.tiktok_shop_web` |
| `Xiaohongshu-Web-V3-API` | `client.xiaohongshu_web_v3` |
| `iOS-Shortcut` | `client.ios_shortcut` |
| `Health-Check` | `client.health_check` |
| `Hybrid-Parsing` | `client.hybrid_parsing` |

## Rule 2: Method name = path basename

The **last segment of the OpenAPI path, verbatim**. We never strip `fetch_` / `get_` / `handler_`, never rename for "consistency", never pluralize, never abbreviate.

| OpenAPI path | SDK method |
|---|---|
| `/api/v1/douyin/web/fetch_one_video` | `client.douyin_web.fetch_one_video(...)` |
| `/api/v1/douyin/web/handler_user_profile` | `client.douyin_web.handler_user_profile(...)` |
| `/api/v1/douyin/web/handler_user_profile_v2` | `client.douyin_web.handler_user_profile_v2(...)` |
| `/api/v1/tiktok/web/generate_xbogus` | `client.tiktok_web.generate_xbogus(...)` |
| `/api/v1/sora2/upload_image` | `client.sora2.upload_image(...)` |

## Rule 3 (corollary): Parameter names = OpenAPI parameter names

If the API documents `aweme_id`, the SDK kwarg is `aweme_id`. If the API documents `uniqueId` (camelCase), the SDK kwarg is `uniqueId`. We do not snake_case or rename for stylistic consistency — that would create a translation layer.

```python
client.douyin_web.fetch_one_video(aweme_id="...")            # snake_case from API
client.tiktok_web.fetch_user_profile(uniqueId="charlidamelio")  # camelCase from API
```

## Why so strict?

- **Discoverability** — anyone reading the [TikHub API docs](https://docs.tikhub.io) can use the SDK without a second mental model.
- **Maintainability** — adding a new endpoint to the API takes one command (`python scripts/refresh_spec.py && python scripts/generate_resources.py`). There's no per-endpoint hand-curation.
- **No drift** — there's no V2-style `fetch_one_video_api_v1_douyin_web_fetch_one_video_get` boilerplate, and no risk of two SDK methods quietly meaning slightly different things.

## Versioned methods

When TikHub ships V1 / V2 / V3 of the same operation, the SDK exposes **all of them** as distinct methods — we don't pick a "best" one and hide the others.

```python
v1 = client.douyin_web.fetch_one_video(aweme_id="...")
v2 = client.douyin_web.fetch_one_video_v2(aweme_id="...")
```

## Deprecated methods

When the upstream spec marks an operation deprecated, the SDK still ships it (with the same verbatim name) and adds a deprecation note to the docstring. Methods are only removed if they disappear from the upstream spec entirely.
