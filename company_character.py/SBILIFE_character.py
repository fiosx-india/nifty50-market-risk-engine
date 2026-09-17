"""
SBILIFE Character Engine
------------------------
Character layer for SBI Life Insurance Company Limited.

This module separates:
    Company Character
        -> life-insurance business identity
        -> distribution and customer model
        -> revenue/value drivers
        -> investment/ALM sensitivity
        -> regulatory and operating risks

    Company Character
        -> 9 tracked Market Characters
        -> later empirical/historical calculation layer

The supplied CSV may contain RANK, PCT_CHANGE, LINKAGE_SCORE and RELATION.
Those values are intentionally NOT hard-coded here.

Actual correlation, beta, lagged impact, linkage strength, probability and
other quantitative outputs must be calculated later from observed data.
"""

from dataclasses import dataclass, field
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
    direct_exposure: Tuple[str, ...] = ()
    indirect_exposure: Tuple[str, ...] = ()
    impact_channels: Tuple[str, ...] = ()
    supply_chain_links: Tuple[str, ...] = ()
    demand_channels: Tuple[str, ...] = ()
    cost_channels: Tuple[str, ...] = ()
    strategic_channels: Tuple[str, ...] = ()
    key_indicators: Tuple[str, ...] = ()
    event_signals: Tuple[str, ...] = ()
    calculation_logic: Tuple[str, ...] = ()


@dataclass(frozen=True)
class CompanyCharacter:
    symbol: str
    company_name: str
    business_character: str
    core_businesses: Tuple[str, ...]
    operating_model: Tuple[str, ...]
    revenue_and_cashflow_drivers: Tuple[str, ...]
    cost_drivers: Tuple[str, ...]
    supply_chain_dependencies: Tuple[str, ...]
    demand_dependencies: Tuple[str, ...]
    strategic_themes: Tuple[str, ...]
    key_indicators: Tuple[str, ...]
    event_signals: Tuple[str, ...]
    risk_channels: Tuple[str, ...]
    market_characters: Dict[str, MarketCharacter] = field(default_factory=dict)


def _mc(
    market: str,
    character: str,
    *,
    direct: Tuple[str, ...] = (),
    indirect: Tuple[str, ...] = (),
    channels: Tuple[str, ...] = (),
    supply: Tuple[str, ...] = (),
    demand: Tuple[str, ...] = (),
    cost: Tuple[str, ...] = (),
    strategy: Tuple[str, ...] = (),
    indicators: Tuple[str, ...] = (),
    events: Tuple[str, ...] = (),
    logic: Tuple[str, ...] = (),
) -> MarketCharacter:
    return MarketCharacter(
        market=market,
        character=character,
        direct_exposure=direct,
        indirect_exposure=indirect,
        impact_channels=channels,
        supply_chain_links=supply,
        demand_channels=demand,
        cost_channels=cost,
        strategic_channels=strategy,
        key_indicators=indicators,
        event_signals=events,
        calculation_logic=logic,
    )


