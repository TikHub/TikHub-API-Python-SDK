# Migrating from `tikhub_sdk_v2`

`tikhub` (V2.1) is a clean-slate replacement for `tikhub_sdk_v2`. Both packages can be installed side-by-side, so you can migrate file-by-file.

```bash
pip install tikhub_sdk_v2 tikhub      # both at once
```

## Why move

| | V1.x (`tikhub_sdk_v2`) | V2.1 (`tikhub`) |
|---|---|---|
| Package | `tikhub_sdk_v2` | `tikhub` |
| Spec version targeted | V1.0.0 (~28 tags) | **V5.3.2 (52 tags, 1010 endpoints)** |
| Naming | `BodyFetchHotTotalHighFanListApiV1DouyinBillboardFetchHotTotalHighFanListPost` | `client.douyin_billboard.fetch_hot_total_high_fan_list(...)` |
| Async | "library: asyncio" was set in the generator config but the emitted code is sync | Native `httpx.AsyncClient` |
| Python | 2 / 3 (with `six`) | **3.9+** |
| Default host | `localhost` (you had to override every time) | `https://api.tikhub.io` |
| Retries / pagination / typed errors | none | built in |

## Construction

=== "V1.x"
    ```python
    from tikhub_sdk_v2 import Configuration, ApiClient, DouyinWebAPIApi

    cfg = Configuration(host="https://api.tikhub.io")
    cfg.access_token = "YOUR_API_KEY"
    api_client = ApiClient(cfg)
    api = DouyinWebAPIApi(api_client)
    ```

=== "V2.1"
    ```python
    from tikhub import TikHub

    client = TikHub(api_key="YOUR_API_KEY")
    ```

## Calling an endpoint

The V2.1 method name is **the last segment of the path, verbatim**. The parameter names are the OpenAPI parameter names verbatim. So you can find any method just by looking at the API doc URL.

=== "V1.x"
    ```python
    api = DouyinWebAPIApi(api_client)
    video = api.fetch_one_video_api_v1_douyin_web_fetch_one_video_get(
        aweme_id="7251234567890123456",
    )
    ```

=== "V2.1"
    ```python
    video = client.douyin_web.fetch_one_video(aweme_id="7251234567890123456")
    ```

## Method mapping

| V1.x class | V2.1 attribute |
|---|---|
| `DouyinWebAPIApi` | `client.douyin_web` |
| `DouyinAppV3APIApi` | `client.douyin_app_v3` |
| `DouyinBillboardAPIApi` | `client.douyin_billboard` |
| `DouyinXingtuAPIApi` | `client.douyin_xingtu` |
| `TikTokWebAPIApi` | `client.tiktok_web` |
| `TikTokAppV3APIApi` | `client.tiktok_app_v3` |
| `TikTokInteractionAPIApi` | `client.tiktok_interaction` |
| `XiaohongshuWebAPIApi` | `client.xiaohongshu_web` |
| `XiaohongshuWebV2APIApi` | `client.xiaohongshu_web_v2` |
| `BilibiliWebAPIApi` | `client.bilibili_web` |
| `KuaishouWebAPIApi` | `client.kuaishou_web` |
| `KuaishouAppAPIApi` | `client.kuaishou_app` |
| `WeiboWebAPIApi` | `client.weibo_web` |
| `TwitterWebAPIApi` | `client.twitter_web` |
| `YouTubeWebAPIApi` | `client.youtube_web` |
| `WeChatMediaPlatformWebAPIApi` | `client.wechat_media_platform_web` |
| `ZhihuWebAPIApi` | `client.zhihu_web` |
| `ToutiaoWebAPIApi` / `ToutiaoAppAPIApi` | `client.toutiao_web` / `client.toutiao_app` |
| `TempMailAPIApi` | `client.temp_mail` |
| `TikHubUserAPIApi` | `client.tikhub_user` |
| `HealthCheckApi` | `client.health_check` |
| `HybridParsingApi` | `client.hybrid_parsing` |
| `IOSShortcutApi` | `client.ios_shortcut` |

For the method on each class, drop the `_api_v1_..._get` / `_post` suffix that V2 added. The V2.1 method is the path basename.

## Methods that no longer exist

These V1.x classes target endpoints that have been **removed** from the upstream API and are not in V2.1:

- `CaptchaSolverApi` — service discontinued
- `NetEaseCloudMusicAPIApi` — service discontinued
- `InstagramWebAndAPPAPIApi` — replaced by `client.instagram_v1` / `v2` / `v3`
- `DouyinAppV1APIApi`, `DouyinAppV2APIApi` — replaced by `client.douyin_app_v3`
- `TikTokAppV2APIApi` — replaced by `client.tiktok_app_v3`

If your code imports any of these classes you'll need to either drop the call entirely (for the discontinued ones) or rewrite it against the new SDK.

## Errors

V1.x raised `ApiException` for any non-2xx response, with the body in `.body`. V2.1 raises a typed exception per status code:

=== "V1.x"
    ```python
    from tikhub_sdk_v2.exceptions import ApiException

    try:
        api.fetch_one_video_api_v1_douyin_web_fetch_one_video_get(aweme_id="bad")
    except ApiException as exc:
        if exc.status == 404:
            ...
    ```

=== "V2.1"
    ```python
    from tikhub import TikHubNotFoundError

    try:
        client.douyin_web.fetch_one_video(aweme_id="bad")
    except TikHubNotFoundError as exc:
        print(exc.url, exc.response_body, exc.request_id)
    ```

See the [errors](errors.md) page for the full hierarchy.

## What about types?

V1.x returned model objects with `to_dict()` / `to_str()` boilerplate. The SDK currently returns raw `dict` for every method (Pydantic v2 model layer is on the roadmap). To opt out of any future parsing entirely, pass `parse_response=False` to the constructor.
