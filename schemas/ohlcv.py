"""Provider-neutral OHLCV record schema.

The schema represents observed data only. It does not contain trading decisions.
"""

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class OHLCVRecord:
    timestamp: Any
    open: float
    high: float
    low: float
    close: float
    volume: float

    def validate(self):
        values = (
            self.open, self.high, self.low,
            self.close, self.volume,
        )
        if any(v is None for v in values):
            raise ValueError("OHLCV values cannot be None")
        if self.high < max(self.open, self.close):
            raise ValueError("high is below open/close")
        if self.low > min(self.open, self.close):
            raise ValueError("low is above open/close")
        if self.volume < 0:
            raise ValueError("volume cannot be negative")
        if self.timestamp is None:
            raise ValueError("timestamp cannot be None")
        return True