COMPANY_CHARACTER = CompanyCharacter(
    symbol="SBILIFE",
    company_name="SBI Life Insurance Company Limited",
    business_character=(
        "SBI Life is a life-insurance and long-term savings/protection business. "
        "Its character is driven primarily by protection, savings, ULIP/linked "
        "and non-linked products, annuity and retirement solutions, customer "
        "persistency, new-business quality, distribution productivity, "
        "investment portfolio performance, asset-liability management, "
        "solvency and regulatory conditions. The company has a broad distribution "
        "model including bancassurance, agency, branches, partners and digital "
        "channels. SBI's relationship is strategically important to the "
        "distribution ecosystem, while the insurer remains an independently "
        "regulated life-insurance business."
    ),
    core_businesses=(
        "Individual life protection",
        "Term insurance",
        "Savings and non-linked insurance",
        "ULIP/linked insurance",
        "Annuity and retirement solutions",
        "Pension products",
        "Child and life-stage products",
        "Group insurance",
        "Micro-insurance",
        "Health-related insurance offerings",
        "Bancassurance distribution",
        "Agency distribution",
        "Partner distribution",
        "Digital insurance journeys",
        "Investment and policyholder asset management",
    ),
    operating_model=(
        "Long-duration life-insurance contracts",
        "Premium collection over multi-year policy lives",
        "Risk pooling across policyholders",
        "Asset-liability management",
        "Investment of policyholder and shareholder funds",
        "Bancassurance-led distribution",
        "Agency and partner distribution",
        "Branch and rural/semi-urban reach",
        "Digital acquisition and servicing",
        "Actuarial pricing and reserving",
        "Regulated solvency framework",
        "Long-term customer persistency model",
    ),
    revenue_and_cashflow_drivers=(
        "Annualised premium equivalent",
        "Individual rated premium",
        "New business premium",
        "Gross written premium",
        "Renewal premium",
        "Persistency",
        "Number of new policies",
        "Protection business growth",
        "Savings business growth",
        "ULIP business and market-linked assets",
        "Annuity/pension business",
        "Investment income",
        "Assets under management",
        "Embedded value",
        "Value of new business",
        "Distribution productivity",
    ),
    cost_drivers=(
        "Acquisition commissions",
        "Distribution expenses",
        "Employee costs",
        "Branch and infrastructure costs",
        "Technology and digital investment",
        "Policy servicing costs",
        "Claims",
        "Actuarial reserves",
        "Investment-management costs",
        "Regulatory/compliance costs",
        "Marketing and customer-acquisition costs",
    ),
    supply_chain_dependencies=(
        "Banking distribution partnerships",
        "Agency network",
        "Corporate/financial distribution partners",
        "Technology platforms",
        "Digital onboarding systems",
        "Cloud/data infrastructure",
        "Actuarial and analytics systems",
        "Investment-management ecosystem",
        "Third-party service providers",
        "Healthcare/medical underwriting ecosystem",
    ),
    demand_dependencies=(
        "Household income growth",
        "Financial awareness",
        "Protection gap",
        "Savings propensity",
        "Retirement planning",
        "Middle-class expansion",
        "Rural and semi-urban penetration",
        "Tax and savings incentives",
        "Capital-market participation",
        "Digital insurance adoption",
        "Customer trust and persistency",
    ),
    strategic_themes=(
        "Profitable growth",
        "Protection penetration",
        "Savings and retirement solutions",
        "Bancassurance scale",
        "Agency productivity",
        "Rural and semi-urban expansion",
        "Digital distribution",
        "Customer persistency",
        "Product innovation",
        "Data and AI-enabled servicing",
        "Asset-liability management",
        "Solvency and financial strength",
        "Responsible selling",
    ),
    key_indicators=(
        "Individual Rated Premium",
        "Annualised Premium Equivalent",
        "New Business Premium",
        "Gross Written Premium",
        "Value of New Business",
        "VoNB margin",
        "Embedded Value",
        "Assets under Management",
        "13th-month persistency",
        "61st-month persistency",
        "Number of new policies",
        "In-force policies",
        "In-force lives covered",
        "Bancassurance share",
        "Agency productivity",
        "Digital sourcing",
        "Claim settlement ratio",
        "Solvency ratio",
        "Expense ratio",
        "ULIP surrender ratio",
    ),
    event_signals=(
        "IRDAI regulation changes",
        "New product launches",
        "Product repricing",
        "Tax-policy changes affecting insurance",
        "Bancassurance partnership changes",
        "SBI/YONO distribution developments",
        "Agency expansion",
        "Digital-platform launches",
        "Major persistency changes",
        "Solvency changes",
        "Large investment-market movements",
        "Interest-rate regime changes",
        "Major claim or mortality events",
        "Technology transformation",
        "Customer/regulatory conduct developments",
    ),
    risk_channels=(
        "Interest-rate risk",
        "Equity-market investment risk",
        "Credit-spread and bond-market risk",
        "Asset-liability mismatch",
        "Persistency risk",
        "Mortality risk",
        "Longevity risk",
        "Regulatory risk",
        "Mis-selling/conduct risk",
        "Distribution concentration",
        "Technology/cyber risk",
        "Market-linked product volatility",
        "Inflation and household affordability",
        "Reputational risk",
    ),
)


