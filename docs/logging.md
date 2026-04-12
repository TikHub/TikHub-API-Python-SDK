# Logging

The SDK uses the standard library `logging` module under the `tikhub.*` namespace. It never installs handlers — your application configures its own root logger.

## Logger namespaces

| Logger | Level | What it emits |
|---|---|---|
| `tikhub.requests` | DEBUG | One line per request: method, URL, status, duration, request id |
| `tikhub.requests.bodies` | DEBUG | Request and response bodies (auth header always redacted) |
| `tikhub.retries` | INFO | "Retrying X after Ys (attempt N/M, reason: …)" |
| `tikhub.rate_limit` | WARNING | "Rate limited, sleeping Xs" |
| `tikhub.deprecation` | WARNING | When you call a method targeting a deprecated upstream endpoint |

## Quick setup

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-7s %(name)s  %(message)s",
)
logging.getLogger("tikhub.requests").setLevel(logging.DEBUG)
```

That's it — every request the SDK makes will now print to stderr.

## Structured logging

The SDK doesn't ship a JSON formatter. If you use `structlog`, `loguru`, or another structured-logging library, configure your root handler the way you normally would and the SDK's emissions will flow through.

## OpenTelemetry

Because the SDK uses a vanilla `httpx.AsyncClient`, the official `opentelemetry-instrumentation-httpx` package works out of the box:

```python
from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor
HTTPXClientInstrumentor().instrument()
```

Every TikHub request will now produce a span with the URL, status, and duration.

## Auth header redaction

The bearer token is **always** redacted in any log output the SDK produces. This is not configurable.
