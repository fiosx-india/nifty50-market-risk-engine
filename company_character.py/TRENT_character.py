"""
TRENT Character Model
=====================
Trent Limited.

Business character + nine tracked market characters.

The supplied CSV is treated as input metadata only. RANK, PCT_CHANGE,
LINKAGE_SCORE and RELATION are intentionally NOT embedded as permanent
business facts. Actual market impact must later be estimated from historical
data, operating metrics, news/events and lag-aware statistical analysis.
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
    fashion_lifestyle_character: Tuple[str, ...]
    grocery_food_character: Tuple[str, ...]
    value_fashion_character: Tuple[str, ...]
    premium_fashion_character: Tuple[str, ...]
    international_and_associate_businesses: Tuple[str, ...]
    sourcing_and_supply_chain: Tuple[str, ...]
    retail_and_digital_model: Tuple[str, ...]
    demand_drivers: Tuple[str, ...]
    revenue_drivers: Tuple[str, ...]
    commodity_dependencies: Tuple[str, ...]
    cost_drivers: Tuple[str, ...]
    strategic_drivers: Tuple[str, ...]
    operational_risks: Tuple[str, ...]
    regulatory_and_market_risks: Tuple[str, ...]
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
    symbol="TRENT",
    company_name="Trent Limited",
    primary_identity=(
        "Tata Group consumer-retail company operating fashion and lifestyle, "
        "value fashion, food and grocery, wholesale and associated branded "
        "retail businesses. The model is strongly retail-led, with significant "
        "in-house brand design, sourcing, merchandising, supply-chain control "
        "and physical-plus-digital customer access."
    ),
    business_segments=(
        "Fashion and Lifestyle",
        "Westside",
        "Zudio",
        "Utsa",
        "Samoh",
        "Burnt Toast",
        "Food and Grocery",
        "Star",
        "StarQuik",
        "Booker Wholesale",
        "International/associate fashion businesses",
        "Zara association",
        "Massimo Dutti association",
        "Trent MAS Fashion",
        "Other emerging lifestyle concepts",
    ),
    fashion_lifestyle_character=(
        "Westside",
        "Utsa",
        "Samoh",
        "Burnt Toast",
        "Apparel",
        "Footwear",
        "Lingerie",
        "Beauty",
        "Cosmetics",
        "Perfumes",
        "Accessories",
        "Home furnishings",
        "Home décor",
        "In-house brands",
        "Private-label merchandise",
    ),
    grocery_food_character=(
        "Star Market",
        "Star Bazaar",
        "Fresh produce",
        "Staples",
        "Beverages",
        "Dairy",
        "Processed foods",
        "Health and beauty",
        "Home needs",
        "Exclusive food brands",
        "StarQuik",
        "Online grocery",
        "Omnichannel grocery",
    ),
    value_fashion_character=(
        "Zudio",
        "Value fashion",
        "Affordable price points",
        "High-frequency merchandise refresh",
        "In-house exclusive brands",
        "Young consumers",
        "Fashion-led value retail",
        "High store-productivity focus",
        "Rapid store expansion",
        "Small-format/accessible retail locations",
    ),
    premium_fashion_character=(
        "Westside",
        "Premium and aspirational fashion",
        "In-house design",
        "Trend-led merchandise",
        "Brand experience",
        "Store ambience",
        "Home décor",
        "Premium customer segments",
        "Digital fashion access",
    ),
    international_and_associate_businesses=(
        "Zara association",
        "Massimo Dutti association",
        "International brand relationships",
        "GCC/Zudio expansion",
        "International sourcing",
        "Cross-border supply chain",
        "Foreign-currency exposure",
        "International retail operations",
    ),
    sourcing_and_supply_chain=(
        "In-house design",
        "Vendor sourcing",
        "Domestic suppliers",
        "International suppliers",
        "Apparel manufacturing",
        "Textile suppliers",
        "Footwear suppliers",
        "Packaging",
        "Warehousing",
        "Distribution centres",
        "Road logistics",
        "Port logistics",
        "Merchandising",
        "Inventory allocation",
        "Store replenishment",
        "Fresh-food supply chain",
        "Cold-chain/logistics where required",
    ),
    retail_and_digital_model=(
        "Company-operated stores",
        "Franchise arrangements",
        "Westside.com",
        "Tata Cliq",
        "Tata Neu",
        "StarQuik",
        "Digital discovery",
        "Omnichannel fulfilment",
        "Store-led fulfilment",
        "Customer loyalty",
        "Store productivity",
        "Location economics",
        "High inventory turns",
    ),
    demand_drivers=(
        "Household income",
        "Consumer confidence",
        "Urban consumption",
        "Rural consumption",
        "Youth consumption",
        "Fashion trends",
        "Premiumisation",
        "Value-conscious consumption",
        "Footfall",
        "Same-store growth",
        "New store additions",
        "Festivals",
        "Wedding season",
        "Back-to-school demand",
        "Holiday shopping",
        "Digital commerce",
        "Food and grocery frequency",
    ),
    revenue_drivers=(
        "Store sales",
        "Same-store sales growth",
        "Like-for-like growth",
        "Footfall",
        "Conversion rate",
        "Average transaction value",
        "Units per transaction",
        "Fashion mix",
        "Value-fashion volume",
        "Premium mix",
        "Store additions",
        "Store productivity",
        "Grocery volumes",
        "Fresh-food sales",
        "Private-label mix",
        "Online sales",
        "International/associate contribution",
    ),
    commodity_dependencies=(
        "Crude oil",
        "Aluminium",
        "Copper",
        "Zinc",
        "Natural gas",
        "Electricity",
        "Cotton and textiles",
        "Synthetic fibres",
        "Leather",
        "Plastics",
        "Packaging materials",
        "Food commodities",
        "Fuels and freight",
    ),
    cost_drivers=(
        "Merchandise sourcing",
        "Textiles",
        "Cotton",
        "Synthetic fibres",
        "Footwear inputs",
        "Packaging",
        "Freight",
        "Fuel",
        "Store rent",
        "Electricity",
        "Employee costs",
        "Advertising",
        "Digital infrastructure",
        "Warehousing",
        "Distribution",
        "Food procurement",
        "Fresh-food wastage",
        "Foreign exchange",
    ),
    strategic_drivers=(
        "Scale Zudio",
        "Scale Westside",
        "Increase store productivity",
        "Expand fashion and lifestyle formats",
        "Strengthen private labels",
        "Increase sourcing control",
        "Improve merchandise freshness",
        "Expand digital retail",
        "Grow Star",
        "Grow StarQuik",
        "Improve food/grocery economics",
        "Expand international concepts",
        "Develop new lifestyle concepts",
        "Optimise store locations",
        "Improve inventory turns",
        "Improve supply-chain efficiency",
    ),
    operational_risks=(
        "Consumer-demand slowdown",
        "Fashion inventory risk",
        "Wrong merchandise mix",
        "Markdown risk",
        "Supply-chain disruption",
        "Freight-cost volatility",
        "Store-rent inflation",
        "Electricity-cost inflation",
        "Food wastage",
        "Fresh-produce supply disruption",
        "Vendor concentration",
        "Foreign-exchange risk",
        "International sourcing risk",
        "Digital disruption",
        "Cybersecurity risk",
        "Store execution risk",
    ),
    regulatory_and_market_risks=(
        "GST changes",
        "Import duties",
        "Customs policy",
        "Consumer-protection rules",
        "Labour regulations",
        "Food-safety regulation",
        "Weights and measures",
        "E-commerce regulation",
        "Data/privacy regulation",
        "Foreign-exchange rules",
        "Retail-sector regulation",
        "Environmental requirements",
        "Packaging/waste rules",
    ),
    key_indicators=(
        "Revenue",
        "Fashion revenue",
        "Westside growth",
        "Zudio growth",
        "Star growth",
        "Store count",
        "New stores",
        "Same-store sales growth",
        "Footfall",
        "Conversion",
        "Average transaction value",
        "Gross margin",
        "EBITDA margin",
        "Inventory days",
        "Inventory turns",
        "Markdown rate",
        "Working capital",
        "Rent cost",
        "Employee cost",
        "Freight cost",
        "Private-label mix",
        "Digital sales",
        "StarQuik sales",
        "Fresh-food sales",
        "Store productivity",
        "Capex",
        "Free cash flow",
        "Net debt",
        "International/associate contribution",
    ),
    event_types=(
        "Quarterly results",
        "Annual results",
        "Monthly business updates",
        "Zudio store launches",
        "Westside store launches",
        "Star store launches",
        "International expansion",
        "New brand launch",
        "Major fashion collection",
        "Large promotional event",
        "GST change",
        "Import-duty change",
        "Food regulation change",
        "Consumer-demand shock",
        "Freight-cost shock",
        "Commodity-cost shock",
        "Supply-chain disruption",
        "Store closure/opening",
        "Management guidance",
        "Capital-allocation update",
    ),
    market_characters={},
)


MARKET_CHARACTERS: Dict[str, MarketCharacter] = {
    "NIFTY 50": _mc(
        "NIFTY 50",
        "Direct equity-market beta plus Indian consumption, discretionary-retail and growth-cycle exposure",
        (
            "Equity beta",
            "Consumer confidence",
            "Risk appetite",
            "Retail-sector valuation",
            "Household wealth",
        ),
        (
            "Retail-sector liquidity",
            "Supplier financing",
            "Commercial-property conditions",
        ),
        (
            "Household consumption",
            "Urban demand",
            "Rural demand",
            "Discretionary spending",
            "Food/grocery frequency",
        ),
        (
            "Funding conditions",
            "Store expansion economics",
            "Retail valuation",
        ),
        (
            "GDP growth",
            "Interest rates",
            "Inflation",
            "Consumer confidence",
            "Liquidity",
        ),
        (
            "Rolling beta",
            "Rolling correlation",
            "Retail-sector relative strength",
            "Same-store sales",
            "Footfall",
            "Volatility",
        ),
        (
            "Quarterly results",
            "Store expansion",
            "Consumer-demand commentary",
            "Management guidance",
        ),
        ("Intraday", "1D", "1W", "1M", "3M", "6M", "1Y"),
        (
            "Control for NIFTY and consumption variables before attributing effects to commodities.",
            "Use residual returns for commodity-specific testing.",
        ),
    ),
    "Crude Oil": _mc(
        "Crude Oil",
        "Indirect retail exposure through freight, fuel, plastics, synthetic fibres, packaging and inflation",
        (
            "Freight cost",
            "Fuel cost",
            "Petrochemical input cost",
            "Packaging cost",
            "Synthetic-fibre cost",
            "Consumer inflation",
        ),
        (
            "Road logistics",
            "International freight",
            "Packaging",
            "Synthetic fibres",
            "Plastics",
            "Warehousing",
        ),
        (
            "Disposable income",
            "Consumer confidence",
            "Discretionary spending",
            "Value-fashion demand",
            "Grocery demand",
        ),
        (
            "Freight",
            "Packaging",
            "Polyester/synthetic fibres",
            "Store logistics",
        ),
        (
            "Inflation",
            "Interest rates",
            "Disposable income",
            "Currency",
        ),
        (
            "Crude return",
            "Freight index",
            "CPI",
            "Synthetic-fibre cost",
            "Packaging cost",
            "Same-store growth",
            "Gross margin",
        ),
        (
            "Oil-price spike",
            "Freight shock",
            "Inflation surprise",
            "Consumer-demand slowdown",
        ),
        ("1D", "1W", "1M", "3M", "6M"),
        (
            "Crude should be tested through logistics/input costs and consumer inflation, not as a direct retail-demand coefficient.",
        ),
    ),
    "Gold": _mc(
        "Gold",
        "Indirect household-wealth, savings-allocation and risk-sentiment exposure",
        (
            "Household wealth",
            "Savings allocation",
            "Risk appetite",
            "Consumer confidence",
        ),
        (
            "Household balance sheets",
            "Consumer liquidity",
            "Retail financing conditions",
        ),
        (
            "Discretionary fashion demand",
            "Premium consumption",
            "Festival/wedding spending",
            "Consumer confidence",
        ),
        (
            "No major direct merchandise-cost channel",
            "Potential indirect macro/wealth channel",
        ),
        (
            "Real rates",
            "Inflation",
            "Risk aversion",
            "Household wealth",
            "Currency",
        ),
        (
            "Gold return",
            "Gold volatility",
            "Consumer confidence",
            "Retail sales",
            "Same-store growth",
            "Premium mix",
        ),
        (
            "Gold-price shock",
            "Risk-off event",
            "Household wealth shift",
        ),
        ("1W", "1M", "3M", "6M"),
        (
            "Do not treat gold as a core Trent merchandise input.",
            "Test the relationship through household wealth, risk and consumption variables.",
        ),
    ),
    "Silver": _mc(
        "Silver",
        "Indirect industrial, electronics and commodity-sentiment exposure",
        (
            "Industrial cycle",
            "Electronics/material sentiment",
            "Risk appetite",
        ),
        (
            "Retail electronics",
            "Store equipment",
            "Industrial suppliers",
            "Packaging/equipment",
        ),
        (
            "Consumer confidence",
            "Technology consumption",
            "Industrial activity",
        ),
        (
            "Minor component exposure",
            "Equipment/input costs",
        ),
        (
            "Industrial growth",
            "Commodity cycle",
            "Risk sentiment",
        ),
        (
            "Silver return",
            "Industrial production",
            "Retail sales",
            "Footfall",
            "Margin",
        ),
        (
            "Silver-price shock",
            "Industrial slowdown",
            "Commodity shock",
        ),
        ("1W", "1M", "3M", "6M"),
        (
            "Silver remains secondary for Trent unless specific product or equipment sourcing data establishes a stronger channel.",
        ),
    ),
    "Natural Gas": _mc(
        "Natural Gas",
        "Indirect textile/manufacturing, food-processing, supplier-energy and industrial-cost exposure",
        (
            "Supplier energy",
            "Textile processing",
            "Food processing",
            "Industrial inflation",
        ),
        (
            "Textile suppliers",
            "Apparel manufacturing",
            "Food processing",
            "Packaging",
            "Warehouse operations",
        ),
        (
            "Industrial activity",
            "Merchandise availability",
            "Consumer demand through inflation",
        ),
        (
            "Supplier energy",
            "Processing cost",
            "Food manufacturing cost",
        ),
        (
            "Energy inflation",
            "Industrial growth",
            "Power conditions",
        ),
        (
            "Natural-gas return",
            "Textile input cost",
            "Food input cost",
            "Supplier inflation",
            "Gross margin",
        ),
        (
            "Gas-price spike",
            "Industrial energy shock",
            "Supplier disruption",
        ),
        ("1W", "1M", "3M", "6M"),
        (
            "Use supplier/manufacturing exposure as the mediator.",
            "Avoid assigning direct gas sensitivity to retail sales without operating evidence.",
        ),
    ),
    "Copper": _mc(
        "Copper",
        "Indirect store infrastructure, electrical equipment, refrigeration and digital-retail exposure",
        (
            "Electrical equipment",
            "Store fit-out",
            "Refrigeration",
            "IT infrastructure",
            "Warehouse equipment",
        ),
        (
            "Store construction",
            "Electrical systems",
            "Cold-chain equipment",
            "Warehouses",
            "Digital infrastructure",
        ),
        (
            "Store expansion",
            "Digital retail",
            "Grocery infrastructure",
        ),
        (
            "Electrical equipment",
            "Store capex",
            "Warehouse capex",
            "IT equipment",
        ),
        (
            "Industrial capex",
            "Retail expansion",
            "Electrification",
        ),
        (
            "Copper return",
            "Store capex",
            "Fit-out cost",
            "Store additions",
            "Warehouse capex",
            "Margin",
        ),
        (
            "Copper-price shock",
            "Electrical-equipment shock",
            "Capex-cost event",
        ),
        ("1W", "1M", "3M", "6M", "1Y"),
        (
            "Copper should be evaluated through store/warehouse/equipment capex.",
            "Separate capex effects from retail-demand effects.",
        ),
    ),
    "Aluminium": _mc(
        "Aluminium",
        "Indirect packaging, store fit-out, fixtures, equipment and consumer-goods supply-chain exposure",
        (
            "Packaging",
            "Store fixtures",
            "Equipment",
            "Retail fit-out",
            "Consumer-goods inputs",
        ),
        (
            "Packaging suppliers",
            "Store construction",
            "Fixtures",
            "Warehouses",
            "Food/grocery suppliers",
        ),
        (
            "Retail expansion",
            "Consumer goods demand",
            "Store productivity",
        ),
        (
            "Packaging",
            "Fixtures",
            "Equipment",
            "Fit-out",
        ),
        (
            "Industrial cycle",
            "Construction",
            "Consumer inflation",
        ),
        (
            "Aluminium return",
            "Packaging cost",
            "Store capex",
            "Fit-out cost",
            "Store additions",
            "Gross margin",
        ),
        (
            "Aluminium-price shock",
            "Packaging-cost shock",
            "Construction-cost event",
        ),
        ("1W", "1M", "3M", "6M", "1Y"),
        (
            "Aluminium is not a primary Trent revenue driver.",
            "Measure the relationship through packaging and retail-capex channels.",
        ),
    ),
    "Zinc": _mc(
        "Zinc",
        "Indirect store-construction, galvanised-steel, warehouse and retail-infrastructure exposure",
        (
            "Galvanised steel",
            "Store construction",
            "Warehouse infrastructure",
            "Equipment cost",
        ),
        (
            "Retail stores",
            "Warehouses",
            "Distribution centres",
            "Steel fixtures",
            "Store infrastructure",
        ),
        (
            "Store expansion",
            "Retail footprint growth",
            "Infrastructure availability",
        ),
        (
            "Construction",
            "Galvanised steel",
            "Equipment",
            "Fixtures",
        ),
        (
            "Construction cycle",
            "Industrial growth",
            "Commodity inflation",
        ),
        (
            "Zinc return",
            "Store capex",
            "Warehouse capex",
            "Store additions",
            "Fit-out cost",
        ),
        (
            "Zinc-price shock",
            "Construction slowdown",
            "Infrastructure-cost shock",
        ),
        ("1W", "1M", "3M", "6M", "1Y"),
        (
            "The causal chain should be zinc -> galvanising -> steel/infrastructure -> store/warehouse capex.",
            "Use actual capex and store-development data to validate it.",
        ),
    ),
    "Electricity": _mc(
        "Electricity",
        "Meaningful retail-store, warehouse, refrigeration, digital and support-operation cost exposure",
        (
            "Store operating cost",
            "Lighting",
            "HVAC",
            "Refrigeration",
            "Warehouse operations",
            "Digital infrastructure",
        ),
        (
            "Fashion stores",
            "Grocery stores",
            "Warehouses",
            "Distribution centres",
            "IT systems",
            "Cold-chain where applicable",
        ),
        (
            "Store operating hours",
            "Digital commerce",
            "Store expansion",
            "Food/grocery availability",
        ),
        (
            "Store electricity",
            "Warehouse electricity",
            "Refrigeration",
            "IT infrastructure",
        ),
        (
            "Power tariffs",
            "Grid reliability",
            "Renewable sourcing",
            "Regional electricity conditions",
        ),
        (
            "Electricity price",
            "Power consumption",
            "Store energy cost",
            "Energy intensity",
            "Store productivity",
            "EBITDA margin",
        ),
        (
            "Power-price spike",
            "Grid disruption",
            "Store outage",
            "Warehouse outage",
        ),
        ("1D", "1W", "1M", "3M", "6M"),
        (
            "Measure electricity against actual store/warehouse operating cost.",
            "Separate energy-cost effects from footfall and consumer-demand effects.",
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
    """Return the complete Trent business character."""
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
    """Structural validation only; market impact is calculated later."""
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
    print("TRENT character validation:", result)

    for market in TRACKED_MARKETS:
        character = get_market_character(market)
        print(
            f"{market}: {character.exposure_type} | "
            f"{len(character.indicators_to_measure)} indicators | "
            f"{len(character.event_signals)} event groups"
        )
