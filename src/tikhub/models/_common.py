"""Shared envelope types used across many TikHub responses."""

from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, ConfigDict

__all__ = ["ApiResponse", "Pagination"]

T = TypeVar("T")


class _OpenModel(BaseModel):
    """Base for all SDK models — preserves unknown fields from the upstream JSON."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)


class ApiResponse(_OpenModel, Generic[T]):
    """Generic envelope wrapping a typed payload.

    Many TikHub endpoints respond with::

        {"code": 200, "router": "...", "params": {...}, "data": {...}}

    Resource methods unwrap the envelope and return the ``data`` field by
    default. Power users who want the full envelope can pass ``_raw=True``
    (added in Phase 2 alongside individual resources).
    """

    code: int | None = None
    router: str | None = None
    params: dict[str, Any] | None = None
    data: T | None = None


class Pagination(_OpenModel):
    """Generic pagination state attached to a list response."""

    cursor: int | str | None = None
    max_cursor: int | str | None = None
    has_more: bool | None = None
    page: int | None = None
    total: int | None = None
