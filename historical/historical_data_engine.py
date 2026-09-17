"""Provider-neutral historical data contract."""
from dataclasses import dataclass
@dataclass(frozen=True)
class HistoricalSeries:
    symbol:str; timestamps:tuple; open:tuple; high:tuple; low:tuple
    close:tuple; volume:tuple; source:str; timezone:str
def validate_series(s):
    n=len(s.timestamps)
    return all(len(x)==n for x in (s.open,s.high,s.low,s.close,s.volume))
