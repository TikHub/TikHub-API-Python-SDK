#!/usr/bin/env python3
"""Generate ``docs/reference.md`` from the SDK source.

Walks every resource exposed on ``TikHub`` and renders an alphabetical
catalogue of all 1010 methods, grouped by resource. The output is a
single markdown file that mkdocs-material renders into the API reference
section of the docs site.

Run from the repo root::

    python scripts/generate_docs.py
"""

from __future__ import annotations

import inspect
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS_PATH = ROOT / "docs" / "reference.md"

sys.path.insert(0, str(ROOT / "src"))

ENDPOINT_LINE = re.compile(r"``([A-Z]+) (/[^`]+)``")


def main() -> int:
    from tikhub import TikHub

    client = TikHub(api_key="dummy-for-introspection")
    resources: list[tuple[str, object]] = []
    for attr in sorted(dir(client)):
        if attr.startswith("_"):
            continue
        obj = getattr(client, attr)
        if hasattr(obj, "_client"):
            resources.append((attr, obj))

    lines: list[str] = []
    lines.append("# API reference")
    lines.append("")
    lines.append(f"All **{_method_count(resources)}** endpoints across **{len(resources)}** resources, generated from `spec/openapi.json` (V5.3.2).")
    lines.append("")
    lines.append("Method names match the OpenAPI path basename verbatim. Parameter names match the OpenAPI parameter names verbatim. See [naming rules](index.md#naming-rules).")
    lines.append("")
    lines.append("## Resources")
    lines.append("")

    # TOC
    for attr, obj in resources:
        cls = type(obj).__name__
        method_count = sum(
            1 for n in dir(obj)
            if not n.startswith("_") and callable(getattr(obj, n, None))
        )
        lines.append(f"- [`client.{attr}`](#client{attr.replace('_','')}) — `{cls}`, {method_count} endpoints")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Per-resource sections
    for attr, obj in resources:
        cls = type(obj).__name__
        methods = sorted(
            n for n in dir(obj)
            if not n.startswith("_") and callable(getattr(obj, n, None))
        )
        lines.append(f"## `client.{attr}`")
        lines.append("")
        lines.append(f"**Class:** `tikhub.resources.{attr}.{cls}` (sync) / `Async{cls}` (async)")
        lines.append("")
        lines.append(f"**Endpoints:** {len(methods)}")
        lines.append("")
        lines.append("| Method | Endpoint | Summary |")
        lines.append("|---|---|---|")
        for name in methods:
            fn = getattr(obj, name)
            doc = (fn.__doc__ or "").strip()
            m = ENDPOINT_LINE.search(doc)
            ep = f"`{m.group(1)} {m.group(2)}`" if m else ""
            # First line of docstring is the summary
            summary = doc.split("\n", 1)[0].strip()
            if m and summary == m.group(0):
                summary = ""
            summary = summary.replace("|", "\\|").replace("\n", " ")[:120]
            sig = _method_signature(fn)
            lines.append(f"| `{name}({sig})` | {ep} | {summary} |")
        lines.append("")

    client.close()
    DOCS_PATH.parent.mkdir(parents=True, exist_ok=True)
    DOCS_PATH.write_text("\n".join(lines))
    print(f"wrote {DOCS_PATH.relative_to(ROOT)}  ({_method_count(resources)} methods, {len(resources)} resources)")
    return 0


def _method_count(resources: list[tuple[str, object]]) -> int:
    total = 0
    for _attr, obj in resources:
        total += sum(
            1 for n in dir(obj)
            if not n.startswith("_") and callable(getattr(obj, n, None))
        )
    return total


def _method_signature(fn: object) -> str:
    try:
        sig = inspect.signature(fn)  # type: ignore[arg-type]
    except (ValueError, TypeError):
        return "..."
    params = []
    for p in sig.parameters.values():
        if p.name == "self":
            continue
        if p.default is inspect.Parameter.empty:
            params.append(p.name)
        else:
            params.append(f"{p.name}=...")
    return ", ".join(params)


if __name__ == "__main__":
    raise SystemExit(main())
