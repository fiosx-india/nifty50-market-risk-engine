"""
BAJFINANCE — Company Character Definition
=========================================

NIFTY 50 Market Risk Engine

Company:
    Bajaj Finance Limited

Purpose
-------
Define Bajaj Finance's business character and its relationship with
the project's 9 research markets.

The supplied CSV may contain:
    RANK
    PCT_CHANGE
    LINKAGE_SCORE
    RELATION

Those are treated only as historical/snapshot fields.
They are NOT permanent company-character truth.

This module contains:
    - Company Character
    - Business Structure
    - Operating Model
    - Revenue Drivers
    - Cost / Risk Drivers
    - Demand Drivers
    - Financial Ecosystem
    - Sector Links
    - 9 Market Characters
    - Indicators
    - Important Events
    - Timeframes
    - Historical Calculation Rules

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
# 3. BAJAJ FINANCE COMPANY CHARACTER
# ============================================================

BAJFINANCE_CHARACTER = CompanyCharacter(

    symbol="BAJFINANCE",

    company_name="Bajaj Finance Limited",

    company_character=(
        "Technology-led diversified Indian NBFC built around consumer finance, "
        "personal loans, MSME finance, commercial finance, rural finance, "
        "mortgages, gold loans, auto finance, loans against securities, "
        "deposits, payments and financial partnerships. Its character is "
        "driven by loan growth, customer acquisition, cross-sell, assets under "
        "management, net interest margin, cost of funds, credit quality, "
        "liquidity, consumer and business credit demand, digital distribution "
        "and disciplined risk management."
    ),

    # ========================================================
    # CORE BUSINESSES
    # ========================================================

    primary_businesses=[
        "Consumer finance",
        "Consumer durable finance",
        "Digital product finance",
        "Lifestyle product finance",
        "E-commerce consumer finance",
        "Personal loans",
        "Salaried personal loans",
        "Retail spend financing",
        "EMI Card",
        "Two-wheeler and three-wheeler finance",
        "SME finance",
        "Working-capital loans",
        "Secured business loans",
        "Loans to self-employed and professionals",
        "Commercial finance",
        "Commercial vehicle finance",
        "New-car finance",
        "Used-car finance",
        "Auto leasing",
        "Medical equipment finance",
        "Loan against property",
        "Rural lending",
        "Gold loans",
        "Microfinance",
        "Tractor finance",
        "Bharat mortgages",
        "Loan against securities",
        "IPO finance",
        "ESOP finance",
        "Vendor finance",
        "Financial-institution lending",
        "Corporate lending",
        "Public and corporate deposits",
        "Payments",
        "PPI",
        "UPI",
        "BBPS",
        "FASTag",
        "Merchant acquiring",
        "Insurance distribution",
        "Financial partnerships",
    ],

    # ========================================================
    # OPERATING MODEL
    # ========================================================

    operating_model=[
        "Digital-first customer acquisition",
        "Large physical distribution network",
        "Point-of-sale financing",
        "App and web based lending",
        "Pre-approved lending",
        "Cross-selling",
        "Customer lifecycle management",
        "Data-driven credit underwriting",
        "Risk-based pricing",
        "Collections and recovery",
        "Consumer finance partnerships",
        "SME and commercial underwriting",
        "Rural distribution",
        "Gold-backed lending",
        "Vehicle finance",
        "Mortgage and property-backed lending",
        "Capital-market financing",
        "Deposit mobilisation",
        "Payments ecosystem",
        "Technology and AI-led operations",
    ],

    # ========================================================
    # REVENUE DRIVERS
    # ========================================================

    revenue_drivers=[
        "Loan book growth",
        "Assets under management",
        "Consumer finance volumes",
        "Personal loan originations",
        "SME loan growth",
        "Commercial finance growth",
        "Rural finance growth",
        "Mortgage and LAP growth",
        "Gold-loan growth",
        "Vehicle-finance growth",
        "Interest income",
        "Net interest income",
        "Net interest margin",
        "Fee income",
        "Processing fees",
        "Cross-sell income",
        "Payment income",
        "Partnership income",
        "Deposit franchise",
        "Loan against securities",
        "Vendor finance",
        "Insurance distribution",
    ],

    # ========================================================
    # COST / RISK DRIVERS
    # ========================================================

    cost_drivers=[
        "Cost of funds",
        "Borrowing costs",
        "Interest expense",
        "Deposit costs",
        "Credit losses",
        "Expected credit loss provisions",
        "Loan-loss provisions",
        "Collection costs",
        "Recovery costs",
        "Employee costs",
        "Technology expenditure",
        "AI and data infrastructure",
        "Cybersecurity expenditure",
        "Digital acquisition costs",
        "Marketing costs",
        "Distribution costs",
        "Compliance costs",
        "Liquidity costs",
        "Capital requirements",
        "Fraud losses",
    ],

    # ========================================================
    # DEMAND DRIVERS
    # ========================================================

    demand_drivers=[
        "Household income",
        "Employment",
        "Consumer confidence",
        "Consumer discretionary spending",
        "Consumer electronics demand",
        "E-commerce activity",
        "Lifestyle spending",
        "Two-wheeler demand",
        "Three-wheeler demand",
        "Automobile demand",
        "Housing demand",
        "Real-estate activity",
        "MSME activity",
        "Small-business cash flow",
        "Rural income",
        "Agricultural income",
        "Tractor demand",
        "Gold-backed liquidity demand",
        "Corporate investment",
        "Interest-rate environment",
        "Credit availability",
        "Digital adoption",
        "Financial inclusion",
    ],

    # ========================================================
    # FINANCIAL ECOSYSTEM
    # ========================================================

    supply_chain_links=[
        "Retail borrowers",
        "Consumer durable retailers",
        "E-commerce merchants",
        "Automobile dealers",
        "Two-wheeler dealers",
        "Three-wheeler dealers",
        "SMEs",
        "Self-employed professionals",
        "Commercial borrowers",
        "Rural borrowers",
        "Farmers and rural businesses",
        "Gold-loan customers",
        "Home buyers",
        "Property owners",
        "Corporate borrowers",
        "Auto-component manufacturers",
        "Financial institutions",
        "Capital markets",
        "Banks and funding partners",
        "Credit bureaus",
        "Payment networks",
        "Technology providers",
        "Fintech ecosystem",
        "RBI and financial regulators",
    ],

    # ========================================================
    # SECTOR LINKS
    # ========================================================

    sector_links=[
        "NBFC",
        "Consumer finance",
        "Retail lending",
        "Personal finance",
        "SME finance",
        "Commercial finance",
        "Rural finance",
        "Mortgage finance",
        "Gold finance",
        "Auto finance",
        "Capital markets",
        "Payments",
        "Fintech",
        "Consumer discretionary",
        "E-commerce",
        "Automobiles",
        "Real estate",
        "Agriculture",
        "Small-business economy",
        "Indian credit cycle",
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
                "affecting liquidity, financial-sector valuation, institutional "
                "flows and investor risk appetite."
            ),

            exposure_character=(
                "Primary systematic-market relationship"
            ),

            impact_path=(
                "NIFTY movement → liquidity / risk appetite / financial-sector "
                "valuation → BAJFINANCE stock behaviour"
            ),

            calculation_logic=(
                "Calculate return correlation, beta, rolling beta, relative "
                "strength, downside sensitivity and lag response. Also compare "
                "against financial-sector benchmarks. Separate systematic market "
                "movement from company-specific earnings, credit and regulatory events."
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
                "business margins and monetary-policy expectations."
            ),

            exposure_character=(
                "Indirect macroeconomic / consumer-credit relationship"
            ),

            impact_path=(
                "Crude movement → inflation / INR / interest-rate expectations "
                "→ household and business cash flow → credit demand / repayment "
                "capacity → BAJFINANCE"
            ),

            calculation_logic=(
                "Test crude returns against consumer credit growth, SME credit, "
                "asset quality, inflation, INR, interest rates and stock returns. "
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
                "Precious-metal and macro-risk asset connected to household "
                "wealth, savings behaviour, real rates, liquidity, currency "
                "conditions and risk sentiment."
            ),

            exposure_character=(
                "Indirect macro / wealth + gold-finance relationship"
            ),

            impact_path=(
                "Gold movement → household wealth / liquidity / savings behaviour "
                "and gold-collateral economics → secured lending demand / risk "
                "conditions → BAJFINANCE"
            ),

            calculation_logic=(
                "Test gold returns against stock returns, gold-loan activity "
                "where available, household savings and macro variables. "
                "Control for NIFTY, INR, interest rates and liquidity. "
                "Do not assume gold price alone determines company earnings."
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
                "Indirect industrial-cycle / credit-demand relationship"
            ),

            impact_path=(
                "Silver cycle → industrial activity / inflation / global growth "
                "→ consumer and SME business conditions → credit demand / "
                "asset quality → BAJFINANCE"
            ),

            calculation_logic=(
                "Measure silver returns, rolling correlation, volatility and "
                "lag response against credit-growth and stock-return variables. "
                "Control for NIFTY, gold and macro conditions."
            ),
        ),

        # ----------------------------------------------------
        # 5. NATURAL GAS
        # ----------------------------------------------------

        "Natural Gas": MarketCharacter(

            market="Natural Gas",

            character=(
                "Energy commodity affecting industrial costs, power economics, "
                "inflation and the financial health of energy-intensive businesses."
            ),

            exposure_character=(
                "Indirect industrial-credit / macro relationship"
            ),

            impact_path=(
                "Natural gas movement → industrial energy costs / inflation "
                "→ SME and corporate cash flow → credit demand / repayment "
                "capacity → BAJFINANCE"
            ),

            calculation_logic=(
                "Test gas returns against SME activity, industrial indicators, "
                "inflation, credit growth and asset quality. Use lagged effects "
                "and sector-level exposure where borrower data exists."
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
                "Indirect economic-growth / SME-credit relationship"
            ),

            impact_path=(
                "Copper cycle → manufacturing / infrastructure / capex → "
                "SME and commercial investment → financing demand and borrower "
                "health → BAJFINANCE"
            ),

            calculation_logic=(
                "Calculate copper-return relationship with industrial activity, "
                "SME indicators, commercial credit and BAJFINANCE returns. "
                "Test leading/lagged effects and control for NIFTY and rates."
            ),
        ),

        # ----------------------------------------------------
        # 7. ALUMINIUM
        # ----------------------------------------------------

        "Aluminium": MarketCharacter(

            market="Aluminium",

            character=(
                "Industrial metal linked to construction, transportation, "
                "manufacturing, consumer durables and infrastructure activity."
            ),

            exposure_character=(
                "Indirect industrial / consumer-credit relationship"
            ),

            impact_path=(
                "Aluminium cycle → manufacturing / construction / consumer "
                "durables → business activity and consumer spending → "
                "financing demand → BAJFINANCE"
            ),

            calculation_logic=(
                "Test aluminium returns against industrial production, consumer "
                "durable activity, vehicle sales, credit growth and stock returns. "
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
                "activity → SME and commercial investment → financing demand "
                "and borrower cash flow → BAJFINANCE"
            ),

            calculation_logic=(
                "Measure zinc returns against infrastructure, industrial "
                "production, SME indicators, credit growth and stock returns. "
                "Use lagged analysis and control for NIFTY and related metals."
            ),
        ),

        # ----------------------------------------------------
        # 9. ELECTRICITY
        # ----------------------------------------------------

        "Electricity": MarketCharacter(

            market="Electricity",

            character=(
                "Important economic input affecting manufacturing, retailers, "
                "SMEs, consumer businesses and the digital infrastructure "
                "supporting financial services."
            ),

            exposure_character=(
                "Indirect borrower-cost / credit-quality relationship"
            ),

            impact_path=(
                "Electricity price / availability → borrower operating costs "
                "and household/business cash flow → credit demand / repayment "
                "capacity → asset quality → BAJFINANCE"
            ),

            calculation_logic=(
                "Where reliable regional electricity data exists, measure "
                "price, volatility and availability against SME activity, "
                "credit growth, asset quality and stock returns. Separate "
                "financial-platform operating costs from borrower-credit effects."
            ),
        ),
    ],

    # ========================================================
    # IMPORTANT INDICATORS
    # ========================================================

    important_indicators=[

        # Core lending
        "Assets under management",
        "Loan book growth",
        "New loans booked",
        "Loan originations",
        "Disbursement growth",
        "Customer franchise",
        "Customer acquisition",
        "Cross-sell",
        "Products per customer",
        "Net interest income",
        "Net interest margin",
        "Yield on assets",
        "Cost of funds",
        "Spread",

        # Credit quality
        "Gross NPA",
        "Net NPA",
        "Credit cost",
        "Expected credit loss",
        "Stage 2 assets",
        "Stage 3 assets",
        "Provision coverage",
        "Slippage ratio",
        "Write-offs",
        "Recoveries",
        "Collection efficiency",

        # Funding / capital
        "Deposits",
        "Deposit growth",
        "Funding mix",
        "Liquidity",
        "Capital adequacy",
        "Tier 1 capital",
        "Borrowing costs",

        # Business segments
        "Consumer finance growth",
        "Personal loan growth",
        "SME loan growth",
        "Commercial finance growth",
        "Rural finance growth",
        "Mortgage growth",
        "Gold-loan growth",
        "Auto-finance growth",
        "Two-wheeler finance",
        "Three-wheeler finance",
        "Working-capital finance",

        # Digital
        "App users",
        "Digital originations",
        "Digital disbursements",
        "Point-of-sale network",
        "Bajaj Mall traffic",
        "Digital service requests",
        "AI-driven underwriting",
        "AI-driven customer service",

        # Macro
        "GDP growth",
        "CPI inflation",
        "RBI policy rate",
        "10Y G-Sec yield",
        "INR/USD",
        "Bank credit growth",
        "Money-market liquidity",
        "Household consumption",
        "Consumer confidence",

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

        # Stock behaviour
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

        "Monthly business update",
        "Quarterly results",
        "Annual results",
        "Annual report",
        "RBI monetary-policy decisions",
        "RBI NBFC regulations",
        "Interest-rate changes",
        "Liquidity changes",
        "Funding-cost changes",
        "Loan-growth guidance",
        "Asset-quality guidance",
        "Credit-cost guidance",
        "Capital-raising events",
        "Deposit-rate changes",
        "New product launches",
        "New lending partnerships",
        "Consumer durable partnerships",
        "E-commerce partnerships",
        "Digital-platform launches",
        "AI transformation initiatives",
        "Cybersecurity events",
        "Payment-product launches",
        "Regulatory changes",
        "Credit-rating actions",
        "Major borrower stress",
        "Consumer-credit regulations",
        "Gold-loan regulations",
        "Rural-finance regulations",
        "SME policy changes",
        "Housing / real-estate policy",
        "Automobile policy",
        "Major crude-oil shocks",
        "Global financial stress",
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

        "Treat BAJFINANCE as a diversified NBFC with multiple lending "
        "segments rather than as a single consumer-finance product.",

        "Separate consumer, SME, commercial, rural, mortgage, gold and "
        "capital-market lending channels during analysis.",

        "Use loan growth, AUM, NIM, cost of funds, credit cost and asset "
        "quality as primary fundamental variables.",

        "Treat crude oil mainly as an inflation / household-income / "
        "borrower-cash-flow channel.",

        "Treat gold separately because gold can influence household wealth, "
        "savings behaviour and gold-loan economics.",

        "Treat metals mainly as industrial, consumer-demand and SME-cycle signals.",

        "Treat electricity through borrower operating costs and repayment "
        "capacity, with a secondary digital-infrastructure channel.",

        "Use interest rates, liquidity, INR and credit growth as control "
        "variables when testing commodity relationships.",

        "Use lagged variables because macro and commodity shocks can take "
        "time to affect loan demand and asset quality.",

        "Use rolling windows to identify regime changes.",

        "Calculate both contemporaneous and forward/lagged relationships.",

        "Separate equity-market correlation from fundamental lending impact.",

        "Use financial-sector benchmarks as sector controls.",

        "Use event studies around RBI decisions, results, business updates "
        "and regulatory events.",

        "Use volume confirmation for stock-price reactions.",

        "Track source quality and data freshness.",

        "Do not assume correlation means causation.",

        "Do not make final BUY/SELL decisions inside this character module.",

        "Pass calculated evidence to the central research and decision layer.",
    ],
)


# ============================================================
# 4. PUBLIC FUNCTIONS
# ============================================================

def get_company_character() -> CompanyCharacter:
    """Return the complete Bajaj Finance company character."""
    return BAJFINANCE_CHARACTER


def get_market_character(market: str) -> MarketCharacter:
    """Return one of the 9 market characters."""

    key = market.strip()

    if key not in BAJFINANCE_CHARACTER.markets:
        raise KeyError(
            f"Unsupported market '{market}'. "
            f"Supported markets: "
            f"{', '.join(BAJFINANCE_CHARACTER.markets)}"
        )

    return BAJFINANCE_CHARACTER.markets[key]


def get_all_markets() -> Dict[str, MarketCharacter]:
    """Return all 9 market characters."""
    return dict(BAJFINANCE_CHARACTER.markets)


def get_company_summary() -> dict:
    """Return a compact machine-readable company summary."""

    return {
        "symbol": BAJFINANCE_CHARACTER.symbol,
        "company_name": BAJFINANCE_CHARACTER.company_name,
        "company_character": BAJFINANCE_CHARACTER.company_character,
        "primary_businesses": list(
            BAJFINANCE_CHARACTER.primary_businesses
        ),
        "sector_links": list(
            BAJFINANCE_CHARACTER.sector_links
        ),
        "market_count": len(
            BAJFINANCE_CHARACTER.markets
        ),
        "markets": list(
            BAJFINANCE_CHARACTER.markets.keys()
        ),
    }


def validate_character() -> bool:
    """
    Validate structure only.

    This does not prove historical correlation, causation or
    prediction accuracy.
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
        BAJFINANCE_CHARACTER.markets.keys()
    )

    if actual_markets != expected_markets:

        missing = expected_markets - actual_markets
        extra = actual_markets - expected_markets

        raise ValueError(
            "Market character validation failed. "
            f"Missing={sorted(missing)}, "
            f"Extra={sorted(extra)}"
        )

    if BAJFINANCE_CHARACTER.symbol != "BAJFINANCE":
        raise ValueError("Invalid company symbol.")

    for market_name, market in (
        BAJFINANCE_CHARACTER.markets.items()
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

    print("BAJFINANCE Character: VALID")
    print(
        f"Company: {BAJFINANCE_CHARACTER.company_name}"
    )

    print(
        f"Markets: {len(BAJFINANCE_CHARACTER.markets)}"
    )

    for name, market in BAJFINANCE_CHARACTER.markets.items():

        print(
            f"- {name}: "
            f"{market.exposure_character}"
        )
