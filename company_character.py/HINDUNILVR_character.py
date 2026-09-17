"""
HINDUNILVR — Company Character & 9-Market Research Model

Research-definition layer for Hindustan Unilever Limited (HUL).

The supplied 9-market CSV contains rank, daily change, linkage score and
relation fields. Those values are intentionally NOT hard-coded here.

This module defines:
    Company Character
    Industry Character
    Demand / Revenue / Cost Drivers
    Supply Chain
    Strategic Drivers
    Key Indicators / Events
    9 Market Characters
    Impact paths
    Historical calculation logic
    Timeframes

Historical linkage, probability and trading decisions belong to later
analytics layers and must be calculated from real data.
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
        "Packaging, home-appliance, transport and manufacturing input-cost signal.",
        "Indirect but meaningful exposure through packaging materials, personal-care "
        "containers, food packaging, appliances, logistics and selected manufacturing "
        "inputs. HUL is primarily a consumer-goods company, not an aluminium producer.",
        "Aluminium -> packaging/container and selected supply-chain costs -> gross "
        "margin -> pricing/pack architecture -> consumer volume and revenue -> HUL.",
        "Use aluminium as a component of a packaging/material-cost basket. Compare "
        "aluminium changes with gross margin, material-cost inflation, price/mix, "
        "volume growth and stock returns. Use lagged regression and event studies "
        "with crude, FX and other commodity controls.",
        (
            "aluminium price",
            "packaging-cost proxy",
            "material-cost inflation",
            "gross margin",
            "UVG/volume growth",
            "HUL relative return",
        ),
        (
            "aluminium price shocks",
            "packaging-cost changes",
            "supply disruptions",
            "major packaging-material innovations",
        ),
        ("1D", "1W", "1M", "1Q", "6M"),
    ),
    "Copper": _mc(
        "Copper",
        "Electrical, equipment, packaging and industrial-input macro signal.",
        "Mostly indirect exposure through electrical equipment, machinery, "
        "manufacturing infrastructure, distribution assets and selected packaging "
        "or supply-chain inputs. It is more important as a broad industrial-cycle "
        "variable than as a direct HUL raw material.",
        "Copper -> industrial/electrical cost and demand cycle -> supplier/customer "
        "economics -> input costs and household/business activity -> HUL volume/margin.",
        "Test copper against HUL material costs, gross margin, volume growth and "
        "relative returns while controlling for NIFTY, crude, FX and broad industrial "
        "activity. Do not assume a direct copper-to-HUL causal relationship.",
        (
            "copper price",
            "industrial-production proxy",
            "material-cost inflation",
            "gross margin",
            "volume growth",
            "HUL return",
        ),
        (
            "industrial-cycle changes",
            "electrical-infrastructure investment",
            "copper supply shocks",
            "manufacturing cost changes",
        ),
        ("1D", "1W", "1M", "1Q"),
    ),
    "Crude Oil": _mc(
        "Crude Oil",
        "Major consumer-goods input-cost, packaging, logistics and household-purchasing-power signal.",
        "Material exposure through petrochemical-derived packaging and chemicals, "
        "surfactants, fragrances, plastics, transport/freight and energy. Oil also "
        "affects household disposable income and therefore consumption.",
        "Crude -> petrochemical/chemical + packaging + freight costs -> gross margin "
        "and pricing pressure; crude -> inflation/disposable income -> consumer "
        "volume and premiumisation -> HUL revenue.",
        "Model both cost and demand channels. Use oil returns and lags against "
        "material-cost inflation, gross margin, pricing, UVG, mix and stock returns. "
        "Control for USD/INR, CPI, rural/urban consumption and other commodity prices. "
        "Test asymmetric effects during oil spikes.",
        (
            "Brent/WTI return",
            "oil volatility",
            "packaging/material-cost proxy",
            "freight-cost proxy",
            "gross margin",
            "UVG/volume growth",
            "price/mix",
        ),
        (
            "OPEC+ decisions",
            "geopolitical supply disruptions",
            "fuel-price changes",
            "petrochemical feedstock shocks",
            "inflation surprises",
        ),
        ("1D", "1W", "1M", "1Q", "6M"),
    ),
    "Electricity": _mc(
        "Electricity",
        "Manufacturing, cold-chain, warehouse, digital and household-cost signal.",
        "Direct operating exposure through factories, warehouses, offices, "
        "distribution and technology infrastructure; indirect exposure through "
        "supplier costs and household purchasing power.",
        "Electricity cost/reliability -> factory/warehouse operating cost -> gross "
        "margin; electricity availability -> production/service continuity; power "
        "cost -> household budget -> consumption.",
        "Where company/plant data exists, compare energy cost per unit with production "
        "and margin. Use regional electricity proxies otherwise. Separate direct "
        "operating-cost effects from consumer-demand effects and control for broader "
        "inflation.",
        (
            "electricity cost",
            "factory energy intensity",
            "production volume",
            "gross margin",
            "CPI/household consumption",
            "HUL return",
        ),
        (
            "tariff changes",
            "power shortages",
            "renewable-energy projects",
            "major plant outages",
            "energy-efficiency investments",
        ),
        ("1D", "1W", "1M", "1Q"),
    ),
    "Gold": _mc(
        "Gold",
        "Household wealth, inflation, risk-sentiment and premium-consumption signal.",
        "Primarily indirect exposure. Gold can affect household wealth perception, "
        "savings allocation, inflation expectations and discretionary/premium "
        "consumption sentiment.",
        "Gold -> wealth/risk/inflation expectations -> household spending and "
        "premiumisation -> beauty, personal care, foods and home-care demand.",
        "Test gold against HUL volume growth, premium portfolio growth, rural/urban "
        "consumption proxies and stock returns. Control for NIFTY, inflation, "
        "interest rates and USD/INR.",
        (
            "gold return",
            "gold volatility",
            "consumer-confidence proxy",
            "premium-segment growth",
            "volume growth",
            "HUL relative return",
        ),
        (
            "large gold-price moves",
            "inflation shocks",
            "geopolitical risk",
            "household savings/consumption changes",
        ),
        ("1D", "1W", "1M", "1Q", "6M"),
    ),
    "NIFTY 50": _mc(
        "NIFTY 50",
        "Indian consumer-equity, liquidity and macro-risk benchmark.",
        "Direct listed-equity market exposure through beta, valuation and investor "
        "flows. Indirectly, NIFTY reflects Indian economic confidence, income and "
        "consumption expectations.",
        "NIFTY -> market liquidity/risk appetite -> HUL valuation and flows; "
        "NIFTY/economic cycle -> household income and consumption -> HUL volume, "
        "mix and earnings expectations.",
        "Calculate rolling correlation, beta, downside beta, relative strength, "
        "drawdown and residual return. Separately model fundamental drivers using "
        "volume growth, margins, commodity basket, FX, inflation and rural/urban "
        "consumption indicators.",
        (
            "NIFTY return",
            "rolling beta",
            "FMCG relative strength",
            "volume",
            "volatility",
            "drawdown",
            "consumer-sector performance",
        ),
        (
            "RBI policy",
            "Union Budget",
            "GST/tax changes",
            "major index rebalancing",
            "consumer-demand shocks",
        ),
        ("5m", "15m", "1H", "1D", "1W", "1M", "1Q", "1Y"),
    ),
    "Natural Gas": _mc(
        "Natural Gas",
        "Energy, chemical-feedstock and industrial-cost signal.",
        "Indirect exposure through chemical/feedstock markets, manufacturing "
        "energy costs, packaging inputs and broad inflation. It is less direct "
        "than crude/petrochemical prices for HUL.",
        "Natural gas -> chemical/feedstock and energy costs -> material inflation "
        "and gross margin; gas -> inflation/industrial activity -> household "
        "purchasing power -> consumer demand.",
        "Use natural gas as a secondary input-cost factor alongside crude, "
        "petrochemical and electricity variables. Test lagged effects on gross "
        "margin, material costs and volume growth.",
        (
            "natural-gas price",
            "gas volatility",
            "chemical-cost proxy",
            "material-cost inflation",
            "gross margin",
            "volume growth",
        ),
        (
            "LNG/gas supply disruptions",
            "global gas-price shocks",
            "chemical-feedstock changes",
            "industrial energy shocks",
        ),
        ("1D", "1W", "1M", "1Q"),
    ),
    "Silver": _mc(
        "Silver",
        "Industrial and household-wealth macro signal.",
        "Indirect exposure through electronics/equipment, industrial activity and "
        "household risk/wealth sentiment. Silver is not a primary HUL raw material.",
        "Silver -> industrial cycle and wealth/risk sentiment -> consumer confidence "
        "and input/equipment economics -> HUL demand/margins.",
        "Compare silver with copper, gold, consumer confidence, HUL volume and "
        "gross margin. Use multivariate lag analysis to determine whether silver "
        "adds information beyond other macro variables.",
        (
            "silver price",
            "silver volatility",
            "gold/silver ratio",
            "consumer-confidence proxy",
            "volume growth",
            "gross margin",
        ),
        (
            "industrial-cycle shocks",
            "precious-metal moves",
            "electronics/industrial demand changes",
            "consumer-confidence changes",
        ),
        ("1D", "1W", "1M", "1Q"),
    ),
    "Zinc": _mc(
        "Zinc",
        "Packaging, galvanised-steel and industrial-demand signal.",
        "Indirect exposure through packaging, metal components, manufacturing "
        "equipment and supplier costs. The strongest relevance is through the "
        "industrial and packaging ecosystem rather than direct product formulation.",
        "Zinc -> packaging/metal-component and industrial costs -> material cost "
        "and supply-chain economics -> HUL margin/volume.",
        "Use zinc as one factor in a broader metals/materials basket. Test lagged "
        "effects on packaging costs, gross margin and volume growth, controlling "
        "for aluminium, crude, FX and inflation.",
        (
            "zinc price",
            "steel/galvanising proxy",
            "packaging-cost proxy",
            "material-cost inflation",
            "gross margin",
            "volume growth",
        ),
        (
            "infrastructure cycle",
            "packaging-material changes",
            "zinc supply disruptions",
            "industrial production changes",
        ),
        ("1D", "1W", "1M", "1Q", "6M"),
    ),
}


COMPANY_CHARACTER = CompanyCharacter(
    symbol="HINDUNILVR",
    company_name="Hindustan Unilever Limited",
    sector="FMCG / Consumer Staples",
    industry_character=(
        "India's largest FMCG platform with a broad everyday-consumption portfolio "
        "across Home Care, Beauty & Wellbeing, Personal Care and Foods. Its economic "
        "character is driven by brand strength, household penetration, distribution "
        "reach, pricing, volume growth, premiumisation, commodity inflation and "
        "consumer income rather than by one single commodity."
    ),
    business_character=(
        "High-frequency consumer-demand character built around trusted brands, "
        "large-scale manufacturing and an extensive distribution ecosystem. The "
        "business spans home care, beauty and wellbeing, personal care and foods, "
        "with multiple price points and channels. The core chain is consumer need "
        "-> brand/proposition -> distribution and availability -> volume/price/mix "
        "-> gross margin -> operating profit and cash flow."
    ),
    demand_drivers=(
        "household consumption",
        "urban consumption",
        "rural consumption",
        "disposable income",
        "consumer confidence",
        "premiumisation",
        "health and wellness awareness",
        "beauty and personal-care routines",
        "home-care penetration",
        "food and beverages consumption",
        "population and household formation",
        "modern trade",
        "e-commerce and quick-commerce",
        "channels of the future",
        "seasonality and festivals",
    ),
    revenue_drivers=(
        "underlying volume growth",
        "pricing",
        "price/mix",
        "premium portfolio growth",
        "Home Care sales",
        "Beauty & Wellbeing sales",
        "Personal Care sales",
        "Foods sales",
        "brand strength",
        "distribution reach",
        "general trade",
        "modern trade",
        "e-commerce",
        "quick-commerce",
        "digital-first demand generation",
        "new product launches",
    ),
    cost_drivers=(
        "crude-linked inputs",
        "palm oil and vegetable oils",
        "petrochemical-derived materials",
        "packaging materials",
        "chemicals and surfactants",
        "food raw materials",
        "tea/coffee and agricultural inputs",
        "freight and logistics",
        "electricity and fuel",
        "employee costs",
        "advertising and promotion",
        "manufacturing",
        "distribution",
        "currency movements",
        "innovation and product-development costs",
    ),
    supply_chain_character=(
        "agricultural raw-material suppliers",
        "chemical and ingredient suppliers",
        "packaging suppliers",
        "plastic and paper suppliers",
        "manufacturing plants",
        "warehouses and logistics providers",
        "distributors",
        "general-trade retailers",
        "modern-trade retailers",
        "e-commerce platforms",
        "quick-commerce channels",
        "millions of consumers",
        "farmer and regenerative-agriculture ecosystem",
    ),
    strategic_drivers=(
        "volume-led revenue growth",
        "brand investment",
        "consumer segmentation",
        "premiumisation",
        "science-led innovation",
        "digital-first demand generation",
        "specialised general trade",
        "modern trade and e-commerce",
        "quick-commerce/channel-of-future expansion",
        "portfolio choices and capital allocation",
        "cost productivity",
        "AI and digital consumer insight",
        "sustainable sourcing",
        "renewable energy and decarbonisation",
        "packaging circularity",
        "Minimalist and OZiva portfolio development",
    ),
    key_indicators=(
        "underlying volume growth",
        "underlying sales growth",
        "turnover",
        "EBITDA",
        "EBITDA margin",
        "gross margin",
        "price/mix",
        "Home Care growth",
        "Beauty & Wellbeing growth",
        "Personal Care growth",
        "Foods growth",
        "rural growth",
        "urban growth",
        "premium portfolio growth",
        "advertising and promotion spend",
        "working capital",
        "free cash flow",
        "commodity-cost basket",
        "HINDUNILVR return, volume and relative strength",
    ),
    key_events=(
        "quarterly and annual results",
        "commodity-cost shocks",
        "crude/petrochemical price changes",
        "palm-oil and agricultural commodity changes",
        "GST/tax changes",
        "rural-demand changes",
        "urban-consumption changes",
        "major brand launches",
        "pricing changes",
        "pack-size changes",
        "distribution expansion",
        "e-commerce/quick-commerce changes",
        "Minimalist/OZiva portfolio developments",
        "manufacturing-capacity changes",
        "renewable-energy projects",
        "packaging/circularity initiatives",
        "major regulatory or food-safety events",
    ),
    market_characters=MARKET_CHARACTERS,
)


def get_company_character() -> CompanyCharacter:
    """Return the complete HINDUNILVR company character."""
    return COMPANY_CHARACTER


def get_market_character(market: str) -> MarketCharacter:
    """Return HINDUNILVR's character/exposure model for one tracked market."""
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
    Validate architecture and structure only.

    Historical linkage, rank, percentage change, probability and trading
    decisions are deliberately outside this module.
    """
    if COMPANY_CHARACTER.symbol != "HINDUNILVR":
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
    print("HINDUNILVR character valid:", validate_character())
    print("Tracked markets:", ", ".join(TRACKED_MARKETS))
    print("Company:", COMPANY_CHARACTER.company_name)
