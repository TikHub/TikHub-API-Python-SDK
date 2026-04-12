# Retries & rate limits

The SDK automatically retries transient failures so your application code doesn't need to.

## What gets retried

| Failure | Retried? |
|---|---|
| Network errors (DNS, connection refused, reset) | ✅ |
| Timeouts | ✅ |
| Proxy errors | ✅ |
| `5xx` server errors | ✅ |
| `502 / 503 / 504` upstream errors | ✅ |
| `429` rate limit | ✅ — sleeps for `Retry-After` if present |
| `4xx` (`400`, `401`, `403`, `404`, `422`) | ❌ — fails fast |
| Pydantic validation errors | ❌ |

## Backoff

The default policy is exponential with jitter:

| Attempt | Sleep before retry |
|---|---|
| 1 → 2 | ~0.5 s |
| 2 → 3 | ~1.0 s |
| 3 → 4 | ~2.0 s |

Capped at 30 s, with ±25 % multiplicative jitter to avoid thundering herds.

## Tuning

```python
from tikhub import TikHub

client = TikHub(
    api_key="sk-...",
    max_retries=5,    # default 3
)
```

If you need to disable retries entirely (e.g. for tests that should fail fast):

```python
client = TikHub(api_key="sk-...", max_retries=0)
```

## Honouring `Retry-After`

When the server returns `429 Too Many Requests` with a `Retry-After` header, the SDK sleeps for exactly that long instead of using the default backoff. The `X-RateLimit-Reset` header is also honoured (both seconds-from-now and unix-timestamp formats).

## Logging

To see retry decisions in action:

```python
import logging
logging.basicConfig(level=logging.INFO)
logging.getLogger("tikhub.retries").setLevel(logging.INFO)
logging.getLogger("tikhub.rate_limit").setLevel(logging.WARNING)
```

You'll see lines like:

```text
INFO  tikhub.retries  Retrying GET https://api.tikhub.io/api/v1/... in 1.04s (attempt 2/3, reason: TikHubServerError)
WARNING  tikhub.rate_limit  Rate limited on GET https://... — sleeping 7.00s (attempt 1/3)
```
