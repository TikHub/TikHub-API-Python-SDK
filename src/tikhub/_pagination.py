"""Pagination helpers.

The TikHub API uses three pagination patterns:

* Cursor / max_cursor + has_more — most Douyin & TikTok user-post listings.
* Page + count — TikTok web search, Bilibili comments.
* Offset + limit — Instagram, Reddit feeds.

This module ships one paginator class per pattern, each implementing both
sync (``__iter__``) and async (``__aiter__``) protocols. Resource methods
that return paginated data return one of these objects instead of a single
model — callers can iterate, call ``first(n)``, or drive page-by-page.

Phase 0 ships the public surface; resource methods will plug their request
factories in during Phase 2.
"""

from __future__ import annotations

from collections.abc import AsyncIterator, Awaitable, Iterator
from typing import (
    Any,
    Callable,
    Generic,
    TypeVar,
)

T = TypeVar("T")


class _PaginatorBase(Generic[T]):
    """Common surface for sync + async paginators.

    Subclasses implement ``_advance`` (sync) or ``_aadvance`` (async),
    which returns one page worth of items and updates internal state.
    """

    def __init__(self) -> None:
        self.has_more: bool = True

    # ------------------------------------------------------------------
    # Sync iteration
    # ------------------------------------------------------------------

    def _advance(self) -> list[T]:  # pragma: no cover - subclass impl
        raise NotImplementedError

    def __iter__(self) -> Iterator[T]:
        while self.has_more:
            yield from self._advance()

    def first(self, n: int) -> list[T]:
        """Eagerly collect at most ``n`` items."""
        out: list[T] = []
        for item in self:
            out.append(item)
            if len(out) >= n:
                break
        return out

    # ------------------------------------------------------------------
    # Async iteration
    # ------------------------------------------------------------------

    async def _aadvance(self) -> list[T]:  # pragma: no cover - subclass impl
        raise NotImplementedError

    def __aiter__(self) -> AsyncIterator[T]:
        return self._aiter()

    async def _aiter(self) -> AsyncIterator[T]:
        while self.has_more:
            page = await self._aadvance()
            for item in page:
                yield item

    async def afirst(self, n: int) -> list[T]:
        """Async equivalent of :meth:`first`."""
        out: list[T] = []
        async for item in self:
            out.append(item)
            if len(out) >= n:
                break
        return out


# ---------------------------------------------------------------------------
# Cursor paginator
# ---------------------------------------------------------------------------

PageFn = Callable[[Any], "Page[T]"]
AsyncPageFn = Callable[[Any], Awaitable["Page[T]"]]


class Page(Generic[T]):
    """Result of one page fetch — items plus the cursor for the next call."""

    __slots__ = ("has_more", "items", "next_cursor")

    def __init__(
        self,
        items: list[T],
        *,
        next_cursor: Any = None,
        has_more: bool = False,
    ) -> None:
        self.items = items
        self.next_cursor = next_cursor
        self.has_more = has_more


class CursorPaginator(_PaginatorBase[T]):
    """Generic cursor pager. Resources supply a sync or async page-fetch callable."""

    def __init__(
        self,
        *,
        sync_fetch: PageFn[T] | None = None,
        async_fetch: AsyncPageFn[T] | None = None,
        initial_cursor: Any = 0,
    ) -> None:
        super().__init__()
        if sync_fetch is None and async_fetch is None:
            raise ValueError("CursorPaginator needs at least one of sync_fetch / async_fetch")
        self._sync_fetch = sync_fetch
        self._async_fetch = async_fetch
        self.cursor: Any = initial_cursor

    def _advance(self) -> list[T]:
        if self._sync_fetch is None:
            raise RuntimeError("This paginator is async-only.")
        page = self._sync_fetch(self.cursor)
        self.cursor = page.next_cursor
        self.has_more = page.has_more
        return page.items

    async def _aadvance(self) -> list[T]:
        if self._async_fetch is None:
            raise RuntimeError("This paginator is sync-only.")
        page = await self._async_fetch(self.cursor)
        self.cursor = page.next_cursor
        self.has_more = page.has_more
        return page.items


class PagePaginator(CursorPaginator[T]):
    """Page-number pager. Same surface as :class:`CursorPaginator`, just named for clarity."""

    def __init__(
        self,
        *,
        sync_fetch: PageFn[T] | None = None,
        async_fetch: AsyncPageFn[T] | None = None,
        initial_page: int = 1,
    ) -> None:
        super().__init__(
            sync_fetch=sync_fetch, async_fetch=async_fetch, initial_cursor=initial_page
        )


class OffsetPaginator(CursorPaginator[T]):
    """Offset/limit pager. Identical to :class:`CursorPaginator`, but cursor is the offset."""

    def __init__(
        self,
        *,
        sync_fetch: PageFn[T] | None = None,
        async_fetch: AsyncPageFn[T] | None = None,
        initial_offset: int = 0,
    ) -> None:
        super().__init__(
            sync_fetch=sync_fetch, async_fetch=async_fetch, initial_cursor=initial_offset
        )
