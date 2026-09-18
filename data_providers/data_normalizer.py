"""Normalize provider records into stable, timestamp-aware OHLCV records.

The normalizer is intentionally provider-neutral. It does not invent timestamps,
fill missing observations, sort data silently, truncate mismatched series, or
apply corporate-action adjustments.
"""

from collections.abc import Mapping
from datetime import datetime, timezone
import math


_REQUIRED_FIELDS = ("timestamp", "open", "high", "low", "close", "volume")


def _number(value, field):
    if value is None:
        raise ValueError(f"missing {field}")
    try:
        number = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"invalid {field}") from exc
    if not math.isfinite(number):
        raise ValueError(f"non_finite {field}")
    return number


def _timestamp(value):
    if value is None:
        raise ValueError("missing timestamp")

    if isinstance(value, datetime):
        dt = value
    elif isinstance(value, str):
        text = value.strip()
        if not text:
            raise ValueError("empty timestamp")
        if text.endswith("Z"):
            text = text[:-1] + "+00:00"
        try:
            dt = datetime.fromisoformat(text)
        except ValueError as exc:
            raise ValueError("invalid timestamp") from exc
    else:
        raise TypeError("timestamp must be a datetime or ISO-8601 string")

    if dt.tzinfo is None or dt.utcoffset() is None:
        raise ValueError("timestamp must be timezone-aware")

    return dt.astimezone(timezone.utc)


def normalize_records(records):
    """Normalize provider rows without changing observation membership.

    Requirements:
    - every row must contain the canonical OHLCV fields;
    - timestamps must be timezone-aware and are normalized to UTC;
    - timestamps must already be strictly chronological;
    - duplicate timestamps are rejected;
    - no gaps are filled and no rows are silently dropped;
    - OHLC values must be finite and internally valid.
    """
    if records is None:
        raise ValueError("records must not be None")

    out = []
    previous_timestamp = None
    seen = set()

    for index, row in enumerate(records):
        if not isinstance(row, Mapping):
            raise TypeError(f"record_{index} must be a mapping")

        missing = [field for field in _REQUIRED_FIELDS if field not in row]
        if missing:
            raise ValueError(
                f"record_{index}:missing_fields:{','.join(missing)}"
            )

        timestamp = _timestamp(row["timestamp"])
        if timestamp in seen:
            raise ValueError(f"record_{index}:duplicate_timestamp")
        if previous_timestamp is not None and timestamp <= previous_timestamp:
            raise ValueError(f"record_{index}:non_increasing_timestamp")

        item = {
            "timestamp": timestamp,
            "open": _number(row["open"], "open"),
            "high": _number(row["high"], "high"),
            "low": _number(row["low"], "low"),
            "close": _number(row["close"], "close"),
            "volume": _number(row["volume"], "volume"),
        }

        if item["high"] < max(item["open"], item["close"]):
            raise ValueError(f"record_{index}:high_is_below_open_close")
        if item["low"] > min(item["open"], item["close"]):
            raise ValueError(f"record_{index}:low_is_above_open_close")
        if item["high"] < item["low"]:
            raise ValueError(f"record_{index}:high_is_below_low")

        out.append(item)
        seen.add(timestamp)
        previous_timestamp = timestamp

    return out
