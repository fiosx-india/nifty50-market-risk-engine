"""Normalize provider records into stable OHLCV records."""
from collections.abc import Mapping

def _number(value, field):
    if value is None:
        raise ValueError(f"missing {field}")
    return float(value)

def normalize_records(records):
    out = []
    for row in records:
        if not isinstance(row, Mapping):
            raise TypeError("each record must be a mapping")
        item = {
            "timestamp": row.get("timestamp"),
            "open": _number(row.get("open"), "open"),
            "high": _number(row.get("high"), "high"),
            "low": _number(row.get("low"), "low"),
            "close": _number(row.get("close"), "close"),
            "volume": _number(row.get("volume"), "volume"),
        }
        if item["timestamp"] is None:
            raise ValueError("missing timestamp")
        if item["high"] < max(item["open"], item["close"]):
            raise ValueError("high is below open/close")
        if item["low"] > min(item["open"], item["close"]):
            raise ValueError("low is above open/close")
        out.append(item)
    return out
