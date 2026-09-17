"""
ADANIENT - Company Character Definition
NIFTY 50 Market Risk & Research Engine

Purpose
-------
Defines the business character of ADANI ENTERPRISES LIMITED (ADANIENT)
and its relationship with the 9 research markets.

IMPORTANT
---------
This file contains CHARACTER / RELATIONSHIP definitions only.

It does NOT contain:
- LINKAGE_SCORE
- RANK
- PCT_CHANGE
- Fixed market impact percentages
- Buy/Sell signals
- Hard-coded prediction rates

All market impact values must be calculated later from real data.
"""

from dataclasses import dataclass, field
from typing import Dict, List


# ============================================================
# 1. MARKET CHARACTER
# ============================================================

@dataclass(frozen=True)
class MarketCharacter:
    name: str
    relationship_type: str
    business_path: List[str]
    what_to_measure: List[str]


# ============================================================
# 2. COMPANY CHARACTER
# ============================================================

@dataclass(frozen=True)
class CompanyCharacter:
    symbol: str
    company_name: str

    primary_character: str

    industries: List[str]
    business_segments: List[str]

    revenue_drivers: List[str]
    cost_drivers: List[str]
    demand_drivers: List[str]

    supply_chain_links: List[str]

    direct_markets: List[str]
    indirect_markets: List[str]

    market_characters: Dict[str, MarketCharacter]

    company_events_to_track: List[str]
    news_categories: List[str]

    indicators_to_measure: List[str]
    timeframes_to_measure: List[str]

    calculation_rules: List[str]


# ============================================================
# 3. ADANIENT - BUSINESS CHARACTER
# ============================================================

