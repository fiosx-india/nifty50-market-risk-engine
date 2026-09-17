"""
SBIN Character Engine
---------------------
Character layer for State Bank of India (SBIN).

This is the company-character layer only.

SBIN is modeled as a diversified banking ecosystem:
    - Retail / personal banking
    - Rural and agriculture banking
    - SME / commercial banking
    - Corporate / wholesale banking
    - Project finance
    - International banking
    - Treasury / Global Markets
    - Government business
    - Digital banking
    - Financial-services subsidiaries and joint ventures

The nine tracked markets describe possible transmission channels.
They do NOT contain hard-coded RANK, PCT_CHANGE, LINKAGE_SCORE or RELATION.

Actual correlation, beta, lag, impact magnitude and probabilities must be
calculated later from observed company and market data.
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
    symbol="SBIN",
    company_name="State Bank of India",
    business_character=(
        "State Bank of India is a large diversified banking and financial-services "
        "ecosystem. Its core character is deposit gathering, retail and corporate "
        "lending, rural/agriculture finance, SME and commercial banking, project "
        "finance, international banking, treasury/global markets, government "
        "business and digital banking. Its economic engine is the spread between "
        "funding and lending/investment returns, adjusted for credit costs, "
        "operating efficiency, treasury performance, capital requirements and "
        "regulation. The wider SBI ecosystem adds insurance, cards, asset "
        "management, pension, capital markets and other financial-services "
        "businesses."
    ),
    core_businesses=(
        "Retail and personal banking",
        "Home loans and housing finance",
        "Personal loans",
        "Vehicle and consumer finance",
        "Agriculture and rural banking",
        "SME banking",
        "Commercial banking",
        "Corporate banking",
        "Project finance and structuring",
        "Infrastructure and large-project lending",
        "International banking",
        "Treasury and Global Markets",
        "Foreign exchange and derivatives",
        "Government banking",
        "Transaction banking",
        "Trade finance",
        "Digital banking and YONO",
        "Financial inclusion and business-correspondent network",
        "Group financial-services ecosystem",
    ),
    operating_model=(
        "Large deposit-funded banking model",
        "Retail, rural, SME and corporate credit diversification",
        "Government and institutional banking relationships",
        "Large branch and distribution network",
        "Digital banking through YONO and other channels",
        "Treasury and investment portfolio management",
        "Domestic and international operations",
        "Risk-based underwriting and provisioning",
        "Capital and liquidity management",
        "Subsidiary and joint-venture ecosystem",
    ),
    revenue_and_cashflow_drivers=(
        "Net interest income",
        "Interest earned on loans and advances",
        "Interest earned on investment securities",
        "Deposit base and funding mix",
        "Net interest margin",
        "Loan growth",
        "Retail loan growth",
        "SME/commercial loan growth",
        "Corporate/project-finance growth",
        "Fee income",
        "Transaction banking",
        "Trade finance",
        "Foreign exchange services",
        "Treasury trading and investment income",
        "Recovery from stressed assets",
        "Subsidiary contributions",
    ),
    cost_drivers=(
        "Interest paid on deposits",
        "Wholesale funding costs",
        "Employee costs",
        "Branch and distribution costs",
        "Technology and digital infrastructure",
        "Credit provisions",
        "Expected credit losses",
        "Fraud and operational-risk costs",
        "Compliance and regulatory costs",
        "Treasury funding costs",
        "Currency and market-risk hedging",
    ),
    supply_chain_dependencies=(
        "Deposit and funding ecosystem",
        "Payment networks",
        "Technology vendors",
        "Cloud/data infrastructure",
        "Cybersecurity infrastructure",
        "Credit-information systems",
        "Fintech partnerships",
        "Branch/ATM infrastructure",
        "Government and institutional payment systems",
        "Capital-market and treasury infrastructure",
    ),
    demand_dependencies=(
        "Household credit demand",
        "Housing demand",
        "Vehicle and consumer demand",
        "Agricultural activity",
        "Rural income",
        "SME investment",
        "Corporate capex",
        "Infrastructure investment",
        "Trade and international business",
        "Government expenditure",
        "Digital-payment adoption",
        "Financial inclusion",
    ),
    strategic_themes=(
        "Deposit franchise strength",
        "Retail credit growth",
        "Rural and agriculture finance",
        "SME expansion",
        "Corporate and project finance",
        "Digital banking and YONO",
        "Financial inclusion",
        "Asset-quality improvement",
        "Capital efficiency",
        "Treasury optimisation",
        "International banking",
        "Government banking",
        "Technology and cybersecurity",
        "Sustainable/green finance",
    ),
    key_indicators=(
        "Total deposits",
        "CASA ratio",
        "Domestic advances",
        "Loan growth",
        "Retail advances",
        "Agriculture advances",
        "SME advances",
        "Corporate credit",
        "Net interest margin",
        "Cost of deposits",
        "Yield on advances",
        "Gross NPA",
        "Net NPA",
        "Provision coverage",
        "Credit cost",
        "Slippage ratio",
        "Recovery/write-offs",
        "Capital adequacy ratio",
        "ROA",
        "ROE",
        "Fee income",
        "Treasury income",
        "YONO/customer activity",
    ),
    event_signals=(
        "RBI policy-rate changes",
        "Deposit-rate changes",
        "Lending-rate changes",
        "Major credit-growth changes",
        "Large corporate/project-finance announcements",
        "Infrastructure lending developments",
        "Government spending changes",
        "Agriculture/rural policy changes",
        "Asset-quality or NPA changes",
        "Large recoveries",
        "Treasury-market shocks",
        "Capital-raising events",
        "Regulatory capital changes",
        "Digital/YONO milestones",
        "Subsidiary developments",
        "Cybersecurity/operational incidents",
    ),
    risk_channels=(
        "Credit risk",
        "Interest-rate risk",
        "Liquidity risk",
        "Asset-liability mismatch",
        "Market and treasury risk",
        "Concentration risk",
        "Corporate/project-finance risk",
        "Agriculture/rural credit risk",
        "Operational risk",
        "Cybersecurity risk",
        "Regulatory risk",
        "Capital adequacy risk",
        "Foreign-exchange risk",
        "Fraud risk",
    ),
)


MARKET_CHARACTERS: Dict[str, MarketCharacter] = {
    "NIFTY 50": _mc(
        "NIFTY 50",
        "Direct equity-market valuation and broad Indian economic-cycle signal. "
        "For SBI, the NIFTY also captures investor risk appetite, credit-cycle "
        "expectations and valuation of the banking sector.",
        direct=("Equity valuation and market beta",),
        indirect=(
            "Indian GDP/economic cycle",
            "Credit cycle",
            "Institutional risk appetite",
            "Corporate investment",
        ),
        channels=(
            "Equity valuation",
            "Economic-growth expectations",
            "Credit-demand transmission",
            "Investor risk appetite",
        ),
        demand=(
            "Retail credit",
            "Corporate credit",
            "SME credit",
            "Investment demand",
        ),
        strategy=("Banking-sector valuation and capital-market conditions",),
        indicators=(
            "SBIN return",
            "NIFTY 50 return",
            "Banking-index return",
            "Rolling beta",
            "Rolling correlation",
            "Relative volatility",
        ),
        events=("Major Indian macro/rate events", "Budget and banking-policy events"),
        logic=(
            "Calculate SBIN versus NIFTY returns using observed data.",
            "Estimate rolling beta/correlation rather than hard-coding linkage.",
            "Separate broad market effects from rate, credit and bank-specific events.",
        ),
    ),
    "Crude Oil": _mc(
        "Crude Oil",
        "Indirect but important macro-credit character. Crude affects inflation, "
        "household disposable income, transport costs, corporate margins, current "
        "account conditions and therefore loan demand and asset quality.",
        indirect=(
            "Inflation",
            "Household purchasing power",
            "Corporate cash flows",
            "Transport costs",
            "Macro growth",
            "Current-account/currency conditions",
        ),
        channels=(
            "Inflation transmission",
            "Borrower cash-flow transmission",
            "Credit-demand transmission",
            "Asset-quality transmission",
            "Interest-rate expectations",
        ),
        demand=(
            "Retail loans",
            "SME loans",
            "Corporate working capital",
            "Transport-sector finance",
        ),
        cost=("Bank operating and travel costs",),
        strategy=(
            "Credit-risk monitoring",
            "Macro-cycle monitoring",
        ),
        indicators=(
            "Crude return",
            "CPI/inflation",
            "SBIN loan growth",
            "Credit cost",
            "GNPA/NNPA",
            "RBI policy rate",
            "INR exchange rate",
        ),
        events=("Large oil shocks", "Energy-inflation changes"),
        logic=(
            "Do not treat crude as a direct bank revenue input.",
            "Measure its transmission through inflation, rates, growth and borrower cash flow.",
            "Test lags because credit quality responds with delay.",
        ),
    ),
    "Gold": _mc(
        "Gold",
        "Indirect but economically meaningful wealth, collateral and savings "
        "character. Gold can influence household wealth, savings allocation, "
        "risk sentiment and collateral dynamics, while also acting as a macro "
        "inflation/real-rate signal.",
        indirect=(
            "Household wealth",
            "Savings allocation",
            "Collateral value",
            "Inflation expectations",
            "Risk aversion",
        ),
        channels=(
            "Wealth effect",
            "Collateral channel",
            "Savings channel",
            "Macro-regime transmission",
        ),
        demand=(
            "Retail credit",
            "Rural/household financial activity",
            "Gold-linked lending where applicable",
        ),
        cost=("No major direct physical cost channel",),
        strategy=(
            "Household financialisation",
            "Risk-regime monitoring",
        ),
        indicators=(
            "Gold return",
            "Gold-price volatility",
            "SBIN return",
            "Retail-credit growth",
            "Rural-credit indicators",
            "NIFTY return",
        ),
        events=("Large gold-price shocks", "Inflation/real-rate regime changes"),
        logic=(
            "Separate gold's macro/wealth effect from any collateral-related effect.",
            "Use observed gold-linked lending data where available.",
            "Test incremental information after controlling for NIFTY and rates.",
        ),
    ),
    "Silver": _mc(
        "Silver",
        "Indirect industrial and commodity-cycle signal. Silver is not a core "
        "banking input, but can reflect manufacturing activity, investment sentiment "
        "and the wider commodity cycle affecting borrowers.",
        indirect=(
            "Industrial cycle",
            "Commodity inflation",
            "Risk sentiment",
            "Manufacturing activity",
        ),
        channels=(
            "Borrower-cycle transmission",
            "Inflation signal",
            "Commodity-risk regime",
        ),
        demand=(
            "SME credit",
            "Corporate credit",
            "Working-capital demand",
        ),
        strategy=("Industrial-credit-cycle monitoring",),
        indicators=(
            "Silver return",
            "Industrial production",
            "SBIN loan growth",
            "Credit cost",
            "NIFTY return",
        ),
        events=("Industrial-metal shocks", "Global manufacturing changes"),
        logic=(
            "Treat silver as a secondary macro/industrial variable.",
            "Test whether it adds information beyond NIFTY, crude and rates.",
        ),
    ),
    "Natural Gas": _mc(
        "Natural Gas",
        "Indirect energy-cost and industrial-credit character. Gas affects "
        "industrial borrowers, power generation, fertiliser and energy-intensive "
        "businesses, which can transmit into loan demand and credit quality.",
        indirect=(
            "Industrial energy costs",
            "Power-sector economics",
            "Fertiliser-sector economics",
            "Industrial borrower cash flow",
        ),
        channels=(
            "Borrower-margin transmission",
            "Industrial credit demand",
            "Asset-quality transmission",
            "Inflation transmission",
        ),
        demand=(
            "Corporate working capital",
            "SME credit",
            "Project finance",
            "Energy-sector lending",
        ),
        cost=("Bank operating-energy costs",),
        strategy=("Sectoral credit-risk monitoring",),
        indicators=(
            "Natural-gas price",
            "Industrial production",
            "Power-sector stress",
            "Corporate credit growth",
            "Credit cost",
        ),
        events=("Gas-price shocks", "Energy-supply disruptions"),
        logic=(
            "Model natural gas through affected borrower sectors.",
            "Test lagged effects on credit growth and asset quality.",
        ),
    ),
    "Electricity": _mc(
        "Electricity",
        "Important indirect economic and borrower-health signal. Electricity "
        "demand reflects industrial, commercial and household activity; electricity "
        "costs affect energy-intensive borrowers and project-finance cash flows.",
        indirect=(
            "Industrial activity",
            "Commercial activity",
            "Power-intensive borrower cash flow",
            "Infrastructure investment",
        ),
        channels=(
            "Borrower cash-flow transmission",
            "Credit-demand transmission",
            "Project-finance transmission",
            "Economic-cycle signal",
        ),
        demand=(
            "Industrial loans",
            "SME loans",
            "Infrastructure finance",
            "Working-capital demand",
        ),
        cost=(
            "Bank branches",
            "ATMs/data centres",
            "Digital infrastructure",
        ),
        strategy=(
            "Infrastructure and project finance",
            "Digital banking",
        ),
        indicators=(
            "Electricity demand",
            "Industrial power demand",
            "Power prices",
            "SBIN corporate-credit growth",
            "Credit cost",
        ),
        events=("Peak-demand events", "Power-sector stress", "Large tariff changes"),
        logic=(
            "Use electricity primarily as a borrower-cycle variable.",
            "Connect it to sectoral credit exposure rather than assuming a direct stock relationship.",
        ),
    ),
    "Copper": _mc(
        "Copper",
        "Indirect industrial-capex and infrastructure-credit character. Copper "
        "can signal manufacturing, construction, electrification and infrastructure "
        "activity that drives corporate/SME/project-finance demand.",
        indirect=(
            "Industrial capex",
            "Infrastructure investment",
            "Electrification",
            "Manufacturing activity",
        ),
        channels=(
            "Corporate-credit demand",
            "Project-finance demand",
            "Borrower cash flow",
            "Collateral/economic-cycle transmission",
        ),
        demand=(
            "Corporate loans",
            "SME loans",
            "Infrastructure/project finance",
            "Working capital",
        ),
        cost=("Technology and infrastructure procurement",),
        strategy=(
            "Corporate banking",
            "Project finance",
            "Infrastructure lending",
        ),
        indicators=(
            "Copper return",
            "Industrial production",
            "Capex indicators",
            "Corporate-credit growth",
            "SME-credit growth",
        ),
        events=("Copper shocks", "Infrastructure-capex cycle changes"),
        logic=(
            "Treat copper as an industrial-cycle signal.",
            "Measure its relationship with corporate/SME credit and SBIN returns.",
            "Control for NIFTY and rates.",
        ),
    ),
    "Aluminium": _mc(
        "Aluminium",
        "Indirect manufacturing, infrastructure and borrower-cycle signal. "
        "Aluminium prices can reflect industrial activity and affect input costs "
        "for borrowers in automotive, construction, engineering and manufacturing.",
        indirect=(
            "Manufacturing cycle",
            "Construction",
            "Automotive activity",
            "Industrial input costs",
        ),
        channels=(
            "Borrower-margin transmission",
            "Credit-demand transmission",
            "Industrial-cycle signal",
        ),
        demand=(
            "Manufacturing finance",
            "SME credit",
            "Working capital",
            "Infrastructure loans",
        ),
        cost=("Limited direct bank operating impact",),
        strategy=("Sectoral lending and credit-risk monitoring",),
        indicators=(
            "Aluminium return",
            "Industrial production",
            "Manufacturing credit",
            "SME credit",
            "Credit cost",
        ),
        events=("Aluminium shocks", "Manufacturing-cycle changes"),
        logic=(
            "Use aluminium as an indirect borrower-cycle variable.",
            "Test effects through industrial output, credit growth and asset quality.",
        ),
    ),
    "Zinc": _mc(
        "Zinc",
        "Indirect construction and manufacturing credit-cycle signal. Zinc is "
        "mainly useful as a proxy for galvanised-steel demand, construction and "
        "industrial activity affecting borrowers.",
        indirect=(
            "Construction cycle",
            "Manufacturing cycle",
            "Infrastructure activity",
            "Commodity inflation",
        ),
        channels=(
            "Borrower cash-flow transmission",
            "Credit-demand transmission",
            "Industrial-cycle signal",
        ),
        demand=(
            "Construction finance",
            "SME credit",
            "Corporate working capital",
            "Infrastructure finance",
        ),
        strategy=("Sectoral credit-cycle monitoring",),
        indicators=(
            "Zinc return",
            "Construction indicators",
            "Industrial production",
            "Credit growth",
            "Credit cost",
        ),
        events=("Zinc/steel shocks", "Construction-cycle changes"),
        logic=(
            "Treat zinc as an indirect industrial/credit-cycle variable.",
            "Test incremental information after controlling for NIFTY, crude and rates.",
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
    """Return the complete SBI company character."""
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

    print("SBIN CHARACTER VALIDATION")
    print("=" * 32)
    print(f"Company: {result['company_name']}")
    print(f"Markets: {result['market_character_count']}/9")
    print(f"Valid: {result['valid']}")

    if result["missing_markets"]:
        print("Missing:", result["missing_markets"])
    if result["extra_markets"]:
        print("Extra:", result["extra_markets"])

    print("\nMARKET CHARACTERS")
    print("=" * 32)

    for market in TRACKED_MARKETS:
        mc = MARKET_CHARACTERS[market]
        print(f"\n[{market}]")
        print(mc.character)
        print("Direct:", ", ".join(mc.direct_exposure) or "None")
        print("Indirect:", ", ".join(mc.indirect_exposure) or "None")
