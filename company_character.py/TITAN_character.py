"""
TITAN Character Model
=====================
Business character + nine tracked market characters for Titan Company Limited.

This file defines the company's actual business character and the causal
channels that should be measured for the nine tracked markets.

It intentionally does NOT hard-code:
RANK, PCT_CHANGE, LINKAGE_SCORE, RELATION, correlation, beta, probability,
or any trading decision.

Historical impact must be calculated later from real commodity prices,
company operating data, consumer indicators, gold volumes/prices, macro data,
news/events and appropriate lagged statistical models.
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
    jewellery_brands_and_channels: Tuple[str, ...]
    watches_and_wearables: Tuple[str, ...]
    eyecare: Tuple[str, ...]
    emerging_businesses: Tuple[str, ...]
    international_business: Tuple[str, ...]
    engineering_and_other_businesses: Tuple[str, ...]
    value_chain: Tuple[str, ...]
    demand_drivers: Tuple[str, ...]
    revenue_drivers: Tuple[str, ...]
    commodity_dependencies: Tuple[str, ...]
    cost_drivers: Tuple[str, ...]
    supply_chain_dependencies: Tuple[str, ...]
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
    symbol="TITAN",
    company_name="Titan Company Limited",
    primary_identity=(
        "Lifestyle and consumer company built around jewellery, watches and "
        "wearables, eyecare and newer lifestyle categories, with a large "
        "omnichannel retail network, strong brands, international expansion "
        "and adjacent engineering/automation capabilities."
    ),
    business_segments=(
        "Jewellery",
        "Watches and Wearables",
        "Eyecare",
        "Indian Dress Wear",
        "Fragrances",
        "Fashion Accessories",
        "International Business",
        "Titan Engineering & Automation",
        "Other emerging businesses",
    ),
    jewellery_brands_and_channels=(
        "Tanishq",
        "Mia",
        "Zoya",
        "CaratLane",
        "Other jewellery brands",
        "Large-format jewellery stores",
        "Exclusive brand outlets",
        "Franchise stores",
        "E-commerce",
        "Omnichannel jewellery retail",
        "Gold exchange",
        "Gold savings / digital-gold related ecosystem",
        "Bullion and jewellery sourcing",
        "Diamond and precious-stone sourcing",
    ),
    watches_and_wearables=(
        "Titan",
        "Fastrack",
        "Sonata",
        "Helios",
        "Titan World",
        "Premium watches",
        "Analog watches",
        "Wearables",
        "Smart products",
        "Watch manufacturing",
        "Assembly",
        "Design and innovation",
        "Retail and e-commerce",
    ),
    eyecare=(
        "Titan EyePlus",
        "Fastrack Eyecare",
        "Prescription eyewear",
        "Frames",
        "Lenses",
        "Contact lenses",
        "International brands",
        "Optical retail",
        "Eye-testing services",
        "Eyewear manufacturing and sourcing",
    ),
    emerging_businesses=(
        "Taneira / Indian Dress Wear",
        "SKINN fragrances",
        "Fastrack fragrances",
        "IRTH women's bags",
        "Fashion accessories",
        "Lifestyle products",
        "Premiumisation",
        "New-category retail",
    ),
    international_business=(
        "International watches",
        "International jewellery",
        "GCC jewellery expansion",
        "International eyewear",
        "International accessories",
        "International fragrances",
        "Global retail distribution",
        "International e-commerce",
        "International brand building",
    ),
    engineering_and_other_businesses=(
        "Titan Engineering & Automation Limited",
        "Automation solutions",
        "Manufacturing services",
        "Engineering solutions",
        "Industrial automation",
        "Precision manufacturing",
        "Corporate/unallocated operations",
    ),
    value_chain=(
        "Design",
        "Product development",
        "Gold and precious-metal sourcing",
        "Diamond and gemstone sourcing",
        "Watch components",
        "Eyewear components",
        "Manufacturing",
        "Assembly",
        "Quality control",
        "Packaging",
        "Warehousing",
        "Retail distribution",
        "Franchise distribution",
        "E-commerce",
        "Omnichannel fulfilment",
        "After-sales service",
        "Brand building",
    ),
    demand_drivers=(
        "Gold jewellery demand",
        "Weddings",
        "Festivals",
        "Household income",
        "Consumer confidence",
        "Urban consumption",
        "Rural consumption",
        "Premiumisation",
        "Gold-price affordability",
        "Jewellery exchange demand",
        "Watch replacement",
        "Premium watch demand",
        "Wearables adoption",
        "Eyewear demand",
        "Fashion and lifestyle spending",
        "International consumer demand",
        "Store expansion",
        "Digital commerce",
    ),
    revenue_drivers=(
        "Jewellery volume",
        "Jewellery value growth",
        "Gold price",
        "Studded jewellery mix",
        "Making-charge realisation",
        "Same-store growth",
        "New-store additions",
        "CaratLane growth",
        "Tanishq growth",
        "Mia growth",
        "Watch volumes",
        "Watch premiumisation",
        "Wearables volumes",
        "Eyecare revenue",
        "Emerging-business growth",
        "International growth",
        "Engineering & Automation orders",
        "Product mix",
        "Gross margin",
    ),
    commodity_dependencies=(
        "Gold",
        "Silver",
        "Diamonds",
        "Precious stones",
        "Watch metals",
        "Aluminium",
        "Copper",
        "Zinc",
        "Packaging materials",
        "Fuel and freight",
        "Electricity",
    ),
    cost_drivers=(
        "Gold procurement cost",
        "Silver procurement cost",
        "Diamond and gemstone cost",
        "Precious-metal inventory",
        "Manufacturing",
        "Store operating cost",
        "Employee cost",
        "Rent",
        "Advertising and promotion",
        "Logistics",
        "Packaging",
        "Electricity",
        "Fuel",
        "Foreign exchange",
        "Interest and funding cost",
        "Engineering input costs",
    ),
    supply_chain_dependencies=(
        "Gold suppliers",
        "Bullion markets",
        "Refiners",
        "Diamond suppliers",
        "Gemstone suppliers",
        "Jewellery manufacturers",
        "Watch-component suppliers",
        "Eyewear suppliers",
        "Logistics",
        "Ports and international freight",
        "Retail locations",
        "Franchise network",
        "E-commerce infrastructure",
    ),
    strategic_drivers=(
        "Strengthen jewellery leadership",
        "Expand Tanishq",
        "Expand Mia",
        "Scale CaratLane",
        "Grow international jewellery",
        "Expand GCC presence",
        "Increase watch premiumisation",
        "Grow wearables",
        "Expand Eyecare",
        "Build emerging lifestyle businesses",
        "Increase store network",
        "Omnichannel integration",
        "Digital customer acquisition",
        "Improve inventory turns",
        "Improve working-capital efficiency",
        "Scale Titan Engineering & Automation",
    ),
    operational_risks=(
        "Gold-price volatility",
        "Consumer-demand slowdown",
        "Inventory risk",
        "Precious-metal price risk",
        "Diamond-price risk",
        "Store execution risk",
        "Brand/reputation risk",
        "Retail disruption",
        "Supply-chain disruption",
        "Currency volatility",
        "International expansion risk",
        "Cyber/digital risk",
        "Acquisition/integration risk",
        "Working-capital risk",
    ),
    regulatory_and_market_risks=(
        "Gold import/customs policy",
        "Jewellery hallmarking",
        "BIS requirements",
        "Consumer-protection regulation",
        "GST and tax changes",
        "Digital-gold regulation",
        "Import/export rules",
        "Diamond/gemstone compliance",
        "Retail regulation",
        "International regulatory requirements",
        "Data/privacy requirements",
    ),
    key_indicators=(
        "Jewellery revenue",
        "Jewellery growth",
        "Jewellery volumes",
        "Gold jewellery volume",
        "Gold price",
        "Gold exchange volume",
        "Studded mix",
        "Average ticket size",
        "Same-store growth",
        "Store additions",
        "Store productivity",
        "Tanishq growth",
        "Mia growth",
        "CaratLane growth",
        "International jewellery growth",
        "Watch revenue",
        "Watch volume",
        "Premium watch mix",
        "Wearables growth",
        "Eyecare revenue",
        "Eyecare store count",
        "Emerging-business revenue",
        "Engineering & Automation revenue",
        "Engineering order book",
        "Gross margin",
        "EBIT margin",
        "Inventory days",
        "Gold inventory",
        "Working capital",
        "Free cash flow",
        "Net debt",
        "ROCE",
    ),
    event_types=(
        "Quarterly results",
        "Annual results",
        "Gold-price shock",
        "Gold import-duty change",
        "Customs-duty change",
        "GST change",
        "Hallmarking regulation",
        "Jewellery demand event",
        "Wedding/festival demand",
        "Major store expansion",
        "New brand launch",
        "CaratLane expansion",
        "International expansion",
        "GCC acquisition",
        "Damas integration",
        "Watch launch",
        "Wearables launch",
        "Eyecare expansion",
        "Engineering order",
        "Supply disruption",
        "Diamond/gemstone price shock",
        "Management guidance",
        "Capital-allocation update",
    ),
    market_characters={},
)


MARKET_CHARACTERS: Dict[str, MarketCharacter] = {
    "NIFTY 50": _mc(
        "NIFTY 50",
        "Direct equity-market beta plus Indian consumption, wealth and retail sentiment",
        (
            "Market beta",
            "Consumer-sector valuation",
            "Risk appetite",
            "Household wealth",
            "Retail-investor flows",
        ),
        (
            "Equity-market liquidity",
            "Consumer-sector capital flows",
            "Retail investment sentiment",
        ),
        (
            "Household consumption",
            "Income growth",
            "Urban demand",
            "Rural demand",
            "Premiumisation",
        ),
        (
            "Valuation multiple",
            "Funding conditions",
            "Retail expansion economics",
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
            "Consumer-sector relative strength",
            "Retail-sector breadth",
            "Volatility",
        ),
        (
            "Quarterly results",
            "Consumer-demand commentary",
            "Gold-price commentary",
            "Store expansion",
            "Capital allocation",
        ),
        ("Intraday", "1D", "1W", "1M", "3M", "6M", "1Y"),
        (
            "Control for NIFTY and consumer-sector effects before testing commodity-specific relationships.",
            "Use residual returns for cross-market attribution.",
        ),
    ),
    "Crude Oil": _mc(
        "Crude Oil",
        "Indirect fuel, logistics, packaging and consumer-inflation exposure",
        (
            "Fuel cost",
            "Freight cost",
            "Packaging cost",
            "Consumer inflation",
            "Household purchasing power",
        ),
        (
            "Road logistics",
            "International freight",
            "Packaging",
            "Retail distribution",
        ),
        (
            "Disposable income",
            "Consumer confidence",
            "Discretionary spending",
            "Urban/rural demand",
        ),
        (
            "Fuel",
            "Freight",
            "Packaging",
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
            "Packaging cost",
            "Consumer inflation",
            "Jewellery volume",
            "Watch volume",
            "EBIT margin",
        ),
        (
            "Oil-price spike",
            "Freight shock",
            "Inflation surprise",
            "Consumer-demand slowdown",
        ),
        ("1D", "1W", "1M", "3M", "6M"),
        (
            "Crude is not a core jewellery input.",
            "Test its effect through logistics, inflation and discretionary consumer demand.",
        ),
    ),
    "Gold": _mc(
        "Gold",
        "Primary direct commodity exposure through jewellery procurement, inventory, consumer affordability and demand",
        (
            "Gold procurement cost",
            "Jewellery selling price",
            "Consumer affordability",
            "Jewellery demand",
            "Inventory valuation",
            "Working capital",
            "Gold exchange economics",
        ),
        (
            "Bullion sourcing",
            "Refiners",
            "Jewellery manufacturing",
            "Gold inventory",
            "Gold exchange",
            "Retail jewellery",
        ),
        (
            "Wedding demand",
            "Festival demand",
            "Investment demand",
            "Jewellery exchange",
            "Consumer affordability",
            "Premium jewellery demand",
        ),
        (
            "Gold procurement",
            "Inventory carrying value",
            "Working capital",
            "Hedging economics",
        ),
        (
            "Real rates",
            "USD",
            "Inflation",
            "Household wealth",
            "Risk appetite",
        ),
        (
            "Gold price",
            "Gold volume",
            "Gold inventory",
            "Gold exchange volume",
            "Jewellery volume",
            "Studded mix",
            "Gross margin",
            "Working capital",
            "Inventory days",
        ),
        (
            "Gold-price spike",
            "Sharp gold correction",
            "Import-duty change",
            "Customs-duty change",
            "Gold-demand shock",
        ),
        ("Intraday", "1D", "1W", "1M", "3M", "6M", "1Y"),
        (
            "Gold is a PRIMARY business variable for Titan and must not be treated like a generic macro commodity.",
            "Measure price and volume separately because higher gold prices can raise reported value while affecting affordability and physical demand.",
            "Test lagged gold-price effects on jewellery volumes, margins and working capital.",
        ),
    ),
    "Silver": _mc(
        "Silver",
        "Direct-to-moderate precious-metal input exposure with smaller importance than gold",
        (
            "Silver procurement",
            "Jewellery cost",
            "Fashion-accessory cost",
            "Precious-metal sentiment",
        ),
        (
            "Silver sourcing",
            "Jewellery manufacturing",
            "Accessory manufacturing",
            "Inventory",
        ),
        (
            "Silver jewellery demand",
            "Fashion demand",
            "Precious-metal affordability",
        ),
        (
            "Silver procurement",
            "Inventory carrying cost",
            "Manufacturing cost",
        ),
        (
            "Precious-metal cycle",
            "Real rates",
            "USD",
            "Risk appetite",
        ),
        (
            "Silver price",
            "Silver volume",
            "Silver inventory",
            "Jewellery mix",
            "Gross margin",
            "Working capital",
        ),
        (
            "Silver-price shock",
            "Precious-metal demand change",
            "Supply disruption",
        ),
        ("1D", "1W", "1M", "3M", "6M"),
        (
            "Silver has a real physical-product pathway but is materially different from gold in Titan's business mix.",
            "Estimate category-specific silver exposure before assigning a company-wide coefficient.",
        ),
    ),
    "Natural Gas": _mc(
        "Natural Gas",
        "Indirect manufacturing-energy and industrial-supply-chain exposure",
        (
            "Manufacturing energy",
            "Process heat",
            "Supplier costs",
            "Industrial inflation",
        ),
        (
            "Jewellery manufacturing",
            "Watch manufacturing",
            "Eyewear manufacturing",
            "Engineering suppliers",
        ),
        (
            "Industrial activity",
            "Manufacturing ecosystem",
            "Consumer demand through inflation",
        ),
        (
            "Factory energy",
            "Supplier energy",
            "Process heat",
        ),
        (
            "Energy inflation",
            "Industrial growth",
            "Currency",
            "Power-market conditions",
        ),
        (
            "Natural-gas return",
            "Factory utility cost",
            "Manufacturing utilisation",
            "Gross margin",
            "Supplier inflation",
        ),
        (
            "Gas-price spike",
            "Industrial energy shock",
            "Manufacturing disruption",
        ),
        ("1W", "1M", "3M", "6M"),
        (
            "Treat natural gas as an operating/supplier variable, not a primary jewellery demand driver.",
            "Use plant-level energy consumption where available.",
        ),
    ),
    "Copper": _mc(
        "Copper",
        "Indirect watch, engineering, electrical-equipment and capex exposure",
        (
            "Electrical component cost",
            "Watch/electronics components",
            "Engineering equipment",
            "Store and facility capex",
        ),
        (
            "Watch components",
            "Electrical systems",
            "Engineering",
            "Retail infrastructure",
        ),
        (
            "Wearables demand",
            "Watch innovation",
            "Engineering automation demand",
            "Retail expansion",
        ),
        (
            "Components",
            "Equipment",
            "Electrical systems",
            "Engineering capex",
        ),
        (
            "Industrial growth",
            "Electronics cycle",
            "Infrastructure spending",
        ),
        (
            "Copper return",
            "Component costs",
            "Engineering order book",
            "Wearables volumes",
            "Capex",
            "Gross margin",
        ),
        (
            "Copper-price shock",
            "Electronics component shock",
            "Industrial slowdown",
        ),
        ("1W", "1M", "3M", "6M", "1Y"),
        (
            "Copper is secondary to gold but has identifiable watch/wearables and engineering channels.",
            "Measure actual component exposure before applying a company-wide effect.",
        ),
    ),
    "Aluminium": _mc(
        "Aluminium",
        "Indirect watch, eyewear, packaging, manufacturing and infrastructure exposure",
        (
            "Watch cases/components",
            "Eyewear frames",
            "Packaging",
            "Manufacturing equipment",
            "Retail infrastructure",
        ),
        (
            "Watch manufacturing",
            "Eyewear manufacturing",
            "Packaging",
            "Stores and facilities",
        ),
        (
            "Premium watches",
            "Eyewear demand",
            "Consumer durables",
            "Retail expansion",
        ),
        (
            "Metal components",
            "Packaging",
            "Equipment",
            "Construction",
        ),
        (
            "Industrial growth",
            "Consumer durables",
            "Commodity inflation",
        ),
        (
            "Aluminium return",
            "Component cost",
            "Packaging cost",
            "Watch volumes",
            "Eyewear volumes",
            "Gross margin",
        ),
        (
            "Aluminium shock",
            "Component-cost event",
            "Consumer-durable slowdown",
        ),
        ("1W", "1M", "3M", "6M", "1Y"),
        (
            "Aluminium has product/component channels but is not a core Titan-wide commodity driver.",
            "Separate watch/eyewear component effects from general macro effects.",
        ),
    ),
    "Zinc": _mc(
        "Zinc",
        "Indirect galvanised-steel, retail-infrastructure and manufacturing-cost exposure",
        (
            "Retail-store construction",
            "Factory infrastructure",
            "Equipment cost",
            "Industrial-cycle signal",
        ),
        (
            "Store construction",
            "Warehouses",
            "Manufacturing facilities",
            "Engineering equipment",
        ),
        (
            "Store expansion",
            "Retail investment",
            "Consumer demand",
        ),
        (
            "Construction",
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
            "Store capex",
            "PP&E additions",
            "Engineering orders",
            "Retail expansion",
        ),
        (
            "Zinc shock",
            "Construction slowdown",
            "Infrastructure-cost shock",
        ),
        ("1W", "1M", "3M", "6M", "1Y"),
        (
            "Zinc is an infrastructure/capex variable for Titan, not a primary product input.",
            "Use actual store and manufacturing capex to validate the relationship.",
        ),
    ),
    "Electricity": _mc(
        "Electricity",
        "Meaningful manufacturing, retail-store, warehouse and digital-operating-cost exposure",
        (
            "Store operating cost",
            "Manufacturing cost",
            "Retail refrigeration/lighting/HVAC where applicable",
            "Warehousing",
            "Digital commerce",
            "Plant uptime",
        ),
        (
            "Jewellery factories",
            "Watch plants",
            "Eyewear facilities",
            "Retail stores",
            "Warehouses",
            "Digital infrastructure",
        ),
        (
            "Store network expansion",
            "Digital commerce",
            "Manufacturing capacity",
            "Retail availability",
        ),
        (
            "Store electricity",
            "Factory electricity",
            "HVAC",
            "Lighting",
            "IT infrastructure",
        ),
        (
            "Power prices",
            "Grid reliability",
            "Renewable sourcing",
            "Regional electricity conditions",
        ),
        (
            "Electricity price",
            "Power consumption",
            "Store energy cost",
            "Factory utility expense",
            "Store productivity",
            "EBIT margin",
        ),
        (
            "Power-price spike",
            "Grid disruption",
            "Plant outage",
            "Retail network disruption",
        ),
        ("1D", "1W", "1M", "3M", "6M"),
        (
            "Measure electricity through actual store/factory operating cost.",
            "Separate power-cost effects from consumer-demand and gold-price effects.",
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
    """Return the complete Titan Company business character."""
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
    """Structural validation only; actual market impact is calculated elsewhere."""
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
    print("TITAN character validation:", result)

    for market in TRACKED_MARKETS:
        character = get_market_character(market)
        print(
            f"{market}: {character.exposure_type} | "
            f"{len(character.indicators_to_measure)} indicators | "
            f"{len(character.event_signals)} event groups"
        )
