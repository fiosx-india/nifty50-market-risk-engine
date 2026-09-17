"""
GRASIM — Company Character & 9-Market Research Model

Purpose
-------
This module defines the business character of GRASIM and, for each of the
9 tracked markets, describes the economic exposure, transmission path,
indicators, events and timeframes that a later historical engine should
calculate from real data.

Important:
- No hard-coded linkage scores, ranks, percentage changes or BUY/SELL/HOLD.
- This file defines the research model; it does not claim that an observed
  relationship is causal.
- Historical calculations should be performed by the shared analytics layer.
"""

from dataclasses import dataclass
from typing import Dict, Tuple


TRACKED_MARKETS: Tuple[str, ...] = (
    "NIFTY 50",
    "Crude Oil",
    "Gold",
    "Silver",
    "Natural Gas",
    "Copper",
    "Aluminium",
    "Zinc",
    "Electricity",
)


@dataclass(frozen=True)
class MarketCharacter:
    market: str
    character: str
    exposure_character: str
    impact_path: str
    calculation_logic: str
    relevant_indicators: Tuple[str, ...]
    relevant_events: Tuple[str, ...]
    expected_timeframes: Tuple[str, ...]


@dataclass(frozen=True)
class CompanyCharacter:
    symbol: str
    company_name: str
    sector: str
    industry_character: str
    business_character: str
    demand_drivers: Tuple[str, ...]
    revenue_drivers: Tuple[str, ...]
    cost_drivers: Tuple[str, ...]
    supply_chain_character: Tuple[str, ...]
    strategic_drivers: Tuple[str, ...]
    key_indicators: Tuple[str, ...]
    key_events: Tuple[str, ...]
    market_characters: Dict[str, MarketCharacter]


def _mc(
    market: str,
    character: str,
    exposure_character: str,
    impact_path: str,
    calculation_logic: str,
    indicators: Tuple[str, ...],
    events: Tuple[str, ...],
    timeframes: Tuple[str, ...],
) -> MarketCharacter:
    return MarketCharacter(
        market=market,
        character=character,
        exposure_character=exposure_character,
        impact_path=impact_path,
        calculation_logic=calculation_logic,
        relevant_indicators=indicators,
        relevant_events=events,
        expected_timeframes=timeframes,
    )


