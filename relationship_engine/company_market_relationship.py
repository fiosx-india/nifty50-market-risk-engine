"""Company + market character relationship layer.

Resolves descriptive exposure channels between an existing company character
and market character. Historical data is required before treating a channel
as empirically supported. This module does not calculate correlation,
causation, probability, or trading direction.
"""

from __future__ import annotations

from collections.abc import Iterable
from typing import Any


def _character_attr(character: Any, name: str, default: Any = ()) -> Any:
    value = getattr(character, name, default)
    return default if value is None else value


def _tuple_channels(character: Any, name: str) -> tuple[Any, ...]:
    value = _character_attr(character, name, ())
    if isinstance(value, (str, bytes)):
        raise TypeError(f"{name} must be an iterable of channel values")
    try:
        return tuple(value)
    except TypeError as exc:
        raise TypeError(f"{name} must be iterable") from exc


def _company_symbol(character: Any) -> str:
    symbol = getattr(character, "symbol", None)
    if symbol is None:
        symbol = getattr(character, "name", None)
    if symbol is None:
        raise ValueError("company character requires symbol or name")

    text = str(symbol).strip()
    if not text:
        raise ValueError("company character symbol/name cannot be empty")
    return text


def _market_name(character: Any) -> str:
    market = getattr(character, "market", None)
    if market is None:
        raise ValueError("market character requires market")

    text = str(market).strip()
    if not text:
        raise ValueError("market character market cannot be empty")
    return text


def resolve_relationship(
    company_character: Any,
    market_character: Any,
) -> dict[str, Any]:
    """Resolve descriptive company/market exposure channels.

    The returned status intentionally remains
    ``requires_historical_validation``. Character definitions are hypotheses
    about economic pathways, not empirical proof of a relationship.
    """
    return {
        "company": _company_symbol(company_character),
        "market": _market_name(market_character),
        "direct_channels": _tuple_channels(
            market_character, "direct_exposure_patterns"
        ),
        "indirect_channels": _tuple_channels(
            market_character, "indirect_exposure_patterns"
        ),
        "cost_channels": _tuple_channels(
            market_character, "cost_channels"
        ),
        "revenue_channels": _tuple_channels(
            market_character, "revenue_channels"
        ),
        "status": "requires_historical_validation",
        "causation_claim": False,
    }


def relationship_is_testable(relationship: dict[str, Any]) -> bool:
    """Return whether the resolved relationship has channels to test."""
    if not isinstance(relationship, dict):
        raise TypeError("relationship must be a dictionary")

    channels = (
        relationship.get("direct_channels", ())
        + relationship.get("indirect_channels", ())
        + relationship.get("cost_channels", ())
        + relationship.get("revenue_channels", ())
    )
    return bool(channels)
