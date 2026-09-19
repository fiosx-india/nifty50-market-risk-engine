from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from math import isfinite
from typing import Iterable, Sequence


@dataclass(frozen=True)
class DataQualityReport:
    """
    Auditable quality report for timestamped market observations.

    This module validates data quality only.
    It does not calculate market relationships, predictions,
    trading signals, or causation.
    """

    status: str
    sample_size: int
    valid_count: int
    missing_count: int
    duplicate_count: int
    out_of_order_count: int
    invalid_ohlcv_count: int
    timezone_error_count: int
    coverage_start: datetime | None
    coverage_end: datetime | None
    issues: tuple[str, ...]
    calculation_safe: bool

    def validate(self) -> None:
        if self.status not in {"PASS", "WARN", "FAIL"}:
            raise ValueError("status must be PASS, WARN, or FAIL")

        for name, value in (
            ("sample_size", self.sample_size),
            ("valid_count", self.valid_count),
            ("missing_count", self.missing_count),
            ("duplicate_count", self.duplicate_count),
            ("out_of_order_count", self.out_of_order_count),
            ("invalid_ohlcv_count", self.invalid_ohlcv_count),
            ("timezone_error_count", self.timezone_error_count),
        ):
            if value < 0:
                raise ValueError(f"{name} cannot be negative")

        for timestamp in (self.coverage_start, self.coverage_end):
            if timestamp is not None:
                if timestamp.tzinfo is None:
                    raise ValueError(
                        "coverage timestamps must be timezone-aware UTC timestamps"
                    )
                if timestamp.utcoffset() != timezone.utc.utcoffset(timestamp):
                    raise ValueError(
                        "coverage timestamps must be normalized to UTC"
                    )

        if self.coverage_start and self.coverage_end:
            if self.coverage_start > self.coverage_end:
                raise ValueError(
                    "coverage_start cannot be later than coverage_end"
                )

        if not isinstance(self.calculation_safe, bool):
            raise ValueError("calculation_safe must be boolean")


def _normalize_timestamp(value: datetime) -> datetime:
    if not isinstance(value, datetime):
        raise ValueError("timestamp must be a datetime")

    if value.tzinfo is None or value.utcoffset() is None:
        raise ValueError(
            "timestamp must be a timezone-aware UTC timestamp"
        )

    return value.astimezone(timezone.utc)


def _finite(value: object) -> bool:
    try:
        return isfinite(float(value))
    except (TypeError, ValueError):
        return False


def validate_ohlcv(
    open_price: object,
    high: object,
    low: object,
    close: object,
    volume: object | None = None,
) -> bool:
    """
    Validate a single OHLCV observation.

    Rules:
    - all OHLC values must be finite
    - high >= low
    - open and close must lie within [low, high]
    - volume, when supplied, must be finite and non-negative
    """

    if not all(
        _finite(value)
        for value in (open_price, high, low, close)
    ):
        return False

    o = float(open_price)
    h = float(high)
    l = float(low)
    c = float(close)

    if h < l:
        return False

    if not (l <= o <= h):
        return False

    if not (l <= c <= h):
        return False

    if volume is not None:
        if not _finite(volume):
            return False

        if float(volume) < 0:
            return False

    return True


