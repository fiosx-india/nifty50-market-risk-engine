"""Market event taxonomy and classification.

Normalizes external market-event records into a controlled event taxonomy.
This module records event type only; it does not estimate impact or trading
direction.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any


EVENT_TYPES = (
    "commodity_shock",
    "rate_decision",
    "inflation",
    "FX_shock",
    "geopolitical",
    "supply_disruption",
    "demand_shock",
    "weather",
    "policy",
)


def classify_event(event: Mapping[str, Any]) -> dict[str, Any]:
    """Return a copy with an event type from the controlled taxonomy."""
    if not isinstance(event, Mapping):
        raise TypeError("event must be a mapping")

    normalized = dict(event)
    if normalized.get("type") not in EVENT_TYPES:
        normalized["type"] = "other"

    return normalized


def is_known_event_type(event_type: Any) -> bool:
    """Return whether event_type belongs to the controlled taxonomy."""
    return isinstance(event_type, str) and event_type in EVENT_TYPES


def list_event_types() -> tuple[str, ...]:
    """Return all supported market event types."""
    return EVENT_TYPES


def validate_event(event: Mapping[str, Any]) -> bool:
    """Validate only the event-type boundary."""
    if not isinstance(event, Mapping):
        return False

    event_type = event.get("type")
    return event_type == "other" or is_known_event_type(event_type)
