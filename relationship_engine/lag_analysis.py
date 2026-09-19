from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from math import isfinite
from typing import Sequence


@dataclass(frozen=True)
class LagAnalysisResult:
    """Timestamp-aligned lag relationship result."""

    lag: int
    correlation: float | None
    sample_size: int
    aligned_timestamps: tuple[datetime, ...]
    market_values: tuple[float, ...]
    company_values: tuple[float, ...]
    calculation_method: str
    causation_claim: bool = False

    def validate(self) -> None:
        if self.lag < 0:
            raise ValueError("lag cannot be negative")

        if self.correlation is not None:
            if not isfinite(float(self.correlation)):
                raise ValueError("correlation must be finite")

            if not -1.0 <= float(self.correlation) <= 1.0:
                raise ValueError(
                    "correlation must be between -1 and 1"
                )

        if self.sample_size < 0:
            raise ValueError("sample_size cannot be negative")

        if self.sample_size != len(self.aligned_timestamps):
            raise ValueError(
                "sample_size must equal aligned timestamp count"
            )

        if len(self.market_values) != self.sample_size:
            raise ValueError(
                "market value count must equal sample size"
            )

        if len(self.company_values) != self.sample_size:
            raise ValueError(
                "company value count must equal sample size"
            )

        if not self.calculation_method:
            raise ValueError(
                "calculation_method cannot be empty"
            )

        if self.causation_claim:
            raise ValueError(
                "lag analysis must not make causation claims"
            )

        previous: datetime | None = None

        for timestamp in self.aligned_timestamps:
            if not isinstance(timestamp, datetime):
                raise ValueError(
                    "aligned timestamps must be datetime values"
                )

            if timestamp.tzinfo is None or timestamp.utcoffset() is None:
                raise ValueError(
                    "aligned timestamps must be timezone-aware"
                )

            normalized = timestamp.astimezone(timezone.utc)

            if previous is not None and normalized <= previous:
                raise ValueError(
                    "aligned timestamps must be strictly chronological"
                )

            previous = normalized


def _utc_timestamp(value: datetime) -> datetime:
    if not isinstance(value, datetime):
        raise ValueError("timestamp must be a datetime")

    if value.tzinfo is None or value.utcoffset() is None:
        raise ValueError(
            "timestamp must be a timezone-aware UTC timestamp"
        )

    return value.astimezone(timezone.utc)


def _pearson(
    x: Sequence[float],
    y: Sequence[float],
) -> float | None:
    if len(x) != len(y):
        raise ValueError(
            "series must have equal length"
        )

    n = len(x)

    if n < 2:
        return None

    mean_x = sum(x) / n
    mean_y = sum(y) / n

    numerator = sum(
        (a - mean_x) * (b - mean_y)
        for a, b in zip(x, y)
    )

    denominator_x = sum(
        (a - mean_x) ** 2
        for a in x
    )

    denominator_y = sum(
        (b - mean_y) ** 2
        for b in y
    )

    denominator = (
        denominator_x * denominator_y
    ) ** 0.5

    if denominator == 0:
        return None

    value = numerator / denominator

    return max(-1.0, min(1.0, value))


def _validate_timestamped_inputs(
    market_timestamps: Sequence[datetime],
    market_values: Sequence[float],
    company_timestamps: Sequence[datetime],
    company_values: Sequence[float],
) -> tuple[
    tuple[datetime, ...],
    tuple[float, ...],
    tuple[datetime, ...],
    tuple[float, ...],
]:
    if len(market_timestamps) != len(market_values):
        raise ValueError(
            "market timestamps and values must have equal length"
        )

    if len(company_timestamps) != len(company_values):
        raise ValueError(
            "company timestamps and values must have equal length"
        )

    market_ts = tuple(
        _utc_timestamp(timestamp)
        for timestamp in market_timestamps
    )

    company_ts = tuple(
        _utc_timestamp(timestamp)
        for timestamp in company_timestamps
    )

    if len(set(market_ts)) != len(market_ts):
        raise ValueError(
            "duplicate market timestamps are not allowed"
        )

    if len(set(company_ts)) != len(company_ts):
        raise ValueError(
            "duplicate company timestamps are not allowed"
        )

    if market_ts != tuple(sorted(market_ts)):
        raise ValueError(
            "market timestamps must be chronological"
        )

    if company_ts != tuple(sorted(company_ts)):
        raise ValueError(
            "company timestamps must be chronological"
        )

    normalized_market_values = tuple(
        float(value)
        for value in market_values
    )

    normalized_company_values = tuple(
        float(value)
        for value in company_values
    )

    if not all(
        isfinite(value)
        for value in normalized_market_values
    ):
        raise ValueError(
            "market values must be finite"
        )

    if not all(
        isfinite(value)
        for value in normalized_company_values
    ):
        raise ValueError(
            "company values must be finite"
        )

    return (
        market_ts,
        normalized_market_values,
        company_ts,
        normalized_company_values,
    )


