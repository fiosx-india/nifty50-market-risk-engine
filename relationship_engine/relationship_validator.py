"""Validation of calculated relationship evidence.

This module validates the structural completeness of relationship results.
It does not confirm economic causation or calculate a trading decision.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any


REQUIRED_FIELDS = ("market", "company")


def validate_result(result: Mapping[str, Any]) -> dict[str, Any]:
    """Validate required relationship identity fields.

    A result is structurally valid only when both ``market`` and ``company``
    contain non-empty values. Additional evidence-quality fields are checked
    when present but are not inferred or fabricated.
    """
    if not isinstance(result, Mapping):
        raise TypeError("result must be a mapping")

    missing = tuple(
        field
        for field in REQUIRED_FIELDS
        if result.get(field) is None
        or (isinstance(result.get(field), str) and not result.get(field).strip())
    )

    status = result.get("status", "unknown")
    if status is None or not isinstance(status, str):
        status = "unknown"

    causation_claim = result.get("causation_claim", False)
    if not isinstance(causation_claim, bool):
        raise TypeError("causation_claim must be boolean when provided")

    return {
        "valid": not missing,
        "missing": missing,
        "status": status,
        "causation_claim": causation_claim,
    }


def is_valid_result(result: Mapping[str, Any]) -> bool:
    """Return only the structural validity flag."""
    return validate_result(result)["valid"]
