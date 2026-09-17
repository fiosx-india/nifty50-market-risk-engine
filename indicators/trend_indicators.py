"""Production trend indicators. Measurements only; no trading decisions."""
from math import isfinite

EPS = 1e-12

def _num(x, name):
    if x is None: raise ValueError(f"{name} cannot be None")
    out=[]
    for v in x:
        if v is None: raise ValueError(f"{name} contains None")
        try: v=float(v)
        except (TypeError,ValueError) as e: raise ValueError(f"{name} contains non-numeric data") from e
        if not isfinite(v): raise ValueError(f"{name} contains non-finite data")
        out.append(v)
    return out

def _p(p):
    if isinstance(p,bool) or not isinstance(p,int) or p<=0: raise ValueError("period must be a positive integer")
    return p

def _ohlc(h,l,c):
    h,l,c=_num(h,"high"),_num(l,"low"),_num(c,"close")
    if not(len(h)==len(l)==len(c)): raise ValueError("high, low and close must have equal lengths")
    for i,(hi,lo,cl) in enumerate(zip(h,l,c)):
        if hi<lo or not(lo<=cl<=hi): raise ValueError(f"invalid OHLC at index {i}")
    return h,l,c

def _tr(h,l,c):
    if not c:return []
    out=[h[0]-l[0]]
    for i in range(1,len(c)): out.append(max(h[i]-l[i],abs(h[i]-c[i-1]),abs(l[i]-c[i-1])))
    return out

def _wilder(x,p):
    if len(x)<p:return []
    prev=sum(x[:p]); out=[prev]
    for v in x[p:]:
        prev=prev-prev/p+v; out.append(prev)
    return out

def adx_series(high,low,close,period=14):
    p=_p(period); h,l,c=_ohlc(high,low,close)
    if len(c)<2*p+1:return {"plus_di":[],"minus_di":[],"dx":[],"adx":[]}
    tr=_tr(h,l,c); plus=[0.0]; minus=[0.0]
    for i in range(1,len(c)):
        up=h[i]-h[i-1]; dn=l[i-1]-l[i]
        plus.append(up if up>dn and up>0 else 0.0)
        minus.append(dn if dn>up and dn>0 else 0.0)
    ts,ps,ms=_wilder(tr,p),_wilder(plus,p),_wilder(minus,p)
    pdi=[]; mdi=[]; dx=[]
    for t,a,b in zip(ts,ps,ms):
        x=0.0 if t<=EPS else 100*a/t; y=0.0 if t<=EPS else 100*b/t
        pdi.append(x); mdi.append(y)
        d=x+y; dx.append(0.0 if d<=EPS else 100*abs(x-y)/d)
    adx=[]
    if len(dx)>=p:
        prev=sum(dx[:p])/p; adx=[prev]
        for v in dx[p:]: prev=((p-1)*prev+v)/p; adx.append(prev)
    return {"plus_di":pdi,"minus_di":mdi,"dx":dx,"adx":adx}

def adx(high,low,close,period=14):
    return (s:=adx_series(high,low,close,period))["adx"][-1] if s["adx"] else None

def supertrend_series(high,low,close,period=10,multiplier=3.0):
    p=_p(period); m=float(multiplier)
    if not isfinite(m) or m<=0: raise ValueError("multiplier must be positive and finite")
    h,l,c=_ohlc(high,low,close)
    if len(c)<p:return {"atr":[],"basic_upper":[],"basic_lower":[],"final_upper":[],"final_lower":[],"supertrend":[],"direction":[]}
    atr=[x/p for x in _wilder(_tr(h,l,c),p)]
    bu=[]; bl=[]; fu=[]; fl=[]; st=[]; direction=[]
    start=p-1
    for j,a in enumerate(atr):
        i=start+j; mid=(h[i]+l[i])/2; u=mid+m*a; d=mid-m*a
        bu.append(u); bl.append(d)
        if j==0: U,L=u,d; S=U if c[i]<=U else L
        else:
            pu,pl=fu[-1],fl[-1]; pc=c[i-1]
            U=u if u<pu or pc>pu else pu
            L=d if d>pl or pc<pl else pl
            if st[-1]==pu: S=U if c[i]<=U else L
            else: S=L if c[i]>=L else U
        fu.append(U); fl.append(L); st.append(S); direction.append("upper" if S==U else "lower")
    return {"atr":atr,"basic_upper":bu,"basic_lower":bl,"final_upper":fu,"final_lower":fl,"supertrend":st,"direction":direction}

def supertrend_inputs(high,low,close,period=10,multiplier=3.0):
    s=supertrend_series(high,low,close,period,multiplier)
    if not s["atr"]: return None
    return {"upper":s["final_upper"][-1],"lower":s["final_lower"][-1],"atr":s["atr"][-1]}

def ichimoku_series(high,low,close,conversion_period=9,base_period=26,span_period=52,displacement=26):
    cp,bp,sp,disp=map(_p,(conversion_period,base_period,span_period,displacement))
    h,l,c=_ohlc(high,low,close); n=len(c)
    conv=[None]*n; base=[None]*n; a=[None]*n; b=[None]*n
    for i in range(n):
        if i+1>=cp: conv[i]=(max(h[i-cp+1:i+1])+min(l[i-cp+1:i+1]))/2
        if i+1>=bp: base[i]=(max(h[i-bp+1:i+1])+min(l[i-bp+1:i+1]))/2
        if conv[i] is not None and base[i] is not None:a[i]=(conv[i]+base[i])/2
        if i+1>=sp:b[i]=(max(h[i-sp+1:i+1])+min(l[i-sp+1:i+1]))/2
    return {"conversion":conv,"base":base,"span_a":a,"span_b":b,"displacement":disp}

def ichimoku(high,low,close):
    s=ichimoku_series(high,low,close)
    if not s["span_b"] or s["span_b"][-1] is None:return None
    return {k:s[k][-1] for k in ("conversion","base","span_a","span_b")}

__all__=["adx","adx_series","supertrend_inputs","supertrend_series","ichimoku","ichimoku_series"]
