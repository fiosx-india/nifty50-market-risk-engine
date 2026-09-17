"""Momentum measurements."""
def stochastic(high, low, close, period=14):
    if len(close)<period: return None
    h=max(map(float,high[-period:])); l=min(map(float,low[-period:]))
    return 100*(float(close[-1])-l)/(h-l) if h!=l else 50.0

def williams_r(high, low, close, period=14):
    if len(close)<period: return None
    h=max(map(float,high[-period:])); l=min(map(float,low[-period:]))
    return -100*(h-float(close[-1]))/(h-l) if h!=l else -50.0

def cci(high, low, close, period=20):
    if len(close)<period: return None
    tp=[(float(h)+float(l)+float(c))/3 for h,l,c in zip(high,low,close)]
    x=tp[-period:]; m=sum(x)/period; md=sum(abs(z-m) for z in x)/period
    return (tp[-1]-m)/(0.015*md) if md else 0.0

def mfi(high, low, close, volume, period=14):
    if len(close)<=period: return None
    tp=[(float(h)+float(l)+float(c))/3 for h,l,c in zip(high,low,close)]
    pos=neg=0.0
    start=len(tp)-period
    for i in range(start,len(tp)):
        flow=tp[i]*float(volume[i])
        if tp[i]>tp[i-1]: pos+=flow
        elif tp[i]<tp[i-1]: neg+=flow
    return 100.0 if neg==0 else 100-100/(1+pos/neg)
