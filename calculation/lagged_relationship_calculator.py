"""Timestamp-aware lagged company/market observations.

Canonical lag direction:
    market[t] -> company[t + lag]

Timestamped observations are mappings containing ``timestamp`` and ``value``.
They must use timezone-aware UTC datetimes, be strictly chronological, and
contain no duplicate timestamps.

Numeric sequences remain supported for backward compatibility. New historical
pipelines should use timestamped observations.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Mapping, Sequence


class TimestampLagAlignmentError(ValueError):
    """Raised when timestamped lag inputs violate the alignment contract."""


def _is_timestamped(values: Sequence[Any]) -> bool:
    return bool(values) and isinstance(values[0], Mapping)


def _validate_timestamped(values: Sequence[Mapping[str, Any]], name: str):
    previous = None
    seen = set()

    for index, item in enumerate(values):
        if not isinstance(item, Mapping):
            raise TimestampLagAlignmentError(
                f"{name}[{index}] must be a timestamped observation"
            )

        if "timestamp" not in item or "value" not in item:
            raise TimestampLagAlignmentError(
                f"{name}[{index}] requires timestamp and value"
            )

        timestamp = item["timestamp"]

        if not isinstance(timestamp, datetime):
            raise TimestampLagAlignmentError(
                f"{name}[{index}] timestamp must be a datetime"
            )

        if timestamp.tzinfo is None or timestamp.utcoffset() is None:
            raise TimestampLagAlignmentError(
                "timezone-aware UTC timestamp required"
            )

        utc_timestamp = timestamp.astimezone(timezone.utc)

        if utc_timestamp in seen:
            raise TimestampLagAlignmentError(
                f"duplicate timestamp in {name}"
            )

        if previous is not None and utc_timestamp <= previous:
            raise TimestampLagAlignmentError(
                f"{name} must be chronologically ordered"
            )

        seen.add(utc_timestamp)
        previous = utc_timestamp

    return values


def _timestamped_lags(market_returns, company_returns, lag):
    _validate_timestamped(market_returns, "market")
    _validate_timestamped(company_returns, "company")

    company_by_timestamp = {
        item["timestamp"].astimezone(timezone.utc): item for item in company_returns
    }

    market_items = [
        (
            item["timestamp"].astimezone(timezone.utc),
            float(item["value"]),
        )
        for item in market_returns
    ]

    company_times = [
        item["timestamp"].astimezone(timezone.utc)
        for item in company_returns
    ]

    # Lag is measured in observations within the company series, not by
    # fabricating a clock interval. This preserves the requested
    # market[t] -> company[t + lag] semantics.
    pairs = []
    aligned_timestamps = []

    for index, (market_timestamp, market_value) in enumerate(market_items):
        target_index = index + lag

        if target_index >= len(company_times):
            continue

        company_timestamp = company_times[target_index]

        # Never allow a future market observation to explain an earlier
        # company observation.
        if market_timestamp >= company_timestamp:
            continue

        company_item = company_by_timestamp.get(company_timestamp)
        if company_item is None:
            continue

        pairs.append((market_value, float(company_item["value"])))
        aligned_timestamps.append((market_timestamp, company_timestamp))

    return {
        "lag": lag,
        "sample_size": len(pairs),
        "pairs": pairs,
        "aligned_timestamps": aligned_timestamps,
        "status": "calculated" if pairs else "insufficient_data",
    }


def calculate_lags(market_returns, company_returns, lags):
    """Calculate lagged market/company pairs.

    For timestamped observations, positive lag means:
        market[t] -> company[t + lag]

    Missing observations are never fabricated and timestamp order is never
    silently repaired. Numeric input retains the historical positional API.
    """
    timestamped = _is_timestamped(market_returns) or _is_timestamped(company_returns)

    if timestamped:
        if not (
            _is_timestamped(market_returns)
            and _is_timestamped(company_returns)
        ):
            raise TimestampLagAlignmentError(
                "market and company observations must both be timestamped"
            )

        out = []
        for lag in lags:
            lag = int(lag)
            if lag < 0:
                raise ValueError("lag must be >= 0")
            out.append(_timestamped_lags(market_returns, company_returns, lag))
        return out

    # Legacy numeric compatibility.
    m = list(map(float, market_returns))
    c = list(map(float, company_returns))
    out = []

    for lag in lags:
        lag = int(lag)
        if lag < 0:
            raise ValueError("lag must be >= 0")

        n = min(len(m), len(c))
        pairs = (
            []
            if n <= lag
            else [(m[-n:][i], c[-n:][i + lag]) for i in range(n - lag)]
        )

        out.append(
            {
                "lag": lag,
                "sample_size": len(pairs),
                "pairs": pairs,
                "status": "calculated" if pairs else "insufficient_data",
            }
        )

    return out


__all__ = ["calculate_lags", "TimestampLagAlignmentError"]
