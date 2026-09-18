"""Company event taxonomy and classification.

This module normalizes event type labels into a controlled taxonomy. It does
not estimate market impact, causation, probability, or trading direction.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any


EVENT_TYPES = (
    "earnings",
    "guidance",
    "order",
    "capex",
    "M&A",
    "management",
    "promoter",
    "debt",
    "credit_rating",
    "regulatory",
    "legal",
    "product",
    "capacity",
    "shutdown",
)


def classify_event(event: Mapping[str, Any]) -> dict[str, Any]:
    """Return a normalized event mapping with a controlled ``type`` field.

    Existing fields are preserved. Unknown or missing event types become
    ``"other"``. A new dictionary is always returned, so the input mapping is
    never mutated.
    """
    if not isinstance(event, Mapping):
        raise TypeError("event must be a mapping")

    normalized = dict(event)
    if normalized.get("type") not in EVENT_TYPES:
        normalized["type"] = "other"

    return normalized


def is_known_event_type(event_type: Any) -> bool:
    """Return whether a value is one of the controlled event types."""
    return isinstance(event_type, str) and event_type in EVENT_TYPES


def list_event_types() -> tuple[str, ...]:
    """Return the supported event taxonomy."""
    return EVENT_TYPES


def validate_event(event: Mapping[str, Any]) -> bool:
    """Validate the basic event boundary without assigning impact."""
    if not isinstance(event, Mapping):
        return False

    event_type = event.get("type")
    return event_type == "other" or is_known_event_type(event_type)
