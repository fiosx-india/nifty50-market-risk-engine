"""
JIOFIN — Jio Financial Services Company Character & 9-Market Relationship.

This module defines business character and research logic only. Snapshot CSV
fields such as RANK, PCT_CHANGE, LINKAGE_SCORE and RELATION are not embedded
as permanent conclusions; the later historical engine must calculate them from
real observations.

Current business character is based on Jio Financial Services' FY2025-26
materials: digital-first financial services spanning Borrow, Transact, Invest
and Protect, including lending, payments bank/payment solutions, insurance
broking, asset management/wealth/broking partnerships and the JioFinance
digital platform.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Tuple


TRACKED_MARKETS: Tuple[str, ...] = (
    "NIFTY 50", "Crude Oil", "Gold", "Silver", "Natural Gas",
    "Copper", "Aluminium", "Zinc", "Electricity",
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


def _mc(market, character, exposure, path, logic, indicators, events, timeframes):
    return MarketCharacter(
        market=market,
        character=character,
        exposure_character=exposure,
        impact_path=path,
        calculation_logic=logic,
        relevant_indicators=indicators,
        relevant_events=events,
        expected_timeframes=timeframes,
    )


MARKET_CHARACTERS: Dict[str, MarketCharacter] = {
    "NIFTY 50": _mc(
        "NIFTY 50",
        "Indian equity, liquidity, valuation and risk-appetite regime.",
        "Direct listed-equity and financial-sector valuation exposure.",
        "NIFTY regime -> liquidity/risk appetite/rates -> financial-sector valuation -> JIOFIN.",
        "Calculate JIOFIN excess returns, rolling beta/correlation, volatility response and event-window returns versus NIFTY. Separate market beta from company-specific business evidence.",
        ("JIOFIN return", "NIFTY return", "rolling beta", "rolling correlation",
         "India VIX", "JIOFIN volume", "FII/DII flows", "financial index"),
        ("RBI policy", "Union Budget", "SEBI/RBI rules", "JIOFIN results",
         "major JV/business launches", "corporate actions"),
        ("intraday", "1D", "1W", "1M", "3M", "6M", "1Y"),
    ),

    "Crude Oil": _mc(
        "Crude Oil",
        "Global energy, inflation and household-purchasing-power signal.",
        "Indirect macro exposure rather than a core financial-services input.",
        "Crude -> inflation/fuel/freight -> household disposable income and business cash flow -> credit demand/asset quality -> JIOFIN.",
        "Test crude returns against JIOFIN with inflation, rates, NIFTY, FX and credit-cycle controls. Examine lagged effects on loan growth, delinquencies and consumer demand rather than assuming direct causation.",
        ("Brent", "WTI", "CPI", "WPI", "interest rates", "credit growth",
         "asset quality", "JIOFIN return"),
        ("OPEC+ decisions", "energy shocks", "inflation surprises",
         "geopolitical disruptions", "RBI policy response"),
        ("1D", "1W", "1M", "1Q", "6M", "1Y"),
    ),

    "Gold": _mc(
        "Gold",
        "Precious-metal, household-wealth, safe-haven and savings signal.",
        "Potentially more relevant than other commodities through household wealth, savings behaviour and gold-linked financial products, but still indirect.",
        "Gold -> household wealth/savings/risk sentiment -> borrowing/investment/insurance behaviour -> JIOFIN.",
        "Measure gold returns, INR gold and volatility against JIOFIN after controlling for NIFTY, rates, inflation and FX. Separately test any gold-loan or gold-linked product exposure where data exists.",
        ("INR gold", "USD gold", "gold volatility", "household savings",
         "interest rates", "credit growth", "JIOFIN return"),
        ("gold-price shocks", "geopolitical risk", "inflation surprises",
         "monetary-policy changes", "gold-product launches"),
        ("intraday", "1D", "1W", "1M", "1Q", "6M"),
    ),

    "Silver": _mc(
        "Silver",
        "Precious/industrial-metal and risk-sentiment market.",
        "Indirect macro exposure; silver is not assumed to be a core JIOFIN input.",
        "Silver -> inflation/industrial-cycle/risk sentiment -> household/business activity -> financial-services demand -> JIOFIN.",
        "Calculate rolling/lagged association after controlling for gold, NIFTY, rates, crude and FX. Retain linkage only when incremental explanatory value is demonstrated.",
        ("silver return", "gold/silver ratio", "industrial-metals index",
         "CPI", "rates", "JIOFIN return"),
        ("industrial-cycle shocks", "inflation releases",
         "geopolitical events", "risk-off events"),
        ("1D", "1W", "1M", "1Q", "6M"),
    ),

    "Natural Gas": _mc(
        "Natural Gas",
        "Energy and industrial-cycle indicator.",
        "Indirect macro exposure through inflation, industrial activity and power costs.",
        "Natural gas -> energy/industrial costs -> inflation and business cash flow -> credit/investment cycle -> JIOFIN.",
        "Test gas against JIOFIN with crude, electricity, inflation, rates, NIFTY and FX controls. Investigate credit-cycle lags.",
        ("gas benchmark", "regional gas price", "electricity price",
         "CPI", "industrial production", "credit growth", "JIOFIN return"),
        ("gas supply disruptions", "weather shocks", "power stress",
         "geopolitical events"),
        ("1D", "1W", "1M", "1Q", "6M"),
    ),

    "Copper": _mc(
        "Copper",
        "Global industrial, construction and electrification-cycle indicator.",
        "Indirect exposure through business investment, SME/corporate cash flow and economic activity.",
        "Copper -> industrial capex/manufacturing cycle -> business credit demand and asset quality -> JIOFIN.",
        "Use copper as an economic-cycle factor; test incremental association after controlling for NIFTY, PMI, rates, crude and credit growth.",
        ("LME copper", "global PMI", "India PMI", "industrial production",
         "credit growth", "corporate capex", "JIOFIN return"),
        ("China/global PMI shocks", "infrastructure stimulus",
         "copper supply disruptions", "industrial capex cycle"),
        ("1W", "1M", "1Q", "6M", "1Y"),
    ),

    "Aluminium": _mc(
        "Aluminium",
        "Industrial metal and manufacturing/infrastructure-cycle signal.",
        "Indirect exposure through SME/corporate activity, infrastructure and household durable economics.",
        "Aluminium -> manufacturing/infrastructure activity -> borrower cash flow/capex -> lending demand and asset quality -> JIOFIN.",
        "Test aluminium with PMI, credit growth, rates and NIFTY controls. Examine whether it adds information for loan growth, collections or credit stress.",
        ("LME aluminium", "aluminium premium", "PMI",
         "industrial production", "credit growth", "asset quality",
         "JIOFIN return"),
        ("metal supply shocks", "infrastructure cycle",
         "manufacturing changes", "trade-policy events"),
        ("1W", "1M", "1Q", "6M", "1Y"),
    ),

    "Zinc": _mc(
        "Zinc",
        "Industrial metal linked to construction, manufacturing and infrastructure.",
        "Low-to-indirect macro and borrower-cycle exposure.",
        "Zinc -> construction/manufacturing activity -> SME/corporate cash flow -> credit demand/asset quality -> JIOFIN.",
        "Require incremental explanatory power beyond copper, aluminium, crude, PMI, rates and NIFTY before treating zinc as material.",
        ("LME zinc", "construction cycle", "PMI", "industrial production",
         "credit growth", "asset quality", "JIOFIN return"),
        ("infrastructure cycle", "metal supply shocks",
         "manufacturing changes", "trade-policy events"),
        ("1W", "1M", "1Q", "6M", "1Y"),
    ),

    "Electricity": _mc(
        "Electricity",
        "Power and digital-infrastructure operating environment.",
        "Indirect macro exposure plus direct relevance to digital financial-services infrastructure and offices.",
        "Electricity -> data-centre/digital infrastructure and operating costs -> unit economics; electricity -> industrial activity -> borrower cash flow -> JIOFIN.",
        "Use reliable regional power-cost/availability data and company infrastructure metrics where available. Test effects on operating costs and credit-cycle variables.",
        ("commercial tariff", "power availability", "data-centre energy use",
         "technology infrastructure cost", "credit growth", "JIOFIN return"),
        ("tariff changes", "power shortages", "extreme weather",
         "data-centre expansion", "digital infrastructure events"),
        ("1D", "1W", "1M", "1Q", "1Y"),
    ),
}


COMPANY_CHARACTER = CompanyCharacter(
    symbol="JIOFIN",
    company_name="Jio Financial Services Limited",
    sector="Financial Services / NBFC / Digital Financial Services",
    industry_character=(
        "Digital-first financial-services ecosystem spanning lending, payments, "
        "banking, insurance distribution, asset management, wealth and broking "
        "partnerships, connected through a technology-led customer platform."
    ),
    business_character=(
        "Jio Financial Services is a financial ecosystem rather than a single "
        "commodity-sensitive operating company. Its core economic character is "
        "financial intermediation plus digital distribution: Borrow, Transact, "
        "Invest and Protect. Therefore the most important drivers are credit "
        "demand, funding/liquidity, interest rates, asset quality, AUM/flows, "
        "payments activity, insurance distribution, technology adoption and "
        "regulatory capital/risk controls."
    ),
    demand_drivers=(
        "Retail credit demand",
        "Home loans",
        "Loans against property",
        "Loans against securities/mutual funds",
        "Corporate and supply-chain finance",
        "Consumer financial inclusion",
        "UPI and digital payments",
        "Merchant payments",
        "Savings and deposits",
        "Mutual-fund participation",
        "Wealth/investment demand",
        "Insurance penetration",
        "Digital financial adoption",
        "Household income and confidence",
        "SME/business activity",
    ),
    revenue_drivers=(
        "Loan book growth",
        "Loan disbursements",
        "Net interest income",
        "Interest income",
        "Net interest margin",
        "Fee and financial-services income",
        "Payments transaction volume",
        "Payments TPV",
        "Bank deposits",
        "Insurance premium facilitated",
        "Asset-management AUM",
        "Wealth and broking activity",
        "Customer acquisition",
        "JioFinance app engagement",
        "Cross-sell across Borrow/Transact/Invest/Protect",
    ),
    cost_drivers=(
        "Cost of funds",
        "Interest expense",
        "Credit provisioning",
        "Expected credit losses",
        "Employee costs",
        "Technology and cloud infrastructure",
        "Digital platform development",
        "Customer acquisition",
        "Payment infrastructure",
        "Compliance and regulatory costs",
        "Branch/physical infrastructure where applicable",
        "Insurance distribution costs",
        "Marketing",
        "Depreciation/amortisation",
    ),
    supply_chain_character=(
        "RBI-regulated financial ecosystem",
        "Banks and funding partners",
        "Capital markets",
        "Credit bureaus",
        "Payment networks",
        "UPI ecosystem",
        "Merchant ecosystem",
        "Cloud and technology providers",
        "Cybersecurity providers",
        "Insurance partners",
        "Asset-management partners",
        "BlackRock joint-venture ecosystem",
        "Digital distribution network",
        "Reliance/Jio digital ecosystem",
    ),
    strategic_drivers=(
        "JioFinance digital platform",
        "AI-native financial experience",
        "Borrow/Transact/Invest/Protect ecosystem",
        "Digital lending scale",
        "Secured lending",
        "Payments ecosystem",
        "Jio Payments Bank",
        "Insurance distribution",
        "JioBlackRock asset management",
        "Wealth and broking expansion",
        "Technology and data advantage",
        "Cross-sell and customer lifetime value",
        "Financial inclusion",
        "Risk and underwriting discipline",
        "Unit economics",
    ),
    key_indicators=(
        "NBFC AUM",
        "Loan book",
        "Loan disbursements",
        "Annual disbursements",
        "Net interest income",
        "PPOP",
        "PAT",
        "NIM",
        "Cost-to-income ratio",
        "Credit cost",
        "GNPA",
        "NNPA",
        "Expected credit loss",
        "Capital adequacy",
        "Borrowings",
        "Cost of funds",
        "Payments TPV",
        "Payments Bank deposits",
        "Customer base",
        "Insurance premium facilitated",
        "Insurance policies/lives covered",
        "AMC closing AUM",
        "Wealth/broking customers",
        "JioFinance app users",
        "JIOFIN return and volatility",
    ),
    key_events=(
        "Quarterly and annual results",
        "RBI policy changes",
        "RBI liquidity measures",
        "Interest-rate changes",
        "Digital lending regulation",
        "Payments/UPI regulation",
        "Insurance regulation",
        "SEBI/asset-management regulation",
        "New loan products",
        "JioFinance platform launches",
        "Jio Payments Bank expansion",
        "JioBlackRock launches",
        "Insurance partnerships",
        "Major technology/AI launches",
        "Capital raising or funding events",
        "Credit-rating changes",
        "Asset-quality events",
        "Material exchange filings",
    ),
    market_characters=MARKET_CHARACTERS,
)


def get_company_character() -> CompanyCharacter:
    return COMPANY_CHARACTER


def get_market_character(market: str) -> MarketCharacter:
    try:
        return MARKET_CHARACTERS[market]
    except KeyError as exc:
        raise ValueError(
            f"Unsupported market: {market!r}. Expected one of: {', '.join(TRACKED_MARKETS)}"
        ) from exc


def get_all_market_characters() -> Dict[str, MarketCharacter]:
    return dict(MARKET_CHARACTERS)


def validate_character() -> bool:
    if COMPANY_CHARACTER.symbol != "JIOFIN":
        return False
    if set(MARKET_CHARACTERS) != set(TRACKED_MARKETS):
        return False
    for market in TRACKED_MARKETS:
        mc = MARKET_CHARACTERS[market]
        if mc.market != market:
            return False
        if not mc.character or not mc.exposure_character:
            return False
        if not mc.impact_path or not mc.calculation_logic:
            return False
        if not mc.relevant_indicators or not mc.expected_timeframes:
            return False
    return True


if __name__ == "__main__":
    print("JIOFIN character valid:", validate_character())
    print("Tracked markets:", ", ".join(TRACKED_MARKETS))
