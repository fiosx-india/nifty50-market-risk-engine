"""Supply-chain pathway builder.

Builds a descriptive market -> industry -> company pathway from an existing
market character. It does not infer economic impact, causation, or direction.
"""

from __future__ import annotations

from collections.abc import Iterable
from typing import Any


def _required_text(value: Any, name: str) -> str:
    if value is None:
        raise ValueError(f"{name} is required")
    text = str(value).strip()
    if not text:
        raise ValueError(f"{name} cannot be empty")
    return text


def _channels(market_character: Any) -> tuple[Any, ...]:
    channels = getattr(market_character, "supply_chain_channels", ())
    if channels is None:
        return ()
    if isinstance(channels, (str, bytes)):
        raise TypeError("supply_chain_channels must be an iterable")
    try:
        return tuple(channels)
    except TypeError as exc:
        raise TypeError("supply_chain_channels must be iterable") from exc


def build_path(
    market_character: Any,
    industry: Any,
    company: Any,
) -> dict[str, Any]:
    """Build a descriptive supply-chain pathway."""
    market = _required_text(getattr(market_character, "market", None), "market")
    industry_text = _required_text(industry, "industry")
    company_text = _required_text(company, "company")
    path = _channels(market_character)

    return {
        "market": market,
        "industry": industry_text,
        "company": company_text,
        "path": path,
        "status": "requires_historical_validation",
        "causation_claim": False,
    }


def validate_path(path: Any) -> bool:
    """Validate the structural completeness of a supply-chain pathway."""
    if not isinstance(path, dict):
        return False

    market = path.get("market")
    company = path.get("company")
    channels = path.get("path")

    if not isinstance(market, str) or not market.strip():
        return False
    if not isinstance(company, str) or not company.strip():
        return False
    if channels is None or isinstance(channels, (str, bytes)):
        return False

    try:
        return bool(tuple(channels))
    except TypeError:
        return False