ADANIENT_CHARACTER = CompanyCharacter(

    symbol="ADANIENT",

    company_name="Adani Enterprises Limited",

    primary_character=(
        "Diversified infrastructure and business-incubation company with "
        "major exposure to transport and logistics, energy transition, "
        "natural resources, industrial businesses and emerging infrastructure."
    ),

    industries=[
        "Infrastructure",
        "Transport & Logistics",
        "Airports",
        "Roads",
        "Mining Services",
        "Integrated Resource Management",
        "Copper",
        "Solar Manufacturing",
        "Wind Manufacturing",
        "Data Centres",
        "Water Infrastructure",
        "Defence & Aerospace",
        "Food & Consumer Businesses",
    ],

    business_segments=[
        "Airports",
        "Roads",
        "Metro & Rail",
        "Data Centres",
        "Solar Manufacturing",
        "Wind Turbine Manufacturing",
        "Copper",
        "Mining Services",
        "Integrated Resource Management",
        "Water",
        "Defence & Aerospace",
        "Agri / Food Businesses",
        "Digital Businesses",
    ],

    # --------------------------------------------------------
    # Revenue Drivers
    # --------------------------------------------------------

    revenue_drivers=[
        "Airport passenger traffic",
        "Airport cargo traffic",
        "Airport commercial revenue",
        "Road traffic and toll collections",
        "Road infrastructure project execution",
        "Mining service volumes",
        "Integrated resource management volumes",
        "Copper production and realisations",
        "Solar module and cell sales",
        "Wind turbine sales",
        "Data centre capacity and contracted capacity",
        "Water infrastructure projects",
        "Defence and aerospace orders",
        "Food and consumer product demand",
    ],

    # --------------------------------------------------------
    # Cost Drivers
    # --------------------------------------------------------

    cost_drivers=[
        "Energy costs",
        "Electricity costs",
        "Fuel and transportation costs",
        "Commodity input costs",
        "Construction material costs",
        "Copper-related operating costs",
        "Mining operating costs",
        "Logistics costs",
        "Interest and financing costs",
        "Project development costs",
        "Imported equipment costs",
        "Foreign exchange movement",
    ],

    # --------------------------------------------------------
    # Demand Drivers
    # --------------------------------------------------------

    demand_drivers=[
        "Indian infrastructure spending",
        "Economic growth",
        "Passenger traffic growth",
        "Cargo growth",
        "Industrial activity",
        "Construction activity",
        "Mining demand",
        "Metal demand",
        "Renewable energy investment",
        "Data consumption growth",
        "Digital infrastructure demand",
        "Government infrastructure projects",
        "Defence spending",
        "Energy-transition investment",
    ],

    # --------------------------------------------------------
    # Supply Chain
    # --------------------------------------------------------

    supply_chain_links=[
        "Energy",
        "Electricity",
        "Fuel",
        "Metals",
        "Construction materials",
        "Mining resources",
        "Ports and logistics",
        "Road infrastructure",
        "Industrial equipment",
        "Solar manufacturing inputs",
        "Wind turbine manufacturing inputs",
        "Data centre infrastructure",
    ],

    # --------------------------------------------------------
    # DIRECT / INDIRECT MARKET RELATIONSHIPS
    # --------------------------------------------------------

    direct_markets=[
        "NIFTY 50",
        "Copper",
        "Electricity",
    ],

    indirect_markets=[
        "Crude Oil",
        "Gold",
        "Silver",
        "Natural Gas",
        "Aluminium",
        "Zinc",
    ],

    # ========================================================
    # 4. NINE MARKET CHARACTERS
    # ========================================================

    market_characters={

        "NIFTY 50": MarketCharacter(

            name="NIFTY 50",

            relationship_type="Market Benchmark / Systematic Risk",

            business_path=[
                "NIFTY movement",
                "Indian market sentiment",
                "Liquidity and risk appetite",
                "Infrastructure-sector valuation",
                "ADANIENT stock response",
            ],

            what_to_measure=[
                "Daily return correlation",
                "Beta",
                "Relative strength",
                "Rolling correlation",
                "Market-regime behaviour",
                "Downside sensitivity",
                "Lag relationship",
            ],
        ),

        "Crude Oil": MarketCharacter(

            name="Crude Oil",

            relationship_type="Indirect Energy / Logistics / Macro Relationship",

            business_path=[
                "Crude price",
                "Fuel and transportation economics",
                "Logistics and operating costs",
                "Inflation / macro conditions",
                "Infrastructure and industrial activity",
                "ADANIENT response",
            ],

            what_to_measure=[
                "Crude return vs ADANIENT return",
                "Lagged crude impact",
                "Rolling relationship",
                "Volatility relationship",
                "NIFTY-controlled relationship",
                "News-confirmed commodity events",
            ],
        ),

        "Gold": MarketCharacter(

            name="Gold",

            relationship_type="Macro / Risk Sentiment Relationship",

            business_path=[
                "Gold movement",
                "Risk sentiment",
                "Currency / liquidity conditions",
                "Macro risk environment",
                "Indian equity sentiment",
                "ADANIENT response",
            ],

            what_to_measure=[
                "Gold return relationship",
                "Risk-off periods",
                "Rolling correlation",
                "Lag relationship",
                "Volatility relationship",
                "Relationship after controlling NIFTY",
            ],
        ),

        "Silver": MarketCharacter(

            name="Silver",

            relationship_type="Industrial Metals / Precious Metals Relationship",

            business_path=[
                "Silver price",
                "Industrial-demand expectations",
                "Precious-metal sentiment",
                "Commodity-cycle conditions",
                "Infrastructure / industrial sentiment",
                "ADANIENT response",
            ],

            what_to_measure=[
                "Silver return relationship",
                "Industrial-cycle relationship",
                "Rolling correlation",
                "Lagged impact",
                "Volatility relationship",
                "Cross-metal interaction",
            ],
        ),

        "Natural Gas": MarketCharacter(

            name="Natural Gas",

            relationship_type="Energy / Industrial Input Relationship",

            business_path=[
                "Natural gas price",
                "Energy economics",
                "Industrial input costs",
                "Energy-transition conditions",
                "Inflation / macro conditions",
                "ADANIENT response",
            ],

            what_to_measure=[
                "Natural gas return relationship",
                "Energy-cost relationship",
                "Lag impact",
                "Rolling relationship",
                "Volatility relationship",
                "NIFTY-controlled relationship",
            ],
        ),

        "Copper": MarketCharacter(

            name="Copper",

            relationship_type="Industrial Metal / Direct Business Relationship",

            business_path=[
                "Copper price",
                "Copper market economics",
                "Copper business revenue / realisation",
                "Industrial demand",
                "Infrastructure demand",
                "ADANIENT earnings expectations",
                "ADANIENT stock response",
            ],

            what_to_measure=[
                "Copper return sensitivity",
                "Copper beta",
                "Rolling copper relationship",
                "Lagged copper impact",
                "Copper volatility relationship",
                "Copper-event response",
                "Relationship after controlling NIFTY",
            ],
        ),

        "Aluminium": MarketCharacter(

            name="Aluminium",

            relationship_type="Industrial Metal / Indirect Cost-Demand Relationship",

            business_path=[
                "Aluminium price",
                "Industrial metal cycle",
                "Infrastructure demand",
                "Manufacturing economics",
                "Material/input conditions",
                "ADANIENT business sentiment",
                "ADANIENT response",
            ],

            what_to_measure=[
                "Aluminium return relationship",
                "Rolling relationship",
                "Lag impact",
                "Industrial-cycle relationship",
                "Volatility relationship",
                "Cross-metal relationship",
            ],
        ),

        "Zinc": MarketCharacter(

            name="Zinc",

            relationship_type="Industrial Metal / Infrastructure Demand Relationship",

            business_path=[
                "Zinc price",
                "Industrial metal cycle",
                "Construction and infrastructure demand",
                "Galvanising / downstream industrial activity",
                "Infrastructure sentiment",
                "ADANIENT response",
            ],

            what_to_measure=[
                "Zinc return relationship",
                "Rolling relationship",
                "Lag impact",
                "Metals-cycle relationship",
                "Volatility relationship",
                "Cross-metal interaction",
            ],
        ),

        "Electricity": MarketCharacter(

            name="Electricity",

            relationship_type="Operational Energy / Infrastructure Relationship",

            business_path=[
                "Electricity price / availability",
                "Operating energy economics",
                "Data-centre energy requirements",
                "Industrial operating costs",
                "Infrastructure project economics",
                "Energy-transition conditions",
                "ADANIENT response",
            ],

            what_to_measure=[
                "Electricity price relationship",
                "Energy-cost relationship",
                "Availability / supply events",
                "Lag impact",
                "Rolling relationship",
                "Volatility relationship",
                "Energy-event response",
            ],
        ),
    },

    # ========================================================
    # 5. COMPANY EVENTS
    # ========================================================

    company_events_to_track=[

        "Quarterly results",

        "Annual results",

        "EBITDA changes",

        "Profit changes",

        "Debt changes",

        "Fund raising",

        "QIP / equity issuance",

        "NCD / debt issuance",

        "Large capital expenditure",

        "Airport developments",

        "Airport passenger / cargo changes",

        "Road project awards",

        "Road project completion",

        "Toll commencement",

        "Mining contract awards",

        "Mining production changes",

        "Integrated resource management volume changes",

        "Copper production changes",

        "Copper capacity expansion",

        "Solar manufacturing capacity changes",

        "Wind manufacturing capacity changes",

        "Data centre capacity / order changes",

        "Defence / aerospace orders",

        "Water project developments",

        "Acquisitions",

        "Divestments",

        "Demerger / restructuring",

        "Regulatory developments",

        "Legal developments",

        "Credit rating changes",

        "Promoter / shareholding changes",

        "Material corporate announcements",
    ],

    # ========================================================
    # 6. NEWS CHARACTER
    # ========================================================

    news_categories=[

        "Company news",

        "Exchange announcements",

        "Quarterly results",

        "Earnings guidance",

        "Large orders",

        "Project awards",

        "Project completion",

        "Infrastructure policy",

        "Government policy",

        "Commodity news",

        "Mining news",

        "Copper news",

        "Energy news",

        "Renewable energy news",

        "Airport news",

        "Road and highway news",

        "Data centre news",

        "Defence news",

        "Regulatory news",

        "Legal news",

        "Credit / debt news",

        "Global macro news",

        "India macro news",

        "Sector news",
    ],

    # ========================================================
    # 7. INDICATORS
    # ========================================================

    indicators_to_measure=[

        "Price return",

        "Gap",

        "Intraday range",

        "ATR",

        "Realised volatility",

        "Volume",

        "Relative volume",

        "VWAP where intraday data is available",

        "RSI",

        "MACD",

        "Moving averages",

        "Trend strength",

        "Momentum",

        "Support / resistance",

        "Relative strength versus NIFTY",

        "Beta",

        "Rolling correlation",

    ],

    # ========================================================
    # 8. TIMEFRAMES
    # ========================================================

    timeframes_to_measure=[

        "5m",

        "15m",

        "30m",

        "1H",

        "2H",

        "4H",

        "1D",

        "1W",

        "1M",

    ],

    # ========================================================
    # 9. CALCULATION RULES
    # ========================================================

    calculation_rules=[

        "Never use a fixed market linkage score.",

        "Calculate relationships from historical market data.",

        "Use returns rather than raw price levels for correlation analysis.",

        "Calculate rolling relationships to detect changing behaviour.",

        "Calculate lagged relationships between each market and ADANIENT.",

        "Measure relative strength against NIFTY 50.",

        "Control for NIFTY 50 before treating a commodity relationship as company-specific.",

        "Separate direct business exposure from indirect macro exposure.",

        "Use volume to confirm unusually strong price movements.",

        "Compare large stock movements with company news and announcements.",

        "Do not treat correlation as proof of causation.",

        "Record conflicting evidence instead of forcing one explanation.",

        "Use data freshness as part of the research result.",

        "Keep company character separate from calculated market impact.",

        "All impact scores must be generated dynamically from data.",
    ],
)


