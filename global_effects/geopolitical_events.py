"""Structured geopolitical event record."""
from dataclasses import dataclass
@dataclass(frozen=True)
class GeopoliticalEvent:
    timestamp:str; region:str; event_type:str; description:str; source:str
