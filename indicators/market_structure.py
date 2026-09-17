"""Market structure: swings, BOS and liquidity observations."""
def swing_points(high,low,left=2,right=2):
    out=[]; n=len(high)
    for i in range(left,n-right):
        h=float(high[i]); l=float(low[i])
        hs=list(map(float,high[i-left:i+right+1])); ls=list(map(float,low[i-left:i+right+1]))
        if h>=max(hs): out.append({"index":i,"type":"swing_high","price":h})
        elif l<=min(ls): out.append({"index":i,"type":"swing_low","price":l})
    return out

def structure_state(high,low):
    p=swing_points(high,low); hs=[x["price"] for x in p if x["type"]=="swing_high"]
    ls=[x["price"] for x in p if x["type"]=="swing_low"]
    return {"higher_high":len(hs)>1 and hs[-1]>hs[-2],
            "higher_low":len(ls)>1 and ls[-1]>ls[-2],
            "lower_high":len(hs)>1 and hs[-1]<hs[-2],
            "lower_low":len(ls)>1 and ls[-1]<ls[-2],"swings":p}

def bos(close,prior_high=None,prior_low=None):
    c=float(close[-1])
    return {"bullish":prior_high is not None and c>float(prior_high),
            "bearish":prior_low is not None and c<float(prior_low)}

def liquidity_zones(high,low,tolerance=.001):
    levels=sorted(map(float,list(high)+list(low))); zones=[]
    for x in levels:
        if not zones or abs(x-zones[-1]["level"])/max(abs(x),1e-9)>tolerance:
            zones.append({"level":x,"touches":1})
        else: zones[-1]["touches"]+=1
    return [z for z in zones if z["touches"]>=2]
