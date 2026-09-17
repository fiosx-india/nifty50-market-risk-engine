"""
ASIANPAINT — Company Character Definition
==========================================

NIFTY 50 Market Risk Engine

Purpose
-------
Define the business character of Asian Paints and its relationship
with the 9 research markets.

This is CHARACTER / RELATIONSHIP metadata.

It does NOT contain:
- fixed linkage scores
- fixed percentage impacts
- ranks
- predicted returns
- BUY/SELL decisions

Those must be calculated later from real historical/live data.
"""

from dataclasses import dataclass, field
from typing import Dict, List


# ============================================================
# 1. MARKET CHARACTER
# ============================================================

@dataclass(frozen=True)
class MarketCharacter:
    market: str
    character: str
    exposure_character: str
    impact_path: str
    calculation_logic: str


# ============================================================
# 2. COMPANY CHARACTER
# ============================================================

@dataclass(frozen=True)
class CompanyCharacter:
    symbol: str
    company_name: str
    company_character: str

    primary_businesses: List[str] = field(default_factory=list)
    operating_model: List[str] = field(default_factory=list)

    revenue_drivers: List[str] = field(default_factory=list)
    cost_drivers: List[str] = field(default_factory=list)
    demand_drivers: List[str] = field(default_factory=list)

    supply_chain_links: List[str] = field(default_factory=list)
    sector_links: List[str] = field(default_factory=list)

    markets: Dict[str, MarketCharacter] = field(default_factory=dict)

    important_indicators: List[str] = field(default_factory=list)
    important_events: List[str] = field(default_factory=list)
    preferred_timeframes: List[str] = field(default_factory=list)

    calculation_rules: List[str] = field(default_factory=list)


# ============================================================
# 3. ASIAN PAINTS COMPANY CHARACTER
# ============================================================

