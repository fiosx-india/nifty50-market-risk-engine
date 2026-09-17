"""Indicator discovery registry; it does not orchestrate analysis."""
INDICATOR_REGISTRY={
 "technical":("sma","ema","wma","roc","momentum","rsi","atr","bollinger","vwap"),
 "momentum":("stochastic","williams_r","cci","mfi"),
 "trend":("adx","supertrend_inputs","ichimoku"),
 "volatility":("returns","realized_volatility","volatility_percentile","true_range_series"),
 "volume":("relative_volume","obv","accumulation_distribution","price_volume_confirmation"),
 "candlestick":("doji","hammer","inverted_hammer","shooting_star","hanging_man","bullish_engulfing","bearish_engulfing","spinning_top","marubozu"),
 "structure":("swing_points","structure_state","bos","liquidity_zones"),
 "chart":("higher_high","higher_low","lower_high","lower_low","range_levels","breakout","breakdown"),
}
def list_indicators(category=None):
    return dict(INDICATOR_REGISTRY) if category is None else INDICATOR_REGISTRY.get(category,())
