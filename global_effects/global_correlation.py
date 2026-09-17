"""Correlation only; correlation is not causation."""
def correlation(x,y):
    n=min(len(x),len(y))
    if n<2:return None
    a=list(map(float,x[-n:])); b=list(map(float,y[-n:]))
    ma=sum(a)/n; mb=sum(b)/n
    da=[z-ma for z in a]; db=[z-mb for z in b]
    den=(sum(z*z for z in da)*sum(z*z for z in db))**.5
    return sum(u*v for u,v in zip(da,db))/den if den else None
