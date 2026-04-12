"""Local smoke test for the tikhub SDK.

Run with::

    export TIKHUB_API_KEY="YOUR_API_KEY"
    python examples/quickstart.py

Or pass the key inline::

    python examples/quickstart.py YOUR_API_KEY

The script exercises 4 calls:
    1. health_check.check          -- no params, smallest possible call
    2. tikhub_user.get_user_info   -- your account / plan / quota
    3. tikhub_user.get_user_daily_usage  -- today's request count
    4. douyin_web.fetch_one_video  -- a real platform call

If any call fails, the script prints the typed exception with the
status code, URL, response body, and request id.
"""

from __future__ import annotations

import json
import sys

from tikhub import (
    TikHub,
    TikHubError,
    TikHubHTTPError,
    __version__,
)

# A widely shared Douyin video — replace with any aweme_id you like.
SAMPLE_AWEME_ID = "7345492945329900800"


def show(label: str, value: object) -> None:
    print(f"\n=== {label} ===")
    if isinstance(value, (dict, list)):
        text = json.dumps(value, indent=2, ensure_ascii=False)
        # Truncate huge responses so the terminal stays usable.
        if len(text) > 2000:
            text = text[:2000] + f"\n... ({len(text) - 2000} more chars)"
        print(text)
    else:
        print(value)


def main() -> int:
    api_key = sys.argv[1] if len(sys.argv) > 1 else None

    print(f"tikhub {__version__}")

    try:
        with TikHub(api_key=api_key) as client:
            # 1. Health check
            show("1. health_check.check()", client.health_check.check())

            # 2. Account info
            show("2. tikhub_user.get_user_info()", client.tikhub_user.get_user_info())

            # 3. Today's usage
            show("3. tikhub_user.get_user_daily_usage()", client.tikhub_user.get_user_daily_usage())

            # 4. Real platform call
            show(
                f"4. douyin_web.fetch_one_video(aweme_id={SAMPLE_AWEME_ID!r})",
                client.douyin_web.fetch_one_video(aweme_id=SAMPLE_AWEME_ID),
            )

    except TikHubHTTPError as exc:
        print(f"\nHTTP error {exc.status_code} on {exc.method} {exc.url}", file=sys.stderr)
        print(f"  request_id: {exc.request_id}", file=sys.stderr)
        print(f"  response:   {exc.response_body}", file=sys.stderr)
        return 1
    except TikHubError as exc:
        print(f"\nSDK error: {exc}", file=sys.stderr)
        return 2

    print("\nDone.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
