"""
BAJAJFINSV — Company Character Definition
=========================================

NIFTY 50 Market Risk Engine

Company:
    Bajaj Finserv Limited

Purpose:
    Define the company's business character and its relationship with
    the 9 research markets used by this project.

IMPORTANT
---------
The original CSV may contain:
    RANK
    PCT_CHANGE
    LINKAGE_SCORE
    RELATION

Those values are historical/snapshot fields and are NOT used as permanent
company-character truth.

This module contains:
    Company Character
    Business Structure
    Revenue Drivers
    Cost / Risk Drivers
    Demand Drivers
    Financial Ecosystem
    Sector Links
    9 Market Characters
    Indicators
    Events
    Timeframes
    Historical Calculation Rules

It does NOT contain fixed:
    scores
    correlations
    percentages
    rankings
    BUY/SELL decisions

Those must be calculated later from real data.
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
# 3. BAJAJ FINSERV COMPANY CHARACTER
# ============================================================

BAJAJFINSV_CHARACTER = CompanyCharacter(

    symbol="BAJAJFINSV",

    company_name="Bajaj Finserv Limited",

    company_character=(
        "Diversified financial-services holding and operating platform built "
        "around consumer and retail finance, housing finance, general and "
        "life insurance, investments, asset management, securities, digital "
        "financial marketplaces and health-tech. Its economic character is "
        "driven by credit demand, assets under management, loan growth, "
        "funding costs, asset quality, insurance premiums, investment flows, "
        "interest rates, liquidity, consumer income and the broader Indian "
        "financial cycle."
    ),

    # ========================================================
    # CORE BUSINESSES
    # ========================================================

    primary_businesses=[
        "Consumer finance",
        "Retail lending",
        "Commercial and SME finance",
        "Housing finance",
        "Mortgage finance",
        "General insurance",
        "Health insurance",
        "Life insurance",
        "Retirement and annuity products",
        "Asset management",
        "Mutual funds",
        "Digital financial marketplace",
        "Digital technology services",
        "Stock broking",
        "Demat and investment services",
        "Margin trade financing",
        "Health-tech services",
        "Investment and alternative assets",
    ],

    # ========================================================
    # OPERATING MODEL
    # ========================================================

    operating_model=[
        "Financial-services holding structure",
        "Consumer and retail lending",
        "Housing and mortgage finance",
        "SME and commercial finance",
        "Insurance underwriting",
        "Insurance distribution",
        "Investment and wealth products",
        "Asset management",
        "Digital financial marketplace",
        "Digital stockbroking",
        "Health-tech platform",
        "Technology-enabled customer acquisition",
        "Cross-selling across financial lifecycle needs",
        "Pan-India distribution",
        "Data and analytics driven underwriting",
        "Digital-first customer journeys",
    ],

    # ========================================================
    # REVENUE DRIVERS
    # ========================================================

    revenue_drivers=[
        "Loan book growth",
        "Assets under management",
        "Net interest income from financing businesses",
        "Net interest margin",
        "Fee income",
        "Consumer finance volumes",
        "Home finance volumes",
        "SME and commercial finance",
        "Insurance gross written premium",
        "Insurance renewal income",
        "Insurance underwriting results",
        "Life insurance premium",
        "Value of new business",
        "Asset-management fees",
        "Mutual-fund AUM",
        "Broking income",
        "Demat and securities activity",
        "Margin financing",
        "Digital marketplace commissions",
        "Technology-services revenue",
        "Health-tech transactions",
        "Investment income",
    ],

    # ========================================================
    # COST / RISK DRIVERS
    # ========================================================

    cost_drivers=[
        "Cost of funds",
        "Interest expense",
        "Deposit and borrowing rates",
        "Credit losses",
        "Loan-loss provisions",
        "Asset-quality deterioration",
        "Insurance claims",
        "Claims ratio",
        "Insurance acquisition costs",
        "Employee costs",
        "Technology expenditure",
        "Cybersecurity expenditure",
        "Digital infrastructure",
        "Distribution costs",
        "Compliance costs",
        "Regulatory capital requirements",
        "Liquidity costs",
        "Marketing expenditure",
        "Customer acquisition costs",
        "Investment-market volatility",
    ],

    # ========================================================
    # DEMAND DRIVERS
    # ========================================================

    demand_drivers=[
        "Indian GDP growth",
        "Household income",
        "Employment",
        "Consumer confidence",
        "Consumer discretionary spending",
        "Housing demand",
        "Real-estate activity",
        "Vehicle demand",
        "Consumer electronics demand",
        "Digital-commerce activity",
        "SME activity",
        "Corporate investment",
        "Infrastructure investment",
        "Insurance penetration",
        "Health-insurance demand",
        "Life-insurance demand",
        "Retirement planning",
        "Savings rate",
        "Investment participation",
        "Equity-market participation",
        "Digital-payment adoption",
        "Financial inclusion",
        "Interest-rate environment",
    ],

    # ========================================================
    # FINANCIAL ECOSYSTEM LINKS
    # ========================================================

    supply_chain_links=[
        "Retail borrowers",
        "SME borrowers",
        "Corporate customers",
        "Home buyers",
        "Vehicle buyers",
        "Consumer durable customers",
        "Insurance policyholders",
        "Insurance agents",
        "Bancassurance and distribution partners",
        "Hospitals and healthcare providers",
        "Financial-market infrastructure",
        "Stock exchanges",
        "Depositories",
        "Mutual-fund ecosystem",
        "Asset managers",
        "Credit bureaus",
        "Banks and funding partners",
        "Debt markets",
        "Technology providers",
        "Fintech ecosystem",
        "RBI and financial regulators",
        "IRDAI and insurance regulation",
        "SEBI and capital-market regulation",
    ],

    # ========================================================
    # SECTOR LINKS
    # ========================================================

    sector_links=[
        "Financial services",
        "NBFC",
        "Consumer finance",
        "Housing finance",
        "Mortgage finance",
        "Insurance",
        "Life insurance",
        "General insurance",
        "Health insurance",
        "Asset management",
        "Mutual funds",
        "Stock broking",
        "Capital markets",
        "Digital finance",
        "Fintech",
        "Health-tech",
        "Real estate",
        "Automobile",
        "Consumer discretionary",
        "SME economy",
        "Indian financial cycle",
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
                "affecting liquidity, institutional flows, financial-sector "
                "valuation and investor risk appetite."
            ),

            exposure_character=(
                "Primary systematic-market relationship"
            ),

            impact_path=(
                "NIFTY movement → liquidity / risk appetite / financial-sector "
                "valuation → investment sentiment and BAJAJFINSV stock behaviour"
            ),

            calculation_logic=(
                "Calculate return correlation, beta, rolling beta, relative "
                "strength, downside sensitivity and lag response. Compare "
                "BAJAJFINSV against NIFTY and financial-sector benchmarks. "
                "Separate systematic movement from company/group-specific events."
            ),
        ),

        # ----------------------------------------------------
        # 2. CRUDE OIL
        # ----------------------------------------------------

        "Crude Oil": MarketCharacter(

            market="Crude Oil",

            character=(
                "Global energy commodity influencing Indian inflation, "
                "currency, household purchasing power, transport costs, "
                "corporate margins and monetary-policy expectations."
            ),

            exposure_character=(
                "Indirect macroeconomic / credit-cycle relationship"
            ),

            impact_path=(
                "Crude movement → inflation / INR / interest-rate expectations "
                "→ household and corporate cash flow → credit demand / asset "
                "quality / insurance demand → BAJAJFINSV"
            ),

            calculation_logic=(
                "Test crude returns against BAJAJFINSV returns, inflation, INR, "
                "interest rates, consumer credit and asset-quality indicators. "
                "Use lagged effects and control for NIFTY. Do not treat crude "
                "as a direct operating input."
            ),
        ),

        # ----------------------------------------------------
        # 3. GOLD
        # ----------------------------------------------------

        "Gold": MarketCharacter(

            market="Gold",

            character=(
                "Precious-metal and macro-risk asset connected to real rates, "
                "currency, liquidity, investor risk aversion, household wealth "
                "and savings behaviour."
            ),

            exposure_character=(
                "Indirect macro / wealth / liquidity relationship"
            ),

            impact_path=(
                "Gold movement → risk sentiment / real rates / liquidity / "
                "household wealth behaviour → savings, investment and credit "
                "decisions → BAJAJFINSV businesses"
            ),

            calculation_logic=(
                "Measure gold returns against BAJAJFINSV returns after controlling "
                "for NIFTY, INR, rates and liquidity. Where relevant, examine "
                "links with household savings, investment flows and secured "
                "lending. Do not assume gold price alone drives profitability."
            ),
        ),

        # ----------------------------------------------------
        # 4. SILVER
        # ----------------------------------------------------

        "Silver": MarketCharacter(

            market="Silver",

            character=(
                "Precious and industrial metal reflecting global growth, "
                "commodity inflation and industrial activity."
            ),

            exposure_character=(
                "Indirect macro / industrial-cycle relationship"
            ),

            impact_path=(
                "Silver cycle → industrial growth / inflation / global risk "
                "sentiment → consumer and SME conditions → credit demand / "
                "asset quality → BAJAJFINSV"
            ),

            calculation_logic=(
                "Measure silver returns, rolling correlation, volatility and "
                "lag response against financing activity and stock returns. "
                "Control for NIFTY, gold and macro variables."
            ),
        ),

        # ----------------------------------------------------
        # 5. NATURAL GAS
        # ----------------------------------------------------

        "Natural Gas": MarketCharacter(

            market="Natural Gas",

            character=(
                "Energy commodity affecting industrial costs, electricity "
                "economics, inflation and the financial health of energy-intensive "
                "businesses."
            ),

            exposure_character=(
                "Indirect industrial-credit / macro relationship"
            ),

            impact_path=(
                "Natural gas movement → industrial energy cost / inflation → "
                "SME and corporate cash flow → credit demand / repayment "
                "capacity → BAJAJFINSV"
            ),

            calculation_logic=(
                "Test gas returns against credit growth, SME indicators, "
                "inflation and stock returns. Use lagged relationships and "
                "sector-specific borrower exposure where available."
            ),
        ),

        # ----------------------------------------------------
        # 6. COPPER
        # ----------------------------------------------------

        "Copper": MarketCharacter(

            market="Copper",

            character=(
                "Industrial metal and global growth indicator linked to "
                "manufacturing, electrical infrastructure, construction and "
                "capital expenditure."
            ),

            exposure_character=(
                "Indirect economic-growth / credit-cycle relationship"
            ),

            impact_path=(
                "Copper cycle → industrial / infrastructure / manufacturing "
                "activity → SME and corporate investment → financing demand "
                "and borrower health → BAJAJFINSV"
            ),

            calculation_logic=(
                "Calculate copper-return relationship with credit growth, "
                "industrial indicators and BAJAJFINSV returns. Test leading "
                "and lagged effects and control for NIFTY and interest rates."
            ),
        ),

        # ----------------------------------------------------
        # 7. ALUMINIUM
        # ----------------------------------------------------

        "Aluminium": MarketCharacter(

            market="Aluminium",

            character=(
                "Industrial metal connected to construction, transportation, "
                "manufacturing, infrastructure and consumer durable supply chains."
            ),

            exposure_character=(
                "Indirect industrial / consumer-credit relationship"
            ),

            impact_path=(
                "Aluminium cycle → manufacturing / construction / consumer "
                "durables → business activity and financing demand → "
                "BAJAJFINSV"
            ),

            calculation_logic=(
                "Measure aluminium returns against industrial production, "
                "consumer-durable activity, loan growth and stock returns. "
                "Use rolling and lagged analysis and control for NIFTY."
            ),
        ),

        # ----------------------------------------------------
        # 8. ZINC
        # ----------------------------------------------------

        "Zinc": MarketCharacter(

            market="Zinc",

            character=(
                "Industrial metal associated with galvanising, construction, "
                "infrastructure, manufacturing and economic activity."
            ),

            exposure_character=(
                "Indirect industrial / infrastructure-credit relationship"
            ),

            impact_path=(
                "Zinc cycle → construction / infrastructure / manufacturing "
                "activity → SME/corporate investment → financing demand and "
                "borrower cash flow → BAJAJFINSV"
            ),

            calculation_logic=(
                "Test zinc returns against infrastructure activity, industrial "
                "production, credit growth and BAJAJFINSV returns. Use lagged "
                "analysis and control for NIFTY and related metals."
            ),
        ),

        # ----------------------------------------------------
        # 9. ELECTRICITY
        # ----------------------------------------------------

        "Electricity": MarketCharacter(

            market="Electricity",

            character=(
                "Operating input for digital financial infrastructure and "
                "branches, but more importantly an economic input affecting "
                "the cash flow of electricity-intensive borrowers and SMEs."
            ),

            exposure_character=(
                "Indirect borrower-cost / credit-quality relationship"
            ),

            impact_path=(
                "Electricity price / availability → borrower operating costs "
                "and household/business cash flow → loan demand / repayment "
                "capacity → asset quality → BAJAJFINSV"
            ),

            calculation_logic=(
                "Where reliable regional electricity data exists, measure "
                "price, volatility and availability against credit growth, "
                "SME indicators, asset quality and stock returns. Separate "
                "financial-platform operating costs from borrower-credit effects."
            ),
        ),
    },

    # ========================================================
    # IMPORTANT INDICATORS
    # ========================================================

    important_indicators=[

        # Group-level
        "Consolidated revenue",
        "Consolidated profit",
        "Assets under management",
        "Capital adequacy",
        "Surplus capital",
        "Return on equity",
        "Return on assets",

        # Lending
        "Loan book growth",
        "New loan originations",
        "Disbursement growth",
        "Customer acquisition",
        "Consumer finance growth",
        "Housing finance growth",
        "SME finance growth",
        "Commercial finance growth",
        "Net interest margin",
        "Cost of funds",
        "Credit cost",
        "Gross NPA",
        "Net NPA",
        "Stage 2 loans",
        "Stage 3 loans",
        "Provision coverage",
        "Write-offs",
        "Recoveries",

        # Deposits / funding
        "Deposit growth",
        "Funding mix",
        "Borrowing cost",
        "Liquidity",
        "Capital adequacy",

        # Insurance
        "Gross written premium",
        "Renewal premium",
        "Value of new business",
        "New business margin",
        "Claims ratio",
        "Combined ratio",
        "Persistency",
        "Solvency ratio",
        "Insurance AUM",

        # Investments
        "Asset-management AUM",
        "Mutual-fund flows",
        "Equity-market participation",
        "Broking activity",
        "Demat accounts",
        "Margin financing",

        # Digital businesses
        "Digital marketplace customers",
        "Financial product distribution",
        "Technology-services revenue",
        "Health-tech transactions",
        "Digital engagement",

        # Macro
        "GDP growth",
        "CPI inflation",
        "RBI policy rate",
        "10Y G-Sec yield",
        "INR/USD",
        "Credit growth",
        "Money-market liquidity",
        "Household consumption",

        # Research markets
        "NIFTY 50",
        "Crude Oil",
        "Gold",
        "Silver",
        "Natural Gas",
        "Copper",
        "Aluminium",
        "Zinc",
        "Electricity",

        # Market behaviour
        "Trading volume",
        "Relative volume",
        "Volatility",
        "Relative strength",
        "Financial-sector relative return",
    ],

    # ========================================================
    # IMPORTANT EVENTS
    # ========================================================

    important_events=[

        "Quarterly results",
        "Annual results",
        "Annual report",
        "RBI monetary-policy decisions",
        "RBI regulatory changes",
        "Interest-rate changes",
        "Liquidity changes",
        "Loan-growth updates",
        "Asset-quality updates",
        "Credit-cost changes",
        "Capital-raising events",
        "Insurance regulatory changes",
        "Insurance ownership changes",
        "Insurance product changes",
        "Large acquisitions",
        "Subsidiary restructuring",
        "Housing-finance developments",
        "Digital-platform launches",
        "Technology transformation",
        "Cybersecurity events",
        "Stockbroking developments",
        "Asset-management launches",
        "Mutual-fund regulatory changes",
        "Major capital-market events",
        "Consumer-credit regulations",
        "NBFC regulations",
        "Credit-rating actions",
        "Bond-market stress",
        "Major crude-oil shocks",
        "Global financial stress",
        "Major commodity shocks",
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

        "Calculate market relationships from actual historical observations.",

        "Treat BAJAJFINSV as a diversified financial-services ecosystem, "
        "not as a single lending company.",

        "Separate financing, insurance, asset-management, securities and "
        "digital-platform channels during analysis.",

        "Use interest rates, liquidity, credit growth and asset quality as "
        "core explanatory variables alongside the 9 research markets.",

        "Treat crude oil mainly as a macro / inflation / borrower-credit "
        "channel rather than direct operating exposure.",

        "Treat metals mainly as industrial-growth and borrower-cycle signals.",

        "Treat electricity mainly through borrower operating costs and "
        "repayment capacity, with a secondary digital-infrastructure channel.",

        "Use lagged variables because commodity and macro shocks may take "
        "time to affect loan demand, insurance demand and asset quality.",

        "Use rolling windows to identify regime changes.",

        "Calculate both contemporaneous and forward/lagged relationships.",

        "Control for NIFTY when measuring individual market relationships.",

        "Use financial-sector benchmarks to distinguish sector movement "
        "from company/group-specific movement.",

        "Use event studies around RBI decisions, results, regulatory events "
        "and major subsidiary developments.",

        "Use volume confirmation for stock-price reactions.",

        "Use source quality and data freshness in the evidence layer.",

        "Do not assume correlation means causation.",

        "Do not make final BUY/SELL decisions inside this character module.",

        "Pass calculated evidence to the central research and decision layer.",
    ],
)


# ============================================================
# 4. PUBLIC FUNCTIONS
# ============================================================

def get_company_character() -> CompanyCharacter:
    """Return the complete Bajaj Finserv company character."""
    return BAJAJFINSV_CHARACTER


def get_market_character(market: str) -> MarketCharacter:
    """Return one of the 9 market characters."""

    key = market.strip()

    if key not in BAJAJFINSV_CHARACTER.markets:
        raise KeyError(
            f"Unsupported market '{market}'. "
            f"Supported markets: "
            f"{', '.join(BAJAJFINSV_CHARACTER.markets)}"
        )

    return BAJAJFINSV_CHARACTER.markets[key]


def get_all_markets() -> Dict[str, MarketCharacter]:
    """Return all 9 market characters."""
    return dict(BAJAJFINSV_CHARACTER.markets)


def get_company_summary() -> dict:
    """Return a compact machine-readable company summary."""

    return {
        "symbol": BAJAJFINSV_CHARACTER.symbol,
        "company_name": BAJAJFINSV_CHARACTER.company_name,
        "company_character": BAJAJFINSV_CHARACTER.company_character,
        "primary_businesses": list(
            BAJAJFINSV_CHARACTER.primary_businesses
        ),
        "sector_links": list(
            BAJAJFINSV_CHARACTER.sector_links
        ),
        "market_count": len(
            BAJAJFINSV_CHARACTER.markets
        ),
        "markets": list(
            BAJAJFINSV_CHARACTER.markets.keys()
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
        BAJAJFINSV_CHARACTER.markets.keys()
    )

    if actual_markets != expected_markets:

        missing = expected_markets - actual_markets
        extra = actual_markets - expected_markets

        raise ValueError(
            "Market character validation failed. "
            f"Missing={sorted(missing)}, "
            f"Extra={sorted(extra)}"
        )

    if BAJAJFINSV_CHARACTER.symbol != "BAJAJFINSV":
        raise ValueError("Invalid company symbol.")

    for market_name, market in (
        BAJAJFINSV_CHARACTER.markets.items()
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

    print("BAJAJFINSV Character: VALID")
    print(
        f"Company: {BAJAJFINSV_CHARACTER.company_name}"
    )

    print(
        f"Markets: {len(BAJAJFINSV_CHARACTER.markets)}"
    )

    for name, market in BAJAJFINSV_CHARACTER.markets.items():

        print(
            f"- {name}: "
            f"{market.exposure_character}"
        )
