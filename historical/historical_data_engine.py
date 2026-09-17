"""Provider-neutral, timestamp-aware historical data contract.

This module owns the historical-series container and structural validation.
It does not fetch vendor data, calculate relationships, generate signals, or
make causation claims.

The canonical representation is a sequence of UTC, timezone-aware
observations with aligned OHLCV fields. Missing timestamps remain gaps; this
module never fills or silently removes them.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from math import isfinite
from typing import Any, Mapping, Sequence


class HistoricalSeriesValidationError(ValueError):
    """Raised when a historical series violates its structural contract."""


def _utc_timestamp(value: Any) -> datetime:
    if not isinstance(value, datetime):
        raise HistoricalSeriesValidationError(
            "timestamps must be datetime values"
        )
    if value.tzinfo is None or value.utcoffset() is None:
        raise HistoricalSeriesValidationError(
            "timestamps must be timezone-aware UTC datetimes"
        )
    return value.astimezone(timezone.utc)


def _numeric(value: Any, field: str) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError) as exc:
        raise HistoricalSeriesValidationError(
            f"{field} must be numeric"
        ) from exc
    if not isfinite(number):
        raise HistoricalSeriesValidationError(
            f"{field} must be finite"
        )
    return number


@dataclass(frozen=True)
class HistoricalSeries:
    """Immutable timestamped OHLCV historical series.

    Tuple fields preserve observation order. Validation is explicit through
    ``validate_series`` so existing construction remains backward compatible.
    """

    symbol: str
    timestamps: tuple
    open: tuple
    high: tuple
    low: tuple
    close: tuple
    volume: tuple
    source: str
    timezone: str = "UTC"


def validate_series(series: HistoricalSeries) -> bool:
    """Validate structure, timestamp integrity, and basic OHLCV values.

    Returns ``True`` for a valid series. Invalid input raises
    ``HistoricalSeriesValidationError`` rather than silently returning false.
    """
    if not isinstance(series, HistoricalSeries):
        raise HistoricalSeriesValidationError(
            "series must be a HistoricalSeries instance"
        )

    fields = (
        series.timestamps,
        series.open,
        series.high,
        series.low,
        series.close,
        series.volume,
    )
    if any(not isinstance(values, tuple) for values in fields):
        raise HistoricalSeriesValidationError(
            "historical fields must be tuples"
        )

    n = len(series.timestamps)
    if any(len(values) != n for values in fields[1:]):
        raise HistoricalSeriesValidationError(
            "all historical fields must have equal length"
        )

    previous: datetime | None = None
    seen: set[datetime] = set()

    for index, timestamp in enumerate(series.timestamps):
        utc_timestamp = _utc_timestamp(timestamp)

        if utc_timestamp in seen:
            raise HistoricalSeriesValidationError(
                f"duplicate timestamp at index {index}: "
                f"{utc_timestamp.isoformat()}"
            )

        if previous is not None and utc_timestamp <= previous:
            raise HistoricalSeriesValidationError(
                "timestamps must be strictly chronological"
            )

        seen.add(utc_timestamp)
        previous = utc_timestamp

        o = _numeric(series.open[index], "open")
        h = _numeric(series.high[index], "high")
        l = _numeric(series.low[index], "low")
        c = _numeric(series.close[index], "close")
        v = _numeric(series.volume[index], "volume")

        if h < max(o, c):
            raise HistoricalSeriesValidationError(
                f"high is below open/close at index {index}"
            )
        if l > min(o, c):
            raise HistoricalSeriesValidationError(
                f"low is above open/close at index {index}"
            )
        if h < l:
            raise HistoricalSeriesValidationError(
                f"high is below low at index {index}"
            )
        if v < 0:
            raise HistoricalSeriesValidationError(
                f"volume cannot be negative at index {index}"
            )

    return True


def historical_series_from_records(
    records: Sequence[Mapping[str, Any]],
    *,
    symbol: str,
    source: str,
    timezone_name: str = "UTC",
) -> HistoricalSeries:
    """Build a HistoricalSeries from canonical timestamped OHLCV mappings.

    Required keys are ``timestamp``, ``open``, ``high``, ``low``, ``close``,
    and ``volume``. Input order is preserved; it is never silently sorted.
    """
    rows = list(records)

    timestamps = []
    opens = []
    highs = []
    lows = []
    closes = []
    volumes = []

    for index, record in enumerate(rows):
        if not isinstance(record, Mapping):
            raise HistoricalSeriesValidationError(
                f"record {index} must be a mapping"
            )

        required = ("timestamp", "open", "high", "low", "close", "volume")
        missing = [key for key in required if key not in record]
        if missing:
            raise HistoricalSeriesValidationError(
                f"record {index} missing fields: {', '.join(missing)}"
            )

        timestamps.append(_utc_timestamp(record["timestamp"]))
        opens.append(_numeric(record["open"], "open"))
        highs.append(_numeric(record["high"], "high"))
        lows.append(_numeric(record["low"], "low"))
        closes.append(_numeric(record["close"], "close"))
        volumes.append(_numeric(record["volume"], "volume"))

    series = HistoricalSeries(
        symbol=str(symbol),
        timestamps=tuple(timestamps),
        open=tuple(opens),
        high=tuple(highs),
        low=tuple(lows),
        close=tuple(closes),
        volume=tuple(volumes),
        source=str(source),
        timezone=str(timezone_name),
    )
    validate_series(series)
    return series


def series_to_records(series: HistoricalSeries) -> tuple[dict[str, Any], ...]:
    """Convert a validated series into canonical timestamped observations."""
    validate_series(series)
    return tuple(
        {
            "timestamp": _utc_timestamp(series.timestamps[index]),
            "open": series.open[index],
            "high": series.high[index],
            "low": series.low[index],
            "close": series.close[index],
            "volume": series.volume[index],
        }
        for index in range(len(series.timestamps))
    )


__all__ = [
    "HistoricalSeries",
    "HistoricalSeriesValidationError",
    "validate_series",
    "historical_series_from_records",
    "series_to_records",
]
