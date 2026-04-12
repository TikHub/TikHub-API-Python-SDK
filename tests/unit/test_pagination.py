"""Pagination scaffolding tests."""

from __future__ import annotations

from typing import Any

from tikhub import CursorPaginator, OffsetPaginator, Page, PagePaginator


def _make_sync_pages(*pages: list[int]):
    state = {"i": 0}

    def fetch(_cursor: Any) -> Page[int]:
        i = state["i"]
        state["i"] = i + 1
        items = pages[i]
        last = i == len(pages) - 1
        return Page(items, next_cursor=i + 1, has_more=not last)

    return fetch


def test_cursor_paginator_iter():
    pager = CursorPaginator(sync_fetch=_make_sync_pages([1, 2], [3, 4], [5]))
    assert list(pager) == [1, 2, 3, 4, 5]


def test_cursor_paginator_first():
    pager = CursorPaginator(sync_fetch=_make_sync_pages([1, 2], [3, 4], [5, 6]))
    assert pager.first(3) == [1, 2, 3]


def test_page_paginator_initial_cursor():
    pager = PagePaginator(sync_fetch=_make_sync_pages([10]), initial_page=5)
    assert pager.cursor == 5
    assert list(pager) == [10]


def test_offset_paginator_initial_offset():
    pager = OffsetPaginator(sync_fetch=_make_sync_pages([7, 8]), initial_offset=20)
    assert pager.cursor == 20
    assert list(pager) == [7, 8]


async def test_cursor_paginator_async_iter():
    state = {"i": 0}

    async def fetch(_cursor: Any) -> Page[int]:
        i = state["i"]
        state["i"] = i + 1
        pages = ([1, 2], [3, 4], [5])
        items = pages[i]
        last = i == len(pages) - 1
        return Page(items, next_cursor=i + 1, has_more=not last)

    pager = CursorPaginator[int](async_fetch=fetch)
    out: list[int] = []
    async for item in pager:
        out.append(item)
    assert out == [1, 2, 3, 4, 5]
