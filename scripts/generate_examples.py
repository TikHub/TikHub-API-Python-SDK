#!/usr/bin/env python3
"""Generate per-resource example scripts under ``examples/``.

Reads ``spec/openapi.json`` and emits one runnable Python file per OpenAPI
tag into ``examples/<resource_attr>.py``. Each file demonstrates how to call
every endpoint in that resource using the example/default values shipped
with the spec, and prints a truncated JSON response per call.

Each generated file is **fully self-contained** — you can copy it out of
the repo and run it standalone with::

    export TIKHUB_API_KEY="YOUR_API_KEY"
    python examples/<resource>.py

Skipped (won't be generated):
    * TikTok-Interaction-API   (mutates state)
    * sora2.upload_image       (multipart, needs a real file)

Usage::

    python scripts/generate_examples.py
"""

from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
SPEC_PATH = ROOT / "spec" / "openapi.json"
EXAMPLES_DIR = ROOT / "examples"

# Make src/ importable so we can introspect method names cleanly.
sys.path.insert(0, str(ROOT / "src"))

SKIP_TAGS = {"TikTok-Interaction-API"}
SKIP_PATHS = {"/api/v1/sora2/upload_image"}

ENDPOINT_RE = re.compile(r"``([A-Z]+) (/[^`]+)``")

# Files in examples/ that we never overwrite.
PROTECTED = {"quickstart.py", "__init__.py"}


# ---------------------------------------------------------------------------
# Spec helpers
# ---------------------------------------------------------------------------


def tag_to_attr(tag: str) -> str:
    if tag.endswith("-API"):
        tag = tag[:-4]
    return tag.replace("-", "_").lower()


def example_for(schema: dict[str, Any] | None) -> Any:
    """Best-effort example value for an OpenAPI schema."""
    if not schema:
        return "test"
    if "example" in schema:
        return schema["example"]
    if "default" in schema:
        return schema["default"]
    examples = schema.get("examples")
    if examples:
        first = next(iter(examples))
        if isinstance(first, dict) and "value" in first:
            return first["value"]
        return first
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


def param_example(param: dict[str, Any]) -> Any:
    """Extract the best example from an OpenAPI parameter object.

    Checks in order: param-level ``example``, schema-level ``example``,
    schema-level ``default``, then falls back to ``example_for(schema)``
    which uses a type-based fallback.
    """
    # 1. Parameter-level example (most common in the TikHub spec).
    if "example" in param:
        return param["example"]
    sch = param.get("schema") or {}
    # 2. Schema-level example or default.
    if "example" in sch:
        return sch["example"]
    if "default" in sch:
        return sch["default"]
    # 3. Type-based fallback.
    return example_for(sch)


def collect_call_kwargs(op: dict[str, Any], spec: dict[str, Any]) -> tuple[dict[str, Any], str]:
    """Return ``(kwargs_dict, body_kind)``.

    Includes ALL query params that have an example/default in the spec
    (not just required ones), so the generated examples show realistic calls.
    Required params without any example still get a type-based fallback.
    """
    kwargs: dict[str, Any] = {}
    for p in op.get("parameters") or []:
        if p.get("in") != "query":
            continue
        val = param_example(p)
        # Always include required params. Include optional ones only if the
        # spec ships a meaningful example (skip type-fallbacks like "test").
        is_required = p.get("required", False)
        has_real_example = (
            "example" in p
            or "example" in (p.get("schema") or {})
            or "default" in (p.get("schema") or {})
        )
        if is_required or has_real_example:
            kwargs[p["name"]] = val

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
                val = example_for(pdef)
                has_real = "example" in pdef or "default" in pdef
                if pname in required or has_real:
                    kwargs[pname] = val
            return kwargs, "props"
        kwargs["body"] = None
        return kwargs, "scalar"

    return kwargs, "none"


def build_endpoint_map() -> dict[tuple[str, str], tuple[str, str]]:
    """Walk the SDK and map ``(http_method, path) -> (resource_attr, sdk_method_name)``."""
    from tikhub import TikHub

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
# Render
# ---------------------------------------------------------------------------


def py_literal(value: Any) -> str:
    """Render a value as a clean inline Python literal."""
    return repr(value)


