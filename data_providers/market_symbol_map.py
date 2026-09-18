"""Provider-neutral symbol configuration for the nine tracked markets.

No vendor-specific ticker is invented here. A real provider mapping must be
supplied explicitly by the integration layer after the instrument is verified.
This module only defines the canonical market names and safe lookup behavior.
"""

from dataclasses import dataclass
from typing import Mapping


TRACKED_MARKETS = (
    "NIFTY 50",
    "Crude Oil",
    "Gold",
    "Silver",
    "Natural Gas",
    "Copper",
    "Aluminium",
    "Zinc",
    "Electricity",
)

# Intentionally empty: vendor symbols/contracts must not be guessed.
DEFAULT_SYMBOLS = {market: () for market in TRACKED_MARKETS}


@dataclass(frozen=True)
class MarketInstrument:
    """Verified provider/instrument mapping supplied by an integration layer."""

    market: str
    provider: str
    symbol: str
    exchange: str = ""
    asset_class: str = ""
    contract_expiry: str = ""
    currency: str = ""
    price_basis: str = ""


def validate_market(market: str) -> bool:
    """Return whether ``market`` is one of the canonical tracked markets."""
    return isinstance(market, str) and market in TRACKED_MARKETS


def get_candidates(market: str):
    """Return explicitly configured candidate symbols for ``market``.

    An empty tuple means no vendor mapping has been configured yet. It does
    not mean that the market has no real-world instrument.
    """
    if not validate_market(market):
        raise KeyError(f"Unsupported tracked market: {market}")
    return tuple(DEFAULT_SYMBOLS[market])


def validate_symbol_map(symbol_map: Mapping[str, object]) -> dict:
    """Validate an externally supplied market-to-symbol mapping.

    The function does not calculate or rank symbols. Unknown market keys and
    empty/non-string symbols are rejected so configuration errors cannot be
    mistaken for valid market data.
    """
    if not isinstance(symbol_map, Mapping):
        raise TypeError("symbol_map must be a mapping")

    unknown = tuple(key for key in symbol_map if key not in TRACKED_MARKETS)
    if unknown:
        raise KeyError(f"Unsupported tracked markets: {unknown}")

    errors = []
    for market, symbols in symbol_map.items():
        if isinstance(symbols, str):
            errors.append(f"{market}:symbols_must_be_a_sequence")
            continue
        try:
            values = tuple(symbols)
        except TypeError:
            errors.append(f"{market}:symbols_must_be_iterable")
            continue

        for index, symbol in enumerate(values):
            if not isinstance(symbol, str) or not symbol.strip():
                errors.append(f"{market}:invalid_symbol_{index}")

    return {
        "valid": not errors,
        "errors": tuple(errors),
        "markets_configured": tuple(symbol_map.keys()),
    }
