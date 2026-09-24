from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from math import isfinite
from typing import Iterable, Mapping, Sequence


@dataclass(frozen=True)
class TimestampedReturn:
    """A single timestamped return observation."""

    timestamp: datetime
    value: float
    previous_timestamp: datetime

    def validate(self) -> None:
        if not isinstance(self.timestamp, datetime):
            raise ValueError("timestamp must be a datetime")

        if not isinstance(self.previous_timestamp, datetime):
            raise ValueError("previous_timestamp must be a datetime")

        if self.timestamp.tzinfo is None or self.timestamp.utcoffset() is None:
            raise ValueError(
                "timestamp must be a timezone-aware UTC timestamp"
            )

        if (
            self.previous_timestamp.tzinfo is None
            or self.previous_timestamp.utcoffset() is None
        ):
            raise ValueError(
                "previous_timestamp must be a timezone-aware UTC timestamp"
            )

        if self.timestamp.astimezone(timezone.utc) < (
            self.previous_timestamp.astimezone(timezone.utc)
        ):
            raise ValueError(
                "timestamp cannot be earlier than previous_timestamp"
            )

        if not isfinite(float(self.value)):
            raise ValueError("return value must be finite")


def _utc_timestamp(value: datetime) -> datetime:
    if not isinstance(value, datetime):
        raise ValueError("timestamp must be a datetime")

    if value.tzinfo is None or value.utcoffset() is None:
        raise ValueError(
            "timestamp must be a timezone-aware UTC timestamp"
        )

    return value.astimezone(timezone.utc)


def _close_from_observation(observation: object) -> float:
    if isinstance(observation, Mapping):
        value = observation.get("close")
    else:
        value = getattr(observation, "close", None)

    if value is None:
        raise ValueError("observation is missing close")

    try:
        result = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError("close must be numeric") from exc

    if not isfinite(result):
        raise ValueError("close must be finite")

    if result <= 0:
        raise ValueError("close must be greater than zero")

    return result


def _timestamp_from_observation(observation: object) -> datetime:
    if isinstance(observation, Mapping):
        value = observation.get("timestamp")
    else:
        value = getattr(observation, "timestamp", None)

    return _utc_timestamp(value)


def _validate_observations(
    observations: Iterable[object],
) -> list[tuple[datetime, float]]:
    rows = [
        (
            _timestamp_from_observation(observation),
            _close_from_observation(observation),
        )
        for observation in observations
    ]

    if not rows:
        return []

    timestamps = [timestamp for timestamp, _ in rows]

    if len(set(timestamps)) != len(timestamps):
        raise ValueError("duplicate timestamps are not allowed")

    if timestamps != sorted(timestamps):
        raise ValueError(
            "observations must be sorted chronologically"
        )

    return rows


def simple_returns(
    observations: Iterable[object],
) -> tuple[TimestampedReturn, ...]:
    """
    Calculate simple close-to-close returns.

    return[t] = close[t] / close[t-1] - 1

    The first observation has no return and is therefore omitted.
    No timestamps are fabricated or silently filled.
    """

    rows = _validate_observations(observations)

    if len(rows) < 2:
        return ()

    results: list[TimestampedReturn] = []

    for index in range(1, len(rows)):
        previous_timestamp, previous_close = rows[index - 1]
        timestamp, close = rows[index]

        value = close / previous_close - 1.0

        result = TimestampedReturn(
            timestamp=timestamp,
            value=value,
            previous_timestamp=previous_timestamp,
        )

        result.validate()
        results.append(result)

    return tuple(results)


def logarithmic_returns(
    observations: Iterable[object],
) -> tuple[TimestampedReturn, ...]:
    """
    Calculate continuously compounded close-to-close returns.

    log_return[t] = ln(close[t] / close[t-1])

    Implemented without silently dropping invalid observations.
    """

    from math import log

    rows = _validate_observations(observations)

    if len(rows) < 2:
        return ()

    results: list[TimestampedReturn] = []

    for index in range(1, len(rows)):
        previous_timestamp, previous_close = rows[index - 1]
        timestamp, close = rows[index]

        value = log(close / previous_close)

        result = TimestampedReturn(
            timestamp=timestamp,
            value=value,
            previous_timestamp=previous_timestamp,
        )

        result.validate()
        results.append(result)

    return tuple(results)


def return_map(
    observations: Iterable[object],
) -> dict[datetime, float]:
    """
    Convert simple returns into a timestamp -> return mapping.
    """

    results = simple_returns(observations)

    return {
        result.timestamp: result.value
        for result in results
    }


def align_returns(
    company_returns: Sequence[TimestampedReturn],
    market_returns: Sequence[TimestampedReturn],
) -> tuple[
    tuple[datetime, ...],
    tuple[float, ...],
    tuple[float, ...],
]:
    """
    Align company and market returns strictly by timestamp.

    No positional pairing.
    No forward fill.
    No interpolation.
    No silent truncation.

    Only timestamps present in both series are returned.
    """

    company_map = {
        item.timestamp: float(item.value)
        for item in company_returns
    }

    market_map = {
        item.timestamp: float(item.value)
        for item in market_returns
    }

    timestamps = tuple(
        sorted(set(company_map).intersection(market_map))
    )

    company_values = tuple(
        company_map[timestamp]
        for timestamp in timestamps
    )

    market_values = tuple(
        market_map[timestamp]
        for timestamp in timestamps
    )

    return timestamps, company_values, market_values

def cumulative_return(
    observations: Iterable[object],
) -> float | None:
    """
    Calculate cumulative simple return from timestamped OHLCV observations.

    cumulative_return = final_close / initial_close - 1

    Returns None when fewer than two observations exist.
    """

    rows = _validate_observations(observations)

    if len(rows) < 2:
        return None

    initial_close = rows[0][1]
    final_close = rows[-1][1]

    result = final_close / initial_close - 1.0

    if not isfinite(result):
        raise ValueError(
            "cumulative return must be finite"
        )

    return result

__all__ = [
    "TimestampedReturn",
    "simple_returns",
    "logarithmic_returns",
    "return_map",
    "align_returns",
    "calculate_return_series",
]
