import pytest

from indicators.candlestick_patterns import (
    bearish_engulfing,
    bullish_engulfing,
    detect_last,
    doji,
    hammer,
    inverted_hammer,
    marubozu,
    shooting_star,
    hanging_man,
)


def test_doji():
    assert doji(100, 105, 95, 100.2)
    assert not doji(100, 105, 95, 104)


def test_hammer_geometry():
    assert hammer(100, 101, 94, 100.5)


def test_inverted_hammer_geometry():
    assert inverted_hammer(100, 106, 99, 100.5)


def test_contextual_shooting_star():
    candle = {"open": 100, "high": 106, "low": 99, "close": 100.5}
    result = detect_last(candle, prior_closes=[95, 97, 99, 100])
    assert result["shooting_star"] is True


def test_contextual_hanging_man():
    candle = {"open": 100, "high": 101, "low": 94, "close": 100.5}
    result = detect_last(candle, prior_closes=[95, 97, 99, 100])
    assert result["hanging_man"] is True


def test_no_context_does_not_label_contextual_patterns():
    candle = {"open": 100, "high": 106, "low": 99, "close": 100.5}
    result = detect_last(candle)
    assert result["inverted_hammer"] is True
    assert result["shooting_star"] is False


def test_engulfing():
    assert bullish_engulfing(105, 100, 99, 106)
    assert bearish_engulfing(100, 105, 106, 99)


def test_marubozu():
    assert marubozu(100, 110, 100, 110)
    assert not marubozu(100, 110, 95, 105)


@pytest.mark.parametrize(
    "ohlc",
    [
        (100, 95, 90, 92),       # high < low
        (100, 105, 95, 110),     # close > high
        (90, 105, 95, 100),      # open < low
    ],
)
def test_invalid_ohlc(ohlc):
    with pytest.raises(ValueError):
        doji(*ohlc)
