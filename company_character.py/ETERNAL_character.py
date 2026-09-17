"""
ETERNAL (Eternal Limited; formerly Zomato Limited)
Company Character & 9-Market Relationship Engine

CHARACTER LAYER ONLY
--------------------
Eternal is modeled as a multi-business consumer-internet and commerce
platform rather than simply as "Zomato".

Current business character:
    1. Zomato       -> food discovery, ordering and delivery
    2. Blinkit      -> quick commerce
    3. District     -> going-out / experiences / transactions
    4. Hyperpure    -> B2B restaurant supply chain

The character layer describes WHAT should be calculated later.

It deliberately does NOT hard-code:
    RANK
    PCT_CHANGE
    LINKAGE_SCORE
    RELATION

Those are historical-calculation outputs and must be derived from real
market, operating, financial, event and news data.
"""

from dataclasses import dataclass, field
from typing import Dict, List


TRACKED_MARKETS = (
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
    relevant_indicators: List[str] = field(default_factory=list)
    relevant_events: List[str] = field(default_factory=list)
    expected_timeframes: List[str] = field(
        default_factory=lambda: [
            "intraday", "1D", "1W", "1M", "3M", "6M", "1Y"
        ]
    )


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
    market_characters: Dict[str, MarketCharacter]


ETERNAL_MARKETS: Dict[str, MarketCharacter] = {

    "NIFTY 50": MarketCharacter(
        market="NIFTY 50",
        character=(
            "Primary systematic equity-market character for Eternal. "
            "The company is a large consumer-internet platform, so broad "
            "liquidity, growth-stock valuation, consumer sentiment and "
            "technology-sector flows can affect its market valuation."
        ),
        exposure_character=(
            "Direct systematic equity exposure with additional consumer-"
            "internet, growth, technology and discretionary-spending factors."
        ),
        impact_path=[
            "NIFTY 50 movement",
            "Indian equity liquidity and risk appetite",
            "growth / consumer-internet sector flows",
            "Eternal valuation",
            "ETERNAL relative performance",
        ],
        calculation_logic=[
            "Calculate ETERNAL returns against NIFTY 50 over matched windows.",
            "Estimate rolling beta and rolling correlation instead of using the supplied fixed linkage.",
            "Calculate excess return after controlling for NIFTY 50.",
            "Where available, separately control for consumer-internet and technology factors.",
            "Test daily, weekly and monthly lead/lag relationships.",
        ],
        relevant_indicators=[
            "ETERNAL return",
            "NIFTY 50 return",
            "rolling beta",
            "rolling correlation",
            "relative strength",
            "volume",
            "volatility",
        ],
        relevant_events=[
            "market-wide risk-on/risk-off events",
            "interest-rate decisions",
            "technology/growth-stock repricing",
            "consumer-spending data",
            "Eternal quarterly results",
        ],
    ),

    "Crude Oil": MarketCharacter(
        market="Crude Oil",
        character=(
            "Important delivery-logistics, consumer purchasing-power and "
            "restaurant/food-supply cost character. Crude affects petrol/diesel, "
            "last-mile delivery economics, logistics, food inflation and "
            "discretionary consumer spending."
        ),
        exposure_character=(
            "Indirect-to-moderate exposure through delivery cost, logistics, "
            "restaurant economics and household purchasing power."
        ),
        impact_path=[
            "Crude oil price",
            "fuel / logistics / delivery cost",
            "restaurant and merchant operating economics",
            "consumer disposable income and order behaviour",
            "Eternal orders / margins / earnings",
        ],
        calculation_logic=[
            "Measure contemporaneous and lagged crude/ETERNAL relationships.",
            "Separate delivery-cost effects from consumer-demand effects.",
            "Control for NIFTY 50 and inflation.",
            "Compare crude shocks with food-delivery order value, order volume and contribution margin where available.",
            "For Hyperpure, test crude against procurement and logistics-cost indicators.",
            "Use event studies around unusually large crude movements.",
        ],
        relevant_indicators=[
            "crude return",
            "petrol/diesel-price proxy",
            "CPI/food-inflation proxy",
            "food-delivery NOV",
            "quick-commerce NOV",
            "contribution margin",
        ],
        relevant_events=[
            "large crude shocks",
            "fuel-price changes",
            "fuel-tax changes",
            "food-inflation shocks",
            "major geopolitical energy events",
        ],
    ),

    "Gold": MarketCharacter(
        market="Gold",
        character=(
            "Indirect household-wealth, liquidity, safe-haven and discretionary-"
            "spending character. Gold is not a direct operating input; it can "
            "serve as a regime variable for household wealth and risk appetite."
        ),
        exposure_character=(
            "Indirect macro, consumer-sentiment and portfolio-flow exposure."
        ),
        impact_path=[
            "Gold price",
            "wealth / liquidity / risk-sentiment signal",
            "consumer confidence and discretionary spending",
            "food, quick-commerce and going-out activity",
            "Eternal valuation / operating demand",
        ],
        calculation_logic=[
            "Measure rolling and lagged gold/ETERNAL relationships.",
            "Control for NIFTY 50, rates, inflation and consumer-sentiment variables.",
            "Test whether relationships differ between risk-off and consumer-expansion regimes.",
            "Compare gold movements with discretionary transaction indicators where available.",
            "Do not infer causation from correlation alone.",
        ],
        relevant_indicators=[
            "gold return",
            "consumer-sentiment proxy",
            "retail spending proxy",
            "B2C NOV",
            "ETERNAL return",
        ],
        relevant_events=[
            "large gold-price moves",
            "wealth/liquidity shocks",
            "rate events",
            "major risk-off events",
        ],
    ),

    "Silver": MarketCharacter(
        market="Silver",
        character=(
            "Indirect industrial, technology and consumer-cycle character. "
            "Silver is not a core Eternal input; it can act as a broad "
            "industrial/commodity-cycle and risk-sentiment variable."
        ),
        exposure_character=(
            "Indirect industrial-cycle, technology and macro exposure."
        ),
        impact_path=[
            "Silver price",
            "industrial / technology / commodity-cycle signal",
            "business investment and consumer environment",
            "commerce / restaurant / delivery activity",
            "Eternal market response",
        ],
        calculation_logic=[
            "Measure rolling and lagged silver/ETERNAL relationships.",
            "Compare silver with copper to identify common industrial-cycle effects.",
            "Control for NIFTY 50 and broader commodity conditions.",
            "Test whether silver leads changes in consumer-commerce activity.",
        ],
        relevant_indicators=[
            "silver return",
            "copper return",
            "industrial-cycle proxy",
            "consumer-spending proxy",
            "ETERNAL return",
        ],
        relevant_events=[
            "global industrial shocks",
            "technology-cycle changes",
            "commodity-volatility events",
        ],
    ),

    "Natural Gas": MarketCharacter(
        market="Natural Gas",
        character=(
            "Indirect food-service, cold-chain, warehouse and industrial-energy "
            "character. Natural gas can influence restaurant, warehouse and "
            "supplier energy costs, while also affecting broader inflation."
        ),
        exposure_character=(
            "Indirect operating-cost, merchant-cost and macro-inflation exposure."
        ),
        impact_path=[
            "Natural-gas price",
            "restaurant / warehouse / food-processing energy economics",
            "merchant and supplier costs",
            "food prices / consumer demand",
            "Eternal transaction economics",
        ],
        calculation_logic=[
            "Measure lagged natural-gas/ETERNAL relationships.",
            "Control for crude oil, electricity and food inflation.",
            "Compare energy shocks with Hyperpure and food-delivery operating metrics where available.",
            "Separate direct merchant-cost effects from broad inflation effects.",
            "Use India-relevant energy data when available.",
        ],
        relevant_indicators=[
            "natural-gas return",
            "food-inflation proxy",
            "electricity proxy",
            "Hyperpure economics",
            "contribution margin",
        ],
        relevant_events=[
            "energy supply disruptions",
            "natural-gas price shocks",
            "food-inflation events",
            "geopolitical energy events",
        ],
    ),

    "Copper": MarketCharacter(
        market="Copper",
        character=(
            "Indirect technology, electronics, data-centre, electrical and "
            "infrastructure-cost character. Copper can affect servers, networking, "
            "electrical equipment, dark stores, warehouses and broader technology "
            "infrastructure, while also serving as an industrial-cycle signal."
        ),
        exposure_character=(
            "Indirect technology-infrastructure and industrial-cycle exposure."
        ),
        impact_path=[
            "Copper price",
            "electrical / networking / infrastructure equipment cost",
            "technology and fulfilment infrastructure economics",
            "capex and operating cost",
            "Eternal margin / cash-flow expectations",
        ],
        calculation_logic=[
            "Measure rolling and lagged copper/ETERNAL relationships.",
            "Compare copper movement with capex and infrastructure-cost indicators.",
            "Control for aluminium, electricity and broader industrial-metal movement.",
            "Use procurement and capex lags rather than same-day correlation only.",
            "Separate input-cost effects from copper's industrial-demand signal.",
        ],
        relevant_indicators=[
            "copper return",
            "industrial-metals basket",
            "capex",
            "warehouse/dark-store expansion",
            "technology infrastructure cost",
            "free cash flow",
        ],
        relevant_events=[
            "copper supply disruptions",
            "data-centre / technology infrastructure expansion",
            "dark-store expansion",
            "major capex events",
        ],
    ),

    "Aluminium": MarketCharacter(
        market="Aluminium",
        character=(
            "Indirect packaging, warehouse, equipment, logistics and quick-commerce "
            "infrastructure character. Aluminium can affect packaging materials, "
            "storage/fulfilment equipment and broader industrial costs."
        ),
        exposure_character=(
            "Indirect infrastructure, packaging and capex-cost exposure."
        ),
        impact_path=[
            "Aluminium price",
            "packaging / equipment / warehouse infrastructure costs",
            "fulfilment and supply-chain economics",
            "capex / operating cost",
            "Eternal margin and cash-flow expectations",
        ],
        calculation_logic=[
            "Measure rolling and lagged aluminium/ETERNAL relationships.",
            "Compare aluminium movement with capex and fulfilment expansion.",
            "Control for copper, electricity and broader industrial-metal conditions.",
            "Use procurement/inventory lags.",
            "Test whether sensitivity increases during rapid quick-commerce expansion.",
        ],
        relevant_indicators=[
            "aluminium return",
            "industrial-metals basket",
            "capex",
            "dark-store/store additions",
            "warehouse expansion",
            "contribution margin",
        ],
        relevant_events=[
            "aluminium supply shocks",
            "packaging-cost changes",
            "rapid fulfilment-network expansion",
            "major capex events",
        ],
    ),

    "Zinc": MarketCharacter(
        market="Zinc",
        character=(
            "Indirect warehouse, fabrication, infrastructure and supply-chain "
            "cost character. Zinc can influence galvanised steel and fabricated "
            "equipment used across fulfilment and logistics infrastructure."
        ),
        exposure_character=(
            "Indirect infrastructure and supplier-cost exposure."
        ),
        impact_path=[
            "Zinc price",
            "galvanised steel / fabrication cost",
            "warehouse / dark-store / logistics infrastructure cost",
            "capex and operating economics",
            "Eternal cash-flow / margin expectations",
        ],
        calculation_logic=[
            "Measure rolling and lagged zinc/ETERNAL relationships.",
            "Compare zinc with aluminium and copper to identify common industrial factors.",
            "Control for NIFTY 50 and electricity.",
            "Use fulfilment-network expansion and procurement lag variables.",
            "Do not treat correlation as direct causation without infrastructure evidence.",
        ],
        relevant_indicators=[
            "zinc return",
            "industrial-metals basket",
            "warehouse/store expansion",
            "capex",
            "fulfilment cost",
            "ETERNAL return",
        ],
        relevant_events=[
            "zinc supply shocks",
            "warehouse expansion",
            "logistics infrastructure changes",
            "major capex events",
        ],
    ),

    "Electricity": MarketCharacter(
        market="Electricity",
        character=(
            "Direct operational-energy character across dark stores, warehouses, "
            "offices, data infrastructure, cold-chain/food operations and other "
            "fulfilment facilities. Electricity reliability also affects delivery "
            "and storage operations."
        ),
        exposure_character=(
            "Direct operating-cost and fulfilment-reliability exposure, increasing "
            "with the scale of quick commerce, warehouses and technology infrastructure."
        ),
        impact_path=[
            "Electricity price / availability",
            "dark-store / warehouse / technology / cold-chain energy cost",
            "fulfilment operating cost",
            "contribution margin and service reliability",
            "Eternal earnings / cash flow",
        ],
        calculation_logic=[
            "Use electricity tariff/market data relevant to major operating geographies.",
            "Measure lagged electricity-cost sensitivity against segment margins.",
            "Separate price impact from outage/reliability impact.",
            "Control for natural gas and broader inflation.",
            "Test whether electricity sensitivity changes as Blinkit store density and fulfilment infrastructure expand.",
        ],
        relevant_indicators=[
            "electricity price",
            "industrial/commercial tariff proxy",
            "power availability",
            "dark-store energy cost",
            "warehouse energy cost",
            "contribution margin",
            "free cash flow",
        ],
        relevant_events=[
            "electricity tariff changes",
            "power shortages/outages",
            "grid events",
            "large warehouse expansion",
            "dark-store expansion",
            "energy-efficiency initiatives",
        ],
    ),
}


ETERNAL_CHARACTER = CompanyCharacter(
    symbol="ETERNAL",
    company_name="Eternal Limited",
    sector="Consumer Internet / Food Technology / Quick Commerce / B2B Commerce",
    industry_character=(
        "Multi-business consumer-internet and commerce platform built around "
        "Zomato, Blinkit, District and Hyperpure. Its economic character is "
        "transaction-volume driven, network-effect driven, technology-intensive, "
        "logistics-intensive and highly sensitive to consumer spending, merchant "
        "economics, delivery density, customer acquisition, order frequency, "
        "take rates, contribution margins and fulfilment efficiency."
    ),
    business_character=[
        "Zomato food discovery and ordering",
        "Food delivery",
        "Restaurant discovery",
        "Restaurant and delivery-partner ecosystem",
        "Blinkit quick commerce",
        "Grocery and daily essentials",
        "Electronics and other quick-commerce categories",
        "Beauty and personal care",
        "Fashion and lifestyle categories",
        "District going-out experiences",
        "Dining and entertainment transactions",
        "Experiences and ticketing",
        "Hyperpure B2B restaurant supplies",
        "Farm-to-kitchen sourcing",
        "Cold-chain / temperature-controlled logistics",
        "Restaurant kitchen supplies",
        "Menu innovation",
        "Supply-chain solutions",
        "Technology platform and digital infrastructure",
        "Consumer and merchant data/network ecosystem",
    ],
    demand_drivers=[
        "Consumer disposable income",
        "Urbanisation",
        "Smartphone penetration",
        "Internet penetration",
        "Digital payment adoption",
        "Food-delivery frequency",
        "Quick-commerce convenience demand",
        "Time-saving consumer behaviour",
        "Restaurant ecosystem growth",
        "Dining and entertainment demand",
        "Seasonality and festivals",
        "Weather",
        "Rainfall and traffic conditions",
        "Household consumption",
        "Premiumisation / discretionary spending",
        "Merchant digitisation",
    ],
    revenue_drivers=[
        "Food-delivery GOV / NOV",
        "Food-delivery order volume",
        "Average order value",
        "Take rate",
        "Platform fees",
        "Advertising revenue",
        "Quick-commerce NOV",
        "Quick-commerce order volume",
        "Quick-commerce assortment",
        "Merchant / brand revenue",
        "District transaction value",
        "Ticketing and going-out transactions",
        "Hyperpure sales",
        "Hyperpure outlet coverage",
        "Logistics / fulfilment economics",
        "Subscription / membership economics where applicable",
    ],
    cost_drivers=[
        "Delivery-partner payouts",
        "Last-mile logistics",
        "Fuel",
        "Electricity",
        "Dark-store / warehouse rent",
        "Fulfilment centres",
        "Cold-chain logistics",
        "Food and grocery procurement",
        "Inventory carrying cost",
        "Customer acquisition",
        "Discounts / incentives",
        "Technology infrastructure",
        "Cloud / data costs",
        "Employee costs",
        "Payment processing",
        "Packaging",
        "Merchant support",
        "Expansion capex",
    ],
    supply_chain_character=[
        "Restaurant partners",
        "Delivery partners",
        "Store partners",
        "Dark-store network",
        "Warehouse network",
        "Farmers and food producers",
        "FMCG and consumer-goods suppliers",
        "Cold-chain providers",
        "Third-party logistics",
        "Technology/cloud providers",
        "Payment ecosystem",
        "Packaging suppliers",
        "District venue and experience partners",
        "Food-service supply chain",
    ],
    strategic_drivers=[
        "Food-delivery profitability",
        "Quick-commerce scale and density",
        "Quick-commerce contribution-margin improvement",
        "Dark-store network expansion",
        "Customer retention and order frequency",
        "Cross-business customer ecosystem",
        "District growth",
        "Hyperpure scale",
        "Supply-chain efficiency",
        "Technology and AI",
        "Advertising monetisation",
        "Merchant monetisation",
        "Geographic expansion",
        "Delivery-density improvement",
        "EV-based delivery transition",
        "Capital efficiency and free-cash-flow generation",
    ],
    key_indicators=[
        "food-delivery GOV/NOV",
        "food-delivery order volume",
        "food-delivery AOV",
        "take rate",
        "monthly transacting customers",
        "quick-commerce NOV",
        "quick-commerce order volume",
        "quick-commerce AOV",
        "quick-commerce store count",
        "quick-commerce customer base",
        "dark-store density",
        "delivery time",
        "delivery cost per order",
        "contribution margin",
        "adjusted EBITDA",
        "adjusted EBITDA margin",
        "free cash flow",
        "customer acquisition cost",
        "customer retention",
        "order frequency",
        "Hyperpure revenue",
        "Hyperpure outlet coverage",
        "District transactions",
        "B2C NOV",
        "capex",
        "working capital",
        "inventory",
        "ETERNAL stock return",
        "ETERNAL volume",
        "relative strength versus NIFTY 50",
    ],
    key_events=[
        "quarterly and annual results",
        "food-delivery GOV/NOV updates",
        "quick-commerce NOV updates",
        "new Blinkit store openings",
        "dark-store expansion",
        "quick-commerce category expansion",
        "food-delivery pricing changes",
        "platform-fee changes",
        "delivery-fee changes",
        "merchant commission changes",
        "large restaurant-partner changes",
        "District product / partnership launches",
        "Hyperpure warehouse expansion",
        "Hyperpure supply-chain partnerships",
        "major technology / AI initiatives",
        "consumer-data/privacy events",
        "competition and regulatory changes",
        "e-commerce / quick-commerce policy",
        "gig-worker / delivery-partner regulation",
        "tax/GST changes",
        "fuel-price shocks",
        "food-inflation shocks",
        "major weather disruptions",
        "cybersecurity incidents",
        "capital-allocation changes",
        "strategic investments / acquisitions",
        "new-business launches",
        "EV delivery transition milestones",
    ],
    market_characters=ETERNAL_MARKETS,
)


def get_company_character() -> CompanyCharacter:
    """Return the complete Eternal company character."""
    return ETERNAL_CHARACTER


def get_market_character(market: str) -> MarketCharacter:
    """Return Eternal's character for one of the nine tracked markets."""
    try:
        return ETERNAL_MARKETS[market]
    except KeyError as exc:
        raise ValueError(
            f"Unsupported market: {market!r}. "
            f"Expected one of: {', '.join(TRACKED_MARKETS)}"
        ) from exc


def get_all_market_characters() -> Dict[str, MarketCharacter]:
    """Return all nine Eternal market characters."""
    return dict(ETERNAL_MARKETS)


def validate_character() -> bool:
    """Validate the Eternal company-character contract."""
    if ETERNAL_CHARACTER.symbol != "ETERNAL":
        return False

    if set(ETERNAL_MARKETS) != set(TRACKED_MARKETS):
        return False

    for market_name, character in ETERNAL_MARKETS.items():
        if character.market != market_name:
            return False
        if not character.character:
            return False
        if not character.exposure_character:
            return False
        if not character.impact_path:
            return False
        if not character.calculation_logic:
            return False

    forbidden_fields = {
        "RANK",
        "PCT_CHANGE",
        "LINKAGE_SCORE",
        "RELATION",
        "SCORE",
    }

    if forbidden_fields.intersection(ETERNAL_CHARACTER.__dataclass_fields__):
        return False

    return True


if __name__ == "__main__":
    print(f"{ETERNAL_CHARACTER.company_name} ({ETERNAL_CHARACTER.symbol})")
    print(f"Tracked markets: {len(ETERNAL_MARKETS)}")
    print(f"Character validation: {validate_character()}")

    for market_name in TRACKED_MARKETS:
        character = ETERNAL_MARKETS[market_name]
        print(f"- {market_name}: {character.character}")
