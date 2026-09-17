"""Volume and price-volume evidence."""
def relative_volume(volume, period=20):
    if len(volume)<period+1: return None
    avg=sum(map(float,volume[-period-1:-1]))/period
    return float(volume[-1])/avg if avg else None

def obv(close, volume):
    value=0.0
    for i in range(1,min(len(close),len(volume))):
        if float(close[i])>float(close[i-1]): value+=float(volume[i])
        elif float(close[i])<float(close[i-1]): value-=float(volume[i])
    return value

def accumulation_distribution(high,low,close,volume):
    total=0.0
    for h,l,c,v in zip(high,low,close,volume):
        h,l,c,v=map(float,(h,l,c,v))
        mfm=((c-l)-(h-c))/(h-l) if h!=l else 0
        total+=mfm*v
    return total

def price_volume_confirmation(close,volume):
    if len(close)<2 or len(volume)<2: return {"confirmed":False}
    pu=float(close[-1])>float(close[-2]); vu=float(volume[-1])>float(volume[-2])
    return {"price_up":pu,"volume_up":vu,"confirmed":pu==vu}