ASIANPAINT_CHARACTER = CompanyCharacter(

    symbol="ASIANPAINT",

    company_name="Asian Paints Limited",

    company_character=(
        "Integrated paints, coatings and home-décor platform built around "
        "decorative paints, home décor, international operations and industrial "
        "coatings. The company's economic character is driven by housing and "
        "renovation demand, construction activity, consumer spending, paint "
        "volumes, product mix, pricing power, raw-material costs, manufacturing "
        "utilisation, distribution reach and brand strength."
    ),

    # ========================================================
    # CORE BUSINESSES
    # ========================================================

    primary_businesses=[
        "Decorative paints",
        "Interior paints",
        "Exterior paints",
        "Waterproofing",
        "Wood finishes",
        "Adhesives",
        "Industrial coatings",
        "Automotive and industrial coatings through associated businesses",
        "Home décor",
        "Modular kitchens",
        "Wardrobes",
        "Bath fittings and sanitaryware",
        "Decorative lighting",
        "Fabric and furnishings",
        "International paint operations",
        "Painting and home-improvement services",
    ],

    # ========================================================
    # OPERATING MODEL
    # ========================================================

    operating_model=[
        "Large-scale paint manufacturing",
        "Raw-material procurement",
        "Product formulation",
        "Distribution through dealers and retail touchpoints",
        "Brand-driven consumer demand generation",
        "Contractor and painter ecosystem",
        "Home décor retail",
        "Industrial customer relationships",
        "International manufacturing and distribution",
        "Research and product innovation",
        "Backward integration",
        "Digital customer and service platforms",
    ],

    # ========================================================
    # REVENUE DRIVERS
    # ========================================================

    revenue_drivers=[
        "Decorative paint volumes",
        "Paint realisations",
        "Premium product mix",
        "Home renovation demand",
        "New-home construction",
        "Repainting cycle",
        "Waterproofing demand",
        "Wood and surface-finishing demand",
        "Industrial coating demand",
        "Automotive coating demand",
        "Infrastructure coating demand",
        "Home décor sales",
        "International market demand",
        "Painting services",
        "Dealer network expansion",
        "B2B demand",
    ],

    # ========================================================
    # COST DRIVERS
    # ========================================================

    cost_drivers=[
        "Crude-oil-linked raw materials",
        "Petrochemical derivatives",
        "Resins",
        "Solvents",
        "Titanium dioxide and pigments",
        "Industrial minerals",
        "Aluminium-related inputs",
        "Zinc-related inputs",
        "Packaging materials",
        "Electricity",
        "Natural gas and other energy inputs",
        "Freight and logistics",
        "Employee costs",
        "Manufacturing overhead",
        "Advertising and brand expenditure",
        "Capital expenditure",
        "Financing costs",
    ],

    # ========================================================
    # DEMAND DRIVERS
    # ========================================================

    demand_drivers=[
        "Housing construction",
        "Residential renovation",
        "Repainting cycle",
        "Urbanisation",
        "Rural consumption",
        "Disposable income",
        "Consumer confidence",
        "Real-estate activity",
        "Infrastructure spending",
        "Industrial production",
        "Automobile production",
        "Commercial construction",
        "Festival and seasonal demand",
        "Home-improvement spending",
        "Interest-rate environment",
        "Construction-material demand",
    ],

    # ========================================================
    # SUPPLY CHAIN
    # ========================================================

    supply_chain_links=[
        "Petrochemical producers",
        "Chemical manufacturers",
        "Pigment suppliers",
        "Titanium dioxide suppliers",
        "Resin suppliers",
        "Solvent suppliers",
        "Packaging suppliers",
        "Aluminium suppliers",
        "Zinc suppliers",
        "Energy suppliers",
        "Electricity providers",
        "Natural-gas suppliers",
        "Transport and logistics providers",
        "Dealers",
        "Retailers",
        "Painters and contractors",
        "Construction companies",
        "Automobile manufacturers",
        "Industrial manufacturers",
    ],

    # ========================================================
    # SECTOR LINKS
    # ========================================================

    sector_links=[
        "Paints",
        "Decorative coatings",
        "Industrial coatings",
        "Home décor",
        "Construction materials",
        "Housing",
        "Real estate",
        "Infrastructure",
        "Automobile ecosystem",
        "Consumer discretionary",
        "Chemicals",
        "Petrochemicals",
        "Manufacturing",
    ],

    # ========================================================
    # 9 MARKET CHARACTERS
    # ========================================================

    markets={

        # ----------------------------------------------------
        # 1. NIFTY 50
        # ----------------------------------------------------

        "NIFTY 50": MarketCharacter(

            market="NIFTY 50",

            character=(
                "Broad Indian equity-market environment influencing "
                "liquidity, institutional flows, risk appetite, valuation "
                "multiples and consumer/business sentiment."
            ),

            exposure_character=(
                "Primary systematic-market relationship"
            ),

            impact_path=(
                "NIFTY movement → market liquidity / investor sentiment / "
                "valuation → ASIANPAINT stock behaviour"
            ),

            calculation_logic=(
                "Calculate return correlation, beta, rolling beta, relative "
                "strength, downside sensitivity and lag response. Separate "
                "systematic market movement from paint-sector and company-specific "
                "events."
            ),
        ),

        # ----------------------------------------------------
        # 2. CRUDE OIL
        # ----------------------------------------------------

        "Crude Oil": MarketCharacter(

            market="Crude Oil",

            character=(
                "Global energy commodity with an important connection to "
                "petrochemical-derived paint raw materials, transportation "
                "costs and broader inflation."
            ),

            exposure_character=(
                "Direct raw-material-cost + logistics/inflation relationship"
            ),

            impact_path=(
                "Crude Oil movement → petrochemical/raw-material costs + "
                "freight/inflation → gross margin / pricing response → "
                "ASIANPAINT earnings and valuation"
            ),

            calculation_logic=(
                "Measure crude returns against raw-material-cost proxies, "
                "gross margin, EBITDA margin and stock returns. Test lagged "
                "effects because procurement and inventory pass-through may "
                "occur with delay. Control for NIFTY and demand conditions."
            ),
        ),

        # ----------------------------------------------------
        # 3. GOLD
        # ----------------------------------------------------

        "Gold": MarketCharacter(

            market="Gold",

            character=(
                "Precious-metal and macro-risk asset reflecting risk sentiment, "
                "currency conditions, real rates and liquidity."
            ),

            exposure_character=(
                "Indirect macro / consumer-sentiment relationship"
            ),

            impact_path=(
                "Gold movement → risk sentiment / currency / liquidity / "
                "macro conditions → consumer spending and equity valuation "
                "→ ASIANPAINT"
            ),

            calculation_logic=(
                "Test whether gold provides incremental explanatory power "
                "after controlling for NIFTY, currency, interest rates and "
                "consumer-demand indicators. Do not assume direct gold exposure."
            ),
        ),

        # ----------------------------------------------------
        # 4. SILVER
        # ----------------------------------------------------

        "Silver": MarketCharacter(

            market="Silver",

            character=(
                "Precious and industrial metal whose movement can reflect "
                "industrial activity, commodity inflation and global growth."
            ),

            exposure_character=(
                "Indirect industrial-cycle / macro relationship"
            ),

            impact_path=(
                "Silver movement → industrial/commodity cycle → construction "
                "and manufacturing environment → paint demand / valuation"
            ),

            calculation_logic=(
                "Calculate historical return, rolling correlation, lag response "
                "and volatility relationship. Control for NIFTY, copper and "
                "broader industrial indicators."
            ),
        ),

        # ----------------------------------------------------
        # 5. NATURAL GAS
        # ----------------------------------------------------

        "Natural Gas": MarketCharacter(

            market="Natural Gas",

            character=(
                "Energy commodity affecting industrial energy costs, "
                "manufacturing economics and inflation."
            ),

            exposure_character=(
                "Indirect energy-cost + manufacturing relationship"
            ),

            impact_path=(
                "Natural Gas movement → manufacturing energy cost / inflation "
                "→ production economics and margins → ASIANPAINT"
            ),

            calculation_logic=(
                "Measure contemporaneous and lagged gas-price relationships "
                "with margins and stock returns. Distinguish actual energy "
                "cost exposure from broad energy-market sentiment."
            ),
        ),

        # ----------------------------------------------------
        # 6. COPPER
        # ----------------------------------------------------

        "Copper": MarketCharacter(

            market="Copper",

            character=(
                "Industrial metal and economic-cycle indicator linked to "
                "construction, electrical infrastructure, manufacturing and "
                "global industrial activity."
            ),

            exposure_character=(
                "Indirect construction / industrial-cycle relationship"
            ),

            impact_path=(
                "Copper cycle → construction / infrastructure / industrial "
                "activity → paint and coatings demand → ASIANPAINT"
            ),

            calculation_logic=(
                "Measure copper returns against company returns, industrial "
                "coatings activity and construction indicators. Use rolling "
                "and lagged analysis and control for NIFTY."
            ),
        ),

        # ----------------------------------------------------
        # 7. ALUMINIUM
        # ----------------------------------------------------

        "Aluminium": MarketCharacter(

            market="Aluminium",

            character=(
                "Industrial metal used throughout construction, transportation, "
                "packaging and manufacturing supply chains."
            ),

            exposure_character=(
                "Indirect industrial-cost + construction-cycle relationship"
            ),

            impact_path=(
                "Aluminium movement → construction/manufacturing activity + "
                "input-cost environment → paint demand / margins → ASIANPAINT"
            ),

            calculation_logic=(
                "Test aluminium returns against company returns, construction "
                "activity and margin data. Separate demand-cycle effects from "
                "possible input-cost effects and use lag analysis."
            ),
        ),

        # ----------------------------------------------------
        # 8. ZINC
        # ----------------------------------------------------

        "Zinc": MarketCharacter(

            market="Zinc",

            character=(
                "Industrial metal strongly associated with galvanising, "
                "construction, infrastructure and manufacturing activity."
            ),

            exposure_character=(
                "Indirect raw-material + construction/infrastructure relationship"
            ),

            impact_path=(
                "Zinc movement → industrial/construction cycle + selected "
                "coating/input economics → industrial paint demand / costs "
                "→ ASIANPAINT"
            ),

            calculation_logic=(
                "Test zinc returns against industrial-coating activity, "
                "construction indicators, margins and stock returns. Use "
                "lagged and rolling analysis; do not assume direct causation."
            ),
        ),

        # ----------------------------------------------------
        # 9. ELECTRICITY
        # ----------------------------------------------------

        "Electricity": MarketCharacter(

            market="Electricity",

            character=(
                "Important manufacturing operating input affecting paint "
                "production, plants, warehouses, technology systems and "
                "overall energy efficiency."
            ),

            exposure_character=(
                "Direct manufacturing energy-cost relationship"
            ),

            impact_path=(
                "Electricity price / availability → manufacturing and facility "
                "operating costs → production economics / margins → ASIANPAINT"
            ),

            calculation_logic=(
                "Measure electricity price, volatility and availability where "
                "reliable regional data exists. Compare with manufacturing "
                "costs, margins and stock behaviour. Account for renewable "
                "electricity usage and geographic plant distribution."
            ),
        ),
    },

    # ========================================================
    # IMPORTANT INDICATORS
    # ========================================================

    important_indicators=[

        # Company
        "Paint volume growth",
        "Revenue growth",
        "Gross margin",
        "EBITDA margin",
        "EBITDA growth",
        "Free cash flow",
        "Working capital",
        "Inventory days",
        "Receivable days",
        "Capacity utilisation",
        "Manufacturing utilisation",
        "Dealer network",
        "Retail reach",
        "Premium product mix",
        "Decorative paint growth",
        "Industrial coatings growth",
        "Home décor growth",
        "International business growth",

        # Demand
        "Housing activity",
        "Real-estate activity",
        "Construction activity",
        "Infrastructure spending",
        "Automobile production",
        "Consumer confidence",
        "Rural demand",
        "Urban demand",
        "Interest rates",

        # Commodity
        "Crude Oil",
        "Natural Gas",
        "Copper",
        "Aluminium",
        "Zinc",
        "Gold",
        "Silver",
        "Electricity",

        # Market
        "NIFTY 50 return",
        "Relative strength",
        "Trading volume",
        "Relative volume",
        "Volatility",
        "Sector-relative return",
    ],

    # ========================================================
    # IMPORTANT EVENTS
    # ========================================================

    important_events=[

        "Quarterly results",
        "Annual results",
        "Annual report",
        "Raw-material price changes",
        "Crude-oil price shocks",
        "Major commodity-cost changes",
        "Price increases",
        "Price reductions",
        "New product launches",
        "Premium product launches",
        "Manufacturing capacity expansion",
        "New plant announcements",
        "Plant shutdowns",
        "Backward-integration projects",
        "Home décor expansion",
        "Dealer-network changes",
        "International business developments",
        "Industrial coating contracts",
        "Infrastructure spending announcements",
        "Automobile production changes",
        "Housing and real-estate policy",
        "Interest-rate changes",
        "GST / taxation changes",
        "Import/export policy changes",
        "Regulatory developments",
        "Major competitor actions",
        "Supply-chain disruptions",
        "Energy-cost shocks",
        "Company exchange filings",
    ],

    # ========================================================
    # TIMEFRAMES
    # ========================================================

    preferred_timeframes=[
        "5m",
        "15m",
        "30m",
        "1h",
        "4h",
        "1d",
        "1w",
        "1M",
    ],

    # ========================================================
    # CALCULATION RULES
    # ========================================================

    calculation_rules=[

        "Do not use the old RANK as a permanent company characteristic.",

        "Do not use the old PCT_CHANGE as a permanent company characteristic.",

        "Do not use the old LINKAGE_SCORE as a permanent relationship.",

        "Do not convert the old RELATION field directly into a prediction.",

        "Calculate relationships from actual historical observations.",

        "Crude Oil must be treated as an important raw-material and "
        "logistics-cost variable rather than merely a generic market signal.",

        "Separate raw-material cost effects from demand-cycle effects.",

        "Use lagged commodity variables because inventory and procurement "
        "cycles can delay the impact on margins.",

        "Use rolling windows to identify changing relationships.",

        "Control for NIFTY 50 when testing individual market relationships.",

        "Control for construction, industrial and consumer-demand variables "
        "where data is available.",

        "Use margin data to distinguish cost inflation from revenue-demand effects.",

        "Use volume confirmation when analysing stock-price reactions.",

        "Use event studies around company-specific announcements.",

        "Use sector-relative performance to distinguish paint-sector effects "
        "from broad-market effects.",

        "Do not assume correlation means causation.",

        "Track data freshness and source quality.",

        "Do not make final BUY/SELL decisions inside this character module.",

        "Pass calculated evidence to the central research and decision layer.",
    ],
)