MARKET_CHARACTERS: Dict[str, MarketCharacter] = {
    "NIFTY 50": _mc(
        "NIFTY 50",
        "Broad equity-market and Indian economic-cycle character. For SBI Life, "
        "NIFTY can influence valuation, investor risk appetite, consumer wealth, "
        "savings behaviour and the performance of market-linked investment books.",
        direct=("Equity-market valuation and market beta",),
        indirect=(
            "Household wealth",
            "Savings/investment sentiment",
            "Economic growth",
            "Market-linked policy asset performance",
        ),
        channels=(
            "Equity valuation",
            "Customer wealth effect",
            "ULIP investment performance",
            "Investor risk appetite",
        ),
        demand=(
            "Protection demand",
            "Savings demand",
            "Investment-linked insurance demand",
        ),
        cost=("Investment-management and market-risk effects",),
        strategy=(
            "Long-term savings growth",
            "ULIP and market-linked product positioning",
        ),
        indicators=(
            "SBI Life return",
            "NIFTY 50 return",
            "Rolling beta",
            "Rolling correlation",
            "ULIP AUM performance",
            "Equity allocation",
        ),
        events=("Large equity-market regime changes", "Major Indian macro events"),
        logic=(
            "Measure SBI Life equity returns against NIFTY using rolling windows.",
            "Separately measure NIFTY effects on ULIP assets and customer behaviour.",
            "Control for interest rates and insurance-sector factors where available.",
        ),
    ),
    "Crude Oil": _mc(
        "Crude Oil",
        "Indirect macro and household-affordability character. Crude is not a "
        "core physical input to life insurance; its relevance comes through "
        "inflation, household disposable income, interest rates and the broader "
        "Indian economic cycle.",
        indirect=(
            "Inflation",
            "Household disposable income",
            "Transport costs",
            "Interest-rate expectations",
            "Economic growth",
        ),
        channels=(
            "Inflation transmission",
            "Household affordability",
            "Macro growth transmission",
            "Interest-rate expectations",
        ),
        demand=(
            "Protection affordability",
            "Savings capacity",
            "Premium growth",
        ),
        cost=("Office/travel/operating inflation",),
        strategy=("Protection and savings penetration",),
        indicators=(
            "Crude return",
            "CPI/inflation",
            "Real household income proxies",
            "SBI Life premium growth",
            "NIFTY return",
        ),
        events=("Large oil shocks", "Inflation regime changes"),
        logic=(
            "Do not treat crude as a direct insurance input.",
            "Test whether crude affects SBI Life through inflation and household-demand variables.",
            "Use lagged windows because insurance demand responds more slowly than commodity prices.",
        ),
    ),
    "Gold": _mc(
        "Gold",
        "Relevant indirect wealth, savings and investment-regime character. Gold "
        "competes with and complements financial savings and can reflect inflation, "
        "risk aversion and household wealth conditions. It is also relevant as a "
        "portfolio/regime signal.",
        indirect=(
            "Household savings allocation",
            "Wealth sentiment",
            "Inflation expectations",
            "Risk aversion",
            "Real rates",
        ),
        channels=(
            "Savings substitution",
            "Wealth effect",
            "Macro-regime transmission",
            "Investment sentiment",
        ),
        demand=(
            "Long-term savings products",
            "Protection/savings demand",
            "Household financialisation",
        ),
        cost=("No meaningful direct physical cost channel",),
        strategy=(
            "Financialisation of household savings",
            "Long-term wealth products",
        ),
        indicators=(
            "Gold return",
            "SBI Life return",
            "Household financial-savings proxies",
            "Insurance premium growth",
            "Real-rate proxy",
        ),
        events=("Large gold-price regimes", "Inflation/real-rate shocks"),
        logic=(
            "Treat gold as a savings and macro-regime variable.",
            "Test whether gold contains incremental information after controlling for NIFTY and rates.",
            "Separate gold's investment effect from its household-savings effect.",
        ),
    ),
    "Silver": _mc(
        "Silver",
        "Indirect industrial and commodity-cycle character. Silver has little "
        "direct operational connection to life insurance but can indicate broader "
        "commodity inflation, industrial activity and risk appetite.",
        indirect=(
            "Commodity cycle",
            "Industrial activity",
            "Inflation sentiment",
            "Risk appetite",
        ),
        channels=(
            "Macro commodity regime",
            "Inflation expectations",
            "Industrial-cycle transmission",
        ),
        demand=("Household income and financial-savings cycle",),
        strategy=("Macro-regime monitoring",),
        indicators=(
            "Silver return",
            "SBI Life return",
            "Commodity basket",
            "Inflation",
            "NIFTY return",
        ),
        events=("Commodity-cycle shocks", "Global macro shocks"),
        logic=(
            "Use silver as a secondary macro signal.",
            "Test incremental explanatory power after controlling for NIFTY, gold and crude.",
        ),
    ),
    "Natural Gas": _mc(
        "Natural Gas",
        "Indirect energy and inflation character. Natural gas is not a core "
        "insurance input; its relevance is through energy costs, inflation, "
        "industrial growth and household disposable income.",
        indirect=(
            "Energy inflation",
            "Industrial activity",
            "Household affordability",
            "Macroeconomic growth",
        ),
        channels=(
            "Inflation transmission",
            "Industrial-cycle transmission",
            "Income/affordability transmission",
        ),
        demand=(
            "Insurance affordability",
            "Savings capacity",
            "Corporate/group-insurance demand",
        ),
        cost=("Operating and travel costs",),
        strategy=("Financial-inclusion and protection penetration",),
        indicators=(
            "Natural gas return",
            "Inflation",
            "Industrial production",
            "Premium growth",
            "Household-income proxies",
        ),
        events=("Large gas shocks", "Energy-inflation changes"),
        logic=(
            "Model natural gas through macro variables rather than direct company costs.",
            "Test lagged relationships with premium growth and market returns.",
        ),
    ),
    "Electricity": _mc(
        "Electricity",
        "Indirect operating-cost and economic-activity character. Electricity "
        "does not drive SBI Life revenue directly, but affects office/branch, "
        "technology and digital infrastructure costs while also reflecting the "
        "broader economic activity that supports insurance demand.",
        indirect=(
            "Office and branch utilities",
            "Digital infrastructure",
            "Data/technology operations",
            "Economic activity",
        ),
        channels=(
            "Operating-cost transmission",
            "Digital-service cost",
            "Economic-growth signal",
        ),
        supply=(
            "Grid electricity",
            "Data centres",
            "Telecom/cloud infrastructure",
        ),
        demand=(
            "Economic activity",
            "Digital adoption",
            "Financial inclusion",
        ),
        cost=(
            "Branch operations",
            "Technology infrastructure",
            "Digital servicing",
        ),
        strategy=("Digital insurance expansion",),
        indicators=(
            "Electricity price",
            "SBI Life operating expense",
            "Digital adoption",
            "Branch costs",
            "Economic activity",
        ),
        events=("Large power-price changes", "Industrial/economic activity shifts"),
        logic=(
            "Treat electricity primarily as an operating-cost and macro variable.",
            "Do not infer a direct insurance-revenue relationship from electricity prices alone.",
        ),
    ),
    "Copper": _mc(
        "Copper",
        "Indirect industrial-cycle and technology-infrastructure signal. Copper "
        "has little direct physical relevance to insurance, but can indicate "
        "industrial investment, digital infrastructure and broader economic activity.",
        indirect=(
            "Industrial capex",
            "Telecom/data infrastructure",
            "Economic growth",
            "Commodity inflation",
        ),
        channels=(
            "Industrial-cycle transmission",
            "Technology-infrastructure signal",
            "Macro inflation",
        ),
        demand=(
            "Corporate insurance",
            "Group insurance",
            "Household income through economic activity",
        ),
        cost=("Technology and infrastructure procurement",),
        strategy=("Digital distribution and technology investment",),
        indicators=(
            "Copper return",
            "Industrial production",
            "SBI Life premium growth",
            "Corporate-insurance indicators",
        ),
        events=("Copper/industrial-cycle shocks",),
        logic=(
            "Use copper as an indirect economic-cycle variable.",
            "Control for NIFTY and industrial-production data before attributing an effect.",
        ),
    ),
    "Aluminium": _mc(
        "Aluminium",
        "Indirect industrial, infrastructure and inflation character. Aluminium "
        "does not form a core insurance input, but can signal manufacturing activity, "
        "construction and household/corporate economic conditions.",
        indirect=(
            "Manufacturing cycle",
            "Construction activity",
            "Commodity inflation",
            "Economic growth",
        ),
        channels=(
            "Industrial-cycle transmission",
            "Inflation transmission",
            "Corporate activity",
        ),
        demand=(
            "Household financial capacity",
            "Corporate insurance demand",
            "Group-insurance demand",
        ),
        cost=("Limited office/infrastructure procurement effects",),
        strategy=("Financial inclusion and long-term savings penetration",),
        indicators=(
            "Aluminium return",
            "Industrial production",
            "Construction indicators",
            "Premium growth",
            "NIFTY return",
        ),
        events=("Aluminium shocks", "Major industrial-cycle changes"),
        logic=(
            "Treat aluminium as an indirect macro/industrial signal.",
            "Test whether it adds information beyond NIFTY, crude and interest rates.",
        ),
    ),
    "Zinc": _mc(
        "Zinc",
        "Indirect industrial and construction-cycle signal. Zinc has no material "
        "direct insurance input connection; its usefulness is as a proxy for "
        "manufacturing, construction and commodity-cycle conditions.",
        indirect=(
            "Construction cycle",
            "Manufacturing cycle",
            "Commodity inflation",
        ),
        channels=(
            "Industrial-cycle transmission",
            "Inflation signal",
        ),
        demand=(
            "Employment/income cycle",
            "Corporate activity",
            "Household savings capacity",
        ),
        cost=("Minimal direct operating impact",),
        strategy=("Macro and demand-regime monitoring",),
        indicators=(
            "Zinc return",
            "Construction indicators",
            "Industrial production",
            "Premium growth",
            "SBI Life return",
        ),
        events=("Zinc/industrial shocks",),
        logic=(
            "Use zinc only as an indirect macro/industrial signal.",
            "Check incremental information after controlling for NIFTY and other macro variables.",
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
    """Return the complete SBI Life company character."""
    return COMPANY_CHARACTER


def get_market_character(market: str) -> MarketCharacter:
    """Return one market character by exact market name."""
    try:
        return MARKET_CHARACTERS[market]
    except KeyError as exc:
        raise ValueError(
            f"Unsupported market: {market!r}. "
            f"Supported markets: {', '.join(TRACKED_MARKETS)}"
        ) from exc


def get_all_market_characters() -> Dict[str, MarketCharacter]:
    """Return all nine market characters."""
    return dict(MARKET_CHARACTERS)


def validate_character() -> Dict[str, object]:
    """Structural validation; empirical linkage is calculated later."""
    missing = [m for m in TRACKED_MARKETS if m not in MARKET_CHARACTERS]
    extra = [m for m in MARKET_CHARACTERS if m not in TRACKED_MARKETS]

    return {
        "symbol": COMPANY_CHARACTER.symbol,
        "company_name": COMPANY_CHARACTER.company_name,
        "tracked_market_count": len(TRACKED_MARKETS),
        "market_character_count": len(MARKET_CHARACTERS),
        "missing_markets": missing,
        "extra_markets": extra,
        "valid": (
            len(TRACKED_MARKETS) == 9
            and not missing
            and not extra
            and bool(COMPANY_CHARACTER.core_businesses)
            and bool(COMPANY_CHARACTER.key_indicators)
        ),
    }


if __name__ == "__main__":
    result = validate_character()

    print("SBILIFE CHARACTER VALIDATION")
    print("=" * 34)
    print(f"Company: {result['company_name']}")
    print(f"Markets: {result['market_character_count']}/9")
    print(f"Valid: {result['valid']}")

    if result["missing_markets"]:
        print("Missing:", result["missing_markets"])
    if result["extra_markets"]:
        print("Extra:", result["extra_markets"])

    print("\nMARKET CHARACTERS")
    print("=" * 34)

    for market in TRACKED_MARKETS:
        mc = MARKET_CHARACTERS[market]
        print(f"\n[{market}]")
        print(mc.character)
        print("Direct:", ", ".join(mc.direct_exposure) or "None")
        print("Indirect:", ", ".join(mc.indirect_exposure) or "None")
