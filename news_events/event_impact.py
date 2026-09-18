"""Event-study window preparation.

Prepares bounded observations around a known event index. This module does
not estimate event impact or make directional/trading decisions.
"""

from __future__ import annotations

from collections.abc import Sequence
from math import isfinite
from typing import Any


def _finite(values: Sequence[Any], name: str) -> list[float]:
    result = []
    for value in values:
        number = float(value)
        if not isfinite(number):
            raise ValueError(f"{name} must contain only finite numbers")
        result.append(number)
    return result


def _window_size(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")
    return value


def event_window(
    values: Sequence[Any],
    event_index: int,
    pre: int = 5,
    post: int = 20,
) -> dict[str, list[float]]:
    """Return observations before, at, and after an event index.

    Bounds are clipped to the available data. No padding, sorting, or
    truncation between separate datasets is performed here.
    """
    data = _finite(values, "values")

    if isinstance(event_index, bool) or not isinstance(event_index, int):
        raise TypeError("event_index must be an integer")
    if not 0 <= event_index < len(data):
        raise IndexError("event_index is outside the available observations")

    pre = _window_size(pre, "pre")
    post = _window_size(post, "post")

    start = max(0, event_index - pre)
    end = min(len(data), event_index + post + 1)

    return {
        "pre": data[start:event_index],
        "event": data[event_index:event_index + 1],
        "post": data[event_index + 1:end],
    }


def event_window_from_timestamp(
    observations: Sequence[dict[str, Any]],
    event_timestamp: Any,
    pre: int = 5,
    post: int = 20,
) -> dict[str, list[dict[str, Any]]]:
    """Prepare a window using an exact observation timestamp.

    Observations must be chronological, unique, and timezone-aware. The event
    timestamp must exactly match one observation; nearest-bar inference is not
    performed.
    """
    if not observations:
        raise ValueError("observations cannot be empty")

    timestamps = []
    for item in observations:
        if not isinstance(item, dict):
            raise TypeError("observations must contain mappings")
        timestamp = item.get("timestamp")
        if timestamp is None:
            raise ValueError("each observation requires timestamp")
        if getattr(timestamp, "tzinfo", None) is None or timestamp.utcoffset() is None:
            raise ValueError("observation timestamps must be timezone-aware")
        timestamps.append(timestamp)

    for previous, current in zip(timestamps, timestamps[1:]):
        if current <= previous:
            raise ValueError("timestamps must be strictly increasing and unique")

    if event_timestamp not in timestamps:
        raise ValueError("event_timestamp must exactly match an observation")

    index = timestamps.index(event_timestamp)
    pre = _window_size(pre, "pre")
    post = _window_size(post, "post")

    start = max(0, index - pre)
    end = min(len(observations), index + post + 1)

    return {
        "pre": list(observations[start:index]),
        "event": list(observations[index:index + 1]),
        "post": list(observations[index + 1:end]),
    }
