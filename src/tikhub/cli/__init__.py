"""Optional command-line wrapper for the TikHub SDK.

Install with the ``cli`` extra::

    pip install "tikhub[cli]"

Then::

    tikhub health
    tikhub fetch https://v.douyin.com/abc/
    tikhub user info

The CLI is intentionally tiny - it's for ad-hoc fetches. For anything more
complex, write a Python script that imports ``tikhub`` directly.
"""

from __future__ import annotations

from tikhub.cli.main import app

__all__ = ["app"]
