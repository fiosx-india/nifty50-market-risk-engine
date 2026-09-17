"""
SHRIRAMFIN Character Model
==========================
Business character + nine tracked market characters for Shriram Finance.

This module defines WHAT should be measured. It intentionally does not
hard-code RANK, PCT_CHANGE, LINKAGE_SCORE, RELATION, correlation, beta,
probability, or a trading decision.

Historical impact must be calculated later from real company, market,
macro, event and time-series data.
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
    customer_segments: Tuple[str, ...]
    lending_engine: Tuple[str, ...]
    value_chain: Tuple[str, ...]
    demand_drivers: Tuple[str, ...]
    revenue_drivers: Tuple[str, ...]
    funding_and_cost_drivers: Tuple[str, ...]
    credit_risk_drivers: Tuple[str, ...]
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
    symbol="SHRIRAMFIN",
    company_name="Shriram Finance Limited",
    primary_identity=(
        "Diversified retail-focused non-banking financial company built around "
        "asset-backed and cash-flow-based financing, with a strong franchise "
        "in commercial vehicles and other mobility, MSME, passenger vehicle, "
        "two-wheeler, tractor, gold and personal finance, supported by a broad "
        "branch, distribution, digital and funding platform."
    ),
    business_segments=(
        "Commercial vehicle finance",
        "Used commercial vehicle finance",
        "New commercial vehicle finance",
        "Passenger vehicle finance",
        "Two-wheeler finance",
        "Tractor and farm-equipment finance",
        "MSME and business finance",
        "Personal finance",
        "Gold loans",
        "Working-capital / small-business finance",
        "Deposits and diversified funding",
        "Digital lending and customer servicing",
    ),
    customer_segments=(
        "Truck and fleet operators",
        "Small transport operators",
        "Owner-drivers",
        "Small businesses",
        "MSMEs",
        "Self-employed borrowers",
        "Rural and semi-urban customers",
        "Vehicle owners and buyers",
        "Personal-loan customers",
        "Gold-loan customers",
    ),
    lending_engine=(
        "Vehicle-backed lending",
        "Used-asset financing",
        "Cash-flow-based underwriting",
        "MSME credit assessment",
        "Rural and semi-urban credit distribution",
        "Relationship-led collections",
        "Branch-led sourcing",
        "Digital sourcing and servicing",
        "Cross-selling across customer relationships",
        "Risk-based pricing",
    ),
    value_chain=(
        "Customer acquisition",
        "Credit assessment",
        "Asset valuation",
        "Loan underwriting",
        "Disbursement",
        "Collections",
        "Recovery",
        "Repossession and asset resolution where required",
        "Funding and liability management",
        "Securitisation / assignment where applicable",
        "Branch operations",
        "Digital servicing",
        "Risk and compliance",
    ),
    demand_drivers=(
        "Commercial vehicle demand",
        "Freight movement",
        "Fleet replacement",
        "Used-vehicle transactions",
        "Rural income",
        "Agricultural activity",
        "MSME cash-flow conditions",
        "Consumer credit demand",
        "Gold-backed liquidity demand",
        "Vehicle affordability",
        "Interest-rate affordability",
        "Economic activity",
    ),
    revenue_drivers=(
        "Loan book growth",
        "Disbursement growth",
        "Yield on advances",
        "Net interest income",
        "Net interest margin",
        "Fee and other income",
        "Cross-sell",
        "Collection efficiency",
        "Recoveries",
        "Asset-quality improvement",
        "Customer retention",
        "Branch productivity",
    ),
    funding_and_cost_drivers=(
        "Borrowing costs",
        "Bank and institutional funding",
        "Deposits",
        "Capital-market funding",
        "Securitisation / assignment economics",
        "Interest-rate environment",
        "Credit spreads",
        "Employee costs",
        "Branch operating costs",
        "Technology expenditure",
        "Collections infrastructure",
        "Credit-loss provisions",
    ),
    credit_risk_drivers=(
        "Borrower cash flow",
        "Freight rates",
        "Fuel costs",
        "Used-vehicle prices",
        "Commercial vehicle utilisation",
        "Rural income",
        "MSME activity",
        "Interest rates",
        "Loan-to-value",
        "Collection efficiency",
        "Delinquencies",
        "Stage migration",
        "Credit costs",
        "Recovery rates",
    ),
    strategic_drivers=(
        "Scale retail lending franchise",
        "Deepen commercial vehicle leadership",
        "Expand MSME and consumer finance",
        "Increase rural and semi-urban penetration",
        "Use branch and digital distribution together",
        "Improve funding diversification",
        "Improve asset quality",
        "Increase cross-sell",
        "Improve collection technology",
        "Use data and analytics in underwriting",
        "Maintain liquidity and capital buffers",
    ),
    operational_risks=(
        "Credit deterioration",
        "Collection disruption",
        "Fraud",
        "Vehicle-value decline",
        "Funding-cost increase",
        "Liquidity stress",
        "Branch productivity weakness",
        "Technology outage",
        "Cyber risk",
        "Operational loss",
        "Concentration risk",
    ),
    regulatory_risks=(
        "RBI regulation",
        "NBFC capital requirements",
        "Liquidity requirements",
        "Fair-practice requirements",
        "Digital-lending rules",
        "Consumer-protection requirements",
        "Collection-practice requirements",
        "KYC / AML requirements",
        "Provisioning and accounting changes",
    ),
    key_indicators=(
        "Assets under management",
        "Loan book growth",
        "Disbursements",
        "Commercial vehicle AUM",
        "Passenger vehicle AUM",
        "Two-wheeler AUM",
        "Tractor AUM",
        "MSME AUM",
        "Gold-loan AUM",
        "Personal-finance AUM",
        "Yield on advances",
        "Cost of funds",
        "Net interest margin",
        "Net interest income",
        "Fee income",
        "Stage 2 assets",
        "Stage 3 assets",
        "Gross NPA",
        "Net NPA",
        "Credit cost",
        "Collection efficiency",
        "Recovery",
        "Provision coverage",
        "Capital adequacy",
        "Liquidity",
        "Branch productivity",
        "Customer additions",
        "Funding mix",
        "Cost-to-income",
        "ROA",
        "ROE",
    ),
    event_types=(
        "Quarterly results",
        "Annual results",
        "AUM update",
        "Disbursement update",
        "RBI policy change",
        "NBFC regulatory change",
        "Interest-rate change",
        "Funding-cost change",
        "Credit-rating action",
        "Large borrowing",
        "Securitisation / assignment transaction",
        "Asset-quality update",
        "NPA movement",
        "Provisioning change",
        "Capital raise",
        "Dividend / capital-allocation action",
        "Branch expansion",
        "Digital platform change",
        "Fraud / operational event",
        "Major vehicle-market change",
        "Rural / MSME credit event",
    ),
    market_characters={},
)


MARKET_CHARACTERS: Dict[str, MarketCharacter] = {
    "NIFTY 50": _mc(
        "NIFTY 50",
        "Direct equity-market beta plus Indian economic and credit-cycle exposure",
        (
            "Equity valuation",
            "Risk appetite",
            "Credit-cycle expectations",
            "Institutional flows",
            "Indian growth expectations",
        ),
        (
            "Capital-market funding",
            "Financial-sector liquidity",
            "Institutional ownership and flows",
        ),
        (
            "Economic activity",
            "Vehicle demand",
            "MSME activity",
            "Rural income",
            "Consumer credit demand",
        ),
        (
            "Funding-market conditions",
            "Valuation multiple sensitivity",
        ),
        (
            "GDP growth",
            "Interest rates",
            "Inflation",
            "Liquidity",
            "Risk appetite",
        ),
        (
            "Rolling beta",
            "Rolling correlation",
            "Financial-sector relative strength",
            "Loan-growth cycle",
            "Volatility",
        ),
        (
            "Quarterly results",
            "RBI decisions",
            "AUM update",
            "Asset-quality update",
            "Capital/funding events",
        ),
        ("Intraday", "1D", "1W", "1M", "3M", "6M", "1Y"),
        (
            "Control for the NIFTY market effect before testing commodity-specific effects.",
            "Calculate residual stock returns after market and financial-sector controls.",
        ),
    ),
    "Crude Oil": _mc(
        "Crude Oil",
        "Indirect but potentially meaningful borrower-cash-flow and credit-risk exposure",
        (
            "Fuel cost",
            "Transport economics",
            "Fleet-operator cash flow",
            "Freight economics",
            "Inflation",
            "Credit demand",
            "Asset quality",
        ),
        (
            "Commercial vehicle operators",
            "Fleet operators",
            "Transport logistics",
            "Used-vehicle ecosystem",
        ),
        (
            "Freight activity",
            "Commercial vehicle utilisation",
            "MSME activity",
            "Rural purchasing power",
        ),
        (
            "Borrower fuel expense",
            "Transport operating cost",
            "Loan-servicing capacity",
        ),
        (
            "Inflation",
            "Interest rates",
            "Freight rates",
            "Economic growth",
            "Rural income",
        ),
        (
            "Crude return",
            "Fuel-price proxy",
            "Freight rates",
            "Commercial vehicle utilisation",
            "Collection efficiency",
            "Stage 2/3 assets",
            "Credit cost",
        ),
        (
            "Oil-price spike",
            "Fuel-price shock",
            "Transport-margin compression",
            "Inflation shock",
        ),
        ("1D", "1W", "1M", "3M", "6M"),
        (
            "Test the borrower cash-flow channel rather than assuming a direct company cost.",
            "Measure lagged effects on collections and asset quality.",
            "Separate fuel-cost impact from broad inflation and economic-cycle effects.",
        ),
    ),
    "Gold": _mc(
        "Gold",
        "Meaningful collateral, savings and household-liquidity exposure",
        (
            "Gold-loan collateral value",
            "Household liquidity",
            "Savings allocation",
            "Risk sentiment",
            "Inflation hedge behaviour",
        ),
        (
            "Gold-loan collateral",
            "Gold-loan sourcing and servicing",
            "Household asset monetisation",
        ),
        (
            "Gold-loan demand",
            "Household liquidity demand",
            "Rural and self-employed liquidity",
        ),
        (
            "Collateral-value dynamics",
            "Loan-to-value dynamics",
            "Potential recovery economics",
        ),
        (
            "Inflation",
            "Real rates",
            "Household wealth",
            "Currency",
            "Risk appetite",
        ),
        (
            "Gold return",
            "Gold-loan AUM",
            "Gold-loan disbursement",
            "LTV",
            "Collection efficiency",
            "Loan yield",
            "Asset quality",
        ),
        (
            "Gold-price breakout",
            "Sharp gold correction",
            "Gold-loan demand surge",
            "Collateral-value shock",
        ),
        ("Intraday", "1D", "1W", "1M", "3M", "6M"),
        (
            "Gold has a more specific business channel than the other commodities because of gold-backed lending.",
            "Test gold-price changes against gold-loan growth and collateral metrics separately.",
            "Do not assume higher gold automatically produces higher profitability; test volume, yield, LTV and credit outcomes.",
        ),
    ),
    "Silver": _mc(
        "Silver",
        "Primarily indirect commodity-cycle and macro exposure",
        (
            "Industrial-cycle signal",
            "Commodity sentiment",
            "Risk appetite",
            "Inflation",
        ),
        (
            "No major direct silver collateral channel in the core lending model",
            "Indirect industrial-cycle channel",
        ),
        (
            "MSME activity",
            "Industrial demand",
            "Economic growth",
        ),
        (
            "Limited direct operating-cost exposure",
        ),
        (
            "Global growth",
            "Commodity inflation",
            "Risk appetite",
            "Industrial activity",
        ),
        (
            "Silver return",
            "Industrial PMI",
            "MSME indicators",
            "Loan growth",
            "Residual stock return",
        ),
        (
            "Industrial slowdown",
            "Commodity shock",
            "Global growth surprise",
        ),
        ("1D", "1W", "1M", "3M", "6M"),
        (
            "Treat silver primarily as an industrial/macro state variable.",
            "Control for NIFTY, crude and rates before attributing any residual effect to silver.",
        ),
    ),
    "Natural Gas": _mc(
        "Natural Gas",
        "Indirect borrower-cost, industrial-cycle and inflation exposure",
        (
            "Industrial energy cost",
            "MSME cash flow",
            "Manufacturing activity",
            "Inflation",
            "Credit demand",
        ),
        (
            "Gas-intensive MSMEs",
            "Industrial borrowers",
            "Manufacturing supply chains",
        ),
        (
            "Industrial production",
            "MSME activity",
            "Borrower cash flow",
        ),
        (
            "Energy cost for borrowers",
            "Industrial operating cost",
            "Potential collection pressure",
        ),
        (
            "Industrial inflation",
            "Interest rates",
            "Economic activity",
            "Commodity cycle",
        ),
        (
            "Natural-gas return",
            "Industrial production",
            "MSME stress",
            "Loan growth",
            "Collection efficiency",
            "Credit cost",
        ),
        (
            "Gas-price spike",
            "Industrial energy shock",
            "MSME margin compression",
        ),
        ("1W", "1M", "3M", "6M"),
        (
            "The primary channel is borrower cash flow, not Shriram Finance's own fuel consumption.",
            "Use sector-level borrower exposure where data is available.",
        ),
    ),
    "Copper": _mc(
        "Copper",
        "Indirect industrial-capex and borrower-cycle exposure",
        (
            "Industrial activity",
            "Infrastructure cycle",
            "Vehicle and equipment demand",
            "MSME capex",
            "Credit demand",
        ),
        (
            "Auto and commercial-vehicle ecosystem",
            "Electrical and engineering MSMEs",
            "Infrastructure borrowers",
        ),
        (
            "Commercial vehicle demand",
            "Industrial capex",
            "MSME expansion",
            "Economic growth",
        ),
        (
            "Borrower input-cost pressure",
            "Equipment-cost inflation",
        ),
        (
            "Global industrial cycle",
            "Infrastructure spending",
            "Inflation",
            "Interest rates",
        ),
        (
            "Copper return",
            "Industrial PMI",
            "CV sales",
            "MSME credit growth",
            "Loan growth",
            "Asset quality",
        ),
        (
            "Copper-cycle reversal",
            "Infrastructure slowdown",
            "Industrial demand shock",
        ),
        ("1W", "1M", "3M", "6M", "1Y"),
        (
            "Use copper as a proxy for the industrial borrowers that drive part of the loan book.",
            "Validate with vehicle sales, industrial production and MSME credit data.",
        ),
    ),
    "Aluminium": _mc(
        "Aluminium",
        "Indirect vehicle, manufacturing, infrastructure and borrower-cycle exposure",
        (
            "Vehicle manufacturing cycle",
            "Equipment demand",
            "Industrial activity",
            "MSME cash flow",
            "Credit demand",
        ),
        (
            "Automotive borrowers",
            "Engineering MSMEs",
            "Transport ecosystem",
            "Infrastructure borrowers",
        ),
        (
            "Vehicle demand",
            "Fleet expansion",
            "Industrial production",
            "MSME investment",
        ),
        (
            "Borrower material-cost pressure",
            "Equipment and vehicle cost",
        ),
        (
            "Industrial growth",
            "Commodity inflation",
            "Vehicle cycle",
            "Interest rates",
        ),
        (
            "Aluminium return",
            "Auto sales",
            "CV sales",
            "MSME credit",
            "Loan growth",
            "Collection efficiency",
        ),
        (
            "Aluminium shock",
            "Auto-cycle change",
            "Industrial slowdown",
        ),
        ("1W", "1M", "3M", "6M", "1Y"),
        (
            "Treat aluminium as a borrower-industry signal rather than a direct company input.",
            "Test whether aluminium moves add explanatory power after controlling for NIFTY and industrial activity.",
        ),
    ),
    "Zinc": _mc(
        "Zinc",
        "Indirect construction, manufacturing and credit-cycle exposure",
        (
            "Construction activity",
            "Galvanised-steel cycle",
            "Industrial investment",
            "MSME activity",
            "Credit demand",
        ),
        (
            "Construction borrowers",
            "Infrastructure borrowers",
            "Engineering MSMEs",
            "Vehicle ecosystem",
        ),
        (
            "Construction",
            "Infrastructure",
            "Industrial activity",
            "Fleet investment",
        ),
        (
            "Borrower material costs",
            "Construction and equipment costs",
        ),
        (
            "Construction cycle",
            "Industrial growth",
            "Commodity inflation",
            "Interest rates",
        ),
        (
            "Zinc return",
            "Construction indicators",
            "Industrial PMI",
            "CV sales",
            "MSME credit",
            "Asset quality",
        ),
        (
            "Zinc shock",
            "Construction slowdown",
            "Industrial-cycle reversal",
        ),
        ("1W", "1M", "3M", "6M", "1Y"),
        (
            "Use zinc as a secondary industrial/construction signal.",
            "Do not treat zinc as a direct Shriram Finance operating input.",
        ),
    ),
    "Electricity": _mc(
        "Electricity",
        "Indirect borrower operating-cost, economic-activity and credit-risk exposure",
        (
            "Borrower operating cost",
            "Industrial production",
            "MSME cash flow",
            "Infrastructure activity",
            "Credit demand",
        ),
        (
            "Industrial MSMEs",
            "Commercial borrowers",
            "Transport-related businesses",
            "Manufacturing borrowers",
        ),
        (
            "Industrial output",
            "Commercial activity",
            "MSME profitability",
            "Loan demand",
        ),
        (
            "Borrower electricity expense",
            "Operating-margin pressure",
            "Debt-servicing capacity",
        ),
        (
            "Power prices",
            "Grid reliability",
            "Industrial growth",
            "Inflation",
            "Interest rates",
        ),
        (
            "Electricity-price change",
            "Industrial production",
            "MSME stress",
            "Collection efficiency",
            "Credit cost",
            "Loan growth",
        ),
        (
            "Power-price shock",
            "Grid disruption",
            "Industrial slowdown",
            "MSME margin shock",
        ),
        ("1D", "1W", "1M", "3M", "6M"),
        (
            "Measure electricity through borrower economics, not as a direct Shriram Finance production cost.",
            "Where borrower-sector data exists, map electricity intensity by sector before calculating impact.",
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
    """Return the complete Shriram Finance company character."""
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
    """Structural validation; historical impact is intentionally not validated here."""
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
    print("SHRIRAMFIN character validation:", result)

    for market in TRACKED_MARKETS:
        character = get_market_character(market)
        print(
            f"{market}: {character.exposure_type} | "
            f"{len(character.indicators_to_measure)} indicators | "
            f"{len(character.event_signals)} event groups"
        )