def render_example_file(
    *,
    tag: str,
    attr: str,
    ops: list[dict[str, Any]],
    spec: dict[str, Any],
) -> str:
    """Render a simple, flat example script.

    Output style — no lambdas, no wrappers, just direct calls::

        import json
        from tikhub import TikHub

        client = TikHub(api_key="...")

        # GET /api/v1/douyin/web/fetch_one_video
        result = client.douyin_web.fetch_one_video(aweme_id="...")
        print(json.dumps(result, indent=2, ensure_ascii=False))

        client.close()
    """
    lines: list[str] = []
    lines.append(f'"""Example: {tag}')
    lines.append("")
    lines.append(f"SDK attribute: ``client.{attr}``")
    lines.append(f"Endpoints: {len(ops)}")
    lines.append("")
    lines.append("Usage::")
    lines.append("")
    lines.append(f"    python examples/{attr}.py")
    lines.append("")
    lines.append("AUTO-GENERATED by scripts/generate_examples.py.")
    lines.append('"""')
    lines.append("")
    lines.append("import asyncio")
    lines.append("import json")
    lines.append("")
    lines.append("from tikhub import AsyncTikHub")
    lines.append("")
    lines.append('API_KEY = "YOUR_API_KEY"')
    lines.append("")
    lines.append("")
    lines.append("async def main():")
    lines.append(f"    async with AsyncTikHub(api_key=API_KEY) as client:")

    for entry in ops:
        kwargs, body_kind = collect_call_kwargs(entry["op"], spec)
        sdk_method = entry["sdk_method"]
        http_method = entry["http_method"]
        path = entry["path"]
        summary = (entry["op"].get("summary") or "").strip().replace("\n", " ")[:100]

        lines.append("")
        lines.append(f"        # {http_method} {path}")
        if summary:
            lines.append(f"        # {summary.rstrip()}")

        if body_kind == "multipart":
            lines.append(f"        # Skipped: multipart upload (needs a real file)")
        else:
            if kwargs:
                args = ", ".join(f"{k}={py_literal(v)}" for k, v in kwargs.items())
                call = f"await client.{attr}.{sdk_method}({args})"
            else:
                call = f"await client.{attr}.{sdk_method}()"
            lines.append(f"        result = {call}")
            lines.append("        print(json.dumps(result, indent=2, ensure_ascii=False))")

    lines.append("")
    lines.append("")
    lines.append('if __name__ == "__main__":')
    lines.append("    asyncio.run(main())")
    return "\n".join(lines) + "\n"


def main() -> int:
    spec = json.loads(SPEC_PATH.read_text())
    endpoint_map = build_endpoint_map()

    by_tag: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for path, methods in spec["paths"].items():
        for http_method, op in methods.items():
            if http_method.lower() not in ("get", "post", "put", "delete", "patch"):
                continue
            if path in SKIP_PATHS:
                continue
            tags = list(dict.fromkeys(op.get("tags") or ["_untagged"]))
            for tag in tags:
                if tag in SKIP_TAGS:
                    continue
                mapping = endpoint_map.get((http_method.upper(), path))
                if mapping is None:
                    continue  # SDK doesn't expose this endpoint
                attr, sdk_method = mapping
                by_tag[tag].append(
                    {
                        "sdk_method": sdk_method,
                        "http_method": http_method.upper(),
                        "path": path,
                        "op": op,
                        "attr": attr,
                    }
                )

    # Dedupe (some operations are tagged with the same tag twice in the spec).
    for tag in by_tag:
        seen: set[tuple[str, str]] = set()
        unique = []
        for e in by_tag[tag]:
            key = (e["http_method"], e["path"])
            if key in seen:
                continue
            seen.add(key)
            unique.append(e)
        by_tag[tag] = unique

    EXAMPLES_DIR.mkdir(exist_ok=True)

    # Wipe previously generated example files (preserve hand-written ones).
    for f in EXAMPLES_DIR.iterdir():
        if not f.is_file() or f.suffix != ".py" or f.name in PROTECTED:
            continue
        text = f.read_text(errors="ignore")
        if "AUTO-GENERATED by scripts/generate_examples.py" in text:
            f.unlink()

    written = 0
    total_endpoints = 0
    for tag in sorted(by_tag):
        ops = by_tag[tag]
        # All ops in this list share the same resource attribute.
        attr = ops[0]["attr"]
        out_path = EXAMPLES_DIR / f"{attr}.py"
        out_path.write_text(render_example_file(tag=tag, attr=attr, ops=ops, spec=spec))
        written += 1
        total_endpoints += len(ops)
        print(f"  wrote examples/{attr}.py  ({len(ops)} endpoints)")

    print(f"\nDone. {written} example files, {total_endpoints} demo calls.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
