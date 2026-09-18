"""Structured geopolitical event record.

Events are descriptive inputs. They are not assigned a market direction here.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass(frozen=True)
class GeopoliticalEvent:
    timestamp: datetime
    region: str
    event_type: str
    description: str
    source: str
    scope: str = ""
    precision: str = ""
    publication_timestamp: Any = None

    def validate(self):
        if self.timestamp.tzinfo is None or self.timestamp.utcoffset() is None:
            raise ValueError("timestamp must be timezone-aware")
        if not self.region.strip():
            raise ValueError("region must not be empty")
        if not self.event_type.strip():
            raise ValueError("event_type must not be empty")
        if not self.source.strip():
            raise ValueError("source must not be empty")
        return True
