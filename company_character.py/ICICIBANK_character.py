"""
ICICIBANK — Company Character & 9-Market Research Model

This module defines ICICI Bank's business character and the research framework
for its exposure to the project's 9 tracked markets.

The supplied CSV may contain rank, daily percentage change, linkage score and
relation. Those values are intentionally NOT hard-coded here.

This is the CHARACTER / EVIDENCE-DEFINITION layer. Historical linkage,
correlation, causality tests, probabilities and trading decisions belong to
later analytics/orchestration layers.
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
        "Industrial, construction, auto and infrastructure credit-cycle signal.",
        "Indirect exposure through ICICI Bank's corporate, commercial, MSME and "
        "retail borrower ecosystems. Aluminium affects borrower input costs, "
        "working capital, capex and repayment capacity rather than being a direct "
        "bank operating input.",
        "Aluminium -> borrower revenue/margin and working-capital cycle -> loan "
        "demand and repayment quality -> provisions/credit cost -> bank earnings.",
        "Use sector-level borrower exposure where available. Test aluminium returns "
        "and shocks against loan growth, slippages, GNPA/NNPA, credit cost and "
        "corporate/MSME credit. Control for GDP/industrial production, rates, "
        "NIFTY and INR.",
        (
            "aluminium return",
            "aluminium volatility",
            "industrial-production proxy",
            "corporate credit growth",
            "MSME credit growth",
            "slippages",
            "credit cost",
        ),
        (
            "aluminium price shocks",
            "industrial-cycle changes",
            "auto/infrastructure demand changes",
            "major aluminium supply disruptions",
        ),
        ("1D", "1W", "1M", "1Q", "6M"),
    ),
    "Copper": _mc(
        "Copper",
        "Electrical, infrastructure, manufacturing and capex credit-cycle signal.",
        "Indirect exposure through borrowers in electrical equipment, power, "
        "renewables, construction, industrial manufacturing, telecom and "
        "technology. Copper is a borrower-economics variable rather than a direct "
        "bank input.",
        "Copper -> industrial/electrical capex and borrower margins -> working "
        "capital/term-loan demand -> repayment capacity -> asset quality and "
        "credit costs.",
        "Combine copper price/volatility with industrial production, corporate "
        "credit growth and sectoral exposure. Test lagged regression and event "
        "windows. Measure incremental information after controlling for NIFTY, "
        "rates and broad economic activity.",
        (
            "copper return",
            "copper volatility",
            "industrial-production proxy",
            "corporate credit growth",
            "project-finance activity",
            "credit cost",
        ),
        (
            "global manufacturing changes",
            "grid/renewable capex",
            "infrastructure spending",
            "copper supply disruptions",
        ),
        ("1D", "1W", "1M", "1Q", "6M"),
    ),
    "Crude Oil": _mc(
        "Crude Oil",
        "Inflation, household purchasing-power, corporate-margin and interest-rate signal.",
        "Broad indirect exposure through retail customers, transport/logistics "
        "borrowers, oil-sensitive corporates, MSMEs, inflation, monetary policy "
        "and loan demand.",
        "Crude -> fuel/inflation -> household real income and corporate margins -> "
        "loan demand/repayment; crude -> inflation expectations -> policy rates/"
        "bond yields -> NIM, treasury and valuation.",
        "Test asymmetric oil shocks on retail/corporate credit growth, slippages, "
        "credit cost, NIM and stock returns. Include CPI, USD/INR, policy rates, "
        "PMI/GDP and NIFTY controls. Separate demand and funding-cost channels.",
        (
            "Brent/WTI return",
            "oil volatility",
            "CPI",
            "USD/INR",
            "policy rate",
            "NIM",
            "credit growth",
            "credit cost",
        ),
        (
            "OPEC+ decisions",
            "geopolitical supply shocks",
            "fuel-price changes",
            "inflation surprises",
            "RBI policy response",
        ),
        ("1D", "1W", "1M", "1Q", "6M"),
    ),
    "Electricity": _mc(
        "Electricity",
        "Industrial operating-cost, household-cost and infrastructure-credit signal.",
        "Indirect exposure through borrowers' electricity-intensive operations, "
        "household expenses and power/infrastructure investment. It is not a "
        "primary ICICI Bank operating cost.",
        "Electricity price/reliability -> borrower margins and cash flow -> "
        "working-capital demand and repayment quality; power infrastructure -> "
        "project finance/corporate credit opportunities.",
        "Use sector-level electricity intensity where available. Test regional "
        "power-price/demand proxies against corporate/MSME credit, project finance, "
        "slippages and credit costs, controlling for industrial activity and rates.",
        (
            "industrial power-price proxy",
            "power demand",
            "industrial production",
            "corporate/MSME credit growth",
            "project-finance activity",
            "credit cost",
        ),
        (
            "power shortages",
            "tariff changes",
            "grid investment",
            "renewable-energy investment",
            "major industrial outages",
        ),
        ("1D", "1W", "1M", "1Q"),
    ),
    "Gold": _mc(
        "Gold",
        "Savings, wealth, safe-haven and treasury/market-services signal.",
        "More meaningful than most commodities because ICICI Bank has retail "
        "customers, wealth/investment distribution and global-market/bullion "
        "activities. Gold also affects household asset allocation and risk sentiment.",
        "Gold -> household wealth/savings allocation -> deposits/investments and "
        "credit behaviour; gold -> risk sentiment/liquidity -> market activity/"
        "treasury conditions; gold -> bullion-related customer flows.",
        "Separate direct gold/bullion activity from macro safe-haven effects. Test "
        "gold returns against deposits, retail credit, investment/wealth activity, "
        "treasury income and stock returns. Control for rates, USD/INR, NIFTY and "
        "liquidity.",
        (
            "gold return",
            "gold volatility",
            "deposit growth",
            "retail credit growth",
            "wealth/investment activity",
            "treasury income",
        ),
        (
            "central-bank rate decisions",
            "inflation shocks",
            "geopolitical risk",
            "large gold-price moves",
            "household savings-flow changes",
        ),
        ("1D", "1W", "1M", "1Q", "6M"),
    ),
    "NIFTY 50": _mc(
        "NIFTY 50",
        "Core Indian equity-market, liquidity and financial-sector benchmark.",
        "Direct listed-equity exposure through ICICI Bank's beta, financial-sector "
        "rotation, liquidity and valuation. Indirectly captures the Indian growth "
        "and credit cycle.",
        "NIFTY -> liquidity/risk appetite -> ICICIBANK valuation and flows; "
        "economic cycle -> corporate/retail credit demand -> bank earnings and "
        "asset quality.",
        "Calculate rolling correlation, beta, downside beta, relative strength, "
        "drawdown and residual return. Separately model fundamentals using deposit "
        "growth, loan growth, NIM, credit costs, asset quality and rates.",
        (
            "NIFTY return",
            "rolling beta",
            "bank-sector relative strength",
            "volume",
            "volatility",
            "drawdown",
        ),
        (
            "RBI policy",
            "Union Budget/fiscal policy",
            "banking regulation",
            "index rebalancing",
            "major market risk-off events",
            "ICICI Bank earnings",
        ),
        ("5m", "15m", "1H", "1D", "1W", "1M", "1Q", "1Y"),
    ),
    "Natural Gas": _mc(
        "Natural Gas",
        "Industrial-energy, chemical and power-sector credit-cycle signal.",
        "Indirect exposure through borrowers in power, chemicals, fertilisers, "
        "manufacturing and energy-intensive industries.",
        "Natural gas -> industrial input/energy cost -> borrower margins and "
        "working capital -> credit demand/asset quality -> ICICI Bank.",
        "Use gas returns with sectoral credit, industrial production, PMI and "
        "asset-quality variables. Test lags and asymmetric shocks while controlling "
        "for crude, electricity, rates and NIFTY.",
        (
            "natural-gas return",
            "gas volatility",
            "industrial-production proxy",
            "sectoral credit growth",
            "slippages",
            "credit cost",
        ),
        (
            "LNG/gas supply disruptions",
            "global gas-price shocks",
            "gas-pricing policy",
            "industrial demand changes",
        ),
        ("1D", "1W", "1M", "1Q"),
    ),
    "Silver": _mc(
        "Silver",
        "Industrial-cycle, precious-metals and household-wealth signal.",
        "Indirect exposure through industrial borrowers, electronics/solar "
        "investment, household asset allocation and risk sentiment.",
        "Silver -> industrial/electrification cycle -> borrower activity and "
        "investment -> credit demand; silver -> household asset allocation/risk "
        "sentiment -> deposits and investment flows.",
        "Compare silver with copper, gold, industrial production, deposits and "
        "credit growth. Use multivariate lag analysis to determine whether silver "
        "adds information beyond broader macro factors.",
        (
            "silver return",
            "silver volatility",
            "gold/silver ratio",
            "industrial-production proxy",
            "credit growth",
            "deposit growth",
        ),
        (
            "industrial-demand shocks",
            "solar/electronics demand changes",
            "precious-metal shocks",
            "household investment-flow changes",
        ),
        ("1D", "1W", "1M", "1Q", "6M"),
    ),
    "Zinc": _mc(
        "Zinc",
        "Steel, construction, infrastructure and manufacturing-credit signal.",
        "Indirect exposure through corporate/MSME borrowers in construction, "
        "infrastructure, auto, engineering and manufacturing.",
        "Zinc -> steel/galvanising/construction cycle -> borrower sales and "
        "working-capital needs -> credit demand and repayment quality -> bank.",
        "Use zinc and steel returns with construction and industrial-production "
        "proxies. Test lagged effects on sectoral credit growth, slippages and "
        "credit cost while controlling for rates and NIFTY.",
        (
            "zinc return",
            "steel return",
            "construction proxy",
            "industrial-production proxy",
            "corporate/MSME credit growth",
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
    symbol="ICICIBANK",
    company_name="ICICI Bank Limited",
    sector="Banking / Financial Services",
    industry_character=(
        "Diversified private-sector banking platform with retail, business banking, "
        "corporate banking, international banking, treasury and financial-market "
        "activities. Its core economic character is the transformation of deposits "
        "and market funding into loans and investments, with profitability determined "
        "by NIM, fees, operating efficiency, credit costs, asset quality, capital "
        "and treasury/market conditions."
    ),
    business_character=(
        "Multi-engine banking character: retail banking and mortgages, personal and "
        "vehicle finance, cards and payments, business banking, corporate/wholesale "
        "banking, trade and cash management, global markets, investment banking, "
        "capital markets/custody and treasury. ICICI Bank's official business "
        "platform also includes forex, derivatives, bullion, bonds and treasury "
        "research, making market conditions relevant alongside the lending cycle. "
        "The core chain is deposits/liquidity -> credit and investment deployment "
        "-> yield/funding cost -> NIM and fee income -> credit cost/capital -> ROA/ROE."
    ),
    demand_drivers=(
        "retail credit demand",
        "home-loan and mortgage activity",
        "personal and consumer finance",
        "vehicle finance",
        "credit-card and payments activity",
        "MSME and business-banking demand",
        "corporate working-capital demand",
        "project and infrastructure finance",
        "trade finance",
        "cash-management activity",
        "wealth and investment activity",
        "economic growth and formalisation",
        "digital banking adoption",
        "international/NRI banking activity",
    ),
    revenue_drivers=(
        "net interest income",
        "net interest margin",
        "retail loan growth",
        "business-banking loan growth",
        "corporate loan growth",
        "SME/MSME credit",
        "home loans",
        "personal and vehicle loans",
        "credit-card balances and payments",
        "transaction-banking fees",
        "trade-finance fees",
        "cash-management fees",
        "forex and derivatives activity",
        "investment-banking fees",
        "capital-markets/custody activity",
        "treasury income",
        "wealth-management and investment distribution",
    ),
    cost_drivers=(
        "deposit funding cost",
        "cost of borrowings",
        "employee costs",
        "branch and infrastructure",
        "technology and digital infrastructure",
        "credit provisions",
        "fraud and operational losses",
        "regulatory/compliance costs",
        "customer acquisition",
        "payment-network costs",
        "cybersecurity",
        "liquidity-management costs",
        "data and cloud infrastructure",
    ),
    supply_chain_character=(
        "retail depositors",
        "retail borrowers",
        "corporate and institutional borrowers",
        "MSMEs and business customers",
        "home-loan ecosystem",
        "auto and commercial-vehicle ecosystem",
        "payment networks",
        "merchant ecosystem",
        "fintech and technology partners",
        "cloud/data/cybersecurity providers",
        "financial-market counterparties",
        "insurance/investment-product partners",
        "global banking and correspondent network",
    ),
    strategic_drivers=(
        "deposit franchise",
        "CASA growth",
        "quality retail-credit growth",
        "business banking and SME expansion",
        "corporate relationship banking",
        "digital banking",
        "payments and transaction banking",
        "wealth management",
        "global markets and treasury",
        "risk-adjusted underwriting",
        "asset-quality resilience",
        "technology modernisation",
        "operating efficiency",
        "capital adequacy",
        "cross-sell and customer lifetime value",
        "subsidiary ecosystem",
    ),
    key_indicators=(
        "total deposits",
        "CASA deposits",
        "retail loan growth",
        "business-banking loan growth",
        "corporate loan growth",
        "home-loan growth",
        "credit-card activity",
        "net interest income",
        "net interest margin",
        "cost-to-income ratio",
        "GNPA",
        "NNPA",
        "slippages",
        "provision coverage",
        "credit cost",
        "capital adequacy/CET1",
        "return on assets",
        "return on equity",
        "liquidity indicators",
        "treasury income",
        "ICICIBANK return, volume and relative strength",
    ),
    key_events=(
        "quarterly and annual results",
        "RBI monetary-policy decisions",
        "RBI banking/regulatory changes",
        "deposit-rate changes",
        "lending-rate changes",
        "credit-policy changes",
        "large corporate-credit events",
        "asset-quality/slippage disclosures",
        "capital and funding-market events",
        "technology/digital-platform changes",
        "cybersecurity/fraud events",
        "housing/real-estate cycle changes",
        "major macro/inflation shocks",
        "subsidiary-related events",
        "management guidance and strategy updates",
    ),
    market_characters=MARKET_CHARACTERS,
)


def get_company_character() -> CompanyCharacter:
    """Return the complete ICICI Bank company character."""
    return COMPANY_CHARACTER


def get_market_character(market: str) -> MarketCharacter:
    """Return ICICI Bank's character/exposure model for one tracked market."""
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
    Validate structure only.

    Historical linkage, rank, percentage change, probability, correlation
    results and trading decisions are deliberately outside this module.
    """
    if COMPANY_CHARACTER.symbol != "ICICIBANK":
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
    print("ICICIBANK character valid:", validate_character())
    print("Tracked markets:", ", ".join(TRACKED_MARKETS))
    print("Company:", COMPANY_CHARACTER.company_name)
