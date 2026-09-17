"""Trend measurements."""
def adx(high, low, close, period=14):
    if len(close)<period*2+1: return None
    tr=[]; plus=[]; minus=[]
    for i in range(1,len(close)):
        h,l,pc=float(high[i]),float(low[i]),float(close[i-1])
        tr.append(max(h-l,abs(h-pc),abs(l-pc)))
        up=float(high[i])-float(high[i-1]); dn=float(low[i-1])-float(low[i])
        plus.append(up if up>dn and up>0 else 0)
        minus.append(dn if dn>up and dn>0 else 0)
    T=sum(tr[-period:]); P=sum(plus[-period:]); M=sum(minus[-period:])
    if not T: return 0.0
    pdi=100*P/T; mdi=100*M/T
    return 100*abs(pdi-mdi)/(pdi+mdi) if pdi+mdi else 0.0

def supertrend_inputs(high, low, close, period=10, multiplier=3.0):
    if len(close)<period+1: return None
    tr=[]
    for i in range(1,len(close)):
        h,l,pc=float(high[i]),float(low[i]),float(close[i-1])
        tr.append(max(h-l,abs(h-pc),abs(l-pc)))
    a=sum(tr[-period:])/period; mid=(float(high[-1])+float(low[-1]))/2
    return {"upper":mid+multiplier*a,"lower":mid-multiplier*a,"atr":a}

def ichimoku(high, low, close):
    if len(close)<52: return None
    conv=(max(map(float,high[-9:]))+min(map(float,low[-9:])))/2
    base=(max(map(float,high[-26:]))+min(map(float,low[-26:])))/2
    span_b=(max(map(float,high[-52:]))+min(map(float,low[-52:]))) / 2
    return {"conversion":conv,"base":base,"span_a":(conv+base)/2,"span_b":span_b}