# ============================================================
# 10. PUBLIC ACCESS FUNCTIONS
# ============================================================

def get_company_character() -> CompanyCharacter:
    """
    Return the complete ADANIENT company character.
    """
    return ADANIENT_CHARACTER


def get_market_character(market: str) -> MarketCharacter:
    """
    Return the character definition for one of the 9 markets.
    """

    if market not in ADANIENT_CHARACTER.market_characters:
        raise KeyError(
            f"Unknown market: {market}. "
            f"Available markets: "
            f"{list(ADANIENT_CHARACTER.market_characters.keys())}"
        )

    return ADANIENT_CHARACTER.market_characters[market]


def get_all_markets() -> List[str]:
    """
    Return the exact 9 markets used by ADANIENT.
    """
    return list(ADANIENT_CHARACTER.market_characters.keys())


def get_company_summary() -> Dict:
    """
    Compact company character summary.
    """

    return {
        "symbol": ADANIENT_CHARACTER.symbol,
        "company_name": ADANIENT_CHARACTER.company_name,
        "primary_character": ADANIENT_CHARACTER.primary_character,
        "industries": ADANIENT_CHARACTER.industries,
        "business_segments": ADANIENT_CHARACTER.business_segments,
        "direct_markets": ADANIENT_CHARACTER.direct_markets,
        "indirect_markets": ADANIENT_CHARACTER.indirect_markets,
        "markets": get_all_markets(),
    }


# ============================================================
# 11. BASIC VALIDATION
# ============================================================

EXPECTED_MARKETS = {
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


def validate_character() -> bool:
    """
    Validate that all 9 required markets exist.
    """

    actual = set(ADANIENT_CHARACTER.market_characters.keys())

    missing = EXPECTED_MARKETS - actual
    extra = actual - EXPECTED_MARKETS

    if missing:
        raise ValueError(f"Missing markets: {sorted(missing)}")

    if extra:
        raise ValueError(f"Unexpected markets: {sorted(extra)}")

    if len(actual) != 9:
        raise ValueError(
            f"Expected 9 markets, found {len(actual)}"
        )

    return True


if __name__ == "__main__":

    validate_character()

    print("=" * 60)
    print("ADANIENT COMPANY CHARACTER")
    print("=" * 60)

    print(f"Symbol       : {ADANIENT_CHARACTER.symbol}")
    print(f"Company      : {ADANIENT_CHARACTER.company_name}")
    print()
    print("Markets:")

    for market in get_all_markets():
        character = get_market_character(market)
        print(f"  - {market}")
        print(f"    Relationship : {character.relationship_type}")

    print()
    print("Character validation: PASSED")
