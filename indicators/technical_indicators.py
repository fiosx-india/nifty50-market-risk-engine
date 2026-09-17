"""Core technical indicators. Pure calculations; no trade decisions."""
from typing import Optional, Sequence

def _f(x): return [float(v) for v in x if v is not None]

def sma(values, period=20):
    v=_f(values)
    return sum(v[-period:])/period if period>0 and len(v)>=period else None

def ema(values, period=20):
    v=_f(values)
    if period<=0 or len(v)<period: return None
    e=sum(v[:period])/period; a=2/(period+1)
    for x in v[period:]: e=a*x+(1-a)*e
    return e

def wma(values, period=20):
    v=_f(values)
    if period<=0 or len(v)<period: return None
    x=v[-period:]; s=period*(period+1)/2
    return sum((i+1)*z for i,z in enumerate(x))/s

def roc(values, period=12):
    v=_f(values)
    return (v[-1]/v[-period-1]-1)*100 if len(v)>period and v[-period-1] else None

def momentum(values, period=10):
    v=_f(values)
    return v[-1]-v[-period-1] if len(v)>period else None

def rsi(values, period=14):
    v=_f(values)
    if len(v)<=period: return None
    d=[v[i]-v[i-1] for i in range(1,len(v))][-period:]
    gain=sum(max(x,0) for x in d)/period
    loss=sum(max(-x,0) for x in d)/period
    return 100.0 if loss==0 else 100-100/(1+gain/loss)

def atr(high, low, close, period=14):
    if len(close)<period+1: return None
    tr=[]
    for i in range(1,len(close)):
        h,l,pc=float(high[i]),float(low[i]),float(close[i-1])
        tr.append(max(h-l,abs(h-pc),abs(l-pc)))
    return sum(tr[-period:])/period if len(tr)>=period else None

def bollinger(values, period=20, deviations=2):
    v=_f(values)
    if len(v)<period: return None
    x=v[-period:]; m=sum(x)/period
    sd=(sum((z-m)**2 for z in x)/period)**0.5
    return {"middle":m,"upper":m+deviations*sd,"lower":m-deviations*sd}

def vwap(high, low, close, volume):
    n=min(len(high),len(low),len(close),len(volume))
    if not n: return None
    pv=sum(((float(high[i])+float(low[i])+float(close[i]))/3)*float(volume[i]) for i in range(n))
    vv=sum(float(v) for v in volume[-n:])
    return pv/vv if vv else None
