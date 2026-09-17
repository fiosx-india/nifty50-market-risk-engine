"""
MAXHEALTH_9_MARKETS_CHARACTER
Max Healthcare Institute Limited (MAXHEALTH)

Character layer for the focused NIFTY 50 / 9-market research engine.

The module describes:
Company Character -> healthcare demand -> revenue -> operating cost ->
capacity/expansion -> supply chain -> strategic events -> market pathways.

No RANK, PCT_CHANGE, LINKAGE_SCORE or fixed RELATION values are hard-coded.
Those must be calculated later from real historical observations.
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
# MAX HEALTHCARE COMPANY CHARACTER
# ---------------------------------------------------------------------------

COMPANY_CHARACTER = CompanyCharacter(
    symbol="MAXHEALTH",
    company_name="Max Healthcare Institute Limited",
    sector="Healthcare Services",
    industry_character=(
        "Hospital-led healthcare platform whose character is driven by patient "
        "volumes, case mix, occupancy, average revenue per occupied bed, clinical "
        "specialty mix, doctor ecosystem, payer mix, medical inflation, capacity "
        "expansion, acquisitions, hospital ramp-up and operating leverage."
    ),
    business_character=[
        "Integrated hospital network with a strong super-speciality and tertiary/quaternary-care character.",
        "Revenue is primarily linked to inpatient and outpatient healthcare activity, clinical specialties and patient case mix.",
        "Hospital economics depend heavily on occupancy, average revenue per occupied bed, length of stay and clinical complexity.",
        "Growth is driven by brownfield/greenfield capacity additions, hospital ramp-up and acquisitions.",
        "A large clinical workforce, doctors, nurses, technicians and support staff form a critical operating ecosystem.",
        "Medical technology, diagnostics, pharmacy, implants, consumables and specialised equipment are important inputs.",
        "Healthcare demand is less directly tied to commodity prices than manufacturing businesses, but operating costs and macro wealth conditions still matter.",
        "The company has an expansion/M&A character, making capital allocation, project execution and new-bed ramp-up important.",
    ],
    demand_drivers=[
        "Growth in healthcare utilisation.",
        "Increasing prevalence of chronic and complex diseases.",
        "Demand for oncology, cardiology, neurosciences, orthopaedics, renal and other specialised care.",
        "Rising healthcare awareness and insurance penetration.",
        "Medical tourism and international patients.",
        "Population growth and ageing.",
        "Urbanisation and expansion of organised tertiary healthcare.",
        "New hospital capacity and geographic expansion.",
        "Doctor availability and specialty capacity.",
    ],
    revenue_drivers=[
        "Inpatient admissions.",
        "Outpatient visits.",
        "Occupancy rate.",
        "Average revenue per occupied bed (ARPOB).",
        "Case mix and clinical complexity.",
        "Specialty mix.",
        "International patient revenue.",
        "Insurance/corporate payer mix.",
        "Diagnostics and ancillary services.",
        "New-bed additions and hospital ramp-up.",
        "Acquired hospital integration and utilisation.",
    ],
    cost_drivers=[
        "Doctor and clinical staff costs.",
        "Nursing and employee costs.",
        "Medical consumables.",
        "Implants and high-value medical devices.",
        "Pharmacy and diagnostic inputs.",
        "Electricity and HVAC/cooling costs.",
        "Diesel/fuel and backup-power costs.",
        "Hospital facility maintenance.",
        "IT and medical technology systems.",
        "Rent/lease costs where applicable.",
        "Construction and capex costs for new hospitals.",
        "Interest and financing costs for expansion.",
    ],
    supply_chain_character=[
        "Hospital operations depend on continuous availability of medicines, implants, medical consumables and specialised equipment.",
        "Critical medical equipment has procurement lead times and import/FX dependencies in some categories.",
        "Hospital uptime depends on reliable electricity, backup power, HVAC, water, oxygen and other utilities.",
        "Expansion depends on land/building availability, construction contractors, equipment procurement, licensing and clinical staffing.",
        "Acquisitions introduce integration, regulatory, operational and ramp-up dependencies.",
        "Specialist doctor availability can constrain capacity more than physical beds alone.",
    ],
    strategic_drivers=[
        "Expansion of bed capacity.",
        "Brownfield and greenfield hospital development.",
        "Acquisition of hospitals and strategic assets.",
        "Higher-acuity/super-speciality mix.",
        "Improvement in occupancy and ARPOB.",
        "Clinical excellence and doctor recruitment.",
        "Geographic expansion into high-demand healthcare markets.",
        "Operating leverage from mature hospitals.",
        "Digital healthcare and technology adoption.",
    ],
    key_indicators=[
        "Occupancy",
        "ARPOB",
        "Average length of stay",
        "Inpatient admissions",
        "Outpatient volumes",
        "Case mix index",
        "Revenue growth",
        "Network operating EBITDA",
        "EBITDA margin",
        "Doctor count",
        "Bed capacity",
        "Operational beds",
        "New beds added",
        "Hospital ramp-up",
        "Medical consumables cost",
        "Employee cost",
        "Capex",
        "Net debt / cash",
        "Acquisition pipeline",
    ],
    key_events=[
        "Quarterly and annual results",
        "New hospital commissioning",
        "New-bed additions",
        "Hospital acquisitions",
        "Acquisition completion/integration",
        "Major specialty-centre launches",
        "Doctor/clinical leadership changes",
        "Regulatory or accreditation developments",
        "Healthcare policy changes",
        "Insurance reimbursement changes",
        "Medical equipment procurement",
        "Large capex announcements",
        "New-city expansion",
    ],
    market_characters={},
)


# ---------------------------------------------------------------------------
# NINE MARKET CHARACTERS
# ---------------------------------------------------------------------------

MARKET_CHARACTERS: Dict[str, MarketCharacter] = {

    "NIFTY 50": _mc(
        "NIFTY 50",
        "Indian equity-market, liquidity and macro-risk character.",
        "Direct market-beta/valuation exposure plus an indirect signal for "
        "household wealth, financing conditions and healthcare spending.",
        [
            "NIFTY regime -> equity risk appetite -> MAXHEALTH valuation",
            "Market/liquidity regime -> wealth/confidence -> elective healthcare demand",
            "Macro cycle -> insurance/corporate spending -> healthcare volumes",
        ],
        [
            "Calculate MAXHEALTH returns versus NIFTY returns.",
            "Estimate rolling correlation and rolling beta.",
            "Estimate downside beta during market stress.",
            "Separate market-wide movement from company-specific residual return.",
            "Test lead/lag behaviour.",
        ],
        [
            "MAXHEALTH return",
            "NIFTY return",
            "Rolling beta",
            "Rolling correlation",
            "Volatility",
            "Relative strength",
        ],
        [
            "Major NIFTY regime changes",
            "RBI/liquidity events",
            "Macro growth shocks",
            "Healthcare policy announcements",
            "Major risk-off episodes",
        ],
        ["intraday", "1D", "1W", "1M", "3M", "6M", "1Y"],
    ),

    "Crude Oil": _mc(
        "Crude Oil",
        "Fuel, logistics, petrochemical and inflation-cost character.",
        "Mostly indirect operating-cost and macro exposure rather than a core "
        "revenue driver.",
        [
            "Crude -> fuel/logistics cost -> hospital operating cost",
            "Crude -> petrochemical/plastic input costs -> medical consumables",
            "Crude -> inflation -> household real income -> healthcare affordability",
            "Crude shock -> rates/inflation -> valuation regime",
        ],
        [
            "Measure lagged MAXHEALTH/crude sensitivity.",
            "Use domestic fuel prices separately from global crude.",
            "Test whether crude affects margins through operating costs.",
            "Control for NIFTY and inflation.",
            "Test high-crude-volatility regimes separately.",
        ],
        [
            "Brent/WTI return",
            "Domestic fuel price",
            "Freight-cost proxy",
            "Medical-consumables cost",
            "EBITDA margin",
        ],
        [
            "OPEC+ decisions",
            "Major crude shocks",
            "Fuel-price changes",
            "Inflation shocks",
            "Logistics disruptions",
        ],
        ["1D", "1W", "1M", "3M", "6M", "1Y"],
    ),

    "Gold": _mc(
        "Gold",
        "Safe-haven, wealth, real-rate and risk-aversion character.",
        "Primarily an indirect macro/wealth indicator; no major direct gold "
        "input requirement in hospital operations.",
        [
            "Gold -> wealth/risk regime -> healthcare discretionary demand",
            "Gold/rates -> financial conditions -> valuation",
            "Gold/USD/global risk -> medical-tourism and macro environment",
        ],
        [
            "Measure rolling MAXHEALTH/gold relationship after controlling for NIFTY.",
            "Use gold as a macro regime variable, not a raw-material variable.",
            "Test high-risk-off periods separately.",
            "Compare with healthcare-sector performance.",
        ],
        [
            "Gold return",
            "Gold volatility",
            "Real-rate proxy",
            "USD index",
            "Healthcare-sector return",
        ],
        [
            "Safe-haven shocks",
            "Rate shocks",
            "Global geopolitical events",
            "Liquidity stress",
        ],
        ["1D", "1W", "1M", "3M", "6M"],
    ),

    "Silver": _mc(
        "Silver",
        "Precious-metal and industrial-cycle character.",
        "Indirect macro/industrial signal; direct hospital-input exposure is limited.",
        [
            "Silver industrial cycle -> broader economic activity -> healthcare demand",
            "Silver/risk regime -> market sentiment -> valuation",
            "Silver/electronics cycle -> medical-device/component availability",
        ],
        [
            "Calculate rolling MAXHEALTH/silver relationship.",
            "Compare silver with broader industrial indicators.",
            "Control for NIFTY and healthcare-sector return.",
            "Test lead/lag effects.",
        ],
        [
            "Silver return",
            "Gold/silver ratio",
            "Industrial-cycle proxy",
            "Healthcare-sector return",
            "MAXHEALTH volatility",
        ],
        [
            "Industrial-cycle shocks",
            "Silver volatility events",
            "Global manufacturing disruptions",
        ],
        ["1D", "1W", "1M", "3M", "6M"],
    ),

    "Natural Gas": _mc(
        "Natural Gas",
        "Industrial energy, electricity-generation and energy-cost character.",
        "Mostly indirect through hospital utilities, backup/energy economics, "
        "supplier costs and inflation.",
        [
            "Gas -> electricity/energy cost -> hospital utility expense",
            "Gas -> industrial input cost -> medical equipment/consumables",
            "Gas/inflation -> household affordability -> healthcare demand",
        ],
        [
            "Measure lagged MAXHEALTH/gas sensitivity.",
            "Use electricity data alongside gas because hospitals consume electricity.",
            "Test energy-cost effects on margins where data is available.",
            "Control for crude and NIFTY.",
        ],
        [
            "Natural-gas return",
            "Gas volatility",
            "Electricity-price proxy",
            "Utility cost",
            "EBITDA margin",
        ],
        [
            "Gas-price shocks",
            "Energy supply disruptions",
            "LNG/global gas events",
            "Large utility-cost changes",
        ],
        ["1D", "1W", "1M", "3M", "6M"],
    ),

    "Copper": _mc(
        "Copper",
        "Medical equipment, electrical systems and industrial-input character.",
        "Mostly indirect but potentially relevant through electrical wiring, "
        "medical equipment, HVAC and hospital construction.",
        [
            "Copper -> electrical/equipment input cost -> hospital capex",
            "Copper -> medical-device/component cost -> procurement cost",
            "Copper industrial cycle -> construction/capex environment",
        ],
        [
            "Calculate lagged MAXHEALTH/copper relationship.",
            "Test copper against hospital capex rather than treating it as a direct revenue driver.",
            "Separate mature-hospital operating cost from new-hospital construction cost.",
            "Control for NIFTY and construction-cost variables.",
        ],
        [
            "Copper return",
            "Copper volatility",
            "Hospital capex",
            "Equipment-cost proxy",
            "Construction-cost proxy",
        ],
        [
            "Copper supply shocks",
            "Medical-equipment procurement changes",
            "Major hospital construction projects",
            "Industrial-metal shocks",
        ],
        ["1D", "1W", "1M", "3M", "6M", "1Y"],
    ),

    "Aluminium": _mc(
        "Aluminium",
        "Medical equipment, construction, HVAC and facility-material character.",
        "Indirect operating/capex exposure through hospital construction, "
        "building systems, equipment and selected medical products.",
        [
            "Aluminium -> construction/material cost -> new hospital capex",
            "Aluminium -> equipment/component cost -> procurement",
            "Aluminium industrial cycle -> expansion cost and project timing",
        ],
        [
            "Measure lagged MAXHEALTH/aluminium relationship.",
            "Compare aluminium movements with capex/project announcements.",
            "Test whether material inflation affects expansion margins.",
            "Control for broader construction-cost and NIFTY variables.",
        ],
        [
            "Aluminium return",
            "Aluminium volatility",
            "Hospital capex",
            "Construction-cost proxy",
            "Equipment procurement cost",
        ],
        [
            "Aluminium price shocks",
            "New hospital construction",
            "Major equipment procurement",
            "Expansion-cost changes",
        ],
        ["1D", "1W", "1M", "3M", "6M", "1Y"],
    ),

    "Zinc": _mc(
        "Zinc",
        "Construction, galvanised-material and industrial-input character.",
        "Indirect exposure through hospital construction, building services "
        "and facility expansion; little direct clinical revenue linkage.",
        [
            "Zinc -> galvanised steel/construction input -> hospital capex",
            "Zinc -> industrial construction cycle -> expansion economics",
            "Zinc shock -> supplier costs -> project timing",
        ],
        [
            "Test MAXHEALTH/zinc lagged relationship.",
            "Relate zinc movements to capex and new-bed expansion periods.",
            "Control for steel and broader construction-material prices.",
            "Avoid treating zinc as a direct healthcare demand variable.",
        ],
        [
            "Zinc return",
            "Zinc volatility",
            "Steel price",
            "Construction-cost proxy",
            "Capex",
        ],
        [
            "Zinc supply shocks",
            "Construction-material inflation",
            "Major hospital expansion projects",
        ],
        ["1D", "1W", "1M", "3M", "6M"],
    ),

    "Electricity": _mc(
        "Electricity",
        "Core hospital operating-utility and facility-capacity character.",
        "The most operationally direct commodity/utility relationship among "
        "these markets: hospitals require continuous electricity for clinical "
        "equipment, HVAC, operating theatres, ICUs, diagnostics and support systems.",
        [
            "Electricity price -> utility expense -> hospital operating margin",
            "Power reliability -> clinical uptime -> patient capacity",
            "Electricity demand -> industrial/grid investment -> facility economics",
            "Power availability -> new hospital commissioning/ramp-up",
        ],
        [
            "Use reliable electricity-price or regional commercial-power data.",
            "Measure lagged electricity-cost sensitivity to margins.",
            "Test power disruptions as event variables.",
            "Separate electricity price from electricity availability.",
            "Compare mature-hospital utility intensity with newly commissioned facilities.",
        ],
        [
            "Commercial/industrial electricity price",
            "Power demand",
            "Peak demand",
            "Hospital utility cost",
            "EBITDA margin",
            "Operational beds",
        ],
        [
            "Power shortages",
            "Electricity-price shocks",
            "Grid disruptions",
            "New hospital commissioning",
            "Energy-efficiency/captive-power projects",
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
    """Return the complete Max Healthcare company character."""
    return COMPANY_CHARACTER


def get_market_character(market: str) -> MarketCharacter:
    """Return one of the nine Max Healthcare market characters."""
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
    """Structural validation only; no market score is calculated."""
    expected = set(TRACKED_MARKETS)
    actual = set(MARKET_CHARACTERS)
    missing = sorted(expected - actual)
    extra = sorted(actual - expected)

    return {
        "symbol": COMPANY_CHARACTER.symbol,
        "markets_expected": 9,
        "markets_found": len(MARKET_CHARACTERS),
        "missing_markets": missing,
        "extra_markets": extra,
        "valid": not missing and not extra and len(MARKET_CHARACTERS) == 9,
        "calculated_fields_present": False,
        "note": (
            "RANK/PCT_CHANGE/LINKAGE_SCORE/RELATION are intentionally absent. "
            "Historical relationships belong to the later calculation engine."
        ),
    }


if __name__ == "__main__":
    print(validate_character())
    for market in TRACKED_MARKETS:
        print(f"{market}: {get_market_character(market).character}")
