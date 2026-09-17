"""Global market observation layer; no directional company score."""
from dataclasses import dataclass
@dataclass(frozen=True)
class GlobalObservation:
    name:str; value:float; timestamp:str; source:str; unit:str=""; quality:str="unknown"
def required_channels():
    return ("US equities","Asian equities","US yields","USD","oil","gold","global volatility","geopolitical risk")
def index(observations): return {x.name:x for x in observations}