MARKET_CHARACTERS: Dict[str, MarketCharacter] = {
    "Aluminium": _mc(
        "Aluminium",
        "Industrial input and construction/consumer-material cycle signal.",
        "Multi-layer exposure through cement/building materials, paints, "
        "construction distribution, electrical/industrial products and packaging; "
        "also relevant to selected downstream businesses.",
        "Aluminium price/availability -> input or project cost -> margins/capex/"
        "construction demand -> UltraTech, Birla Opus, Birla Pivot and other "
        "Grasim-linked operating businesses -> consolidated earnings.",
        "Measure Grasim/subsidiary returns against aluminium returns using rolling "
        "correlation, lagged correlation, regression/beta and event windows. "
        "Separate cost-sensitive businesses from demand-sensitive businesses and "
        "control for NIFTY 50 and broad industrial conditions.",
        (
            "Aluminium spot/futures return",
            "volatility",
            "inventory/availability proxy",
            "Grasim return and volume",
            "cement/paint/building-material indicators",
        ),
        (
            "aluminium supply disruptions",
            "smelter/refinery capacity changes",
            "import/export policy",
            "infrastructure/construction cycle changes",
        ),
        ("1D", "1W", "1M", "1Q", "6M"),
    ),
    "Copper": _mc(
        "Copper",
        "Electrical, industrial and infrastructure-cycle signal.",
        "Indirect-to-moderate exposure through infrastructure, electrical "
        "equipment, construction, renewables and industrial activity rather than "
        "a simple direct commodity input relationship.",
        "Copper cycle -> industrial/infrastructure activity and selected input "
        "costs -> demand/capex/margins in building-material, chemicals, paints, "
        "insulators and renewable-related businesses -> Grasim earnings.",
        "Use lagged cross-correlation, rolling beta and multivariate regression "
        "with NIFTY/industrial controls. Test whether copper adds explanatory "
        "power beyond broad market and construction variables.",
        (
            "copper return",
            "industrial-demand proxy",
            "Grasim return",
            "relative sector performance",
            "volume and volatility",
        ),
        (
            "global manufacturing cycle",
            "power-grid/renewables capex",
            "copper supply disruptions",
            "infrastructure spending changes",
        ),
        ("1D", "1W", "1M", "1Q", "6M"),
    ),
    "Crude Oil": _mc(
        "Crude Oil",
        "Energy and transportation-cost shock with inflation and macro spillovers.",
        "Primarily indirect exposure through freight/logistics, chemicals, "
        "manufacturing energy costs, packaging/materials and inflation-sensitive "
        "consumer demand; effects differ across Grasim businesses.",
        "Crude -> fuel/transport and petrochemical-linked costs -> manufacturing/"
        "distribution cost -> margins; crude -> inflation/rates -> housing/"
        "construction/consumer demand -> cement/paints/textiles/financial services.",
        "Estimate business-sensitive exposure using lagged regression and event "
        "studies. Test asymmetric effects for sharp oil spikes versus declines, "
        "while controlling for INR, NIFTY and inflation/rates.",
        (
            "Brent/WTI return",
            "oil volatility",
            "INR/USD",
            "inflation proxy",
            "Grasim return/volume",
            "freight-cost proxy",
        ),
        (
            "OPEC+ decisions",
            "geopolitical supply disruptions",
            "large oil-price shocks",
            "Indian fuel-tax or policy changes",
        ),
        ("1D", "1W", "1M", "1Q"),
    ),
    "Electricity": _mc(
        "Electricity",
        "Core industrial operating input and reliability constraint.",
        "Direct operating exposure across chemicals, fibres, cement, paints, "
        "textiles, insulators and other manufacturing/renewable operations; "
        "also creates an opportunity through captive/renewable power.",
        "Power price/reliability -> plant operating cost/utilisation -> segment "
        "margin and production volume -> consolidated performance.",
        "Where plant-level power data exists, compare segment cost/margin changes "
        "with power prices and generation conditions. Use lagged regression, "
        "rolling sensitivity and event windows; avoid treating national power "
        "prices as identical to Grasim's actual procurement cost.",
        (
            "power price",
            "industrial electricity demand",
            "plant utilisation",
            "renewable/captive generation",
            "segment EBITDA/margin",
        ),
        (
            "power shortages",
            "tariff changes",
            "renewable capacity additions",
            "captive-power changes",
            "major plant outages",
        ),
        ("1D", "1W", "1M", "1Q"),
    ),
    "Gold": _mc(
        "Gold",
        "Safe-haven, liquidity, inflation and household-wealth sentiment signal.",
        "Mostly indirect exposure through macro sentiment, real rates, liquidity, "
        "INR and household/investment behaviour; not a primary operating input.",
        "Gold -> risk sentiment/liquidity/real-rate expectations -> NIFTY and "
        "financial conditions -> valuation and demand across Grasim's diversified "
        "businesses.",
        "Use gold returns as one explanatory macro factor in a multivariate model. "
        "Test independent contribution after controlling for NIFTY, USD/INR, "
        "rates and volatility; do not infer causation from correlation alone.",
        (
            "gold return",
            "real-rate proxy",
            "USD/INR",
            "market volatility",
            "NIFTY return",
            "Grasim relative return",
        ),
        (
            "central-bank rate decisions",
            "inflation surprises",
            "geopolitical risk events",
            "large gold-price moves",
        ),
        ("1D", "1W", "1M", "1Q"),
    ),
    "NIFTY 50": _mc(
        "NIFTY 50",
        "Systematic Indian-equity market and diversified-conglomerate valuation signal.",
        "Direct market exposure through Grasim's listed equity beta, sector "
        "rotation and valuation regime; also indirect through the operating "
        "business cycle.",
        "NIFTY -> market risk appetite/liquidity -> Grasim valuation and capital "
        "cost -> operating-business expectations -> stock return/volume.",
        "Calculate rolling correlation, beta, downside beta, relative strength, "
        "drawdown and residual return versus NIFTY. Use multiple horizons rather "
        "than a fixed linkage score.",
        (
            "NIFTY return",
            "rolling beta",
            "relative strength",
            "volume",
            "volatility",
            "drawdown",
        ),
        (
            "RBI policy",
            "Union Budget/fiscal policy",
            "major earnings cycles",
            "global risk-off events",
            "large index rebalancing events",
        ),
        ("5m", "15m", "1H", "1D", "1W", "1M", "1Q", "1Y"),
    ),
    "Natural Gas": _mc(
        "Natural Gas",
        "Industrial energy and chemical-feedstock sensitivity signal.",
        "Exposure varies by plant and process: energy use in manufacturing and "
        "indirect chemical/input-cost effects; renewable/captive power can change "
        "net sensitivity.",
        "Natural gas -> energy/chemical input cost -> production economics/margins "
        "-> chemicals, fibres, building materials and other operating businesses.",
        "Use plant/segment energy-cost data when available. Otherwise use gas "
        "returns as a macro factor and test lagged sensitivity with controls for "
        "electricity, crude, NIFTY and industrial conditions.",
        (
            "natural-gas return",
            "gas volatility",
            "industrial energy proxy",
            "chemical-margin proxy",
            "segment EBITDA/margin",
        ),
        (
            "LNG/gas supply disruption",
            "global gas-price shock",
            "Indian gas-price policy changes",
            "industrial demand changes",
        ),
        ("1D", "1W", "1M", "1Q"),
    ),
    "Silver": _mc(
        "Silver",
        "Industrial-metals plus precious-metals macro-cycle signal.",
        "Indirect exposure through industrial activity, electrical/renewable "
        "investment, investor sentiment and inflation/liquidity conditions.",
        "Silver -> industrial/technology cycle and risk sentiment -> construction/"
        "industrial demand and market valuation -> Grasim businesses/stock.",
        "Test silver against Grasim using rolling and lagged correlations and "
        "multivariate regression. Compare its incremental explanatory power with "
        "copper, gold and NIFTY.",
        (
            "silver return",
            "industrial-metals basket",
            "gold/silver ratio",
            "volatility",
            "Grasim relative return",
        ),
        (
            "industrial-demand shocks",
            "precious-metals risk events",
            "solar/electronics demand changes",
            "global manufacturing changes",
        ),
        ("1D", "1W", "1M", "1Q"),
    ),
    "Zinc": _mc(
        "Zinc",
        "Galvanising and infrastructure/steel-cycle indicator.",
        "Indirect exposure through steel-intensive construction, infrastructure, "
        "industrial capex and building-material demand; stronger through the "
        "UltraTech/building-material ecosystem than through a direct zinc input.",
        "Zinc -> steel/galvanising and construction cycle -> infrastructure/building "
        "activity -> cement, paints, B2B building-material demand -> Grasim.",
        "Use lagged zinc returns, construction/steel controls and NIFTY in a "
        "multivariate model. Test whether zinc leads Grasim's relevant business "
        "returns or only co-moves with the industrial cycle.",
        (
            "zinc return",
            "steel return",
            "construction proxy",
            "industrial production proxy",
            "Grasim return/volume",
        ),
        (
            "infrastructure spending",
            "steel-cycle changes",
            "zinc supply disruptions",
            "construction demand shocks",
        ),
        ("1D", "1W", "1M", "1Q", "6M"),
    ),
}


