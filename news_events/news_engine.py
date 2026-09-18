"""News normalization interface.

Normalizes incoming news records into a stable internal representation.
This module does not score sentiment, estimate impact, or make trading
decisions.
"""

from __future__ import annotations

from collections.abc import Mapping
from datetime import datetime
from typing import Any


def _normalize_timestamp(value: Any) -> Any:
    if value is None:
        return None

    if isinstance(value, datetime):
        if value.tzinfo is None or value.utcoffset() is None:
            raise ValueError("timestamp must be timezone-aware")
        return value

    if isinstance(value, str):
        text = value.strip()
        if not text:
            return None
        try:
            parsed = datetime.fromisoformat(text.replace("Z", "+00:00"))
        except ValueError as exc:
            raise ValueError("timestamp must be ISO-8601") from exc
        if parsed.tzinfo is None or parsed.utcoffset() is None:
            raise ValueError("timestamp must be timezone-aware")
        return parsed

    raise TypeError("timestamp must be datetime, ISO-8601 string, or None")


def _text(value: Any, field: str) -> str:
    if value is None:
        return ""
    if not isinstance(value, str):
        raise TypeError(f"{field} must be a string")
    return value.strip()


def _tuple_of_strings(value: Any, field: str) -> tuple[str, ...]:
    if value is None:
        return ()
    if isinstance(value, (str, bytes)):
        raise TypeError(f"{field} must be an iterable of strings")

    try:
        items = tuple(value)
    except TypeError as exc:
        raise TypeError(f"{field} must be iterable") from exc

    result = []
    for item in items:
        if not isinstance(item, str):
            raise TypeError(f"{field} must contain only strings")
        text = item.strip()
        if text:
            result.append(text)

    return tuple(result)


def normalize_news(item: Mapping[str, Any]) -> dict[str, Any]:
    """Normalize one incoming news item without mutating the source."""
    if not isinstance(item, Mapping):
        raise TypeError("item must be a mapping")

    return {
        "timestamp": _normalize_timestamp(item.get("timestamp")),
        "title": _text(item.get("title", ""), "title"),
        "source": _text(item.get("source", ""), "source"),
        "url": _text(item.get("url", ""), "url"),
        "symbols": _tuple_of_strings(item.get("symbols", ()), "symbols"),
        "topics": _tuple_of_strings(item.get("topics", ()), "topics"),
    }


def validate_news(item: Mapping[str, Any]) -> bool:
    """Return whether an input item can be normalized successfully."""
    try:
        normalize_news(item)
    except (TypeError, ValueError):
        return False
    return True
