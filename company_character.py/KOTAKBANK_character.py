"""
KOTAKBANK — Kotak Mahindra Bank Company Character & 9 Market Characters.

Snapshot CSV fields (RANK, PCT_CHANGE, LINKAGE_SCORE, RELATION) are not
hard-coded as permanent conclusions. They belong to the later historical
calculation engine.

Business basis: Kotak Mahindra Bank's principal businesses are Consumer,
Commercial and Wholesale Banking plus Treasury; the wider Kotak ecosystem
also includes securities, capital markets, asset management, life insurance
and other financial businesses. The bank's annual report describes Treasury
as supporting customer segments through asset-liability management and
specialised products/services. This module therefore models KOTAKBANK mainly
through banking economics: deposits, loans, NIM, credit costs, asset quality,
rates, liquidity, treasury and market valuation.
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
        "Indian equity-market, liquidity and risk-appetite regime.",
        "Direct listed-bank valuation and market-beta exposure.",
        "NIFTY -> liquidity/risk appetite/valuation -> banking-sector sentiment -> KOTAKBANK.",
        "Calculate KOTAKBANK excess return, rolling beta/correlation, volatility response and event-window returns versus NIFTY. Separate market beta from bank-specific earnings/regulatory events.",
        ("KOTAKBANK return", "NIFTY return", "rolling beta",
         "rolling correlation", "India VIX", "KOTAKBANK volume",
         "FII/DII flows", "Bank Nifty return"),
        ("RBI policy", "Union Budget", "banking regulation",
         "KOTAKBANK results", "capital-market events", "major corporate actions"),
        ("intraday", "1D", "1W", "1M", "3M", "6M", "1Y"),
    ),

    "Crude Oil": _mc(
        "Crude Oil",
        "Global energy, inflation and household/business cash-flow signal.",
        "Indirect macro exposure through inflation, rates, borrower cash flows and credit demand.",
        "Crude -> fuel/inflation -> household/business disposable cash flow -> loan demand/asset quality -> KOTAKBANK.",
        "Test crude returns against loan growth, credit costs and KOTAKBANK returns while controlling for RBI rates, NIFTY, FX and inflation. Use lags because credit quality adjusts after the initial price shock.",
        ("Brent", "WTI", "CPI", "WPI", "interest rates",
         "credit growth", "GNPA/NNPA", "credit cost", "KOTAKBANK return"),
        ("OPEC+ decisions", "energy shocks", "inflation surprises",
         "geopolitical disruptions", "RBI policy response"),
        ("1D", "1W", "1M", "1Q", "6M", "1Y"),
    ),

    "Gold": _mc(
        "Gold",
        "Precious-metal, household-wealth, savings and safe-haven market.",
        "More relevant than many commodities through household wealth, savings behaviour, collateral and financial-market sentiment; still not a universal bank input.",
        "Gold -> household wealth/collateral/risk sentiment -> savings, borrowing and investment behaviour -> KOTAKBANK.",
        "Measure INR-gold returns against KOTAKBANK after controlling for NIFTY, rates, inflation and FX. Separately test gold-loan/collateral exposure where product-level data exists.",
        ("INR gold", "USD gold", "gold volatility", "household savings",
         "interest rates", "credit growth", "asset quality", "KOTAKBANK return"),
        ("gold-price shocks", "geopolitical risk", "inflation surprises",
         "monetary-policy changes", "gold-linked product events"),
        ("intraday", "1D", "1W", "1M", "1Q", "6M"),
    ),

    "Silver": _mc(
        "Silver",
        "Precious/industrial-metal and risk-sentiment market.",
        "Indirect macro exposure through industrial activity, inflation and wealth sentiment.",
        "Silver -> industrial cycle/inflation/risk sentiment -> business activity and credit cycle -> KOTAKBANK.",
        "Calculate rolling and lagged association after controlling for gold, NIFTY, rates, crude and FX. Require incremental explanatory value.",
        ("silver return", "gold/silver ratio", "industrial-metals index",
         "PMI", "CPI", "credit growth", "KOTAKBANK return"),
        ("industrial-cycle shocks", "inflation releases",
         "geopolitical events", "risk-off events"),
        ("1D", "1W", "1M", "1Q", "6M"),
    ),

    "Natural Gas": _mc(
        "Natural Gas",
        "Energy and industrial-cycle indicator.",
        "Indirect exposure through inflation, industrial activity and borrower cash flow.",
        "Natural gas -> energy/industrial costs -> inflation and business cash flow -> credit demand/asset quality -> KOTAKBANK.",
        "Test gas with crude, electricity, inflation, rates, NIFTY and FX controls. Examine lagged effects on business credit growth and stress.",
        ("gas benchmark", "regional gas price", "electricity price",
         "CPI", "industrial production", "credit growth", "credit cost"),
        ("gas supply disruptions", "weather shocks", "power stress",
         "geopolitical events"),
        ("1D", "1W", "1M", "1Q", "6M"),
    ),

    "Copper": _mc(
        "Copper",
        "Global industrial, construction and electrification-cycle indicator.",
        "Indirect borrower-cycle exposure through corporate/SME activity and capex.",
        "Copper -> industrial/manufacturing capex -> borrower cash flow -> corporate/SME credit demand and asset quality -> KOTAKBANK.",
        "Use copper as an economic-cycle factor; test incremental association after controlling for PMI, rates, NIFTY, crude and credit growth.",
        ("LME copper", "India/global PMI", "industrial production",
         "corporate capex", "commercial credit growth", "asset quality",
         "KOTAKBANK return"),
        ("China/global PMI shocks", "infrastructure stimulus",
         "copper supply disruptions", "industrial capex cycle"),
        ("1W", "1M", "1Q", "6M", "1Y"),
    ),

    "Aluminium": _mc(
        "Aluminium",
        "Industrial metal and manufacturing/infrastructure-cycle signal.",
        "Indirect exposure through borrower activity, corporate capex and household durable economics.",
        "Aluminium -> manufacturing/infrastructure activity -> borrower cash flow/capex -> loan demand and asset quality -> KOTAKBANK.",
        "Test aluminium with PMI, credit growth, rates and NIFTY controls. Examine whether it adds information for corporate/SME credit and collections.",
        ("LME aluminium", "aluminium premium", "PMI",
         "industrial production", "credit growth", "asset quality"),
        ("metal supply shocks", "infrastructure cycle",
         "manufacturing changes", "trade-policy events"),
        ("1W", "1M", "1Q", "6M", "1Y"),
    ),

    "Zinc": _mc(
        "Zinc",
        "Industrial metal linked to construction, manufacturing and infrastructure.",
        "Low-to-indirect borrower-cycle exposure.",
        "Zinc -> construction/manufacturing activity -> SME/corporate cash flow -> credit demand/asset quality -> KOTAKBANK.",
        "Require incremental explanatory value beyond copper, aluminium, crude, PMI, rates and NIFTY before treating zinc as material.",
        ("LME zinc", "construction cycle", "PMI", "industrial production",
         "credit growth", "asset quality", "KOTAKBANK return"),
        ("infrastructure cycle", "metal supply shocks",
         "manufacturing changes", "trade-policy events"),
        ("1W", "1M", "1Q", "6M", "1Y"),
    ),

    "Electricity": _mc(
        "Electricity",
        "Power and digital-infrastructure operating environment.",
        "Mostly indirect for a bank, with modest direct exposure through branches, offices, technology and data infrastructure.",
        "Electricity -> operating/technology cost; electricity -> industrial activity -> borrower cash flow -> credit cycle -> KOTAKBANK.",
        "Use regional commercial/industrial tariffs and infrastructure data. Test direct operating-cost effects separately from the larger macro/borrower-cycle effect.",
        ("commercial tariff", "power availability", "data-centre energy",
         "operating expense", "industrial production", "credit growth"),
        ("tariff changes", "power shortages", "extreme weather",
         "technology infrastructure events"),
        ("1D", "1W", "1M", "1Q", "1Y"),
    ),
}


COMPANY_CHARACTER = CompanyCharacter(
    symbol="KOTAKBANK",
    company_name="Kotak Mahindra Bank Limited",
    sector="Banking / Financial Services",
    industry_character=(
        "Diversified private-sector banking franchise with Consumer Banking, "
        "Commercial Banking, Wholesale Banking and Treasury, supported by a "
        "broader Kotak financial-services ecosystem."
    ),
    business_character=(
        "Balance-sheet-driven financial intermediary. Its core character is the "
        "conversion of deposits and wholesale funding into loans and investments, "
        "with profitability shaped by NIM, credit growth, asset quality, credit "
        "cost, liquidity, capital adequacy and treasury performance. Consumer, "
        "commercial and wholesale borrowers transmit the real economy into the "
        "bank; Treasury manages asset-liability structure, liquidity and market "
        "exposures."
    ),
    demand_drivers=(
        "Retail credit demand",
        "Home loans",
        "Personal loans",
        "Consumer durable finance",
        "Commercial banking demand",
        "SME/MSME activity",
        "Corporate capex",
        "Working-capital demand",
        "Trade finance",
        "Infrastructure investment",
        "Housing cycle",
        "Rural and urban income",
        "Savings/deposit demand",
        "Wealth and investment activity",
    ),
    revenue_drivers=(
        "Loan book growth",
        "Net interest income",
        "Net interest margin",
        "Retail banking income",
        "Commercial banking income",
        "Wholesale banking income",
        "Fee income",
        "Transaction banking",
        "Cash management",
        "Trade finance",
        "Treasury income",
        "Investment income",
        "Capital-markets and securities income through group businesses",
        "Asset-management/insurance distribution through group ecosystem",
    ),
    cost_drivers=(
        "Cost of deposits",
        "Cost of funds",
        "Interest expense",
        "Credit provisioning",
        "Expected credit loss",
        "Employee costs",
        "Branch and office costs",
        "Technology/cloud infrastructure",
        "Digital platform investment",
        "Compliance and regulatory costs",
        "Customer acquisition",
        "Marketing",
        "Treasury funding costs",
        "Depreciation/amortisation",
    ),
    supply_chain_character=(
        "Retail depositors",
        "Corporate depositors",
        "Institutional funding markets",
        "RBI liquidity system",
        "Payment networks",
        "Credit bureaus",
        "Capital markets",
        "Corporate and SME borrowers",
        "Retail borrowers",
        "Mortgage ecosystem",
        "Vehicle/consumer-finance ecosystem",
        "Technology/cloud providers",
        "Cybersecurity ecosystem",
        "Kotak group financial-services subsidiaries",
    ),
    strategic_drivers=(
        "Consumer banking growth",
        "Commercial banking growth",
        "Wholesale banking",
        "Deposit franchise",
        "CASA growth",
        "Digital banking",
        "Kotak811",
        "Technology modernisation",
        "Cross-sell across Kotak ecosystem",
        "Risk-adjusted loan growth",
        "Asset-quality discipline",
        "Capital adequacy",
        "Liquidity management",
        "Wealth/capital-markets ecosystem",
        "Operational efficiency",
    ),
    key_indicators=(
        "Deposits",
        "CASA ratio",
        "Advances",
        "Loan growth",
        "Retail advances",
        "Commercial advances",
        "Wholesale advances",
        "Net interest income",
        "NIM",
        "Fee income",
        "PPOP",
        "PAT",
        "RoA",
        "RoE",
        "GNPA",
        "NNPA",
        "Slippage ratio",
        "Credit cost",
        "Provision coverage",
        "Capital adequacy",
        "CET1",
        "Liquidity Coverage Ratio",
        "Cost-to-income ratio",
        "Cost of funds",
        "Credit-deposit ratio",
        "Treasury book",
        "Investment book",
        "KOTAKBANK return and volatility",
    ),
    key_events=(
        "Quarterly and annual results",
        "RBI monetary-policy decisions",
        "RBI liquidity measures",
        "RBI banking regulations",
        "Deposit-rate changes",
        "Loan-rate changes",
        "Large corporate-credit events",
        "Asset-quality events",
        "Capital raising",
        "Credit-rating changes",
        "Major digital-banking launches",
        "Kotak811 developments",
        "Subsidiary acquisitions/divestments",
        "Securities/capital-market developments",
        "Major technology or cyber events",
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
    if COMPANY_CHARACTER.symbol != "KOTAKBANK":
        return False
    if set(MARKET_CHARACTERS) != set(TRACKED_MARKETS):
        return False
    for market in TRACKED_MARKETS:
        mc = MARKET_CHARACTERS[market]
        if mc.market != market or not mc.character or not mc.exposure_character:
            return False
        if not mc.impact_path or not mc.calculation_logic:
            return False
        if not mc.relevant_indicators or not mc.expected_timeframes:
            return False
    return True


if __name__ == "__main__":
    print("KOTAKBANK character valid:", validate_character())
    print("Tracked markets:", ", ".join(TRACKED_MARKETS))
