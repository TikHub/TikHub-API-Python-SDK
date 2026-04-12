"""Base classes for resources.

Resources are dumb. A resource method does three things: build kwargs, call
``self._client._request(...)``, return the result. All HTTP / retry / error
mapping logic lives in :mod:`tikhub._base_client`.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tikhub._base_client import AsyncBaseClient, BaseClient


class SyncResource:
    """Base class for sync resource modules."""

    def __init__(self, client: BaseClient) -> None:
        self._client = client


class AsyncResource:
    """Base class for async resource modules."""

    def __init__(self, client: AsyncBaseClient) -> None:
        self._client = client
