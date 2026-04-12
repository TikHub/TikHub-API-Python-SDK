#!/usr/bin/env python3
"""Pull the latest TikHub OpenAPI spec into spec/openapi.json.

Run from the repo root::

    python scripts/refresh_spec.py

If the spec changed, prints a summary of added / removed endpoints. After
a successful refresh, run ``python scripts/generate_resources.py`` to
regenerate the SDK.
"""

from __future__ import annotations

import json
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPEC_PATH = ROOT / "spec" / "openapi.json"
SPEC_URL = "https://api.tikhub.io/openapi.json"


def _endpoints(spec: dict) -> set[tuple[str, str]]:
    out: set[tuple[str, str]] = set()
    for path, methods in spec.get("paths", {}).items():
        for m in methods:
            if m.lower() in {"get", "post", "put", "delete", "patch"}:
                out.add((m.upper(), path))
    return out


def main() -> int:
    print(f"Fetching {SPEC_URL} ...")
    with urllib.request.urlopen(SPEC_URL) as resp:
        new_text = resp.read().decode("utf-8")

    new_spec = json.loads(new_text)
    new_version = new_spec.get("info", {}).get("version", "?")
    new_paths = _endpoints(new_spec)

    if SPEC_PATH.exists():
        old_spec = json.loads(SPEC_PATH.read_text())
        old_version = old_spec.get("info", {}).get("version", "?")
        old_paths = _endpoints(old_spec)
    else:
        old_version = "<none>"
        old_paths = set()

    print(f"Old version: {old_version}  ({len(old_paths)} endpoints)")
    print(f"New version: {new_version}  ({len(new_paths)} endpoints)")

    added = sorted(new_paths - old_paths)
    removed = sorted(old_paths - new_paths)

    if added:
        print(f"\nADDED ({len(added)}):")
        for m, p in added[:50]:
            print(f"  + {m:6s} {p}")
        if len(added) > 50:
            print(f"  ... and {len(added) - 50} more")

    if removed:
        print(f"\nREMOVED ({len(removed)}):")
        for m, p in removed[:50]:
            print(f"  - {m:6s} {p}")
        if len(removed) > 50:
            print(f"  ... and {len(removed) - 50} more")

    if not added and not removed:
        print("\nNo endpoint changes.")

    SPEC_PATH.parent.mkdir(parents=True, exist_ok=True)
    SPEC_PATH.write_text(new_text)
    print(f"\nWrote {SPEC_PATH.relative_to(ROOT)}")
    print("Next: run `python scripts/generate_resources.py`")
    return 0


if __name__ == "__main__":
    sys.exit(main())
