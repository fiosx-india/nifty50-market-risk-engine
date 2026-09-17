"""Market character: SILVER. Research layer only; no hard-coded market result."""
from dataclasses import dataclass
from typing import Any, Dict, Tuple

@dataclass(frozen=True)
class MarketCharacter:
    market: str
    market_type: str
    identity: str
    core_drivers: Tuple[str, ...]
    upstream: Tuple[str, ...]
    processing: Tuple[str, ...]
    downstream: Tuple[str, ...]
    demand_sectors: Tuple[str, ...]
    supply_chain_channels: Tuple[str, ...]
    direct_exposure_patterns: Tuple[str, ...]
    indirect_exposure_patterns: Tuple[str, ...]
    cost_channels: Tuple[str, ...]
    revenue_channels: Tuple[str, ...]
    macro_channels: Tuple[str, ...]
    global_channels: Tuple[str, ...]
    event_triggers: Tuple[str, ...]
    indicators: Tuple[str, ...]
    timeframes: Tuple[str, ...]
    lag_windows: Tuple[str, ...]
    data_requirements: Tuple[str, ...]
    calculation_rules: Tuple[str, ...]

MARKET_CHARACTER = MarketCharacter(
    market='SILVER',
    market_type='precious_and_industrial_metal',
    identity='Silver market combining precious-metal behaviour with industrial demand from solar, electronics and manufacturing.',
    core_drivers=('industrial demand', 'solar', 'electronics', 'investment', 'mine supply', 'recycling', 'gold relationship', 'global growth'),
    upstream=('silver mines', 'lead-zinc-copper-gold mines', 'recycling'),
    processing=('concentrate treatment', 'refining', 'fabrication'),
    downstream=('solar', 'electronics', 'electrical', 'industrial equipment', 'jewellery', 'investment'),
    demand_sectors=('solar', 'electronics', 'electrical', 'automotive electronics', 'industrial manufacturing', 'jewellery'),
    supply_chain_channels=('by-product mining', 'refining', 'industrial fabrication', 'investment products'),
    direct_exposure_patterns=('silver mining', 'silver inventory', 'silver-intensive manufacturing'),
    indirect_exposure_patterns=('industrial cycle', 'gold/silver ratio', 'technology capex', 'risk appetite'),
    cost_channels=('metal input', 'energy', 'refining', 'inventory finance'),
    revenue_channels=('industrial volume', 'investment demand', 'mining realization'),
    macro_channels=('global PMI', 'rates', 'USD', 'inflation', 'technology capex'),
    global_channels=('COMEX/LBMA silver', 'gold/silver ratio', 'solar', 'electronics', 'China industry'),
    event_triggers=('solar cycle', 'electronics demand', 'mine disruption', 'inventory'),
    indicators=('silver return', 'gold/silver ratio', 'industrial PMI', 'solar additions', 'USD', 'silver volatility'),
    timeframes=('5m', '15m', '1h', '4h', '1d', '1w', '1m'),
    lag_windows=('same-session', '1d', '3d', '5d', '20d', '60d'),
    data_requirements=(
        "timestamped market OHLCV or benchmark data",
        "company OHLCV and corporate actions",
        "company character and market-exposure character",
        "FX where international benchmark differs from INR exposure",
        "volume/open-interest data where available",
        "company announcements and event timestamps",
        "relevant sector/global benchmark data",
    ),
    calculation_rules=(
        "Never copy RANK, PCT_CHANGE, LINKAGE_SCORE or RELATION from a sample CSV as truth.",
        "Classify direct and indirect pathways from the existing company character.",
        "Calculate synchronized returns before calculating relationships.",
        "Calculate lagged relationships for every declared lag window.",
        "Use rolling correlation/regression rather than one permanent coefficient.",
        "Control for NIFTY/sector effects when statistically possible.",
        "Separate price effect, volume effect, margin effect and macro effect.",
        "Confirm unusual moves with volume, volatility and dated company events.",
        "Use event studies for discrete shocks and regression for continuous exposure.",
        "Estimate confidence from sample size, stability, data quality and conflicting evidence.",
        "Do not convert correlation into causation without an identified mechanism.",
        "Write the final evidence into the shared Market Context; do not create a second decision engine.",
    ),
)

def get_market_character() -> MarketCharacter:
    return MARKET_CHARACTER

def get_company_impact_framework() -> Dict[str, Tuple[str, ...]]:
    return {
        "direct": MARKET_CHARACTER.direct_exposure_patterns,
        "indirect": MARKET_CHARACTER.indirect_exposure_patterns,
        "cost": MARKET_CHARACTER.cost_channels,
        "revenue": MARKET_CHARACTER.revenue_channels,
        "macro": MARKET_CHARACTER.macro_channels,
        "global": MARKET_CHARACTER.global_channels,
        "events": MARKET_CHARACTER.event_triggers,
    }

def build_calculation_plan(company_character: Any) -> Dict[str, Any]:
    symbol = getattr(company_character, "symbol", getattr(company_character, "name", "UNKNOWN"))
    return {
        "market": MARKET_CHARACTER.market,
        "company": symbol,
        "steps": (
            "resolve company character",
            "map market -> industry -> company pathway",
            "classify direct/indirect/cost/revenue exposure",
            "load synchronized historical data",
            "calculate same-period and lagged returns",
            "calculate rolling statistics and regression",
            "control for NIFTY and sector factors",
            "check volume, volatility and company events",
            "store supporting and conflicting evidence",
            "pass evidence to shared Market Context",
        ),
        "timeframes": MARKET_CHARACTER.timeframes,
        "lag_windows": MARKET_CHARACTER.lag_windows,
        "indicators": MARKET_CHARACTER.indicators,
    }

def validate_character() -> Dict[str, Any]:
    required = (
        MARKET_CHARACTER.market, MARKET_CHARACTER.identity,
        MARKET_CHARACTER.core_drivers, MARKET_CHARACTER.indicators,
        MARKET_CHARACTER.timeframes, MARKET_CHARACTER.lag_windows
    )
    return {
        "valid": all(bool(x) for x in required),
        "market": MARKET_CHARACTER.market,
        "indicator_count": len(MARKET_CHARACTER.indicators),
        "timeframe_count": len(MARKET_CHARACTER.timeframes),
        "lag_count": len(MARKET_CHARACTER.lag_windows),
        "hard_coded_scores": False,
    }

if __name__ == "__main__":
    print(validate_character())
