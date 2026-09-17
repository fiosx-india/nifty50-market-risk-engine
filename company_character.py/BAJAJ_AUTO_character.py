"""
BAJAJ-AUTO — Company Character Definition
=========================================

NIFTY 50 Market Risk Engine

Company:
    Bajaj Auto Limited

Purpose:
    Define Bajaj Auto's business character and its relationship with
    the project's 9 research markets.

The supplied CSV may contain RANK, PCT_CHANGE, LINKAGE_SCORE and RELATION.
Those are treated only as historical/snapshot fields and are NOT embedded
as permanent truth.

This module contains:
    - Company character
    - Business segments
    - Operating model
    - Revenue drivers
    - Cost drivers
    - Demand drivers
    - Supply-chain relationships
    - Sector relationships
    - 9 market characters
    - Indicators
    - Important events
    - Timeframes
    - Historical calculation rules

It intentionally contains no fixed:
    - linkage score
    - percentage impact
    - rank
    - prediction
    - BUY/SELL decision

All relationships must be calculated from real historical/live data.
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
# 3. BAJAJ AUTO COMPANY CHARACTER
# ============================================================

BAJAJ_AUTO_CHARACTER = CompanyCharacter(

    symbol="BAJAJ-AUTO",

    company_name="Bajaj Auto Limited",

    company_character=(
        "Diversified two-wheeler and three-wheeler mobility manufacturer "
        "with a strong domestic and export franchise across motorcycles, "
        "commercial three-wheelers and electric mobility. Its character is "
        "driven by vehicle volumes, product mix, premium motorcycles, "
        "commercial-vehicle demand, electric two- and three-wheelers, "
        "exports, foreign-exchange conditions, raw-material costs, "
        "commodity inputs, supply-chain availability, financing availability "
        "and consumer/business mobility demand."
    ),

    # ========================================================
    # CORE BUSINESSES
    # ========================================================

    primary_businesses=[
        "Motorcycles",
        "Premium motorcycles",
        "125cc+ motorcycles",
        "Pulsar",
        "CT and commuter motorcycles",
        "Dominar",
        "KTM motorcycles",
        "Triumph motorcycles",
        "Chetak electric scooters",
        "Electric two-wheelers",
        "ICE three-wheelers",
        "Electric three-wheelers",
        "E-rickshaws",
        "Commercial vehicles",
        "Passenger three-wheelers",
        "Goods-carrier three-wheelers",
        "Spare parts",
        "International vehicle exports",
        "Vehicle financing through group financing ecosystem",
    ],

    # ========================================================
    # OPERATING MODEL
    # ========================================================

    operating_model=[
        "Vehicle product design",
        "Automotive engineering",
        "Motorcycle manufacturing",
        "Three-wheeler manufacturing",
        "Electric vehicle manufacturing",
        "Battery and EV technology integration",
        "Supplier ecosystem",
        "Dealer and service network",
        "Export distribution",
        "Brand-led premiumisation",
        "After-sales service",
        "Spare-parts business",
        "Domestic retail distribution",
        "International market distribution",
        "Vehicle financing ecosystem",
    ],

    # ========================================================
    # REVENUE DRIVERS
    # ========================================================

    revenue_drivers=[
        "Two-wheeler volumes",
        "Motorcycle volumes",
        "Premium motorcycle volumes",
        "125cc+ motorcycle demand",
        "Three-wheeler volumes",
        "Commercial-vehicle volumes",
        "Electric two-wheeler volumes",
        "Electric three-wheeler volumes",
        "E-rickshaw volumes",
        "Average selling price",
        "Product mix",
        "Premiumisation",
        "Export volumes",
        "Export realisations",
        "Foreign-exchange realisation",
        "Spare-parts revenue",
        "After-sales activity",
        "New product launches",
        "Market-share gains",
    ],

    # ========================================================
    # COST DRIVERS
    # ========================================================

    cost_drivers=[
        "Aluminium",
        "Steel",
        "Copper",
        "Zinc",
        "Rubber",
        "Plastics",
        "Battery materials",
        "Rare-earth materials",
        "Electronic components",
        "Semiconductors",
        "Energy and electricity",
        "Natural gas and industrial energy",
        "Freight",
        "Logistics",
        "Employee costs",
        "Warranty costs",
        "R&D expenditure",
        "Marketing expenditure",
        "Export logistics",
        "Foreign-exchange movement",
        "Capital expenditure",
    ],

    # ========================================================
    # DEMAND DRIVERS
    # ========================================================

    demand_drivers=[
        "Household income",
        "Rural income",
        "Urban income",
        "Employment",
        "Consumer confidence",
        "Two-wheeler affordability",
        "Vehicle financing availability",
        "Interest rates",
        "Fuel prices",
        "GST and taxation",
        "Festive demand",
        "Replacement demand",
        "New vehicle demand",
        "Commercial mobility demand",
        "Last-mile transportation demand",
        "Small-business activity",
        "Infrastructure activity",
        "Export-market economic conditions",
        "Currency conditions",
        "EV adoption",
        "Charging infrastructure",
        "Government EV policy",
        "Emission regulations",
    ],

    # ========================================================
    # SUPPLY-CHAIN LINKS
    # ========================================================

    supply_chain_links=[
        "Steel suppliers",
        "Aluminium suppliers",
        "Copper suppliers",
        "Zinc suppliers",
        "Rubber suppliers",
        "Plastic suppliers",
        "Battery suppliers",
        "Rare-earth suppliers",
        "Semiconductor suppliers",
        "Electronic-component suppliers",
        "Tyre manufacturers",
        "Auto-component manufacturers",
        "Powertrain suppliers",
        "EV component suppliers",
        "Logistics providers",
        "Ports and shipping",
        "Dealers",
        "Service centres",
        "Financing partners",
        "Export distributors",
        "Charging ecosystem",
    ],

    # ========================================================
    # SECTOR LINKS
    # ========================================================

    sector_links=[
        "Automobiles",
        "Two-wheelers",
        "Three-wheelers",
        "Electric vehicles",
        "Commercial vehicles",
        "Auto components",
        "Steel",
        "Aluminium",
        "Copper",
        "Zinc",
        "Rubber",
        "Battery ecosystem",
        "Consumer discretionary",
        "Rural consumption",
        "Urban consumption",
        "Logistics",
        "Exports",
        "Mobility",
        "Infrastructure",
        "Small-business economy",
        "Vehicle finance",
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
                "Broad Indian equity-market and systematic-risk environment "
                "affecting liquidity, institutional flows, consumer confidence "
                "and valuation multiples."
            ),

            exposure_character=(
                "Primary systematic-market relationship"
            ),

            impact_path=(
                "NIFTY movement → market liquidity / risk appetite / "
                "consumer and investment sentiment → BAJAJ-AUTO valuation "
                "and stock behaviour"
            ),

            calculation_logic=(
                "Calculate return correlation, beta, rolling beta, relative "
                "strength, downside sensitivity and lag response. Compare "
                "against Auto-sector and relevant benchmark indices. Separate "
                "systematic movement from company-specific sales and product events."
            ),
        ),

        # ----------------------------------------------------
        # 2. CRUDE OIL
        # ----------------------------------------------------

        "Crude Oil": MarketCharacter(

            market="Crude Oil",

            character=(
                "Global energy commodity with an important demand-side link "
                "through fuel prices and an indirect cost link through "
                "petrochemical, plastic, synthetic-rubber and logistics inputs."
            ),

            exposure_character=(
                "Direct mobility-demand + indirect raw-material/logistics relationship"
            ),

            impact_path=(
                "Crude movement → fuel prices / transport economics + "
                "petrochemical input costs → consumer mobility demand / "
                "vehicle operating economics / margins → BAJAJ-AUTO"
            ),

            calculation_logic=(
                "Separate demand effects from cost effects. Test crude returns "
                "against vehicle volumes, two-wheeler demand, commercial-vehicle "
                "demand, margins and stock returns. Use lagged effects and "
                "control for NIFTY, interest rates and seasonal demand."
            ),
        ),

        # ----------------------------------------------------
        # 3. GOLD
        # ----------------------------------------------------

        "Gold": MarketCharacter(

            market="Gold",

            character=(
                "Precious-metal and macro-risk asset reflecting real rates, "
                "currency conditions, liquidity, household savings behaviour "
                "and risk sentiment."
            ),

            exposure_character=(
                "Indirect macro / household-sentiment relationship"
            ),

            impact_path=(
                "Gold movement → savings / liquidity / risk sentiment / "
                "currency conditions → household spending and investment "
                "environment → vehicle demand / valuation → BAJAJ-AUTO"
            ),

            calculation_logic=(
                "Test whether gold adds explanatory power after controlling "
                "for NIFTY, INR, rates, consumer indicators and commodity "
                "conditions. Do not assume direct gold exposure."
            ),
        ),

        # ----------------------------------------------------
        # 4. SILVER
        # ----------------------------------------------------

        "Silver": MarketCharacter(

            market="Silver",

            character=(
                "Precious and industrial metal reflecting industrial activity, "
                "commodity inflation and global growth."
            ),

            exposure_character=(
                "Indirect industrial-cycle / commodity-cost relationship"
            ),

            impact_path=(
                "Silver cycle → industrial activity / commodity inflation → "
                "vehicle supply chain and consumer/business conditions → "
                "BAJAJ-AUTO"
            ),

            calculation_logic=(
                "Measure silver returns, rolling correlation and lag response "
                "against vehicle volumes, margins and stock returns. Control "
                "for NIFTY and related industrial metals."
            ),
        ),

        # ----------------------------------------------------
        # 5. NATURAL GAS
        # ----------------------------------------------------

        "Natural Gas": MarketCharacter(

            market="Natural Gas",

            character=(
                "Energy commodity affecting industrial energy costs, "
                "manufacturing economics and broader inflation."
            ),

            exposure_character=(
                "Indirect manufacturing-cost / macro relationship"
            ),

            impact_path=(
                "Natural gas movement → factory energy costs / inflation → "
                "manufacturing economics + consumer purchasing power → "
                "BAJAJ-AUTO"
            ),

            calculation_logic=(
                "Test gas returns against manufacturing margins, industrial "
                "activity and stock returns. Use lagged analysis and distinguish "
                "actual energy-cost exposure from broad energy sentiment."
            ),
        ),

        # ----------------------------------------------------
        # 6. COPPER
        # ----------------------------------------------------

        "Copper": MarketCharacter(

            market="Copper",

            character=(
                "Industrial metal important to electrical systems, wiring, "
                "motors, electronics, EV components and manufacturing activity."
            ),

            exposure_character=(
                "Direct component/input-cost + industrial-cycle relationship"
            ),

            impact_path=(
                "Copper movement → component/material costs + industrial "
                "cycle → vehicle production economics / demand → BAJAJ-AUTO"
            ),

            calculation_logic=(
                "Measure copper returns against input-cost proxies, gross "
                "margin, production volumes and stock returns. Use lagged "
                "effects because procurement contracts and inventory can delay "
                "cost transmission."
            ),
        ),

        # ----------------------------------------------------
        # 7. ALUMINIUM
        # ----------------------------------------------------

        "Aluminium": MarketCharacter(

            market="Aluminium",

            character=(
                "Major automotive industrial metal used across vehicle "
                "components and lightweighting applications, while also "
                "reflecting manufacturing and transport cycles."
            ),

            exposure_character=(
                "Direct raw-material/component-cost + automotive-cycle relationship"
            ),

            impact_path=(
                "Aluminium price → vehicle component/material costs → "
                "manufacturing cost / gross margin → BAJAJ-AUTO earnings "
                "and valuation"
            ),

            calculation_logic=(
                "Calculate aluminium-return relationship with raw-material "
                "cost proxies, gross margin, EBITDA margin, vehicle volumes "
                "and stock returns. Test lagged pass-through and control for "
                "NIFTY and broader auto demand."
            ),
        ),

        # ----------------------------------------------------
        # 8. ZINC
        # ----------------------------------------------------

        "Zinc": MarketCharacter(

            market="Zinc",

            character=(
                "Industrial metal used in galvanising and selected automotive "
                "and component supply chains, also reflecting manufacturing activity."
            ),

            exposure_character=(
                "Direct/indirect component-cost + industrial-cycle relationship"
            ),

            impact_path=(
                "Zinc movement → component/material cost + industrial activity "
                "→ vehicle manufacturing economics / supplier costs → BAJAJ-AUTO"
            ),

            calculation_logic=(
                "Measure zinc returns against relevant material-cost proxies, "
                "supplier conditions, margins and vehicle production. Use "
                "rolling and lagged analysis and avoid assuming all zinc-price "
                "movement reaches the company immediately."
            ),
        ),

        # ----------------------------------------------------
        # 9. ELECTRICITY
        # ----------------------------------------------------

        "Electricity": MarketCharacter(

            market="Electricity",

            character=(
                "Important manufacturing input for vehicle plants, machining, "
                "assembly, battery/EV operations, warehouses and technology systems."
            ),

            exposure_character=(
                "Direct manufacturing-energy-cost relationship"
            ),

            impact_path=(
                "Electricity price / availability → plant operating costs + "
                "production continuity → manufacturing economics / margins "
                "→ BAJAJ-AUTO"
            ),

            calculation_logic=(
                "Where reliable regional electricity data exists, measure "
                "price, volatility and availability against production, "
                "operating costs and margins. Account for plant geography, "
                "energy efficiency and renewable-energy usage where data exists."
            ),
        ),
    },

    # ========================================================
    # IMPORTANT INDICATORS
    # ========================================================

    important_indicators=[

        # Sales
        "Two-wheeler volumes",
        "Motorcycle volumes",
        "125cc+ volumes",
        "Premium motorcycle volumes",
        "Three-wheeler volumes",
        "Commercial-vehicle volumes",
        "Electric two-wheeler volumes",
        "Electric three-wheeler volumes",
        "E-rickshaw volumes",
        "Domestic volumes",
        "Export volumes",
        "Market share",

        # Products
        "Pulsar volumes",
        "Chetak volumes",
        "KTM volumes",
        "Triumph volumes",
        "Commercial-vehicle mix",
        "EV mix",
        "Premium mix",
        "New product contribution",

        # Financial
        "Revenue",
        "EBITDA",
        "EBITDA margin",
        "PAT",
        "Gross margin",
        "Operating leverage",
        "Free cash flow",
        "Working capital",
        "Inventory days",
        "Receivable days",
        "Surplus cash",

        # Costs
        "Aluminium price",
        "Copper price",
        "Zinc price",
        "Steel price",
        "Rubber price",
        "Battery-material prices",
        "Rare-earth prices",
        "Crude Oil",
        "Natural Gas",
        "Electricity",

        # Demand
        "Fuel prices",
        "Consumer confidence",
        "Rural demand",
        "Urban demand",
        "Vehicle financing",
        "Interest rates",
        "GST",
        "Festive demand",

        # Export
        "INR/USD",
        "Export volumes",
        "Export revenue",
        "LATAM demand",
        "Africa demand",
        "South Asia demand",
        "International dealer network",

        # Market
        "NIFTY 50",
        "Auto-sector relative return",
        "Trading volume",
        "Relative volume",
        "Volatility",
        "Relative strength",
    ],

    # ========================================================
    # IMPORTANT EVENTS
    # ========================================================

    important_events=[

        "Monthly vehicle sales",
        "Quarterly results",
        "Annual results",
        "Annual report",
        "New motorcycle launches",
        "New premium motorcycle launches",
        "Pulsar launches",
        "Chetak launches",
        "New electric scooter launches",
        "New electric three-wheeler launches",
        "New e-rickshaw launches",
        "Commercial-vehicle launches",
        "Price changes",
        "Discount changes",
        "Production changes",
        "Factory expansion",
        "New manufacturing capacity",
        "Supplier disruptions",
        "Semiconductor shortages",
        "Rare-earth supply disruptions",
        "Battery supply disruptions",
        "Export-market disruptions",
        "Currency shocks",
        "Trade restrictions",
        "Import/export policy",
        "GST changes",
        "EV policy changes",
        "Emission regulations",
        "Fuel-price changes",
        "Interest-rate changes",
        "Vehicle-finance changes",
        "Government mobility policy",
        "Infrastructure policy",
        "Major dealer-network changes",
        "Strategic partnerships",
        "KTM developments",
        "Triumph developments",
        "Chetak developments",
        "Major litigation or regulatory events",
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

        "Calculate all relationships from actual historical observations.",

        "Treat aluminium as an important automotive material-cost variable, "
        "but verify its actual historical transmission into margins.",

        "Treat copper as both an input-cost variable and an industrial/EV-cycle signal.",

        "Treat zinc as a component/material and industrial-cycle variable.",

        "Treat crude oil through both fuel-demand and petrochemical/logistics "
        "channels; do not assume the effect has one direction in every regime.",

        "Separate domestic demand from export demand.",

        "Separate ICE vehicle economics from EV vehicle economics.",

        "Separate two-wheeler demand from commercial three-wheeler demand.",

        "Separate price/mix effects from volume effects.",

        "Use FX variables for export analysis because export revenue and "
        "profitability can respond differently to currency movement.",

        "Use lagged commodity variables because procurement contracts, "
        "inventory and price pass-through can delay the impact.",

        "Use rolling windows to detect regime changes.",

        "Control for NIFTY 50 and Auto-sector movement when testing individual markets.",

        "Use monthly sales data for high-frequency fundamental validation.",

        "Use event studies around launches, monthly sales, commodity shocks "
        "and company announcements.",

        "Use volume confirmation for stock-price reactions.",

        "Do not assume correlation means causation.",

        "Track source quality and data freshness.",

        "Do not make final BUY/SELL decisions inside this character module.",

        "Pass calculated evidence to the central research and decision layer.",
    ],
)


# ============================================================
# 4. PUBLIC FUNCTIONS
# ============================================================

def get_company_character() -> CompanyCharacter:
    """Return the complete Bajaj Auto company character."""
    return BAJAJ_AUTO_CHARACTER


def get_market_character(market: str) -> MarketCharacter:
    """Return one of the 9 market characters."""

    key = market.strip()

    if key not in BAJAJ_AUTO_CHARACTER.markets:
        raise KeyError(
            f"Unsupported market '{market}'. "
            f"Supported markets: "
            f"{', '.join(BAJAJ_AUTO_CHARACTER.markets)}"
        )

    return BAJAJ_AUTO_CHARACTER.markets[key]


def get_all_markets() -> Dict[str, MarketCharacter]:
    """Return all 9 market characters."""
    return dict(BAJAJ_AUTO_CHARACTER.markets)


def get_company_summary() -> dict:
    """Return a compact machine-readable company summary."""

    return {
        "symbol": BAJAJ_AUTO_CHARACTER.symbol,
        "company_name": BAJAJ_AUTO_CHARACTER.company_name,
        "company_character": BAJAJ_AUTO_CHARACTER.company_character,
        "primary_businesses": list(
            BAJAJ_AUTO_CHARACTER.primary_businesses
        ),
        "sector_links": list(
            BAJAJ_AUTO_CHARACTER.sector_links
        ),
        "market_count": len(
            BAJAJ_AUTO_CHARACTER.markets
        ),
        "markets": list(
            BAJAJ_AUTO_CHARACTER.markets.keys()
        ),
    }


def validate_character() -> bool:
    """
    Validate structure only.

    This does not prove historical correlation, causation or prediction accuracy.
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
        BAJAJ_AUTO_CHARACTER.markets.keys()
    )

    if actual_markets != expected_markets:

        missing = expected_markets - actual_markets
        extra = actual_markets - expected_markets

        raise ValueError(
            "Market character validation failed. "
            f"Missing={sorted(missing)}, "
            f"Extra={sorted(extra)}"
        )

    if BAJAJ_AUTO_CHARACTER.symbol != "BAJAJ-AUTO":
        raise ValueError("Invalid company symbol.")

    for market_name, market in (
        BAJAJ_AUTO_CHARACTER.markets.items()
    ):

        if not all([
            market.market,
            market.character,
            market.exposure_character,
            market.impact_path,
            market.calculation_logic,
        ]):
            raise ValueError(
                f"Incomplete market character: {market_name}"
            )

    return True


# ============================================================
# 5. DIRECT EXECUTION TEST
# ============================================================

if __name__ == "__main__":

    validate_character()

    print("BAJAJ-AUTO Character: VALID")
    print(
        f"Company: {BAJAJ_AUTO_CHARACTER.company_name}"
    )

    print(
        f"Markets: {len(BAJAJ_AUTO_CHARACTER.markets)}"
    )

    for name, market in BAJAJ_AUTO_CHARACTER.markets.items():

        print(
            f"- {name}: "
            f"{market.exposure_character}"
        )
