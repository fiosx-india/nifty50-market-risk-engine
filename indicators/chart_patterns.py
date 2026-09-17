"""Multi-candle/chart pattern observations."""
def higher_high(high): return len(high)>=2 and float(high[-1])>float(high[-2])
def higher_low(low): return len(low)>=2 and float(low[-1])>float(low[-2])
def lower_high(high): return len(high)>=2 and float(high[-1])<float(high[-2])
def lower_low(low): return len(low)>=2 and float(low[-1])<float(low[-2])

def range_levels(high,low,lookback=20):
    if len(high)<lookback or len(low)<lookback: return None
    return {"resistance":max(map(float,high[-lookback:])),
            "support":min(map(float,low[-lookback:]))}

def breakout(close,level): return bool(close and float(close[-1])>float(level))
def breakdown(close,level): return bool(close and float(close[-1])<float(level))
