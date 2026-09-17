"""Candlestick observations. No BUY/SELL decisions."""
def doji(o,h,l,c,threshold=0.10):
    o,h,l,c=map(float,(o,h,l,c)); r=h-l
    return bool(r and abs(c-o)/r<=threshold)

def hammer(o,h,l,c):
    o,h,l,c=map(float,(o,h,l,c)); body=abs(c-o)
    return (min(o,c)-l)>=2*max(body,1e-12) and (h-max(o,c))<=max(body,1e-12)

def inverted_hammer(o,h,l,c):
    o,h,l,c=map(float,(o,h,l,c)); body=abs(c-o)
    return (h-max(o,c))>=2*max(body,1e-12) and (min(o,c)-l)<=max(body,1e-12)

def shooting_star(o,h,l,c): return inverted_hammer(o,h,l,c)

def hanging_man(o,h,l,c): return hammer(o,h,l,c)

def bullish_engulfing(po,pc,o,c):
    po,pc,o,c=map(float,(po,pc,o,c))
    return pc<po and c>o and o<=pc and c>=po

def bearish_engulfing(po,pc,o,c):
    po,pc,o,c=map(float,(po,pc,o,c))
    return pc>po and c<o and o>=pc and c<=po

def spinning_top(o,h,l,c,threshold=.35):
    o,h,l,c=map(float,(o,h,l,c)); r=h-l
    return bool(r and abs(c-o)/r<=threshold)

def marubozu(o,h,l,c,threshold=.05):
    o,h,l,c=map(float,(o,h,l,c)); r=h-l
    return bool(r and ((abs(o-l)/r<=threshold and abs(h-c)/r<=threshold) or
                       (abs(h-o)/r<=threshold and abs(c-l)/r<=threshold)))

def detect_last(c):
    o,h,l,cl=c["open"],c["high"],c["low"],c["close"]
    return {"doji":doji(o,h,l,cl),"hammer":hammer(o,h,l,cl),
            "inverted_hammer":inverted_hammer(o,h,l,cl),
            "shooting_star":shooting_star(o,h,l,cl),
            "hanging_man":hanging_man(o,h,l,cl),
            "spinning_top":spinning_top(o,h,l,cl),
            "marubozu":marubozu(o,h,l,cl)}
