"""
AXISBANK — Company Character Definition
=======================================

NIFTY 50 Market Risk Engine

This module defines:
1. Axis Bank's business/company character
2. Its relationship with the 9 research markets

IMPORTANT
---------
The old CSV values such as RANK, PCT_CHANGE, LINKAGE_SCORE and RELATION
are NOT treated as permanent truth.

This file contains character and research logic only.

No fixed:
- impact score
- correlation
- percentage impact
- ranking
- BUY/SELL decision

Those must be calculated from actual historical/live data.
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
# 3. AXIS BANK COMPANY CHARACTER
# ============================================================

AXISBANK_CHARACTER = CompanyCharacter(

    symbol="AXISBANK",

    company_name="Axis Bank Limited",

    company_character=(
        "Diversified Indian banking and financial-services platform built "
        "around retail banking, wholesale/corporate banking and treasury. "
        "Its economic character is driven by deposits, loan growth, net "
        "interest income, lending spreads, credit quality, liquidity, "
        "capital adequacy, fee income, transaction banking, treasury "
        "activity, digital banking and the health of the Indian economy."
    ),

    # ========================================================
    # CORE BUSINESSES
    # ========================================================

    primary_businesses=[
        "Retail banking",
        "Corporate and commercial banking",
        "Wholesale banking",
        "Transaction banking",
        "Treasury and markets",
        "Trade finance",
        "Supply-chain finance",
        "Credit cards",
        "Consumer loans",
        "Home loans",
        "Vehicle loans",
        "Personal loans",
        "MSME banking",
        "Wealth management",
        "Investment banking and capital markets",
        "Digital banking",
        "Payments",
        "Forex and derivatives",
    ],

    # ========================================================
    # OPERATING MODEL
    # ========================================================

    operating_model=[
        "Deposit mobilisation",
        "Retail lending",
        "Corporate lending",
        "Commercial banking",
        "Working-capital finance",
        "Term lending",
        "Transaction banking",
        "Trade finance",
        "Supply-chain finance",
        "Treasury and liquidity management",
        "Foreign exchange services",
        "Derivatives and risk-management solutions",
        "Capital-market services",
        "Digital banking",
        "Branch and distribution network",
        "Credit underwriting and risk management",
    ],

    # ========================================================
    # REVENUE DRIVERS
    # ========================================================

    revenue_drivers=[
        "Net interest income",
        "Loan book growth",
        "Deposit growth",
        "Net interest margin",
        "Retail lending",
        "Corporate lending",
        "MSME lending",
        "Home loans",
        "Vehicle loans",
        "Personal loans",
        "Credit-card business",
        "Transaction banking fees",
        "Trade-finance fees",
        "Supply-chain finance fees",
        "Wealth-management fees",
        "Investment-banking fees",
        "Forex and treasury income",
        "Fee income",
        "Third-party product distribution",
    ],

    # ========================================================
    # COST / RISK DRIVERS
    # ========================================================

    cost_drivers=[
        "Cost of deposits",
        "Interest expense",
        "Deposit repricing",
        "Credit costs",
        "Loan-loss provisions",
        "Employee costs",
        "Branch operating costs",
        "Technology expenditure",
        "Cybersecurity expenditure",
        "Digital infrastructure",
        "Marketing costs",
        "Compliance costs",
        "Fraud-related losses",
        "Liquidity costs",
        "Borrowing costs",
        "Capital requirements",
    ],

    # ========================================================
    # DEMAND DRIVERS
    # ========================================================

    demand_drivers=[
        "Indian GDP growth",
        "Household income",
        "Employment",
        "Consumer spending",
        "Housing demand",
        "Automobile demand",
        "MSME activity",
        "Corporate capex",
        "Infrastructure investment",
        "Working-capital requirements",
        "Trade activity",
        "Export and import activity",
        "Credit demand",
        "Financial inclusion",
        "Digital-payment adoption",
        "Interest-rate environment",
        "Business confidence",
        "Asset-price conditions",
    ],

    # ========================================================
    # SUPPLY / FINANCIAL ECOSYSTEM
    # ========================================================

    supply_chain_links=[
        "Depositors",
        "Retail customers",
        "Corporate borrowers",
        "MSMEs",
        "Government and institutional clients",
        "Insurance ecosystem",
        "Asset-management ecosystem",
        "Capital markets",
        "Payment networks",
        "Fintech ecosystem",
        "Technology providers",
        "Credit bureaus",
        "RBI and banking regulators",
        "Financial-market infrastructure",
        "Foreign-exchange markets",
        "Debt markets",
    ],

    # ========================================================
    # SECTOR LINKS
    # ========================================================

    sector_links=[
        "Private banking",
        "Financial services",
        "Retail banking",
        "Corporate banking",
        "MSME finance",
        "Housing finance",
        "Consumer finance",
        "Capital markets",
        "Treasury",
        "Payments",
        "Fintech",
        "Insurance",
        "Asset management",
        "Indian economy",
        "Real estate",
        "Automobile",
        "Infrastructure",
        "Manufacturing",
        "Trade and exports",
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
                "affecting liquidity, institutional flows, valuation multiples "
                "and financial-sector risk appetite."
            ),

            exposure_character=(
                "Primary systematic-market relationship"
            ),

            impact_path=(
                "NIFTY movement → market liquidity / risk appetite / "
                "institutional flows / valuation → AXISBANK stock behaviour"
            ),

            calculation_logic=(
                "Calculate return correlation, beta, rolling beta, relative "
                "strength, downside sensitivity and lag response. Separate "
                "systematic market effects from bank-specific earnings, "
                "asset-quality and regulatory events."
            ),
        ),

        # ----------------------------------------------------
        # 2. CRUDE OIL
        # ----------------------------------------------------

        "Crude Oil": MarketCharacter(

            market="Crude Oil",

            character=(
                "Global energy commodity that can influence Indian inflation, "
                "trade balance, currency conditions, household purchasing power "
                "and corporate working-capital stress."
            ),

            exposure_character=(
                "Indirect macroeconomic / credit-cycle relationship"
            ),

            impact_path=(
                "Crude movement → inflation / current-account / currency / "
                "interest-rate expectations → household and corporate credit "
                "conditions → asset quality / loan demand / valuation → AXISBANK"
            ),

            calculation_logic=(
                "Measure crude returns against bank returns, inflation, INR, "
                "interest rates, loan growth and asset-quality indicators. "
                "Use lagged analysis and control for NIFTY. Separate macro "
                "effects from direct commodity exposure because Axis Bank "
                "is not a crude producer."
            ),
        ),

        # ----------------------------------------------------
        # 3. GOLD
        # ----------------------------------------------------

        "Gold": MarketCharacter(

            market="Gold",

            character=(
                "Precious-metal and macro-risk asset linked to inflation "
                "expectations, real rates, currency conditions, liquidity "
                "and investor risk sentiment."
            ),

            exposure_character=(
                "Indirect macro / liquidity / collateral relationship"
            ),

            impact_path=(
                "Gold movement → risk sentiment / liquidity / real rates / "
                "currency conditions → credit and investment environment → "
                "AXISBANK valuation and business activity"
            ),

            calculation_logic=(
                "Test gold returns against bank returns after controlling "
                "for NIFTY, INR, interest rates and liquidity indicators. "
                "Where relevant, examine relationships with collateral, "
                "wealth and safe-haven flows. Do not assume direct gold "
                "price exposure equals bank profitability."
            ),
        ),

        # ----------------------------------------------------
        # 4. SILVER
        # ----------------------------------------------------

        "Silver": MarketCharacter(

            market="Silver",

            character=(
                "Precious and industrial metal whose movement can reflect "
                "global growth, industrial demand, inflation and commodity "
                "risk sentiment."
            ),

            exposure_character=(
                "Indirect industrial-cycle / macro-credit relationship"
            ),

            impact_path=(
                "Silver cycle → industrial activity / inflation / global growth "
                "→ corporate demand and credit cycle → AXISBANK"
            ),

            calculation_logic=(
                "Measure silver return, rolling relationship and lag response "
                "against bank returns, corporate-credit indicators and NIFTY. "
                "Control for gold and other macro variables to test incremental "
                "information."
            ),
        ),

        # ----------------------------------------------------
        # 5. NATURAL GAS
        # ----------------------------------------------------

        "Natural Gas": MarketCharacter(

            market="Natural Gas",

            character=(
                "Energy commodity affecting industrial production, power costs, "
                "inflation and the financial condition of energy-intensive borrowers."
            ),

            exposure_character=(
                "Indirect industrial-credit / macro relationship"
            ),

            impact_path=(
                "Natural Gas movement → industrial energy costs / inflation → "
                "corporate cash flow and working-capital conditions → credit "
                "demand / asset quality → AXISBANK"
            ),

            calculation_logic=(
                "Test gas returns against bank returns, industrial indicators, "
                "inflation and corporate-credit variables. Use lagged effects "
                "and sector-level exposure where borrower data is available. "
                "Do not treat gas as a direct bank revenue input."
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
                "Indirect economic-growth / corporate-credit relationship"
            ),

            impact_path=(
                "Copper cycle → manufacturing / infrastructure / capex → "
                "corporate credit demand and borrower cash flows → "
                "AXISBANK credit cycle and valuation"
            ),

            calculation_logic=(
                "Measure copper returns against loan growth, corporate-credit "
                "activity, NIFTY and bank returns. Test leading/lagging "
                "relationships and distinguish global-growth information "
                "from commodity-price effects."
            ),
        ),

        # ----------------------------------------------------
        # 7. ALUMINIUM
        # ----------------------------------------------------

        "Aluminium": MarketCharacter(

            market="Aluminium",

            character=(
                "Industrial metal linked to construction, transportation, "
                "manufacturing, infrastructure and industrial production."
            ),

            exposure_character=(
                "Indirect industrial-credit / capex-cycle relationship"
            ),

            impact_path=(
                "Aluminium cycle → industrial production / construction / "
                "capex → corporate borrowing and working-capital demand → "
                "AXISBANK"
            ),

            calculation_logic=(
                "Test aluminium returns against corporate-credit growth, "
                "industrial indicators and bank returns. Use rolling and "
                "lagged analysis and control for NIFTY, rates and global-growth "
                "variables."
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
                "activity → borrower investment and working-capital needs → "
                "credit demand / asset quality → AXISBANK"
            ),

            calculation_logic=(
                "Measure zinc returns against industrial activity, corporate "
                "credit, infrastructure indicators and bank returns. Use lag "
                "analysis and control for NIFTY and related industrial metals."
            ),
        ),

        # ----------------------------------------------------
        # 9. ELECTRICITY
        # ----------------------------------------------------

        "Electricity": MarketCharacter(

            market="Electricity",

            character=(
                "Operational and macro input affecting bank branches, ATMs, "
                "digital infrastructure and, more importantly, the operating "
                "health of electricity-intensive corporate borrowers."
            ),

            exposure_character=(
                "Indirect operating-cost / borrower-credit relationship"
            ),

            impact_path=(
                "Electricity cost / availability → borrower operating costs "
                "and household/business cash flow → credit demand / repayment "
                "capacity → asset quality and loan growth → AXISBANK"
            ),

            calculation_logic=(
                "Where reliable regional electricity data exists, test price, "
                "volatility and availability against bank returns, industrial "
                "activity, loan growth and asset-quality indicators. Separate "
                "bank operating-cost effects from borrower-credit effects."
            ),
        ),
    },

    # ========================================================
    # IMPORTANT INDICATORS
    # ========================================================

    important_indicators=[

        # Banking core
        "Loan book growth",
        "Deposit growth",
        "CASA ratio",
        "Net interest income",
        "Net interest margin",
        "Cost of funds",
        "Credit-deposit ratio",
        "Fee income",
        "Operating profit",
        "Cost-to-income ratio",

        # Credit quality
        "Gross NPA",
        "Net NPA",
        "Provision coverage ratio",
        "Credit cost",
        "Slippage ratio",
        "Restructured loans",
        "Write-offs",
        "Recovery",
        "Stage 2 loans",
        "Stage 3 loans",

        # Capital / liquidity
        "CET1 ratio",
        "CRAR",
        "Liquidity coverage ratio",
        "Net stable funding ratio",
        "Capital adequacy",
        "Deposit liquidity",

        # Business
        "Retail advances",
        "Corporate advances",
        "MSME advances",
        "Home loans",
        "Vehicle loans",
        "Personal loans",
        "Credit-card portfolio",
        "Transaction banking",
        "Trade finance",
        "Supply-chain finance",
        "Wealth management",
        "Digital transactions",

        # Macro
        "GDP growth",
        "CPI inflation",
        "WPI inflation",
        "RBI policy rate",
        "Government bond yields",
        "10Y G-Sec yield",
        "INR/USD",
        "Money-market liquidity",
        "Credit growth",

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
        "Bank NIFTY relative strength",
        "Sector-relative return",
    ],

    # ========================================================
    # IMPORTANT EVENTS
    # ========================================================

    important_events=[

        "Quarterly results",
        "Annual results",
        "Annual report",
        "RBI monetary-policy decisions",
        "RBI banking regulations",
        "RBI liquidity measures",
        "Deposit-rate changes",
        "Lending-rate changes",
        "Loan-growth updates",
        "Deposit-growth updates",
        "NIM guidance",
        "Asset-quality updates",
        "NPA / credit-cost changes",
        "Large corporate loan developments",
        "Large loan recoveries",
        "Loan restructuring announcements",
        "Capital-raising announcements",
        "Dividend announcements",
        "Credit-rating changes",
        "Bond-market developments",
        "Government banking policy",
        "Digital-payment developments",
        "Cybersecurity incidents",
        "Technology platform changes",
        "Major fintech partnerships",
        "Acquisitions or strategic transactions",
        "Subsidiary developments",
        "Capital-market transactions",
        "Forex-market events",
        "Major commodity shocks",
        "Crude-oil shocks",
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

        "Treat NIFTY 50 as a systematic control variable when measuring "
        "individual market relationships.",

        "For a bank, interest rates, liquidity, credit growth, deposits, "
        "NIM and asset quality are core explanatory variables and should "
        "not be replaced by commodity correlations.",

        "Treat crude oil mainly as a macroeconomic and borrower-credit "
        "channel rather than direct bank input cost.",

        "Treat metals mainly as economic-cycle / industrial-credit signals.",

        "Treat electricity mainly through borrower operating conditions "
        "and secondarily through the bank's own operating costs.",

        "Use lagged variables because macro and commodity shocks may take "
        "time to affect credit demand and asset quality.",

        "Use rolling windows to detect regime changes.",

        "Measure both contemporaneous and forward/lagged relationships.",

        "Separate equity-market correlation from fundamental banking impact.",

        "Use loan-growth, NIM and asset-quality data to validate macro signals.",

        "Use event studies around RBI decisions, results and major bank events.",

        "Use volume confirmation for stock-price reactions.",

        "Use Bank NIFTY / financial-sector relative performance as a sector control.",

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
    """Return the complete Axis Bank company character."""
    return AXISBANK_CHARACTER


def get_market_character(market: str) -> MarketCharacter:
    """Return one supported market character."""

    key = market.strip()

    if key not in AXISBANK_CHARACTER.markets:
        raise KeyError(
            f"Unsupported market '{market}'. "
            f"Supported markets: "
            f"{', '.join(AXISBANK_CHARACTER.markets)}"
        )

    return AXISBANK_CHARACTER.markets[key]


def get_all_markets() -> Dict[str, MarketCharacter]:
    """Return all 9 market characters."""
    return dict(AXISBANK_CHARACTER.markets)


def get_company_summary() -> dict:
    """Return a compact machine-readable company summary."""

    return {
        "symbol": AXISBANK_CHARACTER.symbol,
        "company_name": AXISBANK_CHARACTER.company_name,
        "company_character": AXISBANK_CHARACTER.company_character,
        "primary_businesses": list(
            AXISBANK_CHARACTER.primary_businesses
        ),
        "sector_links": list(
            AXISBANK_CHARACTER.sector_links
        ),
        "market_count": len(
            AXISBANK_CHARACTER.markets
        ),
        "markets": list(
            AXISBANK_CHARACTER.markets.keys()
        ),
    }


def validate_character() -> bool:
    """
    Validate structure only.

    This does not prove correlation, causation or prediction accuracy.
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
        AXISBANK_CHARACTER.markets.keys()
    )

    if actual_markets != expected_markets:

        missing = expected_markets - actual_markets
        extra = actual_markets - expected_markets

        raise ValueError(
            "Market character validation failed. "
            f"Missing={sorted(missing)}, "
            f"Extra={sorted(extra)}"
        )

    if AXISBANK_CHARACTER.symbol != "AXISBANK":
        raise ValueError("Invalid company symbol.")

    for market_name, market in (
        AXISBANK_CHARACTER.markets.items()
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

    print("AXISBANK Character: VALID")
    print(
        f"Company: {AXISBANK_CHARACTER.company_name}"
    )

    print(
        f"Markets: {len(AXISBANK_CHARACTER.markets)}"
    )

    for name, market in AXISBANK_CHARACTER.markets.items():
        print(
            f"- {name}: "
            f"{market.exposure_character}"
        )
