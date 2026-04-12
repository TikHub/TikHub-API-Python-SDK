# Errors

Every HTTP failure becomes a typed exception that carries the original request, the parsed response body, and the upstream `x-request-id` so you can debug without re-running the call.

## Hierarchy

```text
TikHubError                              base class for everything raised by the SDK
├── TikHubConfigError                    bad config (missing API key, etc.)
├── TikHubConnectionError                network failed before any HTTP response
│   ├── TikHubTimeoutError
│   └── TikHubProxyError
├── TikHubHTTPError                      base for any 4xx / 5xx
│   ├── TikHubBadRequestError            400, 422
│   ├── TikHubAuthError                  401
│   ├── TikHubPermissionError            403
│   ├── TikHubNotFoundError              404
│   ├── TikHubRateLimitError             429 — exposes .retry_after
│   ├── TikHubServerError                5xx
│   └── TikHubUpstreamError              502 / 503 / 504 (TikHub couldn't reach platform)
├── TikHubValidationError                response body failed Pydantic parsing
└── TikHubFeatureRemovedError            method targets a deprecated tag
```

All HTTP errors carry:

| Attribute | Description |
|---|---|
| `status_code` | The HTTP status |
| `method` | `"GET"`, `"POST"`, … |
| `url` | The full URL we requested |
| `params` | Query parameters dict |
| `request_body` | Whatever we sent as JSON / multipart |
| `response_body` | The parsed response body (dict if JSON, else text) |
| `request_id` | The `x-request-id` header from TikHub |
| `headers` | Response headers (auth header always redacted) |

## Catching specific errors

```python
from tikhub import (
    TikHub,
    TikHubAuthError,
    TikHubNotFoundError,
    TikHubRateLimitError,
)

with TikHub() as client:
    try:
        client.douyin_web.fetch_one_video(aweme_id="not-a-real-id")
    except TikHubNotFoundError as exc:
        print(f"404: {exc.url} — {exc.response_body}")
    except TikHubRateLimitError as exc:
        print(f"Rate limited; retry after {exc.retry_after}s")
    except TikHubAuthError as exc:
        print("API key rejected:", exc.response_body)
```

## Retries are automatic for transient failures

You don't need to handle 5xx, 429, or transient network errors yourself — the SDK retries them with exponential backoff. See [Retries & rate limits](retries.md).

## Producing a debug dump

```python
try:
    client.douyin_web.fetch_one_video(aweme_id="bad")
except TikHubHTTPError as exc:
    # repr() returns a multi-line dump suitable for bug reports.
    print(repr(exc))
```
