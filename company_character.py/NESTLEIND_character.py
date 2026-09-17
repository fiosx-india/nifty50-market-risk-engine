"""
NESTLEIND_9_MARKETS_CHARACTER
Nestlé India Limited (NESTLEIND)

Character layer for the focused NIFTY 50 / 9-market research engine.

Nestlé India's operating business is food. Its principal product groups are:
- Milk Products and Nutrition
- Prepared Dishes and Cooking Aids
- Powdered and Liquid Beverages
- Confectionery

The nine market characters below describe plausible business transmission
mechanisms to be tested with real historical data. They are not fixed scores.

No RANK, PCT_CHANGE, LINKAGE_SCORE, RELATION, correlation, beta or probability
is hard-coded here. Those belong to the later calculation engine.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Tuple


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
    impact_path: List[str]
    calculation_logic: List[str]
    relevant_indicators: List[str]
    relevant_events: List[str]
    expected_timeframes: List[str]


@dataclass(frozen=True)
class CompanyCharacter:
    symbol: str
    company_name: str
    sector: str
    industry_character: str
    business_character: List[str]
    demand_drivers: List[str]
    revenue_drivers: List[str]
    cost_drivers: List[str]
    supply_chain_character: List[str]
    strategic_drivers: List[str]
    key_indicators: List[str]
    key_events: List[str]
    market_characters: Dict[str, MarketCharacter] = field(default_factory=dict)


def _mc(
    market: str,
    character: str,
    exposure_character: str,
    impact_path: List[str],
    calculation_logic: List[str],
    relevant_indicators: List[str],
    relevant_events: List[str],
    expected_timeframes: List[str],
) -> MarketCharacter:
    return MarketCharacter(
        market=market,
        character=character,
        exposure_character=exposure_character,
        impact_path=impact_path,
        calculation_logic=calculation_logic,
        relevant_indicators=relevant_indicators,
        relevant_events=relevant_events,
        expected_timeframes=expected_timeframes,
    )


COMPANY_CHARACTER = CompanyCharacter(
    symbol="NESTLEIND",
    company_name="Nestlé India Limited",
    sector="FMCG - Food",
    industry_character=(
        "Large branded-food and beverage business whose character is driven by "
        "consumer demand, household penetration, brand strength, premiumisation, "
        "distribution reach, product innovation and agricultural/food commodity "
        "costs. The business operates as a single Food segment covering Milk "
        "Products and Nutrition, Prepared Dishes and Cooking Aids, Powdered and "
        "Liquid Beverages and Confectionery."
    ),
    business_character=[
        "Branded food and beverage portfolio with strong household-consumption characteristics.",
        "Milk Products and Nutrition includes products such as milk-based foods, nutrition and related categories.",
        "Prepared Dishes and Cooking Aids includes convenient cooking/meal products.",
        "Powdered and Liquid Beverages includes coffee and other beverage categories.",
        "Confectionery includes major chocolate/confectionery brands.",
        "Petcare and newer nutrition/health-oriented initiatives provide additional category diversification where applicable.",
        "Business economics depend heavily on brand equity, distribution, innovation and consumer trust.",
        "The company is primarily India-based, so domestic consumer demand, Indian commodity costs and local operating conditions are especially important.",
    ],
    demand_drivers=[
        "Household consumption and FMCG demand.",
        "Urban and rural income growth.",
        "Population and household penetration.",
        "Premiumisation and trading-up.",
        "Modern trade, e-commerce and quick-commerce growth.",
        "Product innovation and new-category penetration.",
        "Brand investment and consumer engagement.",
        "Food-service/out-of-home consumption for relevant products.",
        "Seasonality and festival demand.",
        "Distribution reach and product availability.",
    ],
    revenue_drivers=[
        "Volume growth.",
        "Realisation/price increases.",
        "Product mix.",
        "Premium product mix.",
        "Household penetration.",
        "Market share.",
        "Distribution reach.",
        "E-commerce and modern-trade contribution.",
        "Innovation/new product launches.",
        "Category growth across beverages, confectionery, nutrition and prepared foods.",
    ],
    cost_drivers=[
        "Fresh milk and dairy inputs.",
        "Coffee and cocoa/other agricultural commodities.",
        "Wheat, maize, sugar, spices and edible oils.",
        "Packaging materials.",
        "Crude-linked packaging and logistics costs.",
        "Fuel and freight.",
        "Electricity and factory energy.",
        "Natural gas/industrial energy where used.",
        "Imported ingredients and foreign-exchange exposure.",
        "Advertising and marketing expenditure.",
        "Employee and distribution costs.",
    ],
    supply_chain_character=[
        "Agricultural sourcing is an important upstream dependency.",
        "Milk, coffee, cocoa, wheat, sugar, oils and other food inputs have weather and supply-cycle sensitivity.",
        "Packaging supply is important across food and beverage categories.",
        "Manufacturing plants depend on reliable utilities and food-safety systems.",
        "Distribution availability across general trade, modern trade and digital channels affects realised demand.",
        "Commodity procurement and pricing decisions can create a lag between global commodity prices and reported margins.",
        "Quality, traceability, food safety and regulatory compliance are critical supply-chain characteristics.",
    ],
    strategic_drivers=[
        "Household penetration and distribution expansion.",
        "Premiumisation.",
        "Innovation and renovation of the portfolio.",
        "Digital/e-commerce and quick-commerce execution.",
        "Local sourcing and supply-chain resilience.",
        "Manufacturing capacity and efficiency.",
        "Nutrition and health-oriented product development.",
        "Sustainable agriculture and responsible sourcing.",
        "Brand investment and consumer engagement.",
    ],
    key_indicators=[
        "Volume growth",
        "Domestic sales growth",
        "Net sales",
        "EBITDA margin",
        "Gross margin",
        "Commodity-cost inflation",
        "Milk cost",
        "Coffee cost",
        "Cocoa cost",
        "Wheat/maize/oil/sugar costs",
        "Packaging-cost index",
        "Market share",
        "Household penetration",
        "Distribution reach",
        "E-commerce growth",
        "Premium mix",
        "Advertising and marketing spend",
        "Inventory",
        "Working capital",
    ],
    key_events=[
        "Quarterly and annual results",
        "Major commodity-price changes",
        "Monsoon/agricultural production changes",
        "Coffee/cocoa supply shocks",
        "Milk-price changes",
        "Sugar/wheat/edible-oil price changes",
        "Packaging-cost changes",
        "New product launches",
        "Major brand campaigns",
        "Distribution expansion",
        "E-commerce/quick-commerce developments",
        "Food-safety or regulatory changes",
        "Factory expansion or commissioning",
        "Supply-chain disruptions",
    ],
    market_characters={},
)


MARKET_CHARACTERS: Dict[str, MarketCharacter] = {

    "NIFTY 50": _mc(
        "NIFTY 50",
        "Indian equity-market, liquidity and consumer-cycle character.",
        "Direct market-beta/valuation exposure and indirect signal for household "
        "income, consumption confidence and financial conditions.",
        [
            "NIFTY regime -> equity risk appetite -> NESTLEIND valuation",
            "Economic/liquidity cycle -> household confidence -> FMCG demand",
            "Market regime -> inflation/rates -> consumer spending conditions",
        ],
        [
            "Calculate NESTLEIND returns versus NIFTY.",
            "Estimate rolling correlation and beta.",
            "Estimate downside beta during market stress.",
            "Separate market-wide movement from company-specific residual return.",
            "Test lead/lag windows.",
        ],
        [
            "NESTLEIND return",
            "NIFTY return",
            "Rolling beta",
            "Rolling correlation",
            "Volatility",
            "Relative strength",
        ],
        [
            "NIFTY regime changes",
            "RBI/liquidity events",
            "Budget/tax changes",
            "Consumption shocks",
            "Major risk-off episodes",
        ],
        ["intraday", "1D", "1W", "1M", "3M", "6M", "1Y"],
    ),

    "Crude Oil": _mc(
        "Crude Oil",
        "Packaging, fuel, freight, petrochemical-input and household-inflation character.",
        "Important indirect cost exposure through packaging, logistics and fuel, "
        "plus a macro effect through food inflation and consumer purchasing power.",
        [
            "Crude -> packaging/resin cost -> product cost",
            "Crude -> fuel/freight -> distribution cost",
            "Crude -> inflation -> real household income -> FMCG demand",
            "Crude -> petrochemical inputs -> packaging and supply chain",
        ],
        [
            "Measure lagged NESTLEIND/crude sensitivity.",
            "Use domestic fuel prices and packaging indices alongside crude.",
            "Test margin response rather than assuming stock-price correlation is causal.",
            "Control for NIFTY and food-commodity prices.",
            "Use event studies for major crude shocks.",
        ],
        [
            "Brent/WTI return",
            "Domestic fuel price",
            "Packaging-cost proxy",
            "Freight-cost proxy",
            "Gross margin",
            "Volume growth",
        ],
        [
            "OPEC+ decisions",
            "Large crude shocks",
            "Fuel-price changes",
            "Packaging inflation",
            "Broad inflation shocks",
        ],
        ["1D", "1W", "1M", "3M", "6M", "1Y"],
    ),

    "Gold": _mc(
        "Gold",
        "Household wealth, safe-haven, real-rate and risk-aversion character.",
        "Mostly indirect. Gold is a macro/wealth signal rather than a core food "
        "input, although it can coincide with changes in consumer confidence.",
        [
            "Gold -> wealth/risk regime -> consumer confidence",
            "Gold/rates -> financial conditions -> household spending",
            "Gold/USD/global risk -> equity valuation regime",
        ],
        [
            "Measure NESTLEIND/gold relationship after controlling for NIFTY.",
            "Use gold as a macro regime variable.",
            "Test high-risk-off periods separately.",
            "Compare with FMCG-sector returns and consumption indicators.",
        ],
        [
            "Gold return",
            "Gold volatility",
            "Real-rate proxy",
            "USD index",
            "FMCG-sector return",
            "NESTLEIND volume growth",
        ],
        [
            "Safe-haven shocks",
            "Major rate decisions",
            "Geopolitical risk events",
            "Liquidity stress",
        ],
        ["1D", "1W", "1M", "3M", "6M"],
    ),

    "Silver": _mc(
        "Silver",
        "Precious-metal and industrial-cycle character.",
        "Indirect macro/industrial exposure with limited direct relevance to "
        "Nestlé India's food-input basket.",
        [
            "Silver industrial cycle -> broader economic activity -> consumption",
            "Silver/risk regime -> market sentiment -> valuation",
            "Silver/electronics/industrial cycle -> broader inflation/growth regime",
        ],
        [
            "Calculate rolling NESTLEIND/silver relationship.",
            "Compare silver with broader industrial-cycle variables.",
            "Control for NIFTY and FMCG-sector returns.",
            "Test whether silver leads macro consumption changes.",
        ],
        [
            "Silver return",
            "Gold/silver ratio",
            "Industrial-cycle proxy",
            "FMCG-sector return",
            "NESTLEIND volatility",
        ],
        [
            "Industrial-cycle shocks",
            "Silver volatility events",
            "Global growth changes",
        ],
        ["1D", "1W", "1M", "3M", "6M"],
    ),

    "Natural Gas": _mc(
        "Natural Gas",
        "Industrial energy, factory utility and packaging/chemical-input character.",
        "Indirect operating-cost exposure through manufacturing energy and parts "
        "of the packaging/industrial supply chain.",
        [
            "Gas -> factory energy cost -> manufacturing margin",
            "Gas -> industrial chemical/packaging economics -> input cost",
            "Gas -> inflation -> household purchasing power -> FMCG demand",
        ],
        [
            "Measure lagged NESTLEIND/gas sensitivity.",
            "Use electricity data separately because electricity is a distinct cost channel.",
            "Test utility-cost effects on gross/operating margin.",
            "Control for crude, food commodities and NIFTY.",
        ],
        [
            "Natural-gas return",
            "Gas volatility",
            "Industrial energy-cost proxy",
            "Factory energy cost",
            "Gross margin",
        ],
        [
            "Gas-price shocks",
            "Energy disruptions",
            "Industrial energy-cost changes",
            "LNG/global gas events",
        ],
        ["1D", "1W", "1M", "3M", "6M"],
    ),

    "Copper": _mc(
        "Copper",
        "Electrical equipment, packaging machinery and industrial-capex character.",
        "Mostly indirect through factory equipment, electrical infrastructure and "
        "industrial capex rather than as a major food ingredient.",
        [
            "Copper -> electrical/equipment cost -> factory capex",
            "Copper -> machinery/component cost -> maintenance/capex",
            "Copper industrial cycle -> broader investment/growth regime",
        ],
        [
            "Measure lagged NESTLEIND/copper relationship.",
            "Relate copper changes to capex rather than treating it as a direct food cost.",
            "Test major copper shocks around factory-expansion periods.",
            "Control for NIFTY and industrial-capex indicators.",
        ],
        [
            "Copper return",
            "Copper volatility",
            "Factory capex",
            "Equipment-cost proxy",
            "Capex intensity",
        ],
        [
            "Copper supply disruptions",
            "Major copper-price shocks",
            "Factory expansion",
            "Industrial-equipment cost changes",
        ],
        ["1D", "1W", "1M", "3M", "6M", "1Y"],
    ),

    "Aluminium": _mc(
        "Aluminium",
        "Packaging, beverage cans, machinery, equipment and industrial-material character.",
        "Indirect-to-moderate exposure through packaging/materials, manufacturing "
        "equipment and capex; not a primary food commodity.",
        [
            "Aluminium -> packaging/material cost -> product cost",
            "Aluminium -> equipment/factory capex -> expansion cost",
            "Aluminium industrial cycle -> manufacturing/investment environment",
        ],
        [
            "Measure lagged NESTLEIND/aluminium sensitivity.",
            "Separate packaging exposure from capex exposure.",
            "Use packaging-cost indicators where available.",
            "Test margin response after controlling for other food commodities.",
        ],
        [
            "Aluminium return",
            "Aluminium volatility",
            "Packaging-cost proxy",
            "Factory capex",
            "Gross margin",
        ],
        [
            "Aluminium price shocks",
            "Packaging-cost changes",
            "Factory expansion",
            "Supply disruptions",
        ],
        ["1D", "1W", "1M", "3M", "6M"],
    ),

    "Zinc": _mc(
        "Zinc",
        "Packaging, galvanised equipment and industrial-capex character.",
        "Indirect exposure through factory construction/equipment and selected "
        "packaging/material supply chains; direct food-input exposure is limited.",
        [
            "Zinc -> galvanised steel/equipment cost -> factory capex",
            "Zinc -> industrial supply chain -> maintenance/expansion cost",
            "Zinc industrial cycle -> broader investment/growth regime",
        ],
        [
            "Test lagged NESTLEIND/zinc relationship.",
            "Relate zinc movements to capex and industrial-cost indicators.",
            "Control for steel and other industrial metals.",
            "Avoid treating zinc as a direct food-demand variable.",
        ],
        [
            "Zinc return",
            "Zinc volatility",
            "Steel price",
            "Factory capex",
            "Construction-cost proxy",
        ],
        [
            "Zinc supply shocks",
            "Industrial-metal inflation",
            "Factory construction",
            "Equipment-cost changes",
        ],
        ["1D", "1W", "1M", "3M", "6M"],
    ),

    "Electricity": _mc(
        "Electricity",
        "Core food-manufacturing, refrigeration, processing and distribution-utility character.",
        "Direct operating exposure: factories, processing, refrigeration, water "
        "systems, warehouses and other food-supply-chain facilities require reliable power.",
        [
            "Electricity cost -> factory utility expense -> gross/operating margin",
            "Power reliability -> production uptime -> product availability",
            "Electricity cost -> cold-chain/distribution cost -> supply-chain economics",
            "Power availability -> capacity utilisation -> volume fulfilment",
        ],
        [
            "Use reliable industrial/commercial electricity data.",
            "Measure lagged electricity-cost sensitivity to margins.",
            "Test outages/disruptions as event variables.",
            "Separate electricity price from availability/reliability.",
            "Compare electricity effects with fuel and food-commodity costs.",
        ],
        [
            "Industrial electricity price",
            "Power demand",
            "Peak demand",
            "Factory utilisation",
            "Energy cost",
            "Gross margin",
            "Production volume",
        ],
        [
            "Power shortages",
            "Electricity-price shocks",
            "Factory disruptions",
            "Capacity additions",
            "Energy-efficiency projects",
        ],
        ["intraday", "1D", "1W", "1M", "3M", "6M", "1Y"],
    ),
}


COMPANY_CHARACTER = CompanyCharacter(
    symbol=COMPANY_CHARACTER.symbol,
    company_name=COMPANY_CHARACTER.company_name,
    sector=COMPANY_CHARACTER.sector,
    industry_character=COMPANY_CHARACTER.industry_character,
    business_character=COMPANY_CHARACTER.business_character,
    demand_drivers=COMPANY_CHARACTER.demand_drivers,
    revenue_drivers=COMPANY_CHARACTER.revenue_drivers,
    cost_drivers=COMPANY_CHARACTER.cost_drivers,
    supply_chain_character=COMPANY_CHARACTER.supply_chain_character,
    strategic_drivers=COMPANY_CHARACTER.strategic_drivers,
    key_indicators=COMPANY_CHARACTER.key_indicators,
    key_events=COMPANY_CHARACTER.key_events,
    market_characters=MARKET_CHARACTERS,
)


def get_company_character() -> CompanyCharacter:
    """Return the complete Nestlé India company character."""
    return COMPANY_CHARACTER


def get_market_character(market: str) -> MarketCharacter:
    """Return one market character for Nestlé India."""
    key = market.strip()
    if key not in MARKET_CHARACTERS:
        raise KeyError(
            f"Unsupported market: {market!r}. "
            f"Expected one of: {', '.join(TRACKED_MARKETS)}"
        )
    return MARKET_CHARACTERS[key]


def get_all_market_characters() -> Dict[str, MarketCharacter]:
    """Return all nine market characters."""
    return dict(MARKET_CHARACTERS)


def validate_character() -> dict:
    """Structural validation only; no market scores are calculated."""
    expected = set(TRACKED_MARKETS)
    actual = set(MARKET_CHARACTERS)
    missing = sorted(expected - actual)
    extra = sorted(actual - expected)

    return {
        "symbol": COMPANY_CHARACTER.symbol,
        "markets_expected": 9,
        "markets_found": len(MARKET_CHARACTERS),
        "missing_markets": missing,
        "extra_markets": extra,
        "valid": not missing and not extra and len(MARKET_CHARACTERS) == 9,
        "calculated_fields_present": False,
        "note": (
            "RANK/PCT_CHANGE/LINKAGE_SCORE/RELATION are intentionally absent. "
            "Historical relationships belong to the later calculation engine."
        ),
    }


if __name__ == "__main__":
    print(validate_character())
    for market in TRACKED_MARKETS:
        print(f"{market}: {get_market_character(market).character}")
