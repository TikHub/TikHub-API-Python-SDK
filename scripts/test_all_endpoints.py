#!/usr/bin/env python3
"""Hit every endpoint in spec/openapi.json with example/default params.

Usage::

    export TIKHUB_API_KEY="YOUR_API_KEY"
    python scripts/test_all_endpoints.py [--limit N] [--tag Douyin-Web-API]

Writes ``test_results.json`` (machine-readable) and ``test_results.md``
(human-readable summary) to the repo root.

Skips by default:
    * TikTok-Interaction-API     (mutates state)
    * sora2.upload_image         (needs a real file)

Each call uses ``max_retries=0`` so we see the *first* failure cleanly,
not a slow exponential backoff loop.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import re
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
SPEC_PATH = ROOT / "spec" / "openapi.json"
RESULTS_JSON = ROOT / "test_results.json"
RESULTS_MD = ROOT / "test_results.md"

sys.path.insert(0, str(ROOT / "src"))

from tikhub import (  # noqa: E402
    AsyncTikHub,
    TikHub,
    TikHubConnectionError,
    TikHubError,
    TikHubHTTPError,
)

# ---------------------------------------------------------------------------
# Skip lists
# ---------------------------------------------------------------------------

SKIP_TAGS = {"TikTok-Interaction-API"}  # mutate state
SKIP_PATHS = {
    "/api/v1/sora2/upload_image",  # multipart, needs a real file
}

# Concurrency: how many requests in flight at once. Higher = faster but
# more likely to trip TikHub's rate limit. The SDK retries 429s with
# exponential backoff (see _retries.py), so 2-3 is usually safe.
CONCURRENCY = int(os.environ.get("TIKHUB_TEST_CONCURRENCY", "2"))
# How many retries the SDK should attempt on transient failures (5xx, 429,
# network errors) before bubbling the error up.
MAX_RETRIES = int(os.environ.get("TIKHUB_TEST_MAX_RETRIES", "3"))

# ---------------------------------------------------------------------------
# Spec helpers
# ---------------------------------------------------------------------------


def load_spec() -> dict[str, Any]:
    return json.loads(SPEC_PATH.read_text())


def example_for(schema: dict[str, Any] | None) -> Any:
    """Best-effort example value for an OpenAPI parameter or property schema.

    Falls back to a sensible literal when no example is given.
    """
    if not schema:
        return "test"
    # Highest priority: explicit example.
    if "example" in schema:
        return schema["example"]
    if "default" in schema:
        return schema["default"]
    if schema.get("examples"):
        first = next(iter(schema["examples"]))
        if isinstance(first, dict) and "value" in first:
            return first["value"]
        return first
    # Type-based fallback.
    t = schema.get("type")
    if t == "string":
        return "test"
    if t == "integer":
        return 1
    if t == "number":
        return 1.0
    if t == "boolean":
        return True
    if t == "array":
        return []
    if t == "object":
        return {}
    if "anyOf" in schema:
        for s in schema["anyOf"]:
            if s.get("type") != "null":
                return example_for(s)
    return "test"


def build_kwargs(op: dict[str, Any], spec: dict[str, Any]) -> tuple[dict[str, Any], str]:
    """Return ``(kwargs, body_kind)``.

    ``body_kind`` is one of ``"none" | "props" | "array" | "scalar" | "multipart"``.
    For "props" the body params are merged into the same kwargs dict
    alongside any query params (matches how the SDK is generated).
    """
    kwargs: dict[str, Any] = {}
    for p in op.get("parameters") or []:
        if p.get("in") != "query":
            continue
        # Always send required params; optional ones we leave out so the
        # SDK's _drop_none can simulate "did not pass anything".
        if p.get("required"):
            kwargs[p["name"]] = example_for(p.get("schema") or {})

    rb = op.get("requestBody") or {}
    content = rb.get("content") or {}

    if "multipart/form-data" in content:
        return kwargs, "multipart"

    if "application/json" in content:
        sch = content["application/json"]["schema"]
        if "$ref" in sch:
            ref_name = sch["$ref"].split("/")[-1]
            sch = spec["components"]["schemas"].get(ref_name, {})
        if sch.get("type") == "array":
            kwargs["body"] = []
            return kwargs, "array"
        props = sch.get("properties") or {}
        if props:
            required = set(sch.get("required") or [])
            for pname, pdef in props.items():
                if pname in required:
                    kwargs[pname] = example_for(pdef)
            return kwargs, "props"
        kwargs["body"] = None
        return kwargs, "scalar"

    return kwargs, "none"


# ---------------------------------------------------------------------------
# Endpoint -> SDK method introspection
# ---------------------------------------------------------------------------

ENDPOINT_RE = re.compile(r"``([A-Z]+) (/[^`]+)``")


def build_endpoint_map() -> dict[tuple[str, str], tuple[str, str]]:
    """Walk the SDK and map ``(http_method, path) -> (resource_attr, method_name)``."""
    out: dict[tuple[str, str], tuple[str, str]] = {}
    client = TikHub(api_key="dummy-for-introspection")
    for attr in dir(client):
        if attr.startswith("_"):
            continue
        obj = getattr(client, attr)
        if not hasattr(obj, "_client"):
            continue
        for name in dir(obj):
            if name.startswith("_"):
                continue
            fn = getattr(obj, name, None)
            if not callable(fn):
                continue
            doc = (fn.__doc__ or "").strip()
            m = ENDPOINT_RE.search(doc)
            if m:
                out[(m.group(1), m.group(2))] = (attr, name)
    client.close()
    return out


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------


async def run_one(
    client: AsyncTikHub,
    sem: asyncio.Semaphore,
    *,
    resource: str,
    method: str,
    http_method: str,
    path: str,
    kwargs: dict[str, Any],
    tag: str,
) -> dict[str, Any]:
    record: dict[str, Any] = {
        "tag": tag,
        "resource": resource,
        "method": method,
        "http_method": http_method,
        "path": path,
        "kwargs_keys": sorted(kwargs.keys()),
    }
    async with sem:
        started = time.perf_counter()
        try:
            resource_obj = getattr(client, resource)
            method_fn = getattr(resource_obj, method)
            result = await method_fn(**kwargs)
            record["duration_ms"] = round((time.perf_counter() - started) * 1000)
            record["status"] = "ok"
            record["http_status"] = 200
            # Capture a tiny shape preview rather than full response.
            if isinstance(result, dict):
                record["response_keys"] = sorted(list(result.keys()))[:8]
                inner = result.get("data") if isinstance(result.get("data"), dict) else None
                if inner:
                    record["data_keys"] = sorted(list(inner.keys()))[:8]
            elif isinstance(result, list):
                record["response_keys"] = f"<list len={len(result)}>"
            return record
        except TikHubHTTPError as exc:
            record["duration_ms"] = round((time.perf_counter() - started) * 1000)
            record["http_status"] = exc.status_code
            # 3xx is typically an intentional redirect (e.g. downloader endpoints).
            # Treat it as a success-equivalent: the endpoint was reached and the
            # SDK is correctly wired.
            if 300 <= exc.status_code < 400:
                record["status"] = "ok_redirect"
            else:
                record["status"] = "http_error"
            record["error"] = str(exc)[:300]
            record["response_body"] = (
                str(exc.response_body)[:200]
                if exc.response_body is not None
                else None
            )
            record["request_id"] = exc.request_id
            return record
        except TikHubConnectionError as exc:
            record["duration_ms"] = round((time.perf_counter() - started) * 1000)
            record["status"] = "connection_error"
            record["error"] = str(exc)[:300]
            return record
        except TikHubError as exc:
            record["duration_ms"] = round((time.perf_counter() - started) * 1000)
            record["status"] = "sdk_error"
            record["error"] = str(exc)[:300]
            return record
        except TypeError as exc:
            # Most likely a missing required param the spec didn't expose.
            record["duration_ms"] = round((time.perf_counter() - started) * 1000)
            record["status"] = "param_error"
            record["error"] = str(exc)[:300]
            return record
        except Exception as exc:
            record["duration_ms"] = round((time.perf_counter() - started) * 1000)
            record["status"] = "unknown_error"
            record["error"] = f"{type(exc).__name__}: {str(exc)[:280]}"
            return record


async def run_all(targets: list[dict[str, Any]], api_key: str) -> list[dict[str, Any]]:
    sem = asyncio.Semaphore(CONCURRENCY)
    async with AsyncTikHub(api_key=api_key, max_retries=MAX_RETRIES, timeout=45) as client:
        tasks = [
            run_one(
                client,
                sem,
                resource=t["resource"],
                method=t["method"],
                http_method=t["http_method"],
                path=t["path"],
                kwargs=t["kwargs"],
                tag=t["tag"],
            )
            for t in targets
        ]

        results: list[dict[str, Any]] = []
        done = 0
        total = len(tasks)
        for coro in asyncio.as_completed(tasks):
            r = await coro
            results.append(r)
            done += 1
            if done % 25 == 0 or done == total:
                ok = sum(1 for x in results if x["status"] in {"ok", "ok_redirect"})
                bad = done - ok
                print(f"  {done}/{total}  (ok={ok} bad={bad})", flush=True)
        return results


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------


def write_report(results: list[dict[str, Any]], skipped: list[dict[str, Any]]) -> None:
    RESULTS_JSON.write_text(
        json.dumps({"tested": results, "skipped": skipped}, indent=2, ensure_ascii=False)
    )

    total = len(results)
    by_status: Counter[str] = Counter(r["status"] for r in results)
    by_http: Counter[int] = Counter(r.get("http_status") for r in results if r.get("http_status"))
    by_tag_status: dict[str, Counter[str]] = defaultdict(Counter)
    for r in results:
        by_tag_status[r["tag"]][r["status"]] += 1

    lines: list[str] = []
    lines.append("# TikHub SDK end-to-end test report")
    lines.append("")
    lines.append(f"Tested **{total}** endpoints against the live API.")
    lines.append(f"Skipped **{len(skipped)}** ({len(SKIP_TAGS)} write tag(s) + special cases).")
    lines.append("")
    lines.append("## Outcome breakdown")
    lines.append("")
    lines.append("| Status | Count |")
    lines.append("|---|---|")
    for status, n in by_status.most_common():
        lines.append(f"| `{status}` | {n} |")
    lines.append("")
    lines.append("## HTTP status codes")
    lines.append("")
    lines.append("| Code | Count |")
    lines.append("|---|---|")
    for code, n in sorted(by_http.items()):
        lines.append(f"| {code} | {n} |")
    lines.append("")
    lines.append("## Per-tag breakdown")
    lines.append("")
    lines.append("| Tag | OK | HTTP error | Other |")
    lines.append("|---|---|---|---|")
    for tag in sorted(by_tag_status):
        c = by_tag_status[tag]
        ok = c.get("ok", 0) + c.get("ok_redirect", 0)
        herr = c.get("http_error", 0)
        other = sum(v for k, v in c.items() if k not in {"ok", "ok_redirect", "http_error"})
        lines.append(f"| `{tag}` | {ok} | {herr} | {other} |")
    lines.append("")
    lines.append("## Failure samples (first 30 non-OK)")
    lines.append("")
    bad = [r for r in results if r["status"] not in {"ok", "ok_redirect"}]
    bad.sort(key=lambda r: (r["tag"], r["resource"], r["method"]))
    for r in bad[:30]:
        st = r.get("http_status") or r["status"]
        msg = r.get("error", "")[:160]
        lines.append(f"- **{r['resource']}.{r['method']}** ({st}) — {msg}")
    if len(bad) > 30:
        lines.append(f"- ... and {len(bad) - 30} more")
    lines.append("")
    lines.append("## How to drill in")
    lines.append("")
    lines.append("Full machine-readable results in `test_results.json`. Open it for")
    lines.append("per-call timings, request IDs, and response bodies.")
    RESULTS_MD.write_text("\n".join(lines))
    print(f"\nWrote {RESULTS_JSON.relative_to(ROOT)}")
    print(f"Wrote {RESULTS_MD.relative_to(ROOT)}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=0, help="Only test first N endpoints (debug).")
    parser.add_argument("--tag", default=None, help="Only test the named OpenAPI tag.")
    parser.add_argument(
        "--include-writes",
        action="store_true",
        help="Also test write endpoints (TikTok-Interaction-API). USE WITH CARE.",
    )
    args = parser.parse_args()

    api_key = os.environ.get("TIKHUB_API_KEY")
    if not api_key:
        print("error: set TIKHUB_API_KEY first", file=sys.stderr)
        return 2

    spec = load_spec()
    endpoint_map = build_endpoint_map()

    targets: list[dict[str, Any]] = []
    skipped: list[dict[str, Any]] = []

    for path, methods in spec["paths"].items():
        for http_method, op in methods.items():
            if http_method.lower() not in ("get", "post", "put", "delete", "patch"):
                continue
            tag = (op.get("tags") or ["_untagged"])[0]
            entry = {
                "tag": tag,
                "http_method": http_method.upper(),
                "path": path,
            }
            if args.tag and tag != args.tag:
                continue
            if not args.include_writes and tag in SKIP_TAGS:
                skipped.append({**entry, "reason": "write tag"})
                continue
            if path in SKIP_PATHS:
                skipped.append({**entry, "reason": "special skip"})
                continue
            mapping = endpoint_map.get((http_method.upper(), path))
            if mapping is None:
                skipped.append({**entry, "reason": "no SDK method found"})
                continue
            resource, method = mapping
            kwargs, _kind = build_kwargs(op, spec)
            targets.append(
                {
                    "tag": tag,
                    "http_method": http_method.upper(),
                    "path": path,
                    "resource": resource,
                    "method": method,
                    "kwargs": kwargs,
                }
            )

    if args.limit:
        targets = targets[: args.limit]

    print(f"Testing {len(targets)} endpoints (skipping {len(skipped)})")
    print(f"Concurrency: {CONCURRENCY}")
    print()

    results = asyncio.run(run_all(targets, api_key))
    write_report(results, skipped)

    ok = sum(1 for r in results if r["status"] in {"ok", "ok_redirect"})
    print(f"\nDone. {ok}/{len(results)} OK ({100*ok//max(1,len(results))}%)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
