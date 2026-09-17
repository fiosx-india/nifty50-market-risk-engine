import pytest
from indicators.trend_indicators import adx,adx_series,supertrend_inputs,supertrend_series,ichimoku,ichimoku_series

def data(n=80):
    c=[100+i*.5 for i in range(n)]; return [x+1 for x in c],[x-1 for x in c],c

def test_adx():
    h,l,c=data(); s=adx_series(h,l,c,14)
    assert s["adx"] and 0<=adx(h,l,c,14)<=100
    assert len(s["plus_di"])==len(s["minus_di"])==len(s["dx"])

def test_adx_insufficient():
    h,l,c=data(20); assert adx(h,l,c,14) is None

def test_supertrend():
    h,l,c=data(); s=supertrend_series(h,l,c,10,3)
    assert len(s["atr"])==len(s["supertrend"]) and s["direction"][-1] in {"upper","lower"}
    assert supertrend_inputs(h,l,c,10,3)["atr"]>0

def test_ichimoku():
    h,l,c=data(); s=ichimoku_series(h,l,c)
    assert s["displacement"]==26 and s["span_b"][-1] is not None
    assert ichimoku(h,l,c) is not None

def test_validation():
    h,l,c=data()
    with pytest.raises(ValueError): adx(h[:-1],l,c,14)
    with pytest.raises(ValueError): adx(h,l,c,0)
    with pytest.raises(ValueError): supertrend_series(h,l,c,10,0)