COMPANY_CHARACTER = CompanyCharacter(
    symbol="GRASIM",
    company_name="Grasim Industries Limited",
    sector="Diversified Industrials / Building Materials / Chemicals / Textiles / Financial Services",
    industry_character=(
        "A highly diversified, conglomerate-style operating structure. Grasim's "
        "current portfolio spans cellulosic fibres, chemicals, cement through "
        "UltraTech, paints through Birla Opus, B2B e-commerce through Birla Pivot, "
        "financial services through Aditya Birla Capital, textiles, renewables "
        "and insulators. Therefore its market sensitivity is multi-channel rather "
        "than reducible to one commodity relationship."
    ),
    business_character=(
        "Portfolio and capital-allocation character: industrial manufacturing "
        "plus building materials, chemicals, consumer-facing paints, textile "
        "materials, financial services and renewable-energy exposure. The model "
        "must evaluate each operating channel separately and then aggregate "
        "evidence at the Grasim level."
    ),
    demand_drivers=(
        "Indian infrastructure and construction activity",
        "housing and real-estate activity",
        "cement and building-material demand",
        "decorative-paints demand and dealer/contractor expansion",
        "textile and apparel demand",
        "global cellulosic-fibre demand",
        "industrial chemical demand",
        "MSME construction-material procurement",
        "credit demand and financialisation",
        "renewable-energy investment",
    ),
    revenue_drivers=(
        "cellulosic-fibre volumes and product mix",
        "chemical volumes and realisations",
        "UltraTech cement volumes and realisations",
        "Birla Opus paints volumes, distribution and mix",
        "Birla Pivot transaction/revenue growth",
        "Aditya Birla Capital lending, AUM and fee income",
        "textiles volumes and premium mix",
        "renewable-energy capacity and generation",
        "insulator volumes and exports",
    ),
    cost_drivers=(
        "energy and electricity",
        "coal/fuel and freight",
        "chemical feedstock and input costs",
        "raw materials and packaging",
        "logistics and distribution",
        "employee costs",
        "capacity-expansion and commissioning costs",
        "interest/financing costs",
        "working capital",
        "maintenance and environmental compliance",
    ),
    supply_chain_character=(
        "large multi-plant manufacturing network",
        "chemical and industrial feedstock suppliers",
        "coal, fuel and electricity suppliers",
        "limestone and other cement raw materials",
        "transport and logistics providers",
        "dealer/distributor/contractor network for paints and building materials",
        "textile and fibre downstream customers",
        "MSME buyers through B2B e-commerce",
        "financial-services distribution and digital channels",
        "renewable-energy project ecosystem",
    ),
    strategic_drivers=(
        "cement capacity expansion and operating efficiency",
        "Birla Opus scale-up and distribution density",
        "specialty and higher-value cellulosic fibres",
        "chemical integration and product mix",
        "Birla Pivot scale and repeat buyers",
        "financial-services growth and capital allocation",
        "renewable-energy expansion",
        "portfolio synergies across building materials and industrial businesses",
        "capital efficiency and free cash flow",
        "deleveraging and disciplined investment",
    ),
    key_indicators=(
        "consolidated revenue",
        "consolidated EBITDA and margin",
        "segment revenue and EBITDA",
        "cement volume and realisation",
        "cellulosic-fibre volume and realisation",
        "chemical sales volume and realisation",
        "paint revenue, volume and distribution",
        "Birla Pivot revenue/order activity",
        "financial-services lending/AUM and profitability",
        "power/energy cost",
        "capacity utilisation",
        "capex",
        "working capital",
        "operating cash flow/free cash flow",
        "GRASIM return, volume and relative strength",
    ),
    key_events=(
        "quarterly and annual results",
        "UltraTech capacity additions/acquisitions",
        "Birla Opus plant commissioning and distribution expansion",
        "chemical capacity additions or shutdowns",
        "cellulosic-fibre capacity/product-mix changes",
        "large capex announcements",
        "Aditya Birla Capital funding/capital-allocation events",
        "renewable project additions",
        "major environmental/regulatory changes",
        "input-cost and energy shocks",
        "large M&A or subsidiary restructuring",
        "management guidance changes",
    ),
    market_characters=MARKET_CHARACTERS,
)


