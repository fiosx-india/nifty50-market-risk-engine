"""Indicator discovery registry; it does not orchestrate analysis.

The registry describes available indicator names by category. It does not
execute indicators or make market decisions.
"""

from __future__ import annotations

from types import MappingProxyType
from typing import Final


INDICATOR_REGISTRY: Final[dict[str, tuple[str, ...]]] = {
    "technical": (
        "sma", "ema", "wma", "roc", "momentum", "rsi", "atr",
        "bollinger", "vwap",
    ),
    "momentum": ("stochastic", "williams_r", "cci", "mfi"),
    "trend": ("adx", "supertrend_inputs", "ichimoku"),
    "volatility": (
        "returns", "realized_volatility", "volatility_percentile",
        "true_range_series",
    ),
    "volume": (
        "relative_volume", "obv", "accumulation_distribution",
        "price_volume_confirmation",
    ),
    "candlestick": (
        "doji", "hammer", "inverted_hammer", "shooting_star",
        "hanging_man", "bullish_engulfing", "bearish_engulfing",
        "spinning_top", "marubozu",
    ),
    "structure": (
        "swing_points", "structure_state", "bos", "liquidity_zones",
    ),
    "chart": (
        "higher_high", "higher_low", "lower_high", "lower_low",
        "range_levels", "breakout", "breakdown",
    ),
}

# Prevent accidental mutation of the top-level mapping while retaining the
# existing tuple-based category values.
_REGISTRY_VIEW = MappingProxyType(INDICATOR_REGISTRY)


def list_indicators(category: str | None = None):
    """Return registered indicator names.

    With no category, return a plain dictionary copy for backward
    compatibility. With a category, return an immutable tuple. Unknown
    categories return an empty tuple.
    """
    if category is None:
        return dict(_REGISTRY_VIEW)
    if not isinstance(category, str):
        raise TypeError("category must be a string or None")
    return _REGISTRY_VIEW.get(category, ())


def categories() -> tuple[str, ...]:
    """Return all registered indicator categories."""
    return tuple(_REGISTRY_VIEW)


def indicator_count(category: str | None = None) -> int:
    """Return the number of indicators in one category or across all categories."""
    if category is None:
        return sum(len(names) for names in _REGISTRY_VIEW.values())
    return len(list_indicators(category))


def validate_registry() -> bool:
    """Validate category names, indicator names and duplicate entries."""
    if not _REGISTRY_VIEW:
        return False

    for category, names in _REGISTRY_VIEW.items():
        if not isinstance(category, str) or not category:
            return False
        if not isinstance(names, tuple):
            return False
        if any(not isinstance(name, str) or not name for name in names):
            return False
        if len(names) != len(set(names)):
            return False

    return True
