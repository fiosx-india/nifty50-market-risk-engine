import pytest
from indicators.momentum_indicators import stochastic, stochastic_series, williams_r, cci, mfi

def data():
    return ([10,11,12,13,14,15,16,17], [8,9,10,11,12,13,14,15],
            [9,10,11,12,13,14,15,16], [100,110,120,130,140,150,160,170])

def test_stochastic():
    h,l,c,v=data()
    s=stochastic_series(h,l,c,3,3)
    assert len(s["k"]) == 6 and len(s["d"]) == 6
    assert stochastic(h,l,c,3) == pytest.approx(100)

def test_williams_r():
    h,l,c,_=data()
    assert williams_r(h,l,c,3) == pytest.approx(0)

def test_cci_and_mfi():
    h,l,c,v=data()
    assert cci(h,l,c,3) > 0
    assert 0 <= mfi(h,l,c,v,3) <= 100

def test_validation():
    h,l,c,v=data()
    with pytest.raises(ValueError): stochastic(h[:-1],l,c,3)
    with pytest.raises(ValueError): mfi(h,l,c,v[:-1],3)
    with pytest.raises(ValueError): stochastic(h,l,c,0)
