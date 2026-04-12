"""Shared pytest fixtures."""

from __future__ import annotations

from collections.abc import Iterator

import pytest


@pytest.fixture(autouse=True)
def _clear_tikhub_env(monkeypatch: pytest.MonkeyPatch) -> Iterator[None]:
    """Make sure ``$TIKHUB_API_KEY`` doesn't leak between tests."""
    monkeypatch.delenv("TIKHUB_API_KEY", raising=False)
    yield
