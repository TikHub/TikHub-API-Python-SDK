"""Internal type aliases and sentinels."""

from __future__ import annotations

from typing import Any, Final


class _NotGivenType:
    """Sentinel marker distinct from ``None``.

    Used so a method can tell "user explicitly passed ``None``" apart from
    "user passed nothing at all". Compares only by identity.
    """

    _singleton: _NotGivenType | None = None

    def __new__(cls) -> _NotGivenType:
        if cls._singleton is None:
            cls._singleton = super().__new__(cls)
        return cls._singleton

    def __repr__(self) -> str:
        return "NOT_GIVEN"

    def __bool__(self) -> bool:
        return False


NOT_GIVEN: Final[Any] = _NotGivenType()
"""Sentinel value used as a default for unset optional kwargs."""


JSON = Any
"""Loose alias for any JSON-serializable value."""
