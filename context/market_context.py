"""Shared evidence context. CentralBrain remains the only orchestrator."""
from dataclasses import dataclass,field
@dataclass
class MarketContext:
    symbol:str
    timestamp:str
    market_observations:dict=field(default_factory=dict)
    company_observations:dict=field(default_factory=dict)
    technical_evidence:dict=field(default_factory=dict)
    pattern_evidence:dict=field(default_factory=dict)
    global_evidence:dict=field(default_factory=dict)
    relationship_evidence:list=field(default_factory=list)
    news_evidence:list=field(default_factory=list)
    conflicts:list=field(default_factory=list)
    def add_relationship_evidence(self,evidence): self.relationship_evidence.append(dict(evidence))
    def add_conflict(self,evidence): self.conflicts.append(dict(evidence))
