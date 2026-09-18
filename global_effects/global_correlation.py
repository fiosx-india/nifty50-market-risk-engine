"""Timestamp-aware global correlation helper.

Correlation is an association statistic only. No causation or directional
market conclusion is produced here.
"""

from statistics import mean
from typing import Any, Mapping, Sequence


def _timestamped(values: Sequence[Any]) -> bool:
    return bool(values) and isinstance(values[0], Mapping)


def _pearson(a, b):
    if len(a) < 2:
        return None
    ma, mb = mean(a), mean(b)
    da = [x - ma for x in a]
    db = [x - mb for x in b]
    den = (sum(x * x for x in da) * sum(x * x for x in db)) ** 0.5
    return sum(x * y for x, y in zip(da, db)) / den if den else None


def _align(left, right):
    left_by_ts = {row["timestamp"]: float(row["value"]) for row in left}
    right_by_ts = {row["timestamp"]: float(row["value"]) for row in right}
    timestamps = sorted(set(left_by_ts).intersection(right_by_ts))
    return (
        timestamps,
        [left_by_ts[t] for t in timestamps],
        [right_by_ts[t] for t in timestamps],
    )


def correlation(x, y):
    """Calculate correlation using timestamp intersection when available.

    Numeric sequences retain positional compatibility. New historical pipelines
    should pass mappings containing timestamp and value.
    """
    if _timestamped(x) or _timestamped(y):
        if not (_timestamped(x) and _timestamped(y)):
            raise ValueError("both inputs must be timestamped")
        timestamps, a, b = _align(x, y)
        return {
            "correlation": _pearson(a, b),
            "sample_size": len(timestamps),
            "aligned_timestamps": tuple(timestamps),
            "causation_claim": False,
        }

    n = min(len(x), len(y))
    if n < 2:
        return None
    a = list(map(float, x[-n:]))
    b = list(map(float, y[-n:]))
    return _pearson(a, b)