# ============================================================
# 4. PUBLIC FUNCTIONS
# ============================================================

def get_company_character() -> CompanyCharacter:
    """Return the complete Asian Paints company character."""
    return ASIANPAINT_CHARACTER


def get_market_character(market: str) -> MarketCharacter:
    """Return the character definition for one supported market."""

    key = market.strip()

    if key not in ASIANPAINT_CHARACTER.markets:
        raise KeyError(
            f"Unsupported market '{market}'. "
            f"Supported markets: "
            f"{', '.join(ASIANPAINT_CHARACTER.markets)}"
        )

    return ASIANPAINT_CHARACTER.markets[key]


def get_all_markets() -> Dict[str, MarketCharacter]:
    """Return all 9 market characters."""
    return dict(ASIANPAINT_CHARACTER.markets)


def get_company_summary() -> dict:
    """Return a compact machine-readable company summary."""

    return {
        "symbol": ASIANPAINT_CHARACTER.symbol,
        "company_name": ASIANPAINT_CHARACTER.company_name,
        "company_character": ASIANPAINT_CHARACTER.company_character,
        "primary_businesses": list(
            ASIANPAINT_CHARACTER.primary_businesses
        ),
        "sector_links": list(
            ASIANPAINT_CHARACTER.sector_links
        ),
        "market_count": len(
            ASIANPAINT_CHARACTER.markets
        ),
        "markets": list(
            ASIANPAINT_CHARACTER.markets.keys()
        ),
    }


