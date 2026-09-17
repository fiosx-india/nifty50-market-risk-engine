"""
HDFCBANK — Company Character & 9-Market Research Model

This file defines HDFC Bank's business character and the research logic for
its exposure to the project's 9 tracked markets.

The CSV supplied for this company contains observed/ranking fields, but those
values are deliberately NOT hard-coded here. Historical linkage must be
calculated later from real data.

Important:
- No fixed linkage scores.
- No fixed percentage changes.
- No rank fields.
- No BUY/SELL/HOLD decision.
- Commodity relationships are hypotheses to test, not assumed causation.
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
    character: str
    exposure_character: str
    impact_path: str
    calculation_logic: str
    relevant_indicators: Tuple[str, ...]
    relevant_events: Tuple[str, ...]
    expected_timeframes: Tuple[str, ...]


@dataclass(frozen=True)
class CompanyCharacter:
    symbol: str
    company_name: str
    sector: str
    industry_character: str
    business_character: str
    demand_drivers: Tuple[str, ...]
    revenue_drivers: Tuple[str, ...]
    cost_drivers: Tuple[str, ...]
    supply_chain_character: Tuple[str, ...]
    strategic_drivers: Tuple[str, ...]
    key_indicators: Tuple[str, ...]
    key_events: Tuple[str, ...]
    market_characters: Dict[str, MarketCharacter]


def _mc(
    market: str,
    character: str,
    exposure_character: str,
    impact_path: str,
    calculation_logic: str,
    indicators: Tuple[str, ...],
    events: Tuple[str, ...],
    timeframes: Tuple[str, ...],
) -> MarketCharacter:
    return MarketCharacter(
        market=market,
        character=character,
        exposure_character=exposure_character,
        impact_path=impact_path,
        calculation_logic=calculation_logic,
        relevant_indicators=indicators,
        relevant_events=events,
        expected_timeframes=timeframes,
    )


MARKET_CHARACTERS: Dict[str, MarketCharacter] = {
    "Aluminium": _mc(
        "Aluminium",
        "Industrial activity, construction, transport and manufacturing-cycle signal.",
        "Primarily indirect exposure. Aluminium prices can affect HDFC Bank borrowers "
        "in construction, auto, infrastructure, manufacturing and MSME businesses. "
        "The bank is mainly exposed through credit quality, loan demand and borrower "
        "cash flows rather than direct aluminium consumption.",
        "Aluminium -> borrower input costs/realisations -> borrower cash flow and "
        "working capital -> loan demand/repayment capacity -> credit cost and asset "
        "quality -> HDFC Bank earnings.",
        "Test aluminium returns against HDFC Bank loan growth, GNPA/NNPA, credit-cost "
        "and stock-return changes using lagged regression and event studies. Segment "
        "analysis should distinguish corporate/SME/retail exposures. Control for "
        "NIFTY, GDP/industrial production, rates and INR.",
        (
            "aluminium return",
            "aluminium volatility",
            "industrial-production proxy",
            "credit growth",
            "GNPA/NNPA",
            "credit cost",
        ),
        (
            "aluminium price shocks",
            "industrial-cycle changes",
            "infrastructure/auto demand changes",
            "major commodity supply disruptions",
        ),
        ("1D", "1W", "1M", "1Q", "6M"),
    ),
    "Copper": _mc(
        "Copper",
        "Industrial, electrical, infrastructure and capex-cycle signal.",
        "Indirect exposure through corporate and MSME borrowers in electrical "
        "equipment, infrastructure, construction, manufacturing, renewable energy "
        "and industrial sectors.",
        "Copper -> industrial demand/input economics -> borrower revenue, margins "
        "and capex -> working-capital/term-loan demand and repayment quality -> "
        "HDFC Bank credit cycle.",
        "Use lagged copper returns with industrial-production, capex and credit "
        "growth variables. Test whether copper adds information for bank asset "
        "quality or loan demand after controlling for NIFTY and macro conditions.",
        (
            "copper return",
            "copper volatility",
            "industrial-production proxy",
            "corporate credit growth",
            "SME credit growth",
            "asset-quality indicators",
        ),
        (
            "global manufacturing changes",
            "infrastructure investment",
            "renewable/grid capex",
            "copper supply disruptions",
        ),
        ("1D", "1W", "1M", "1Q", "6M"),
    ),
    "Crude Oil": _mc(
        "Crude Oil",
        "Inflation, household purchasing-power and borrower-cost shock.",
        "Indirect but economically broad exposure. Oil affects transport, logistics, "
        "manufacturing costs, inflation, household disposable income and corporate "
        "cash flows across HDFC Bank's borrower base.",
        "Crude -> fuel/transport costs and inflation -> household consumption and "
        "corporate margins -> loan demand/repayment -> credit costs; crude -> rates/"
        "liquidity expectations -> NIM, treasury and valuation.",
        "Measure asymmetric oil-shock effects on loan growth, NIM, credit cost and "
        "stock returns. Include INR, CPI, policy rates, GDP/PMI and NIFTY controls. "
        "Test sector-specific borrower sensitivity rather than using one aggregate "
        "commodity coefficient.",
        (
            "Brent/WTI return",
            "oil volatility",
            "CPI/inflation",
            "USD/INR",
            "credit growth",
            "credit cost",
            "NIM",
        ),
        (
            "OPEC+ decisions",
            "geopolitical supply shocks",
            "large oil-price spikes",
            "fuel-price policy changes",
            "inflation surprises",
        ),
        ("1D", "1W", "1M", "1Q"),
    ),
    "Electricity": _mc(
        "Electricity",
        "Business-operating-cost, industrial-capex and household-income signal.",
        "Indirect exposure through borrowers' operating costs and cash flows. "
        "Electricity-intensive businesses can experience margin and working-capital "
        "pressure; power infrastructure investment can increase project and "
        "corporate-finance demand.",
        "Electricity price/reliability -> borrower operating margin and cash flow -> "
        "repayment/working-capital needs -> asset quality and loan demand. Separately, "
        "power-sector investment -> project finance/corporate credit opportunities.",
        "Where borrower-sector data exists, calculate sector-level exposure using "
        "power-sensitive industries. Combine electricity variables with industrial "
        "production and credit-quality data; avoid treating a national electricity "
        "price as the bank's direct cost.",
        (
            "industrial power-price proxy",
            "power demand",
            "industrial production",
            "corporate credit growth",
            "credit cost",
            "GNPA/NNPA",
        ),
        (
            "power shortages",
            "tariff changes",
            "grid/infrastructure capex",
            "renewable-energy investment",
            "large industrial outages",
        ),
        ("1D", "1W", "1M", "1Q"),
    ),
    "Gold": _mc(
        "Gold",
        "Wealth, safe-haven, liquidity and retail-credit sentiment signal.",
        "More relevant than most commodities because HDFC Bank has retail "
        "customers, wealth-management activity, gold-linked lending and a treasury "
        "business. Gold can also proxy risk aversion and household wealth effects.",
        "Gold -> household wealth/savings and risk sentiment -> deposits, investment "
        "flows, consumption and credit behaviour; gold -> bullion/market activity -> "
        "gold-linked financial products and treasury/customer flows.",
        "Separate direct gold-linked business exposure from macro safe-haven effects. "
        "Test gold returns against deposits, retail credit, gold-loan activity where "
        "available, treasury income and stock returns. Control for rates, USD/INR, "
        "NIFTY and liquidity.",
        (
            "gold return",
            "gold volatility",
            "gold-loan growth where available",
            "deposit growth",
            "retail credit growth",
            "treasury income",
        ),
        (
            "central-bank rate decisions",
            "inflation surprises",
            "geopolitical risk",
            "large gold-price moves",
            "household investment-flow changes",
        ),
        ("1D", "1W", "1M", "1Q"),
    ),
    "NIFTY 50": _mc(
        "NIFTY 50",
        "Systematic Indian-equity, liquidity and financial-sector risk benchmark.",
        "Direct market exposure through HDFC Bank's listed equity beta, financial "
        "sector rotation, liquidity and valuation regime. It is also a broad proxy "
        "for domestic risk appetite.",
        "NIFTY -> market liquidity/risk appetite -> HDFC Bank valuation and investor "
        "flows. NIFTY/growth cycle -> corporate profitability and credit demand -> "
        "bank fundamentals.",
        "Calculate rolling correlation, beta, downside beta, relative strength, "
        "drawdown and residual return. Separately model fundamentals with rates, "
        "credit growth, NIM, asset quality and macro variables so market beta is "
        "not confused with business causation.",
        (
            "NIFTY return",
            "rolling beta",
            "financial-sector relative strength",
            "volume",
            "volatility",
            "drawdown",
        ),
        (
            "RBI policy",
            "Union Budget/fiscal policy",
            "major index rebalancing",
            "banking-sector regulatory changes",
            "HDFC Bank earnings",
        ),
        ("5m", "15m", "1H", "1D", "1W", "1M", "1Q", "1Y"),
    ),
    "Natural Gas": _mc(
        "Natural Gas",
        "Industrial-energy and borrower-cost-cycle signal.",
        "Indirect exposure through gas-intensive industrial, chemical, fertilizer, "
        "power and manufacturing borrowers. Effects flow through borrower cash flow "
        "and credit demand rather than HDFC Bank's own operating consumption.",
        "Natural gas -> industrial input/energy cost -> borrower margins and working "
        "capital -> repayment quality and credit demand -> HDFC Bank.",
        "Use gas returns with sectoral credit, industrial production, PMI and asset-"
        "quality variables. Test lagged effects and asymmetric shocks, controlling "
        "for crude, electricity, rates and NIFTY.",
        (
            "natural-gas return",
            "gas volatility",
            "industrial-production proxy",
            "sectoral credit growth",
            "credit cost",
            "GNPA/NNPA",
        ),
        (
            "LNG/gas supply disruptions",
            "global gas-price shocks",
            "gas-pricing policy changes",
            "industrial demand changes",
        ),
        ("1D", "1W", "1M", "1Q"),
    ),
    "Silver": _mc(
        "Silver",
        "Industrial-metals plus precious-metals wealth/risk signal.",
        "Mostly indirect exposure through industrial borrowers and investor/household "
        "sentiment. Silver may also proxy technology/solar investment and global "
        "industrial conditions.",
        "Silver -> industrial cycle and risk sentiment -> borrower activity, "
        "investment and household wealth -> loan/deposit behaviour and asset quality.",
        "Compare silver with copper, gold and industrial indicators. Use multivariate "
        "models and lag tests to determine whether silver adds independent information "
        "for HDFC Bank after controlling for NIFTY, rates, INR and macro activity.",
        (
            "silver return",
            "silver volatility",
            "gold/silver ratio",
            "industrial-production proxy",
            "credit growth",
            "HDFC Bank relative return",
        ),
        (
            "industrial-demand shocks",
            "solar/electronics demand changes",
            "precious-metals risk events",
            "global manufacturing changes",
        ),
        ("1D", "1W", "1M", "1Q"),
    ),
    "Zinc": _mc(
        "Zinc",
        "Steel, construction, infrastructure and manufacturing-cycle signal.",
        "Indirect exposure through corporate, MSME, infrastructure, construction "
        "and manufacturing borrowers whose cash flows can respond to zinc/steel "
        "cycles.",
        "Zinc -> steel/galvanising/construction activity -> borrower sales and "
        "working-capital needs -> loan demand and asset quality -> HDFC Bank.",
        "Use zinc and steel returns with construction/industrial proxies and sectoral "
        "credit data. Test lagged relationships and incremental explanatory power "
        "after controlling for NIFTY, rates and broad industrial activity.",
        (
            "zinc return",
            "steel return",
            "construction proxy",
            "industrial-production proxy",
            "corporate/SME credit growth",
            "asset-quality indicators",
        ),
        (
            "infrastructure spending",
            "construction-cycle changes",
            "steel-cycle changes",
            "zinc supply disruptions",
        ),
        ("1D", "1W", "1M", "1Q", "6M"),
    ),
}


COMPANY_CHARACTER = CompanyCharacter(
    symbol="HDFCBANK",
    company_name="HDFC Bank Limited",
    sector="Banking / Financial Services",
    industry_character=(
        "Large diversified Indian banking platform whose economic character is "
        "driven by deposits, retail and wholesale credit, transaction banking, "
        "payments, treasury, liquidity, interest-rate risk, credit quality and "
        "capital allocation. Its commodity exposure is predominantly indirect "
        "through borrowers and macroeconomic conditions rather than physical "
        "commodity consumption."
    ),
    business_character=(
        "Multi-engine banking character: Retail Banking, Home Loan/Mortgages, "
        "Wholesale/Corporate Banking, Commercial and Rural Banking and Treasury, "
        "with technology/digital distribution and financial-services subsidiaries. "
        "The central economic chain is deposits/liquidity -> loan growth and asset "
        "mix -> yields/funding cost -> NIM and fee income -> credit cost/capital "
        "requirements -> profitability and valuation."
    ),
    demand_drivers=(
        "household credit demand",
        "mortgage and housing activity",
        "personal and consumer finance",
        "auto and commercial-vehicle finance",
        "MSME and business-banking demand",
        "corporate working-capital demand",
        "infrastructure and project finance",
        "trade and supply-chain finance",
        "rural/agricultural credit demand",
        "payments and transaction activity",
        "wealth-management and investment activity",
        "economic growth and formalisation",
    ),
    revenue_drivers=(
        "net interest income",
        "net interest margin",
        "retail loan growth",
        "wholesale/corporate loan growth",
        "commercial and rural banking growth",
        "home-loan/mortgage growth",
        "CASA and total deposit growth",
        "fees from payments and transaction banking",
        "credit-card activity",
        "trade-finance and cash-management fees",
        "forex and derivatives activity",
        "treasury income",
        "wealth and third-party product distribution",
        "insurance and other subsidiary/associate economics",
    ),
    cost_drivers=(
        "deposit funding cost",
        "cost of borrowings",
        "employee costs",
        "branch and infrastructure costs",
        "technology and digital infrastructure",
        "credit costs/provisions",
        "fraud and operational losses",
        "regulatory/compliance costs",
        "distribution and customer-acquisition costs",
        "liquidity-management costs",
        "data/cybersecurity costs",
    ),
    supply_chain_character=(
        "depositors and retail customers",
        "corporate and institutional borrowers",
        "MSMEs and emerging businesses",
        "housing developers and home-loan ecosystem",
        "auto and commercial-vehicle ecosystem",
        "government and public-sector ecosystem",
        "payment networks and merchants",
        "fintech and technology partners",
        "cloud/data and cybersecurity providers",
        "financial-market counterparties",
        "insurance and investment-product partners",
        "branch and digital distribution network",
    ),
    strategic_drivers=(
        "deposit franchise and CASA growth",
        "quality retail-credit growth",
        "wholesale and commercial banking expansion",
        "mortgage integration and housing finance",
        "MSME and rural banking growth",
        "payments and digital banking",
        "technology modernisation",
        "risk management and underwriting quality",
        "asset-quality resilience",
        "liability franchise strength",
        "capital adequacy and capital allocation",
        "cross-selling and customer lifetime value",
        "operating efficiency",
        "subsidiary ecosystem development",
    ),
    key_indicators=(
        "total deposits",
        "CASA deposits",
        "retail loan growth",
        "wholesale loan growth",
        "commercial/rural credit growth",
        "home-loan/mortgage growth",
        "credit-card and payments activity",
        "net interest income",
        "net interest margin",
        "cost-to-income ratio",
        "GNPA",
        "NNPA",
        "provision coverage",
        "credit cost",
        "slippages",
        "capital adequacy/CET1",
        "return on assets",
        "return on equity",
        "liquidity indicators",
        "HDFCBANK return, volume and relative strength",
    ),
    key_events=(
        "quarterly and annual results",
        "RBI monetary-policy decisions",
        "RBI banking/regulatory changes",
        "deposit-rate changes",
        "lending-rate changes",
        "major credit-policy changes",
        "large corporate-credit events",
        "asset-quality/slippage disclosures",
        "capital or funding-market events",
        "technology/digital platform changes",
        "cybersecurity or fraud events",
        "housing/real-estate cycle changes",
        "major macro/inflation shocks",
        "M&A or subsidiary-related events",
        "management guidance and strategic updates",
    ),
    market_characters=MARKET_CHARACTERS,
)


def get_company_character() -> CompanyCharacter:
    """Return the complete HDFC Bank company character."""
    return COMPANY_CHARACTER


def get_market_character(market: str) -> MarketCharacter:
    """Return HDFC Bank's character/exposure model for one tracked market."""
    try:
        return COMPANY_CHARACTER.market_characters[market]
    except KeyError as exc:
        raise ValueError(
            f"Unsupported market: {market!r}. "
            f"Expected one of: {', '.join(TRACKED_MARKETS)}"
        ) from exc


def get_all_market_characters() -> Dict[str, MarketCharacter]:
    """Return all 9 market character definitions."""
    return dict(COMPANY_CHARACTER.market_characters)


def validate_character() -> bool:
    """
    Validate the character structure only.

    Historical scores, rankings, correlations and market decisions are
    intentionally outside this module.
    """
    if COMPANY_CHARACTER.symbol != "HDFCBANK":
        return False

    if tuple(COMPANY_CHARACTER.market_characters.keys()) != TRACKED_MARKETS:
        return False

    for market in TRACKED_MARKETS:
        item = COMPANY_CHARACTER.market_characters[market]
        if item.market != market:
            return False
        if not item.character or not item.exposure_character:
            return False
        if not item.impact_path or not item.calculation_logic:
            return False
        if not item.relevant_indicators or not item.relevant_events:
            return False
        if not item.expected_timeframes:
            return False

    return True


if __name__ == "__main__":
    print("HDFCBANK character valid:", validate_character())
    print("Tracked markets:", ", ".join(TRACKED_MARKETS))
    print("Company:", COMPANY_CHARACTER.company_name)
