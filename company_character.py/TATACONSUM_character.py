"""
TATACONSUM Character Model
===========================
Business character + nine tracked market characters for Tata Consumer Products.

This module defines the company's business character and WHAT should be
measured for each of the nine markets.

It intentionally does not hard-code:
- RANK
- PCT_CHANGE
- LINKAGE_SCORE
- RELATION
- correlation
- beta
- probability
- trading decisions

Those values must be calculated later from real historical, operational,
commodity, macro, news and event data.
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
    exposure_type: str
    impact_channels: Tuple[str, ...]
    supply_chain_links: Tuple[str, ...]
    demand_links: Tuple[str, ...]
    cost_links: Tuple[str, ...]
    macro_links: Tuple[str, ...]
    indicators_to_measure: Tuple[str, ...]
    event_signals: Tuple[str, ...]
    time_horizon: Tuple[str, ...]
    calculation_notes: Tuple[str, ...]


@dataclass(frozen=True)
class CompanyCharacter:
    symbol: str
    company_name: str
    primary_identity: str
    business_segments: Tuple[str, ...]
    product_categories: Tuple[str, ...]
    geographies: Tuple[str, ...]
    value_chain: Tuple[str, ...]
    demand_drivers: Tuple[str, ...]
    revenue_drivers: Tuple[str, ...]
    commodity_dependencies: Tuple[str, ...]
    cost_drivers: Tuple[str, ...]
    supply_chain_dependencies: Tuple[str, ...]
    strategic_drivers: Tuple[str, ...]
    operational_risks: Tuple[str, ...]
    regulatory_risks: Tuple[str, ...]
    key_indicators: Tuple[str, ...]
    event_types: Tuple[str, ...]
    market_characters: Dict[str, MarketCharacter]


def _mc(
    market: str,
    exposure_type: str,
    impact_channels: Tuple[str, ...],
    supply_chain_links: Tuple[str, ...],
    demand_links: Tuple[str, ...],
    cost_links: Tuple[str, ...],
    macro_links: Tuple[str, ...],
    indicators_to_measure: Tuple[str, ...],
    event_signals: Tuple[str, ...],
    time_horizon: Tuple[str, ...],
    calculation_notes: Tuple[str, ...],
) -> MarketCharacter:
    return MarketCharacter(
        market=market,
        exposure_type=exposure_type,
        impact_channels=impact_channels,
        supply_chain_links=supply_chain_links,
        demand_links=demand_links,
        cost_links=cost_links,
        macro_links=macro_links,
        indicators_to_measure=indicators_to_measure,
        event_signals=event_signals,
        time_horizon=time_horizon,
        calculation_notes=calculation_notes,
    )


COMPANY_CHARACTER = CompanyCharacter(
    symbol="TATACONSUM",
    company_name="Tata Consumer Products Limited",
    primary_identity=(
        "Integrated food and beverage consumer-products company with a "
        "diversified portfolio across tea, coffee, salt, packaged foods, "
        "staples, ready-to-drink beverages, water, wellness and out-of-home "
        "consumption, supported by strong brands, broad distribution and "
        "India and international operations."
    ),
    business_segments=(
        "India Beverages",
        "India Foods",
        "International Business",
        "Out-of-Home / Starbucks joint venture",
        "Solubles / B2B ingredients",
        "Growth businesses",
        "Ready-to-Drink beverages",
        "Packaged foods and pantry",
        "Wellness and better-for-you products",
    ),
    product_categories=(
        "Tea",
        "Coffee",
        "Salt",
        "Pulses",
        "Spices",
        "Ready-to-cook mixes",
        "Cereals",
        "Snacks",
        "Mini-meals",
        "Ready-to-Drink beverages",
        "Packaged water",
        "Enhanced / flavoured water",
        "Breakfast products",
        "Millet products",
        "Dry fruits and nuts",
        "Cooking oils",
        "Wellness products",
        "Instant tea and coffee extracts",
        "Out-of-home beverages and food",
    ),
    geographies=(
        "India",
        "United States",
        "United Kingdom",
        "Canada",
        "South Africa",
        "Other international markets",
    ),
    value_chain=(
        "Agricultural commodity sourcing",
        "Supplier development",
        "Blending and processing",
        "Manufacturing",
        "Packaging",
        "Quality control",
        "Warehousing",
        "Distribution",
        "Modern trade",
        "General trade",
        "E-commerce",
        "Quick commerce",
        "Out-of-home consumption",
        "International distribution",
        "Brand building",
        "Pricing and revenue management",
    ),
    demand_drivers=(
        "Household consumption",
        "Tea consumption",
        "Coffee consumption",
        "Staples demand",
        "Packaged-food adoption",
        "Convenience-led consumption",
        "Health and wellness demand",
        "Premiumisation",
        "Urban consumption",
        "Rural consumption",
        "E-commerce adoption",
        "Quick-commerce growth",
        "On-the-go consumption",
        "International consumer demand",
        "Out-of-home consumption",
    ),
    revenue_drivers=(
        "Volume growth",
        "Realisation growth",
        "Price-mix",
        "Market share",
        "Tea sales",
        "Coffee sales",
        "Salt sales",
        "Foods growth",
        "RTD growth",
        "International growth",
        "Innovation-led growth",
        "Premium portfolio mix",
        "Distribution expansion",
        "Modern trade",
        "E-commerce",
        "Quick commerce",
        "Out-of-home business",
        "Acquired-brand integration",
    ),
    commodity_dependencies=(
        "Tea",
        "Coffee",
        "Milk and dairy-related inputs where applicable",
        "Agricultural staples",
        "Spices",
        "Pulses",
        "Edible oils",
        "Sugar and sweeteners where applicable",
        "Packaging materials",
        "Fuel and freight",
        "Water and utilities",
    ),
    cost_drivers=(
        "Tea prices",
        "Coffee prices",
        "Agricultural commodity prices",
        "Packaging",
        "Fuel",
        "Freight",
        "Electricity",
        "Water",
        "Employee costs",
        "Advertising and promotion",
        "Distribution",
        "Warehousing",
        "International logistics",
        "Foreign exchange",
    ),
    supply_chain_dependencies=(
        "Tea-growing regions",
        "Coffee-growing and coffee-sourcing regions",
        "Agricultural suppliers",
        "Packaging suppliers",
        "Contract manufacturers where applicable",
        "Owned manufacturing facilities",
        "Warehouses",
        "Ports and freight",
        "Retail distributors",
        "Modern-trade partners",
        "E-commerce platforms",
        "Quick-commerce platforms",
    ),
    strategic_drivers=(
        "Strengthen core tea and salt franchises",
        "Accelerate growth businesses",
        "Expand packaged foods",
        "Build ready-to-drink beverages",
        "Grow international business",
        "Increase premiumisation",
        "Expand distribution",
        "Build omni-channel capabilities",
        "Increase innovation",
        "Improve supply-chain resilience",
        "Improve productivity",
        "Scale acquisitions and new brands",
        "Develop wellness and better-for-you portfolio",
    ),
    operational_risks=(
        "Commodity-price volatility",
        "Agricultural supply disruption",
        "Climate-related crop risk",
        "Freight disruption",
        "Packaging-cost inflation",
        "Foreign-exchange volatility",
        "Manufacturing disruption",
        "Quality issues",
        "Brand/reputation risk",
        "Channel disruption",
        "Inventory imbalance",
        "Acquisition integration risk",
    ),
    regulatory_risks=(
        "Food-safety regulation",
        "Food labelling requirements",
        "Quality standards",
        "Import/export rules",
        "Agricultural commodity regulation",
        "Packaging requirements",
        "Advertising standards",
        "Environmental requirements",
        "International food regulations",
    ),
    key_indicators=(
        "Revenue growth",
        "Volume growth",
        "Price-mix",
        "India beverages growth",
        "India foods growth",
        "International growth",
        "Tea market share",
        "Salt market share",
        "Coffee volumes",
        "RTD volumes",
        "Foods distribution",
        "Numeric distribution",
        "Weighted distribution",
        "Modern-trade growth",
        "E-commerce growth",
        "Quick-commerce growth",
        "Innovation-to-sales ratio",
        "Gross margin",
        "EBITDA margin",
        "Commodity inflation",
        "Tea input cost",
        "Coffee input cost",
        "Working capital",
        "Inventory days",
        "Receivable days",
        "Free cash flow",
        "Foreign-exchange exposure",
        "Capacity utilisation",
        "Advertising and promotion",
    ),
    event_types=(
        "Quarterly results",
        "Annual results",
        "Commodity-price shock",
        "Tea-price movement",
        "Coffee-price movement",
        "New product launch",
        "Major pricing action",
        "Market-share change",
        "Distribution expansion",
        "Quick-commerce expansion",
        "International expansion",
        "Acquisition",
        "Brand integration",
        "Manufacturing expansion",
        "Plant disruption",
        "Supply disruption",
        "Food-safety event",
        "Regulatory change",
        "Freight disruption",
        "Currency shock",
        "Management guidance",
        "Capital-allocation update",
    ),
    market_characters={},
)


MARKET_CHARACTERS: Dict[str, MarketCharacter] = {
    "NIFTY 50": _mc(
        "NIFTY 50",
        "Direct equity-market beta plus Indian consumer-cycle exposure",
        (
            "Market beta",
            "Consumer-sector valuation",
            "Risk appetite",
            "Indian consumption expectations",
            "Institutional flows",
        ),
        (
            "Equity-market liquidity",
            "Consumer-sector capital flows",
        ),
        (
            "Household consumption",
            "Income growth",
            "Rural demand",
            "Urban demand",
            "Premiumisation",
        ),
        (
            "Valuation multiple sensitivity",
            "Advertising and distribution investment",
        ),
        (
            "GDP growth",
            "Inflation",
            "Interest rates",
            "Consumer confidence",
            "Market liquidity",
        ),
        (
            "Rolling beta",
            "Rolling correlation",
            "FMCG relative strength",
            "Consumer-sector breadth",
            "Volatility",
        ),
        (
            "Quarterly results",
            "Commodity-cost commentary",
            "Consumer-demand commentary",
            "Guidance",
            "M&A",
        ),
        ("Intraday", "1D", "1W", "1M", "3M", "6M", "1Y"),
        (
            "Control for broad market and FMCG-sector effects before measuring commodity-specific impact.",
            "Use residual returns for later cross-market attribution.",
        ),
    ),
    "Crude Oil": _mc(
        "Crude Oil",
        "Indirect but meaningful packaging, freight, fuel and inflation exposure",
        (
            "Freight cost",
            "Fuel cost",
            "Petrochemical packaging inputs",
            "Consumer inflation",
            "Household purchasing power",
        ),
        (
            "Packaging materials",
            "Road logistics",
            "International freight",
            "Distribution",
        ),
        (
            "Consumer affordability",
            "Household consumption",
            "Rural purchasing power",
        ),
        (
            "Packaging",
            "Fuel",
            "Freight",
            "Distribution",
        ),
        (
            "Inflation",
            "Interest rates",
            "Disposable income",
            "Currency",
        ),
        (
            "Crude return",
            "Freight proxy",
            "Packaging cost",
            "Gross margin",
            "EBITDA margin",
            "Volume growth",
        ),
        (
            "Oil-price spike",
            "Fuel shock",
            "Freight shock",
            "Inflation surprise",
        ),
        ("1D", "1W", "1M", "3M", "6M"),
        (
            "Separate direct cost channels from consumer-demand channels.",
            "Use lagged commodity moves against margins and residual stock returns.",
        ),
    ),
    "Gold": _mc(
        "Gold",
        "Primarily macro, wealth and consumer-confidence exposure",
        (
            "Household wealth effect",
            "Risk sentiment",
            "Inflation expectations",
            "Savings allocation",
        ),
        (
            "No major direct gold input",
            "Indirect consumer and macro channel",
        ),
        (
            "Household confidence",
            "Premium consumption",
            "Discretionary food and beverage demand",
        ),
        (
            "Limited direct production-cost linkage",
        ),
        (
            "Real rates",
            "Inflation",
            "Currency",
            "Risk aversion",
            "Household wealth",
        ),
        (
            "Gold return",
            "Real yields",
            "USD",
            "Consumer confidence",
            "Premiumisation",
        ),
        (
            "Gold breakout",
            "Real-rate shock",
            "Risk-off event",
            "Household savings shift",
        ),
        ("1D", "1W", "1M", "3M", "6M"),
        (
            "Treat gold primarily as a macro-state variable.",
            "Do not infer direct FMCG input-cost exposure from gold.",
        ),
    ),
    "Silver": _mc(
        "Silver",
        "Indirect industrial and macro-cycle exposure",
        (
            "Industrial-cycle signal",
            "Commodity sentiment",
            "Risk appetite",
        ),
        (
            "No major direct silver input",
            "Indirect industrial supply-chain signal",
        ),
        (
            "Economic activity",
            "Consumer confidence",
            "Industrial employment and income",
        ),
        (
            "Limited direct cost exposure",
        ),
        (
            "Global growth",
            "Industrial cycle",
            "Inflation",
            "Risk appetite",
        ),
        (
            "Silver return",
            "Global PMI",
            "Consumer indicators",
            "Residual stock return",
        ),
        (
            "Industrial slowdown",
            "Commodity-cycle reversal",
            "Global growth shock",
        ),
        ("1W", "1M", "3M", "6M"),
        (
            "Use silver mainly as an industrial/macro regime variable.",
            "Control for NIFTY and crude before assigning explanatory power.",
        ),
    ),
    "Natural Gas": _mc(
        "Natural Gas",
        "Indirect manufacturing-energy, packaging and industrial-cost exposure",
        (
            "Factory energy cost",
            "Process heat",
            "Packaging/chemical input costs",
            "Industrial inflation",
        ),
        (
            "Food-processing facilities",
            "Beverage plants",
            "Packaging suppliers",
            "Industrial suppliers",
        ),
        (
            "Industrial activity",
            "Consumer affordability",
        ),
        (
            "Manufacturing energy",
            "Supplier input costs",
            "Packaging",
        ),
        (
            "Energy inflation",
            "Industrial production",
            "Interest rates",
            "Currency",
        ),
        (
            "Natural-gas return",
            "Utility expense",
            "Gross margin",
            "Factory utilisation",
            "Supplier-cost inflation",
        ),
        (
            "Gas-price spike",
            "Industrial energy shock",
            "Supplier-cost shock",
        ),
        ("1W", "1M", "3M", "6M"),
        (
            "Measure plant-level gas consumption where available.",
            "Do not treat natural gas as a uniform direct input across every Tata Consumer category.",
        ),
    ),
    "Copper": _mc(
        "Copper",
        "Indirect packaging, equipment, capex and industrial-cycle exposure",
        (
            "Electrical equipment cost",
            "Plant capex",
            "Industrial-cycle signal",
            "Infrastructure cost",
        ),
        (
            "Factory electrical systems",
            "Manufacturing equipment",
            "Warehouses",
            "Distribution infrastructure",
        ),
        (
            "Industrial investment",
            "Retail infrastructure",
            "Consumer-sector expansion",
        ),
        (
            "Equipment",
            "Electrical systems",
            "Capex",
        ),
        (
            "Industrial growth",
            "Infrastructure spending",
            "Commodity inflation",
        ),
        (
            "Copper return",
            "Capex",
            "PP&E additions",
            "Plant cost",
            "Margin",
        ),
        (
            "Copper shock",
            "Capex-cycle change",
            "Industrial slowdown",
        ),
        ("1W", "1M", "3M", "6M", "1Y"),
        (
            "Copper is a secondary capex/industrial variable, not a core food raw material.",
            "Use company capex and equipment disclosures to validate materiality.",
        ),
    ),
    "Aluminium": _mc(
        "Aluminium",
        "Meaningful indirect packaging, equipment, logistics and capex exposure",
        (
            "Packaging-material cost",
            "Equipment cost",
            "Warehouse and logistics infrastructure",
            "Industrial-cycle signal",
        ),
        (
            "Packaging",
            "Containers and packaging components",
            "Plant equipment",
            "Distribution infrastructure",
        ),
        (
            "Consumer demand",
            "Industrial activity",
            "Retail-channel expansion",
        ),
        (
            "Packaging",
            "Equipment",
            "Capex",
        ),
        (
            "Commodity inflation",
            "Industrial growth",
            "Consumer demand",
        ),
        (
            "Aluminium return",
            "Packaging cost",
            "Capex",
            "Gross margin",
            "Inventory value",
        ),
        (
            "Aluminium shock",
            "Packaging-cost event",
            "Industrial-cycle reversal",
        ),
        ("1W", "1M", "3M", "6M", "1Y"),
        (
            "Separate packaging exposure from broad commodity effects.",
            "Measure actual packaging intensity before assigning a coefficient.",
        ),
    ),
    "Zinc": _mc(
        "Zinc",
        "Indirect construction, infrastructure and equipment-cost exposure",
        (
            "Galvanised-steel cost",
            "Plant and warehouse capex",
            "Infrastructure cost",
            "Industrial-cycle signal",
        ),
        (
            "Plant structures",
            "Warehouses",
            "Distribution infrastructure",
            "Equipment",
        ),
        (
            "Consumer distribution expansion",
            "Industrial activity",
            "Construction activity",
        ),
        (
            "Plant construction",
            "Equipment",
            "Infrastructure",
        ),
        (
            "Construction cycle",
            "Industrial growth",
            "Commodity inflation",
        ),
        (
            "Zinc return",
            "Capex",
            "PP&E additions",
            "Construction indicators",
            "Margin",
        ),
        (
            "Zinc shock",
            "Construction slowdown",
            "Industrial supply shock",
        ),
        ("1W", "1M", "3M", "6M", "1Y"),
        (
            "Zinc is not treated as a core food/beverage input.",
            "Test its relationship mainly through infrastructure, capex and industrial-cycle channels.",
        ),
    ),
    "Electricity": _mc(
        "Electricity",
        "Meaningful manufacturing, refrigeration, processing and distribution operating-cost exposure",
        (
            "Factory operating cost",
            "Food and beverage processing",
            "Refrigeration",
            "Warehousing",
            "Water processing",
            "Digital/office infrastructure",
        ),
        (
            "Manufacturing plants",
            "Beverage plants",
            "Food-processing facilities",
            "Water plants",
            "Cold storage",
            "Warehouses",
        ),
        (
            "Production capacity",
            "Product availability",
            "Supply reliability",
        ),
        (
            "Electricity consumption",
            "HVAC",
            "Refrigeration",
            "Processing equipment",
            "Water treatment",
            "Warehousing",
        ),
        (
            "Industrial power prices",
            "Grid reliability",
            "Renewable sourcing",
            "Regional electricity conditions",
        ),
        (
            "Power price",
            "Power consumption",
            "Utility expense",
            "Plant utilisation",
            "Gross margin",
            "EBITDA margin",
        ),
        (
            "Power-price spike",
            "Grid disruption",
            "Plant outage",
            "Utility contract change",
        ),
        ("1D", "1W", "1M", "3M", "6M"),
        (
            "Where plant-level electricity data exists, calculate actual energy intensity.",
            "Separate electricity-price impact from production-volume and commodity-cost effects.",
        ),
    ),
}


COMPANY_CHARACTER = CompanyCharacter(
    **{
        **COMPANY_CHARACTER.__dict__,
        "market_characters": MARKET_CHARACTERS,
    }
)


def get_company_character() -> CompanyCharacter:
    """Return the complete Tata Consumer Products company character."""
    return COMPANY_CHARACTER


def get_market_character(market: str) -> MarketCharacter:
    """Return one market character from the fixed nine-market universe."""
    normalized = market.strip()
    if normalized not in MARKET_CHARACTERS:
        raise KeyError(
            f"Unsupported market: {market!r}. "
            f"Supported markets: {', '.join(TRACKED_MARKETS)}"
        )
    return MARKET_CHARACTERS[normalized]


def get_all_market_characters() -> Dict[str, MarketCharacter]:
    """Return all nine market characters."""
    return dict(MARKET_CHARACTERS)


def validate_character() -> dict:
    """Structural validation only; actual impact must be calculated later."""
    markets = tuple(MARKET_CHARACTERS.keys())
    missing = tuple(m for m in TRACKED_MARKETS if m not in MARKET_CHARACTERS)
    extra = tuple(m for m in markets if m not in TRACKED_MARKETS)

    return {
        "symbol": COMPANY_CHARACTER.symbol,
        "valid": not missing and not extra and len(markets) == 9,
        "market_count": len(markets),
        "expected_market_count": 9,
        "missing_markets": missing,
        "extra_markets": extra,
        "hard_coded_result_fields_present": False,
        "historical_calculation_required": True,
    }


if __name__ == "__main__":
    result = validate_character()
    print("TATACONSUM character validation:", result)

    for market in TRACKED_MARKETS:
        character = get_market_character(market)
        print(
            f"{market}: {character.exposure_type} | "
            f"{len(character.indicators_to_measure)} indicators | "
            f"{len(character.event_signals)} event groups"
        )