def get_company_character() -> CompanyCharacter:
    """Return the complete GRASIM company character."""
    return COMPANY_CHARACTER


def get_market_character(market: str) -> MarketCharacter:
    """Return GRASIM's character/exposure model for one tracked market."""
    try:
        return COMPANY_CHARACTER.market_characters[market]
    except KeyError as exc:
        raise ValueError(
            f"Unsupported market: {market!r}. "
            f"Expected one of: {', '.join(TRACKED_MARKETS)}"
        ) from exc


def get_all_market_characters() -> Dict[str, MarketCharacter]:
    """Return all 9 market character definitions."""
    return dict(COMPANY_CHARACTER.market_characters)


def validate_character() -> bool:
    """
    Validate architecture-level requirements.

    This intentionally checks structure only. It does not manufacture
    historical scores or infer a market prediction.
    """
    if COMPANY_CHARACTER.symbol != "GRASIM":
        return False

    if tuple(COMPANY_CHARACTER.market_characters.keys()) != TRACKED_MARKETS:
        return False

    for market in TRACKED_MARKETS:
        item = COMPANY_CHARACTER.market_characters[market]
        if item.market != market:
            return False
        if not item.character or not item.exposure_character:
            return False
        if not item.impact_path or not item.calculation_logic:
            return False
        if not item.relevant_indicators or not item.relevant_events:
            return False
        if not item.expected_timeframes:
            return False

    return True


if __name__ == "__main__":
    print("GRASIM character valid:", validate_character())
    print("Tracked markets:", ", ".join(TRACKED_MARKETS))
    print("Company:", COMPANY_CHARACTER.company_name)
    print("Business character:", COMPANY_CHARACTER.business_character)
