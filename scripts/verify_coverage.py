#!/usr/bin/env python3
"""Verify the SDK covers every endpoint in spec/openapi.json.

Run from the repo root::

    python scripts/verify_coverage.py

Exits non-zero (and prints the gaps) if any spec endpoint is missing from
the generated SDK, or if the SDK exposes a method whose path no longer
exists in the spec.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPEC_PATH = ROOT / "spec" / "openapi.json"

# Make ``src/`` importable without installing.
sys.path.insert(0, str(ROOT / "src"))


def spec_endpoints() -> set[tuple[str, str]]:
    with SPEC_PATH.open() as f:
        spec = json.load(f)
    out: set[tuple[str, str]] = set()
    for path, methods in spec["paths"].items():
        for m in methods:
            if m.lower() in {"get", "post", "put", "delete", "patch"}:
                out.add((m.upper(), path))
    return out


def sdk_endpoints() -> set[tuple[str, str]]:
    """Walk every resource attribute on TikHub and inspect each method's
    docstring for the ``HTTP /api/v1/...`` line written by the generator.
    """
    import re

    from tikhub import TikHub

    client = TikHub(api_key="dummy-for-introspection")
    out: set[tuple[str, str]] = set()
    pattern = re.compile(r"``([A-Z]+) (/[^`]+)``")
    for attr in dir(client):
        if attr.startswith("_"):
            continue
        resource = getattr(client, attr)
        for name in dir(resource):
            if name.startswith("_"):
                continue
            fn = getattr(resource, name, None)
            if not callable(fn):
                continue
            doc = (fn.__doc__ or "").strip()
            m = pattern.search(doc)
            if m:
                out.add((m.group(1), m.group(2)))
    client.close()
    return out


def main() -> int:
    spec = spec_endpoints()
    sdk = sdk_endpoints()

    missing_in_sdk = sorted(spec - sdk)
    extra_in_sdk = sorted(sdk - spec)

    print(f"Spec:    {len(spec):4d} endpoints")
    print(f"SDK:     {len(sdk):4d} endpoints")
    print(f"Overlap: {len(spec & sdk):4d}")
    print()

    if missing_in_sdk:
        print(f"MISSING in SDK ({len(missing_in_sdk)}):")
        for m, p in missing_in_sdk[:50]:
            print(f"  {m:6s} {p}")
        if len(missing_in_sdk) > 50:
            print(f"  ... and {len(missing_in_sdk) - 50} more")
        print()

    if extra_in_sdk:
        print(f"EXTRA in SDK (not in spec, {len(extra_in_sdk)}):")
        for m, p in extra_in_sdk[:50]:
            print(f"  {m:6s} {p}")
        if len(extra_in_sdk) > 50:
            print(f"  ... and {len(extra_in_sdk) - 50} more")
        print()

    if missing_in_sdk or extra_in_sdk:
        return 1
    print("OK - SDK covers every spec endpoint and nothing extra.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
