"""Historical company/market relationship calculations.

This module preserves the legacy numeric-sequence API while adding the
canonical timestamp-aware alignment contract.

For timestamped observations, alignment is performed by exact UTC timestamp
intersection. No positional pairing, silent truncation, filling, or sorting
is performed here. Correlation remains an association measure only and never
claims causation.
"""

from __future__ import annotations

from statistics import mean
from typing import Any, Mapping, Sequence

from calculation.timestamp_alignment import (
    TimestampAlignmentError,
    align_timestamp_intersection,
)


def _is_timestamped(values: Sequence[Any]) -> bool:
    return bool(values) and isinstance(values[0], Mapping)


def _aligned(a, b):
    """Legacy positional alignment retained for numeric-only compatibility."""
    n = min(len(a), len(b))
    return list(map(float, a[-n:])), list(map(float, b[-n:]))


def _pearson(a, b):
    """Calculate Pearson correlation for already aligned numeric sequences."""
    n = min(len(a), len(b))
    if n < 2:
        return None

    a, b = _aligned(a, b)
    ma, mb = mean(a), mean(b)
    da = [x - ma for x in a]
    db = [x - mb for x in b]
    den = (sum(x * x for x in da) * sum(x * x for x in db)) ** 0.5
    return sum(x * y for x, y in zip(da, db)) / den if den else None


def _calculate_timestamped(market_returns, company_returns, benchmark_returns=None):
    aligned = align_timestamp_intersection(market_returns, company_returns)

    pairs = aligned["pairs"]
    result = {
        "sample_size": aligned["sample_size"],
        "correlation": _pearson(
            [pair[0] for pair in pairs],
            [pair[1] for pair in pairs],
        ),
        "mean_market_return": (
            mean(pair[0] for pair in pairs) if pairs else None
        ),
        "mean_company_return": (
            mean(pair[1] for pair in pairs) if pairs else None
        ),
        "aligned_timestamps": aligned["aligned_timestamps"],
        "pairs": pairs,
        "left_count": aligned["left_count"],
        "right_count": aligned["right_count"],
        "status": aligned["status"],
        "causation_claim": False,
    }

    if benchmark_returns is not None:
        benchmark_aligned = align_timestamp_intersection(
            benchmark_returns,
            company_returns,
        )
        benchmark_pairs = benchmark_aligned["pairs"]

        result["benchmark_aligned_timestamps"] = (
            benchmark_aligned["aligned_timestamps"]
        )
        result["benchmark_pairs"] = benchmark_pairs
        result["benchmark_excess_return_mean"] = (
            mean(company - benchmark for benchmark, company in benchmark_pairs)
            if benchmark_pairs
            else None
        )

    return result


def calculate(market_returns, company_returns, benchmark_returns=None):
    """Calculate historical company/market association evidence.

    Timestamped input must contain mappings with ``timestamp`` and ``value``.
    Numeric sequences continue to use the legacy positional API for backward
    compatibility. New historical pipelines must use timestamped observations.
    """
    if _is_timestamped(market_returns) or _is_timestamped(company_returns):
        if not (
            _is_timestamped(market_returns)
            and _is_timestamped(company_returns)
        ):
            raise TimestampAlignmentError(
                "market and company observations must both be timestamped"
            )

        return _calculate_timestamped(
            market_returns,
            company_returns,
            benchmark_returns,
        )

    m, c = _aligned(market_returns, company_returns)

    result = {
        "sample_size": len(m),
        "correlation": _pearson(m, c),
        "mean_market_return": mean(m) if m else None,
        "mean_company_return": mean(c) if c else None,
        "causation_claim": False,
        "status": "calculated" if len(m) >= 2 else "insufficient_data",
    }

    if benchmark_returns is not None:
        b, c2 = _aligned(benchmark_returns, company_returns)
        n = min(len(b), len(c2))
        result["benchmark_excess_return_mean"] = (
            mean(c2[-n:][i] - b[-n:][i] for i in range(n))
            if n
            else None
        )

    return result


__all__ = ["calculate"]