def assess_data_quality(
    observations: Iterable[object],
    *,
    require_volume: bool = False,
    minimum_sample_size: int = 2,
) -> DataQualityReport:
    """
    Assess timestamp ordering, duplicates, timezone validity,
    OHLCV validity, and minimum sample requirements.

    Each observation may be:
      - an object with timestamp/open/high/low/close/volume attributes
      - a mapping with the same keys
    """

    if minimum_sample_size < 1:
        raise ValueError("minimum_sample_size must be >= 1")

    rows = list(observations)

    sample_size = len(rows)

    missing_count = 0
    duplicate_count = 0
    out_of_order_count = 0
    invalid_ohlcv_count = 0
    timezone_error_count = 0

    issues: list[str] = []
    normalized_timestamps: list[datetime] = []

    def get_value(row: object, key: str) -> object:
        if isinstance(row, dict):
            return row.get(key)

        return getattr(row, key, None)

    previous_timestamp: datetime | None = None
    seen: set[datetime] = set()

    for index, row in enumerate(rows):
        timestamp = get_value(row, "timestamp")

        if timestamp is None:
            missing_count += 1
            issues.append(f"row {index}: missing timestamp")
            continue

        try:
            normalized = _normalize_timestamp(timestamp)
        except ValueError as exc:
            timezone_error_count += 1
            issues.append(f"row {index}: {exc}")
            continue

        normalized_timestamps.append(normalized)

        if normalized in seen:
            duplicate_count += 1
            issues.append(
                f"row {index}: duplicate timestamp {normalized.isoformat()}"
            )

        seen.add(normalized)

        if (
            previous_timestamp is not None
            and normalized < previous_timestamp
        ):
            out_of_order_count += 1
            issues.append(
                f"row {index}: timestamp is out of chronological order"
            )

        previous_timestamp = normalized

        open_price = get_value(row, "open")
        high = get_value(row, "high")
        low = get_value(row, "low")
        close = get_value(row, "close")
        volume = get_value(row, "volume")

        if require_volume and volume is None:
            invalid_ohlcv_count += 1
            issues.append(f"row {index}: missing volume")
            continue

        if not validate_ohlcv(
            open_price,
            high,
            low,
            close,
            volume,
        ):
            invalid_ohlcv_count += 1
            issues.append(f"row {index}: invalid OHLCV")

    valid_count = (
        sample_size
        - missing_count
        - timezone_error_count
        - invalid_ohlcv_count
    )

    valid_count = max(valid_count, 0)

    if sample_size == 0:
        status = "FAIL"
        issues.append("no observations supplied")

    elif valid_count < minimum_sample_size:
        status = "FAIL"
        issues.append(
            f"insufficient valid observations: "
            f"{valid_count} < {minimum_sample_size}"
        )

    elif (
        duplicate_count > 0
        or out_of_order_count > 0
        or timezone_error_count > 0
        or invalid_ohlcv_count > 0
    ):
        status = "FAIL"

    elif missing_count > 0:
        status = "WARN"

    else:
        status = "PASS"

    unique_valid_timestamps = sorted(set(normalized_timestamps))

    coverage_start = (
        unique_valid_timestamps[0]
        if unique_valid_timestamps
        else None
    )

    coverage_end = (
        unique_valid_timestamps[-1]
        if unique_valid_timestamps
        else None
    )

    calculation_safe = status == "PASS"

    report = DataQualityReport(
        status=status,
        sample_size=sample_size,
        valid_count=valid_count,
        missing_count=missing_count,
        duplicate_count=duplicate_count,
        out_of_order_count=out_of_order_count,
        invalid_ohlcv_count=invalid_ohlcv_count,
        timezone_error_count=timezone_error_count,
        coverage_start=coverage_start,
        coverage_end=coverage_end,
        issues=tuple(issues),
        calculation_safe=calculation_safe,
    )

    report.validate()
    return report


def validate_timestamp_sequence(
    timestamps: Sequence[datetime],
) -> DataQualityReport:
    """
    Validate only timestamp integrity.

    This is useful before relationship calculations.
    """

    rows = [
        {
            "timestamp": timestamp,
            "open": 1.0,
            "high": 1.0,
            "low": 1.0,
            "close": 1.0,
            "volume": 0.0,
        }
        for timestamp in timestamps
    ]

    return assess_data_quality(
        rows,
        require_volume=True,
        minimum_sample_size=1,
    )


def quality_status(
    observations: Iterable[object],
    *,
    require_volume: bool = False,
    minimum_sample_size: int = 2,
) -> str:
    """
    Convenience wrapper returning only PASS/WARN/FAIL.
    """

    return assess_data_quality(
        observations,
        require_volume=require_volume,
        minimum_sample_size=minimum_sample_size,
    ).status


__all__ = [
    "DataQualityReport",
    "validate_ohlcv",
    "assess_data_quality",
    "validate_timestamp_sequence",
    "quality_status",
]