def validate_character() -> bool:
    """
    Validate the company character structure.

    This validates completeness only.
    It does not prove historical correlation or causation.
    """

    expected_markets = {
        "NIFTY 50",
        "Crude Oil",
        "Gold",
        "Silver",
        "Natural Gas",
        "Copper",
        "Aluminium",
        "Zinc",
        "Electricity",
    }

    actual_markets = set(
        ASIANPAINT_CHARACTER.markets.keys()
    )

    if actual_markets != expected_markets:

        missing = expected_markets - actual_markets
        extra = actual_markets - expected_markets

        raise ValueError(
            "Market character validation failed. "
            f"Missing={sorted(missing)}, "
            f"Extra={sorted(extra)}"
        )

    if ASIANPAINT_CHARACTER.symbol != "ASIANPAINT":
        raise ValueError(
            "Invalid company symbol."
        )

    for market_name, market in (
        ASIANPAINT_CHARACTER.markets.items()
    ):

        required_fields = [
            market.market,
            market.character,
            market.exposure_character,
            market.impact_path,
            market.calculation_logic,
        ]

        if not all(required_fields):

            raise ValueError(
                f"Incomplete market character: "
                f"{market_name}"
            )

    return True


# ============================================================
# 5. DIRECT EXECUTION TEST
# ============================================================

if __name__ == "__main__":

    validate_character()

    print("ASIANPAINT Character: VALID")
    print(
        f"Company: "
        f"{ASIANPAINT_CHARACTER.company_name}"
    )

    print(
        f"Markets: "
        f"{len(ASIANPAINT_CHARACTER.markets)}"
    )

    for name, market in (
        ASIANPAINT_CHARACTER.markets.items()
    ):

        print(
            f"- {name}: "
            f"{market.exposure_character}"
)
