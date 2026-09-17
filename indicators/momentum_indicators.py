"""Momentum indicators. Pure measurements; no trading decisions."""
from __future__ import annotations
from math import isfinite

_EPS = 1e-12

def _num(values, name):
    if values is None:
        raise ValueError(f"{name} cannot be None")
    out = []
    for x in values:
        if x is None:
            raise ValueError(f"{name} contains None; alignment must be preserved")
        try:
            x = float(x)
        except (TypeError, ValueError) as e:
            raise ValueError(f"{name} contains non-numeric data") from e
        if not isfinite(x):
            raise ValueError(f"{name} contains non-finite data")
        out.append(x)
    return out

def _period(period):
    if isinstance(period, bool) or not isinstance(period, int) or period <= 0:
        raise ValueError("period must be a positive integer")
    return period

def _hlc(high, low, close):
    h, l, c = _num(high, "high"), _num(low, "low"), _num(close, "close")
    if not (len(h) == len(l) == len(c)):
        raise ValueError("high, low and close must have equal lengths")
    for i, (hi, lo, cl) in enumerate(zip(h, l, c)):
        if hi < lo or not (lo <= cl <= hi):
            raise ValueError(f"invalid OHLC at index {i}")
    return h, l, c

def _stochastic_k(high, low, close, period):
    p = _period(period)
    h, l, c = _hlc(high, low, close)
    if len(c) < p:
        return []
    out = []
    for i in range(p - 1, len(c)):
        hi, lo = max(h[i-p+1:i+1]), min(l[i-p+1:i+1])
        out.append(50.0 if hi - lo <= _EPS else 100.0 * (c[i] - lo) / (hi - lo))
    return out

def stochastic_series(high, low, close, period=14, d_period=3):
    """Return full stochastic %K and %D series; %D is SMA of %K."""
    d = _period(d_period)
    k = _stochastic_k(high, low, close, period)
    ds = []
    for i in range(len(k)):
        w = k[max(0, i-d+1):i+1]
        ds.append(sum(w) / len(w))
    return {"k": k, "d": ds}

def stochastic(high, low, close, period=14):
    """Latest stochastic %K."""
    k = stochastic_series(high, low, close, period)["k"]
    return k[-1] if k else None

def williams_r(high, low, close, period=14):
    """Latest Williams %R."""
    p = _period(period)
    h, l, c = _hlc(high, low, close)
    if len(c) < p:
        return None
    hi, lo = max(h[-p:]), min(l[-p:])
    return -50.0 if hi - lo <= _EPS else -100.0 * (hi - c[-1]) / (hi - lo)

def cci(high, low, close, period=20):
    """Latest Commodity Channel Index."""
    p = _period(period)
    h, l, c = _hlc(high, low, close)
    if len(c) < p:
        return None
    tp = [(hi+lo+cl)/3.0 for hi,lo,cl in zip(h,l,c)]
    w = tp[-p:]
    mean = sum(w)/p
    md = sum(abs(x-mean) for x in w)/p
    return 0.0 if md <= _EPS else (tp[-1]-mean)/(0.015*md)

def mfi(high, low, close, volume, period=14):
    """Latest Money Flow Index."""
    p = _period(period)
    h, l, c = _hlc(high, low, close)
    v = _num(volume, "volume")
    if len(v) != len(c):
        raise ValueError("volume must have the same length as OHLC")
    if any(x < 0 for x in v):
        raise ValueError("volume cannot be negative")
    if len(c) <= p:
        return None
    tp = [(hi+lo+cl)/3.0 for hi,lo,cl in zip(h,l,c)]
    pos = neg = 0.0
    for i in range(len(tp)-p, len(tp)):
        flow = tp[i] * v[i]
        if tp[i] > tp[i-1]:
            pos += flow
        elif tp[i] < tp[i-1]:
            neg += flow
    if neg <= _EPS:
        return 100.0 if pos > _EPS else 50.0
    return 100.0 - 100.0/(1.0 + pos/neg)

__all__ = ["stochastic", "stochastic_series", "williams_r", "cci", "mfi"]
