"""Logger namespaces used throughout the SDK.

The SDK never installs handlers — it only emits records under
``tikhub.*`` loggers. Applications configure their own root handler.
"""

from __future__ import annotations

import logging

# Top-level package logger. Children inherit its level.
logger: logging.Logger = logging.getLogger("tikhub")

# Per-concern child loggers — see PLAN_V3.md §15.
requests_logger: logging.Logger = logging.getLogger("tikhub.requests")
"""DEBUG: one line per HTTP request (method, URL, status, duration, request id)."""

bodies_logger: logging.Logger = logging.getLogger("tikhub.requests.bodies")
"""DEBUG: request and response bodies. Auth header is always redacted."""

retries_logger: logging.Logger = logging.getLogger("tikhub.retries")
"""INFO: retry attempts (which call, why, how long we slept)."""

rate_limit_logger: logging.Logger = logging.getLogger("tikhub.rate_limit")
"""WARNING: when we sleep because of an upstream rate limit."""

deprecation_logger: logging.Logger = logging.getLogger("tikhub.deprecation")
"""WARNING: when caller hits a method that targets a deprecated TikHub endpoint."""


# Library-default: silent unless the application opts in.
logger.addHandler(logging.NullHandler())
