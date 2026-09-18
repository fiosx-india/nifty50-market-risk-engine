"""Earnings event record.

Records earnings observations only; no impact, probability, or trading decision
is produced here.
"""

from __future__ import annotations

from collections.abc import Mapping
from datetime import datetime
from math import isfinite
from typing import Any


def _validate_timestamp(timestamp: Any) -> Any:
    if isinstance(timestamp, datetime):
        if timestamp.tzinfo is None or timestamp.utcoffset() is None:
            raise ValueError("timestamp must be timezone-aware")
        return timestamp

    if isinstance(timestamp, str):
        text = timestamp.strip()
        if not text:
            raise ValueError("timestamp string must not be empty")
        try:
            parsed = datetime.fromisoformat(text.replace("Z", "+00:00"))
        except ValueError as exc:
            raise ValueError("timestamp string must be ISO-8601") from exc
        if parsed.tzinfo is None or parsed.utcoffset() is None:
            raise ValueError("timestamp string must be timezone-aware")
        return parsed

    raise TypeError("timestamp must be a timezone-aware datetime or ISO-8601 string")


def _optional_number(value: Any, name: str) -> Any:
    if value is None:
        return None
    number = float(value)
    if not isfinite(number):
        raise ValueError(f"{name} must be finite")
    return number


def earnings_event(
    symbol: str,
    timestamp: Any,
    period: str,
    actual: Any = None,
    estimate: Any = None,
) -> dict[str, Any]:
    """Create a validated earnings event record."""
    if not isinstance(symbol, str) or not symbol.strip():
        raise ValueError("symbol must be a non-empty string")
    if not isinstance(period, str) or not period.strip():
        raise ValueError("period must be a non-empty string")

    return {
        "symbol": symbol.strip(),
        "timestamp": _validate_timestamp(timestamp),
        "period": period.strip(),
        "actual": _optional_number(actual, "actual"),
        "estimate": _optional_number(estimate, "estimate"),
        "event_type": "earnings",
    }


def validate_earnings_event(event: Mapping[str, Any]) -> bool:
    """Validate the basic schema of an earnings event."""
    if not isinstance(event, Mapping):
        return False
    try:
        record = earnings_event(
            event["symbol"],
            event["timestamp"],
            event["period"],
            event.get("actual"),
            event.get("estimate"),
        )
    except (KeyError, TypeError, ValueError):
        return False
    return record["event_type"] == "earnings"
