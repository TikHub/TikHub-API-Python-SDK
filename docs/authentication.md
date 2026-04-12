# Authentication

TikHub uses bearer-token authentication. The SDK supports exactly this — no API-key-in-query, no basic auth, no OAuth flow.

## Setting your API key

The constructor reads from three sources, in priority order:

1. **Explicit argument** — `TikHub(api_key="YOUR_API_KEY")`
2. **Environment variable** — `$TIKHUB_API_KEY`
3. None — raises `TikHubConfigError` on the first request.

```python
import os
from tikhub import TikHub

# Explicit
client = TikHub(api_key="YOUR_API_KEY")

# Or via environment
os.environ["TIKHUB_API_KEY"] = "YOUR_API_KEY"
client = TikHub()
```

## Errors

If the key is missing or wrong:

```python
from tikhub import TikHub, TikHubAuthError, TikHubConfigError

try:
    with TikHub() as client:                        # no key set anywhere
        client.health_check.check()
except TikHubConfigError as exc:
    print(exc)  # "No API key provided. Pass api_key= or set $TIKHUB_API_KEY."

try:
    with TikHub(api_key="sk-bogus") as client:
        client.health_check.check()
except TikHubAuthError as exc:
    print(exc.status_code)        # 401
    print(exc.response_body)      # upstream error message
```

## Custom headers

If you need additional headers (e.g. for telemetry), pass your own `httpx.Client`:

```python
import httpx
from tikhub import TikHub

http = httpx.Client(
    base_url="https://api.tikhub.io",
    headers={"X-My-App": "production"},
)
client = TikHub(api_key="sk-...", http_client=http)
```

The SDK still injects the `Authorization: Bearer …` header per request, so your client is never mutated.

## Custom user agent

```python
client = TikHub(api_key="sk-...", user_agent="my-app/2.1.0")
```

If unset, the SDK sends `tikhub-py/<version>`.
