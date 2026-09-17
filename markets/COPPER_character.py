"""Market character: COPPER. Research layer only; no hard-coded market result."""
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
    market='COPPER',
    market_type='industrial_energy_transition_metal',
    identity='Copper market connecting mining, refining, construction, grids, EVs, electronics and data-centre capex.',
    core_drivers=('global industry', 'China demand', 'mine supply', 'treatment charges', 'grid investment', 'EVs', 'data centres', 'construction'),
    upstream=('copper mines', 'concentrate', 'recycling'),
    processing=('smelting', 'refining', 'rod', 'fabrication'),
    downstream=('grids', 'cables', 'transformers', 'motors', 'EVs', 'electronics', 'construction', 'data centres'),
    demand_sectors=('power', 'construction', 'auto', 'EV', 'telecom', 'electronics', 'data centres', 'renewables'),
    supply_chain_channels=('mine -> concentrate', 'smelter -> cathode', 'cathode -> rod', 'rod -> cable/equipment'),
    direct_exposure_patterns=('copper producer', 'cable manufacturer', 'copper-intensive equipment', 'inventory'),
    indirect_exposure_patterns=('capex cycle', 'grid expansion', 'EV cycle', 'electronics cycle', 'PMI'),
    cost_channels=('copper input', 'energy', 'smelting', 'working capital', 'freight'),
    revenue_channels=('metal realization', 'cable volume', 'equipment demand', 'project capex'),
    macro_channels=('China PMI', 'global PMI', 'infrastructure', 'rates', 'USD'),
    global_channels=('LME/COMEX', 'China imports', 'mine disruption', 'smelter charges', 'grid/EV capex'),
    event_triggers=('mine disruption', 'grid order', 'EV production', 'data-centre capex'),
    indicators=('copper return', 'inventories', 'treatment charges', 'China PMI', 'global PMI', 'copper/gold ratio', 'USD'),
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
