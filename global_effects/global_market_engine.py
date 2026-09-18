"""Global market observation registry.

This module records globally relevant observations. It does not calculate a
company impact score or make directional trading decisions.
"""

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class GlobalObservation:
    name: str
    value: float
    timestamp: Any
    source: str
    unit: str = ""
    quality: str = "unknown"


def required_channels():
    return (
        "US equities",
        "Asian equities",
        "US yields",
        "USD",
        "oil",
        "gold",
        "global volatility",
        "geopolitical risk",
    )


def index(observations):
    return {observation.name: observation for observation in observations}