def analyze_lag(
    market_timestamps: Sequence[datetime],
    market_values: Sequence[float],
    company_timestamps: Sequence[datetime],
    company_values: Sequence[float],
    *,
    lag: int = 0,
) -> LagAnalysisResult:
    """
    Calculate a timestamp-aware lag relationship.

    Semantics:

        lag=0:
            market[t] -> company[t]

        lag=1:
            market[t] -> company[t+1 observation]

        lag=2:
            market[t] -> company[t+2 observation]

    Positive lag therefore means the market observation precedes
    the company observation by the requested number of observations.

    Pairing is based on chronological observation order.
    No timestamps are fabricated, filled, or silently truncated.
    """

    if not isinstance(lag, int):
        raise TypeError("lag must be an integer")

    if lag < 0:
        raise ValueError(
            "lag must be >= 0"
        )

    (
        market_ts,
        market_vals,
        company_ts,
        company_vals,
    ) = _validate_timestamped_inputs(
        market_timestamps,
        market_values,
        company_timestamps,
        company_values,
    )

    pairs: list[
        tuple[datetime, float, float]
    ] = []

    max_index = min(
        len(market_ts),
        len(company_ts) - lag,
    )

    for market_index in range(max_index):
        company_index = market_index + lag

        pairs.append(
            (
                company_ts[company_index],
                market_vals[market_index],
                company_vals[company_index],
            )
        )

    pairs.sort(key=lambda item: item[0])

    aligned_timestamps = tuple(
        item[0]
        for item in pairs
    )

    aligned_market = tuple(
        item[1]
        for item in pairs
    )

    aligned_company = tuple(
        item[2]
        for item in pairs
    )

    correlation = _pearson(
        aligned_market,
        aligned_company,
    )

    result = LagAnalysisResult(
        lag=lag,
        correlation=correlation,
        sample_size=len(pairs),
        aligned_timestamps=aligned_timestamps,
        market_values=aligned_market,
        company_values=aligned_company,
        calculation_method=(
            "timestamp-aware observation-step lagged Pearson correlation"
        ),
        causation_claim=False,
    )

    result.validate()

    return result


def analyze_multiple_lags(
    market_timestamps: Sequence[datetime],
    market_values: Sequence[float],
    company_timestamps: Sequence[datetime],
    company_values: Sequence[float],
    lags: Sequence[int],
) -> tuple[LagAnalysisResult, ...]:
    """
    Calculate several lag observations independently.
    """

    normalized_lags = tuple(lags)

    if len(set(normalized_lags)) != len(normalized_lags):
        raise ValueError(
            "duplicate lag values are not allowed"
        )

    return tuple(
        analyze_lag(
            market_timestamps,
            market_values,
            company_timestamps,
            company_values,
            lag=lag,
        )
        for lag in normalized_lags
    )


def strongest_observed_lag(
    results: Sequence[LagAnalysisResult],
) -> LagAnalysisResult | None:
    """
    Return the lag with the largest absolute observed
    correlation.

    This is a descriptive statistic only.
    It does not establish causation or predictive validity.
    """

    valid = [
        result
        for result in results
        if result.correlation is not None
    ]

    if not valid:
        return None

    return max(
        valid,
        key=lambda result: abs(
            float(result.correlation)
        ),
    )


__all__ = [
    "LagAnalysisResult",
    "analyze_lag",
    "analyze_multiple_lags",
    "strongest_observed_lag",
]
