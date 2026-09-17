"""
HDFCLIFE — Company Character & 9-Market Research Model

Purpose
-------
Define the real business character of HDFC Life and the research framework for
its exposure to the project's 9 tracked markets.

This file is a CHARACTER / RESEARCH DEFINITION layer.
It intentionally does NOT hard-code:
    - rank
    - daily percentage change
    - linkage score
    - positive/negative relation
    - probability
    - BUY/SELL/HOLD

Those values belong to a later historical calculation / evidence engine.
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
        "Long-duration asset-allocation and real-economy savings signal.",
        "Primarily indirect exposure. Aluminium affects HDFC Life through the "
        "industrial/construction cycle, household income, corporate activity and "
        "investment sentiment rather than as a material operating input.",
        "Aluminium -> industrial/construction activity and borrower/household income "
        "-> savings capacity and financialisation -> protection/savings/pension "
        "product demand -> new business and persistency.",
        "Use aluminium as a secondary macro factor. Test lagged aluminium returns "
        "against HDFC Life's premium growth, product mix and stock return after "
        "controlling for NIFTY, rates, inflation and industrial activity. Test "
        "whether commodity shocks affect household savings behaviour with a lag.",
        (
            "aluminium return",
            "industrial-production proxy",
            "household consumption proxy",
            "new business premium",
            "individual APE",
            "HDFCLIFE return",
        ),
        (
            "large aluminium-price shocks",
            "construction/industrial-cycle changes",
            "infrastructure investment",
            "household income shocks",
        ),
        ("1D", "1W", "1M", "1Q", "6M", "1Y"),
    ),
    "Copper": _mc(
        "Copper",
        "Electrification, infrastructure and industrial-cycle macro signal.",
        "Indirect exposure through economic growth, corporate investment, "
        "household income and financial-market sentiment. Copper is not a direct "
        "HDFC Life operating input.",
        "Copper -> industrial/electrification capex -> employment/income and business "
        "confidence -> household savings/protection demand -> insurance growth.",
        "Measure copper as a macro/industrial factor using lagged regression and "
        "event studies. Control for NIFTY, rates, inflation and GDP/PMI proxies. "
        "Compare commodity shocks with premium growth and stock-market residual "
        "returns.",
        (
            "copper return",
            "industrial-production proxy",
            "PMI",
            "new business premium",
            "APE",
            "HDFCLIFE relative return",
        ),
        (
            "global manufacturing changes",
            "infrastructure/renewable capex",
            "employment-cycle changes",
            "copper supply disruptions",
        ),
        ("1D", "1W", "1M", "1Q", "6M"),
    ),
    "Crude Oil": _mc(
        "Crude Oil",
        "Inflation, household purchasing-power and interest-rate macro signal.",
        "Indirect but potentially broad exposure because oil affects inflation, "
        "household disposable income, transport costs, corporate earnings, bond "
        "yields and monetary policy.",
        "Crude -> fuel/inflation -> household real disposable income and savings "
        "capacity; crude -> inflation expectations -> rates/bond yields -> insurer "
        "investment returns and product economics -> new business/persistency.",
        "Test asymmetric oil shocks against premium growth, product mix, margins, "
        "investment income and stock returns. Include CPI, USD/INR, bond yields, "
        "RBI policy and NIFTY as controls. Use lag structures because insurance "
        "demand is not normally an intraday commodity response.",
        (
            "Brent/WTI return",
            "oil volatility",
            "CPI/inflation",
            "10Y government yield",
            "new business premium",
            "HDFCLIFE return",
        ),
        (
            "OPEC+ decisions",
            "geopolitical supply shocks",
            "fuel-price changes",
            "inflation surprises",
            "RBI policy response",
        ),
        ("1D", "1W", "1M", "1Q", "6M", "1Y"),
    ),
    "Electricity": _mc(
        "Electricity",
        "Household-cost, business-confidence and infrastructure signal.",
        "Primarily indirect exposure through household budgets, employment, "
        "corporate profitability and digital/branch operating infrastructure.",
        "Electricity cost/reliability -> household and corporate cash-flow conditions "
        "-> savings/protection affordability and insurance distribution activity -> "
        "premium growth; power infrastructure -> economic development -> insurance "
        "penetration.",
        "Use regional electricity-price and demand proxies rather than assuming a "
        "direct company cost relationship. Test lagged relationships with premium "
        "growth, household savings proxies, claims trends and operating expense.",
        (
            "power-price proxy",
            "power demand",
            "CPI",
            "household consumption proxy",
            "premium growth",
            "operating expense",
        ),
        (
            "power tariff changes",
            "major power disruptions",
            "renewable investment",
            "industrial power-demand changes",
        ),
        ("1D", "1W", "1M", "1Q"),
    ),
    "Gold": _mc(
        "Gold",
        "Savings, wealth-preservation, risk-sentiment and asset-allocation signal.",
        "Potentially meaningful indirect exposure because gold competes for household "
        "savings/investment allocation while also signalling risk aversion, inflation "
        "expectations and wealth effects. Gold can therefore interact with savings, "
        "investment-linked insurance and annuity demand.",
        "Gold -> household wealth/savings allocation and risk sentiment -> insurance "
        "versus alternative-asset allocation -> product mix and new business; gold -> "
        "inflation/risk expectations -> bond/equity markets -> insurer investment "
        "portfolio and embedded-value dynamics.",
        "Separate the household asset-allocation channel from the macro safe-haven "
        "channel. Compare gold with premium growth, ULIP/mkt-linked product mix, "
        "guaranteed/savings products, AUM, EV and stock returns. Control for rates, "
        "NIFTY and USD/INR.",
        (
            "gold return",
            "gold volatility",
            "gold/financial-asset allocation proxy",
            "ULIP/product mix",
            "AUM",
            "embedded value",
        ),
        (
            "large gold-price moves",
            "inflation shocks",
            "geopolitical risk",
            "household savings-flow changes",
            "interest-rate changes",
        ),
        ("1D", "1W", "1M", "1Q", "6M"),
    ),
    "NIFTY 50": _mc(
        "NIFTY 50",
        "Core Indian equity-market, household-wealth and valuation benchmark.",
        "Direct market exposure through HDFC Life's listed equity beta and "
        "indirect exposure through household wealth, financialisation, investment-"
        "linked products and equity-linked asset performance.",
        "NIFTY -> equity risk appetite/liquidity -> HDFCLIFE valuation and investor "
        "flows; NIFTY -> household wealth and market-linked savings -> ULIP/product "
        "demand; NIFTY -> insurer investment portfolio -> EV/AUM effects.",
        "Calculate rolling correlation, beta, downside beta, relative strength, "
        "drawdown and residual return. Separately model fundamental channels using "
        "rates, APE, premium growth, AUM, EV and product mix. Do not treat a stock "
        "correlation as proof of business causation.",
        (
            "NIFTY return",
            "rolling beta",
            "financial-sector relative strength",
            "market volatility",
            "AUM",
            "embedded value",
            "ULIP performance",
        ),
        (
            "RBI policy",
            "SEBI/IRDAI regulatory changes",
            "Union Budget",
            "major index rebalancing",
            "large market corrections/rallies",
        ),
        ("5m", "15m", "1H", "1D", "1W", "1M", "1Q", "1Y"),
    ),
    "Natural Gas": _mc(
        "Natural Gas",
        "Industrial-energy and household-cost macro signal.",
        "Indirect exposure through industrial activity, inflation, household "
        "budgets and corporate profitability. It is not a core direct input to "
        "life-insurance operations.",
        "Natural gas -> industrial/energy cost -> inflation and business activity "
        "-> household income/savings -> insurance demand; gas -> inflation/rates -> "
        "investment portfolio and valuation.",
        "Use gas as a secondary macro factor. Test lagged effects on premium growth "
        "and stock returns with inflation, rates, crude and NIFTY controls. Avoid "
        "attributing an insurance outcome to gas alone.",
        (
            "natural-gas return",
            "gas volatility",
            "industrial-production proxy",
            "CPI",
            "premium growth",
            "HDFCLIFE return",
        ),
        (
            "LNG/gas supply disruptions",
            "global gas-price shocks",
            "industrial energy-policy changes",
            "inflation shocks",
        ),
        ("1D", "1W", "1M", "1Q"),
    ),
    "Silver": _mc(
        "Silver",
        "Precious/industrial-metals and household asset-allocation signal.",
        "Indirect exposure through household investment allocation, industrial "
        "growth and risk sentiment. Silver can compete with other real assets "
        "within household savings behaviour but is not a direct insurer input.",
        "Silver -> household asset-allocation/risk sentiment and industrial cycle "
        "-> savings behaviour -> protection/savings/investment product demand.",
        "Compare silver with gold, equity returns, rates and household savings "
        "proxies. Use lagged multivariate models to test whether silver provides "
        "independent information for HDFC Life premium growth or valuation.",
        (
            "silver return",
            "silver volatility",
            "gold/silver ratio",
            "household savings proxy",
            "premium growth",
            "HDFCLIFE relative return",
        ),
        (
            "industrial-cycle shocks",
            "precious-metal demand changes",
            "large silver-price moves",
            "household investment-flow changes",
        ),
        ("1D", "1W", "1M", "1Q", "6M"),
    ),
    "Zinc": _mc(
        "Zinc",
        "Construction, infrastructure and manufacturing-cycle macro signal.",
        "Indirect exposure through employment, income, corporate activity and "
        "infrastructure investment.",
        "Zinc -> construction/industrial activity -> employment/business income -> "
        "household savings and protection demand -> insurance growth.",
        "Use zinc as an industrial-cycle variable. Test lagged relationships with "
        "new business premium, APE, household savings and HDFCLIFE returns while "
        "controlling for NIFTY, rates and broader industrial activity.",
        (
            "zinc return",
            "steel/construction proxy",
            "industrial-production proxy",
            "premium growth",
            "APE",
            "HDFCLIFE return",
        ),
        (
            "infrastructure spending",
            "construction-cycle changes",
            "manufacturing-cycle changes",
            "zinc supply disruptions",
        ),
        ("1D", "1W", "1M", "1Q", "6M"),
    ),
}


COMPANY_CHARACTER = CompanyCharacter(
    symbol="HDFCLIFE",
    company_name="HDFC Life Insurance Company Limited",
    sector="Life Insurance / Financial Services",
    industry_character=(
        "Long-duration life-insurance and financial-protection business. HDFC Life "
        "serves protection, pension, savings, investment, annuity and health needs. "
        "Its economics are driven by new business quality, persistency, product mix, "
        "distribution productivity, claims/mortality and morbidity assumptions, "
        "investment returns, interest rates, capital requirements and embedded value."
    ),
    business_character=(
        "Multi-product, multi-channel life-insurance character: protection products, "
        "savings/guaranteed products, market-linked products, pension/retirement, "
        "annuity and group business distributed through bancassurance, agency, "
        "digital/direct and partner channels. The economic chain is customer need "
        "and savings capacity -> distribution -> new business -> persistency -> "
        "investment/asset performance and claims -> embedded value/profitability."
    ),
    demand_drivers=(
        "life-insurance penetration",
        "household income and savings",
        "financialisation of household savings",
        "protection awareness",
        "retirement and pension needs",
        "longevity trends",
        "health and mortality-risk awareness",
        "urbanisation and formal employment",
        "tax/regulatory environment",
        "interest-rate environment",
        "equity-market participation",
        "bancassurance reach",
        "digital insurance adoption",
    ),
    revenue_drivers=(
        "individual new business premium",
        "individual APE",
        "regular-premium business",
        "single-premium business",
        "renewal premium",
        "protection business",
        "savings and guaranteed products",
        "ULIP/market-linked products",
        "pension and annuity business",
        "group new business",
        "persistency",
        "assets under management",
        "investment income",
        "fee/margin contribution",
    ),
    cost_drivers=(
        "commissions and acquisition costs",
        "employee costs",
        "branch/distribution costs",
        "technology and digital infrastructure",
        "claims and benefits",
        "reinsurance costs",
        "investment-management costs",
        "customer servicing",
        "regulatory/compliance costs",
        "fraud and operational risk",
        "new-business overrun",
    ),
    supply_chain_character=(
        "bancassurance partners",
        "agency network",
        "corporate/group distribution",
        "brokers and intermediaries",
        "digital/direct channels",
        "insurance technology providers",
        "reinsurers",
        "asset managers and investment ecosystem",
        "hospitals/health ecosystem where applicable",
        "third-party service and claims ecosystem",
        "HDFC group distribution relationships",
    ),
    strategic_drivers=(
        "balanced product mix",
        "protection penetration",
        "retirement and annuity growth",
        "persistency improvement",
        "distribution diversification",
        "bancassurance productivity",
        "agency productivity",
        "digital acquisition and servicing",
        "pricing discipline",
        "product innovation",
        "asset-liability management",
        "embedded-value growth",
        "capital efficiency",
        "technology-led underwriting and servicing",
        "customer retention and cross-sell",
    ),
    key_indicators=(
        "new business premium",
        "individual APE",
        "individual weighted received premium",
        "group new business premium",
        "renewal premium",
        "overall new business margin",
        "new business value",
        "embedded value",
        "assets under management",
        "persistency ratios",
        "solvency ratio",
        "claim settlement/claim experience",
        "product mix",
        "protection share",
        "ULIP share",
        "annuity/pension share",
        "distribution productivity",
        "bancassurance contribution",
        "agency contribution",
        "HDFCLIFE return, volume and relative strength",
    ),
    key_events=(
        "quarterly and annual results",
        "IRDAI regulations and product rules",
        "tax-policy changes affecting insurance",
        "GST/tax changes",
        "RBI interest-rate decisions",
        "bond-yield curve changes",
        "equity-market shocks",
        "new product launches",
        "pricing changes",
        "distribution partnerships",
        "bancassurance changes",
        "agency expansion",
        "large group-business wins",
        "persistency/claim experience changes",
        "investment-portfolio events",
        "capital/solvency events",
        "cybersecurity or data-privacy events",
    ),
    market_characters=MARKET_CHARACTERS,
)


def get_company_character() -> CompanyCharacter:
    """Return the complete HDFC Life company character."""
    return COMPANY_CHARACTER


def get_market_character(market: str) -> MarketCharacter:
    """Return HDFC Life's character/exposure model for one tracked market."""
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

    Historical linkage, rank, percentage change, probability and trading
    decisions are deliberately outside this module.
    """
    if COMPANY_CHARACTER.symbol != "HDFCLIFE":
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
    print("HDFCLIFE character valid:", validate_character())
    print("Tracked markets:", ", ".join(TRACKED_MARKETS))
    print("Company:", COMPANY_CHARACTER.company_name)
