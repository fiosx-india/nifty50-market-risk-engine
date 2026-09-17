"""
LT_9_MARKETS_CHARACTER
Larsen & Toubro Limited (LT)

Purpose
-------
This module defines the business character of Larsen & Toubro and its
character-based relationship with the project's nine tracked markets.

IMPORTANT
---------
- This file defines what should be researched/calculated.
- It does NOT hard-code Rank, PCT_CHANGE, LINKAGE_SCORE, correlation,
  beta, probability, or trading decisions.
- Historical relationships must be calculated later from real observations.
- Market exposure is expressed as a mechanism/path, not as a fixed score.

Business basis
--------------
L&T is an engineering, EPC, hi-tech manufacturing and services group with
major exposure to infrastructure, energy, manufacturing/defence, technology,
financial services and development businesses. Its FY2025-26 reporting
describes Infrastructure Projects, Energy Projects, Hi-Tech Manufacturing,
IT & Technology Services, Financial Services and Development Projects among
its operating segments.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Tuple


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
    impact_path: List[str]
    calculation_logic: List[str]
    relevant_indicators: List[str]
    relevant_events: List[str]
    expected_timeframes: List[str]


@dataclass(frozen=True)
class CompanyCharacter:
    symbol: str
    company_name: str
    sector: str
    industry_character: str
    business_character: List[str]
    demand_drivers: List[str]
    revenue_drivers: List[str]
    cost_drivers: List[str]
    supply_chain_character: List[str]
    strategic_drivers: List[str]
    key_indicators: List[str]
    key_events: List[str]
    market_characters: Dict[str, MarketCharacter] = field(default_factory=dict)


def _mc(
    market: str,
    character: str,
    exposure_character: str,
    impact_path: List[str],
    calculation_logic: List[str],
    relevant_indicators: List[str],
    relevant_events: List[str],
    expected_timeframes: List[str],
) -> MarketCharacter:
    return MarketCharacter(
        market=market,
        character=character,
        exposure_character=exposure_character,
        impact_path=impact_path,
        calculation_logic=calculation_logic,
        relevant_indicators=relevant_indicators,
        relevant_events=relevant_events,
        expected_timeframes=expected_timeframes,
    )


# ---------------------------------------------------------------------------
# L&T COMPANY CHARACTER
# ---------------------------------------------------------------------------

COMPANY_CHARACTER = CompanyCharacter(
    symbol="LT",
    company_name="Larsen & Toubro Limited",
    sector="Engineering, EPC, Hi-Tech Manufacturing & Services",
    industry_character=(
        "Diversified engineering and project-execution group whose economic "
        "character is driven by large order inflows, order-book conversion, "
        "project execution, working capital, commodity/input costs, energy "
        "economics, government/private capex and international project activity."
    ),
    business_character=[
        "Infrastructure EPC: buildings & factories, transportation, heavy civil, utilities, power transmission & distribution, water and minerals/metals.",
        "Energy projects: hydrocarbon onshore/offshore, power-generation solutions, carbon-related solutions and green/clean-energy EPC.",
        "Hi-Tech Manufacturing: engineered equipment, process-plant equipment, nuclear/energy equipment, defence/aerospace systems, precision engineering and electrolysers.",
        "Technology services: IT, engineering services, digital platforms, cloud/data-centre and semiconductor design activities.",
        "Financial services and development businesses provide additional diversification outside core EPC.",
        "International execution creates exposure to GCC and other global project cycles, currencies, logistics and geopolitical conditions.",
    ],
    demand_drivers=[
        "Indian public capital expenditure and infrastructure spending.",
        "Private industrial capex and capacity expansion.",
        "Energy transition, renewables, transmission and grid investment.",
        "Hydrocarbon, refinery, petrochemical and offshore project investment.",
        "Defence, aerospace, nuclear and strategic manufacturing localisation.",
        "Urbanisation, transportation infrastructure and water infrastructure.",
        "International infrastructure and energy investment, especially GCC project activity.",
        "Digital transformation, engineering R&D, cloud and semiconductor demand.",
    ],
    revenue_drivers=[
        "New order inflows.",
        "Opening order book and executable order book.",
        "Order-book conversion into revenue.",
        "Project execution speed and milestone completion.",
        "International order inflows and geographic mix.",
        "Engineering/manufacturing project wins.",
        "Technology-services growth and large deal wins.",
        "Real-estate/development-project sales where applicable.",
    ],
    cost_drivers=[
        "Steel and non-ferrous metal inputs.",
        "Copper and aluminium content in electrical and engineered systems.",
        "Fuel, logistics and freight costs.",
        "Electricity and energy used in manufacturing and fabrication.",
        "Natural gas/energy costs in selected manufacturing and industrial processes.",
        "Imported equipment and component costs.",
        "Foreign-exchange movements on international procurement and execution.",
        "Labour, subcontracting and project execution costs.",
        "Financing and working-capital costs.",
    ],
    supply_chain_character=[
        "Engineering → procurement → fabrication/manufacturing → construction/installation → commissioning.",
        "Large-project procurement can create long lead times and working-capital requirements.",
        "Metal, electrical, equipment and specialised component availability can affect execution.",
        "International projects introduce shipping, customs, FX and geopolitical dependencies.",
        "Project execution depends on subcontractors, specialist suppliers and customer approvals.",
        "Manufacturing businesses have plant-capacity, raw-material and logistics dependencies.",
    ],
    strategic_drivers=[
        "Infrastructure build-out and urbanisation.",
        "Energy transition and green-energy investment.",
        "Defence and aerospace localisation.",
        "Digital engineering, AI and technology transformation.",
        "Expansion of international EPC opportunities.",
        "Improved project profitability and working-capital discipline.",
        "Development of new technology and green-energy businesses.",
    ],
    key_indicators=[
        "Order inflow",
        "Order book",
        "Order-book-to-revenue visibility",
        "Revenue growth by segment",
        "EBIT/EBITDA margin by segment",
        "Execution/progress of major projects",
        "Working capital",
        "Receivables and contract assets",
        "Cash flow from operations",
        "Net debt / leverage",
        "International order share",
        "Commodity input costs",
        "Electricity and fuel costs",
        "Technology-services growth",
    ],
    key_events=[
        "Quarterly and annual results",
        "Large EPC order wins",
        "Order cancellations or delays",
        "Major project commissioning",
        "Government infrastructure/defence capex announcements",
        "Oil & gas/refinery/petrochemical project awards",
        "Renewable, transmission and green-hydrogen awards",
        "Defence and aerospace contracts",
        "Large international/GCC project wins",
        "Material acquisitions/divestments",
        "Regulatory or geopolitical developments affecting overseas projects",
        "Major commodity-cost or supply-chain disruptions",
    ],
    market_characters={},
)


# ---------------------------------------------------------------------------
# MARKET CHARACTERS
# ---------------------------------------------------------------------------

MARKET_CHARACTERS: Dict[str, MarketCharacter] = {

    "NIFTY 50": _mc(
        "NIFTY 50",
        "Broad Indian equity-market and domestic risk-appetite character.",
        "Direct market-beta and valuation channel, plus indirect signal about "
        "Indian capex, liquidity and macro conditions.",
        [
            "NIFTY regime → equity risk appetite → L&T valuation/multiple",
            "NIFTY trend → domestic investment sentiment → order expectations",
            "Market volatility → financing/risk premium → valuation",
        ],
        [
            "Calculate LT returns versus NIFTY returns.",
            "Calculate rolling correlation across multiple windows.",
            "Estimate rolling beta and downside beta.",
            "Separate market effect from company-specific residual return.",
            "Test lead/lag behaviour rather than assuming same-day causation.",
        ],
        [
            "LT daily/weekly return",
            "NIFTY return",
            "Rolling beta",
            "Rolling correlation",
            "Volatility",
            "Relative strength",
        ],
        [
            "NIFTY regime changes",
            "Large domestic macro announcements",
            "RBI/liquidity events",
            "Major capex-policy announcements",
            "Global risk-off events",
        ],
        ["intraday", "1D", "1W", "1M", "3M", "6M", "1Y"],
    ),

    "Crude Oil": _mc(
        "Crude Oil",
        "Global energy, fuel, freight, inflation and oil-and-gas capex character.",
        "Mixed direct/indirect exposure: energy and logistics costs can affect "
        "project economics, while higher oil/gas-sector investment can increase "
        "EPC opportunity.",
        [
            "Crude price → fuel/freight/inflation → project cost",
            "Crude price → upstream/refining/petrochemical capex → EPC demand",
            "Oil-market cycle → customer budgets → order inflow",
            "Crude volatility → geopolitical/logistics risk → project execution",
        ],
        [
            "Use crude returns and changes in volatility.",
            "Test LT returns against crude returns with multiple lags.",
            "Model project/customer exposure separately from cost exposure.",
            "Control for NIFTY when estimating incremental crude sensitivity.",
            "Use event windows around major oil shocks.",
        ],
        [
            "Brent/WTI return",
            "Crude volatility",
            "Fuel-cost proxy",
            "Oil & gas capex indicators",
            "LT Energy order inflow",
        ],
        [
            "OPEC+ decisions",
            "Large oil-price shocks",
            "Major refinery/petrochemical awards",
            "Middle-East geopolitical disruptions",
            "Large hydrocarbon EPC wins",
        ],
        ["1D", "1W", "1M", "3M", "6M", "1Y"],
    ),

    "Gold": _mc(
        "Gold",
        "Global safe-haven, real-rate, liquidity and risk-aversion character.",
        "Mostly indirect. Gold can act as a macro risk/real-rate signal rather "
        "than a core operating input for L&T.",
        [
            "Gold movement → global risk/real-rate regime → equity valuation",
            "Gold/risk-off → capital-market conditions → project financing sentiment",
            "Gold macro regime → USD/rates → international project economics",
        ],
        [
            "Measure LT sensitivity to gold returns after controlling for NIFTY.",
            "Use rolling correlation and conditional downside periods.",
            "Test gold as a macro regime variable rather than a direct cost input.",
            "Compare normal periods with high-volatility/risk-off regimes.",
        ],
        [
            "Gold return",
            "Gold volatility",
            "Real-rate proxy",
            "USD index",
            "LT/NIFTY relative return",
        ],
        [
            "Sharp safe-haven moves",
            "Central-bank/rate shocks",
            "Major geopolitical escalation",
            "Global liquidity stress",
        ],
        ["1D", "1W", "1M", "3M", "6M"],
    ),

    "Silver": _mc(
        "Silver",
        "Hybrid precious-metal and industrial-demand character.",
        "Indirect macro/industrial-cycle exposure; potentially more useful as an "
        "industrial activity signal than as a direct L&T input.",
        [
            "Silver industrial demand → global manufacturing cycle → capex",
            "Silver risk signal → market regime → valuation",
            "Silver/industrial cycle → electrical/technology investment → EPC demand",
        ],
        [
            "Test rolling LT/silver correlation.",
            "Compare silver sensitivity with copper sensitivity.",
            "Control for NIFTY and broad industrial-cycle variables.",
            "Test whether silver leads LT during industrial-cycle transitions.",
        ],
        [
            "Silver return",
            "Gold/silver ratio",
            "Industrial-demand proxy",
            "LT relative return",
        ],
        [
            "Industrial-cycle shocks",
            "Precious-metal volatility events",
            "Global manufacturing slowdowns/recoveries",
        ],
        ["1D", "1W", "1M", "3M", "6M"],
    ),

    "Natural Gas": _mc(
        "Natural Gas",
        "Energy/feedstock and industrial-project investment character.",
        "Mixed exposure: energy costs for selected operations/projects and strong "
        "demand linkage through gas, LNG, power, hydrocarbon and energy-transition EPC.",
        [
            "Natural gas price → industrial energy economics → project costs",
            "Gas/LNG investment → EPC capex → L&T Energy order demand",
            "Gas volatility → customer investment timing → order-cycle changes",
            "Gas-market disruptions → logistics/geopolitics → project execution risk",
        ],
        [
            "Calculate lagged LT response to gas returns.",
            "Separate operating-cost exposure from customer-capex exposure.",
            "Test LNG/gas-cycle regimes and order-inflow response.",
            "Control for crude and NIFTY to isolate incremental gas sensitivity.",
        ],
        [
            "Natural gas return",
            "Gas volatility",
            "LNG investment proxy",
            "Hydrocarbon order inflow",
            "Energy segment margin",
        ],
        [
            "LNG/project awards",
            "Major gas-price shocks",
            "Pipeline/LNG infrastructure announcements",
            "Middle-East/global gas disruptions",
            "Hydrocarbon EPC contracts",
        ],
        ["1D", "1W", "1M", "3M", "6M", "1Y"],
    ),

    "Copper": _mc(
        "Copper",
        "Electrification, power infrastructure, industrial capex and electrical-equipment character.",
        "Important indirect/direct input channel for electrical systems, cables, "
        "equipment and industrial projects; also a global growth signal.",
        [
            "Copper price → material procurement cost → project margin",
            "Copper demand → electrification/capex → infrastructure orders",
            "Copper supply disruption → procurement/logistics → execution risk",
            "Copper cycle → industrial investment → order inflow",
        ],
        [
            "Estimate LT sensitivity to copper returns with lag structures.",
            "Compare copper moves with infrastructure/energy order inflows.",
            "Use procurement-cost proxies where available.",
            "Control for NIFTY and crude when measuring incremental sensitivity.",
            "Use event studies around major copper supply shocks.",
        ],
        [
            "Copper return",
            "Copper volatility",
            "Copper-to-equity-cycle indicator",
            "LT Infrastructure/Power order inflow",
            "Project margin",
        ],
        [
            "Mine/smelter disruptions",
            "Large copper price shocks",
            "Grid/electrification capex announcements",
            "Major power-transmission orders",
        ],
        ["1D", "1W", "1M", "3M", "6M", "1Y"],
    ),

    "Aluminium": _mc(
        "Aluminium",
        "Lightweight engineering, electrical, transport, fabrication and industrial-input character.",
        "Mixed input and demand exposure through engineered products, electrical "
        "systems, transport infrastructure, construction and industrial equipment.",
        [
            "Aluminium price → procurement/input cost → project margin",
            "Aluminium demand → construction/transport/industrial capex → EPC demand",
            "Aluminium volatility → procurement uncertainty → execution economics",
            "Aluminium cycle → global industrial activity → international orders",
        ],
        [
            "Measure LT/aluminium rolling correlation and lagged sensitivity.",
            "Test cost-sensitive segments separately from demand-sensitive segments.",
            "Use aluminium volatility and price shocks as event variables.",
            "Control for copper, NIFTY and crude where appropriate.",
        ],
        [
            "Aluminium return",
            "Aluminium volatility",
            "Industrial-metal index",
            "Project margin",
            "Infrastructure order inflow",
        ],
        [
            "Major aluminium price shocks",
            "Smelter/supply disruptions",
            "Infrastructure and transport capex announcements",
            "Large material-cost changes",
        ],
        ["1D", "1W", "1M", "3M", "6M", "1Y"],
    ),

    "Zinc": _mc(
        "Zinc",
        "Galvanising, corrosion protection and industrial/construction-cycle character.",
        "Primarily indirect through steel/infrastructure ecosystem, galvanised "
        "products, construction and industrial capex rather than as a dominant L&T raw material.",
        [
            "Zinc cycle → galvanised steel/infrastructure demand → project activity",
            "Zinc price → industrial input-cost signal → capex cycle",
            "Zinc supply/price shock → broader metal-cycle regime → project economics",
        ],
        [
            "Test LT/zinc rolling correlation and lagged relationships.",
            "Compare zinc with steel and copper as industrial-cycle variables.",
            "Control for NIFTY and broad metal indices.",
            "Use regime analysis for construction/industrial expansions and contractions.",
        ],
        [
            "Zinc return",
            "Zinc volatility",
            "Steel/metal index",
            "Infrastructure order inflow",
            "Industrial-production proxy",
        ],
        [
            "Major zinc supply shocks",
            "Infrastructure-cycle changes",
            "Industrial-metal price shocks",
            "Large construction-capex changes",
        ],
        ["1D", "1W", "1M", "3M", "6M", "1Y"],
    ),

    "Electricity": _mc(
        "Core industrial operating-cost and power-infrastructure character.",
        "Direct operating/input exposure for manufacturing and fabrication, plus "
        "major positive demand linkage through power transmission, distribution, "
        "generation and energy-infrastructure EPC.",
        [
            "Electricity cost → manufacturing/fabrication cost → project margin",
            "Power demand → generation/transmission investment → EPC demand",
            "Power shortages/volatility → execution/production risk",
            "Grid investment → transmission/distribution orders → revenue visibility",
        ],
        [
            "Use a reliable electricity-price or power-market series.",
            "Measure LT sensitivity to electricity-cost changes with lags.",
            "Separate electricity-price effects from power-infrastructure demand.",
            "Test project-margin response where segment data permits.",
            "Control for NIFTY, crude and industrial-cycle variables.",
        ],
        [
            "Power price",
            "Power demand",
            "Peak demand",
            "Grid/transmission capex",
            "Manufacturing energy cost",
            "Power-sector order inflow",
        ],
        [
            "Grid expansion announcements",
            "Power shortages",
            "Large electricity-price shocks",
            "Transmission/distribution orders",
            "Generation and renewable-capex announcements",
        ],
        ["intraday", "1D", "1W", "1M", "3M", "6M", "1Y"],
    ),
}


# Attach the nine market characters to the company character.
COMPANY_CHARACTER = CompanyCharacter(
    symbol=COMPANY_CHARACTER.symbol,
    company_name=COMPANY_CHARACTER.company_name,
    sector=COMPANY_CHARACTER.sector,
    industry_character=COMPANY_CHARACTER.industry_character,
    business_character=COMPANY_CHARACTER.business_character,
    demand_drivers=COMPANY_CHARACTER.demand_drivers,
    revenue_drivers=COMPANY_CHARACTER.revenue_drivers,
    cost_drivers=COMPANY_CHARACTER.cost_drivers,
    supply_chain_character=COMPANY_CHARACTER.supply_chain_character,
    strategic_drivers=COMPANY_CHARACTER.strategic_drivers,
    key_indicators=COMPANY_CHARACTER.key_indicators,
    key_events=COMPANY_CHARACTER.key_events,
    market_characters=MARKET_CHARACTERS,
)


def get_company_character() -> CompanyCharacter:
    """Return the complete L&T company character."""
    return COMPANY_CHARACTER


def get_market_character(market: str) -> MarketCharacter:
    """Return one market character for L&T."""
    key = market.strip()
    if key not in MARKET_CHARACTERS:
        raise KeyError(
            f"Unsupported market: {market!r}. "
            f"Expected one of: {', '.join(TRACKED_MARKETS)}"
        )
    return MARKET_CHARACTERS[key]


def get_all_market_characters() -> Dict[str, MarketCharacter]:
    """Return all nine market characters."""
    return dict(MARKET_CHARACTERS)


def validate_character() -> dict:
    """
    Structural validation only.

    This deliberately does not validate market-performance values because
    those must come from the later historical-data calculation engine.
    """
    expected = set(TRACKED_MARKETS)
    actual = set(MARKET_CHARACTERS)

    missing = sorted(expected - actual)
    extra = sorted(actual - expected)

    return {
        "symbol": COMPANY_CHARACTER.symbol,
        "markets_expected": len(TRACKED_MARKETS),
        "markets_found": len(MARKET_CHARACTERS),
        "missing_markets": missing,
        "extra_markets": extra,
        "valid": not missing and not extra and len(MARKET_CHARACTERS) == 9,
        "calculated_fields_present": False,
        "note": (
            "Rank/PCT_CHANGE/LINKAGE_SCORE/RELATION are intentionally not "
            "stored here. Historical calculations belong to the later engine."
        ),
    }


if __name__ == "__main__":
    print(validate_character())
    for market in TRACKED_MARKETS:
        mc = get_market_character(market)
        print(f"{market}: {mc.character}")
