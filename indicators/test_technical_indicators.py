import pytest

from indicators.technical_indicators import (
    atr,
    bollinger,
    ema,
    momentum,
    roc,
    rsi,
    sma,
    vwap,
    wma,
)


def test_sma():
    assert sma([1, 2, 3, 4, 5], 3) == pytest.approx(4.0)
    assert sma([1, 2], 3) is None


def test_ema():
    # Period-3 seed = 2; alpha = 0.5; next value = 2.5.
    assert ema([1, 2, 3, 4], 3) == pytest.approx(3.0)


def test_wma():
    assert wma([1, 2, 3], 3) == pytest.approx((1 + 4 + 9) / 6)


def test_roc_and_momentum():
    values = [100, 105, 110, 120]
    assert roc(values, 2) == pytest.approx((120 / 105 - 1) * 100)
    assert momentum(values, 2) == pytest.approx(15)


def test_rsi_is_bounded():
    values = [100, 101, 102, 101, 103, 104, 103, 105]
    result = rsi(values, 3)
    assert result is not None
    assert 0 <= result <= 100


def test_atr_validates_alignment():
    with pytest.raises(ValueError):
        atr([10, 11], [9], [9.5, 10])


def test_atr_returns_value():
    high = [11, 12, 13, 14, 15]
    low = [9, 10, 11, 12, 13]
    close = [10, 11, 12, 13, 14]
    assert atr(high, low, close, 3) is not None


def test_bollinger():
    result = bollinger([1, 2, 3, 4, 5], 5, 2)
    assert result["middle"] == pytest.approx(3.0)
    assert result["upper"] > result["middle"]
    assert result["lower"] < result["middle"]


def test_vwap_alignment_and_zero_volume():
    assert vwap([10, 11], [8, 9], [9, 10], [100, 200]) == pytest.approx(
        (((10 + 8 + 9) / 3) * 100 + ((11 + 9 + 10) / 3) * 200) / 300
    )
    assert vwap([10], [8], [9], [0]) is None


def test_none_is_not_silently_dropped():
    with pytest.raises(ValueError):
        sma([1, None, 3], 2)


@pytest.mark.parametrize("fn", [sma, ema, wma, roc, momentum, rsi, atr])
def test_invalid_period(fn):
    if fn is atr:
        with pytest.raises(ValueError):
            fn([2], [1], [1.5], 0)
    else:
        with pytest.raises(ValueError):
            fn([1, 2, 3], 0)
