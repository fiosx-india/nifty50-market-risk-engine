"""
COALINDIA (Coal India Limited) — Company Character & 9-Market Relationship Engine

CHARACTER LAYER ONLY
--------------------
This module describes:
    Company Character
        -> coal-mining / energy-sector character
        -> demand and customer character
        -> production / dispatch / realization character
        -> cost and mining-operation character
        -> diversification character
        -> 9 tracked market characters
        -> historical-calculation instructions

It deliberately does NOT hard-code:
    RANK
    PCT_CHANGE
    LINKAGE_SCORE
    RELATION

Those are historical-calculation outputs and must be derived later from
real market, operating, financial and event data.

Important:
Coal India is not treated like a normal commodity consumer. Coal is its
core product. Therefore the nine-market relationships are modeled primarily
through electricity demand, substitution economics, industrial activity,
energy prices, mining inputs and broad equity/macroeconomic conditions.
"""

from dataclasses import dataclass, field
from typing import Dict, List


TRACKED_MARKETS = (
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
    relevant_indicators: List[str] = field(default_factory=list)
    relevant_events: List[str] = field(default_factory=list)
    expected_timeframes: List[str] = field(
        default_factory=lambda: [
            "intraday", "1D", "1W", "1M", "3M", "6M", "1Y"
        ]
    )


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
    market_characters: Dict[str, MarketCharacter]


COALINDIA_MARKETS: Dict[str, MarketCharacter] = {

    "NIFTY 50": MarketCharacter(
        market="NIFTY 50",
        character=(
            "Primary systematic equity-market character for Coal India. "
            "Large-cap institutional flows, Indian risk appetite, PSU sentiment, "
            "energy-sector expectations and broad market liquidity can affect "
            "valuation and relative performance."
        ),
        exposure_character=(
            "Direct systematic equity exposure with additional PSU, energy and "
            "commodity-sector factor exposure."
        ),
        impact_path=[
            "NIFTY 50 movement",
            "Indian equity liquidity and risk appetite",
            "PSU / energy / commodity sector flows",
            "Coal India valuation",
            "COALINDIA relative performance",
        ],
        calculation_logic=[
            "Calculate Coal India return against NIFTY 50 over matched windows.",
            "Estimate rolling correlation and rolling beta rather than using the supplied fixed linkage.",
            "Calculate excess return after controlling for NIFTY 50.",
            "Where data permits, separately control for PSU and energy-sector factors.",
            "Test lead/lag behaviour around commodity and power-demand shocks.",
        ],
        relevant_indicators=[
            "Coal India return",
            "NIFTY 50 return",
            "rolling beta",
            "rolling correlation",
            "relative strength",
            "volume",
            "volatility",
        ],
        relevant_events=[
            "market-wide risk-on/risk-off events",
            "Union Budget",
            "coal-sector policy",
            "energy-sector policy",
            "Coal India production/dispatch updates",
            "quarterly and annual results",
        ],
    ),

    "Crude Oil": MarketCharacter(
        market="Crude Oil",
        character=(
            "Energy-substitution, freight, mining-input and macro-inflation "
            "character. Crude is not Coal India's core product, but it can affect "
            "energy substitution economics, diesel-heavy mining/logistics costs "
            "and the broader energy market."
        ),
        exposure_character=(
            "Indirect exposure through mining fuel, logistics, inflation and "
            "relative economics between coal and other energy sources."
        ),
        impact_path=[
            "Crude oil price",
            "diesel / transport / mining operating cost",
            "coal logistics and mine economics",
            "power-sector fuel economics and coal demand",
            "Coal India margins / earnings expectations",
        ],
        calculation_logic=[
            "Measure contemporaneous and lagged crude/Coal India relationships.",
            "Separate mining-cost sensitivity from broader energy-substitution effects.",
            "Control for NIFTY 50 and electricity/power-demand conditions.",
            "Compare crude shocks with diesel-related operating-cost indicators when available.",
            "Use event studies for unusually large crude movements.",
        ],
        relevant_indicators=[
            "crude return",
            "diesel-price proxy",
            "freight/logistics proxy",
            "coal production",
            "coal dispatch",
            "operating margin",
        ],
        relevant_events=[
            "large crude shocks",
            "fuel-price changes",
            "geopolitical energy disruptions",
            "major freight-cost changes",
        ],
    ),

    "Gold": MarketCharacter(
        market="Gold",
        character=(
            "Macro safe-haven, real-rate and liquidity character. Gold has no "
            "direct core operational role in Coal India; it is useful primarily "
            "as a global risk and capital-flow regime variable."
        ),
        exposure_character=(
            "Indirect macro and portfolio-flow exposure."
        ),
        impact_path=[
            "Gold price",
            "global risk / real-rate / liquidity regime",
            "Indian equity and commodity-sector flows",
            "PSU / energy valuation sentiment",
            "Coal India stock response",
        ],
        calculation_logic=[
            "Measure rolling and lagged gold/Coal India relationships.",
            "Control for NIFTY 50 and volatility conditions.",
            "Test whether gold sensitivity changes during risk-off regimes.",
            "Compare gold with USD/INR and rates to distinguish common macro factors.",
            "Do not infer a causal relationship from correlation alone.",
        ],
        relevant_indicators=[
            "gold return",
            "USD/INR",
            "real-rate proxy",
            "volatility proxy",
            "Coal India relative strength",
        ],
        relevant_events=[
            "global risk-off events",
            "central-bank rate decisions",
            "major geopolitical shocks",
            "currency stress events",
        ],
    ),

    "Silver": MarketCharacter(
        market="Silver",
        character=(
            "Industrial-cycle and precious-metal sentiment character. Silver is "
            "not a core Coal India input or output; it can act as a proxy for "
            "industrial activity, commodity sentiment and global growth conditions."
        ),
        exposure_character=(
            "Indirect industrial-cycle and commodity-sentiment exposure."
        ),
        impact_path=[
            "Silver price",
            "industrial / commodity-cycle signal",
            "power and manufacturing activity expectations",
            "coal demand expectations",
            "Coal India market response",
        ],
        calculation_logic=[
            "Measure rolling and lagged silver/Coal India relationships.",
            "Compare silver with copper to identify common industrial-cycle factors.",
            "Control for NIFTY 50 and electricity/power demand.",
            "Test relationships during expansion, slowdown and commodity-risk regimes.",
        ],
        relevant_indicators=[
            "silver return",
            "copper return",
            "industrial-cycle proxy",
            "power demand",
            "Coal India return",
        ],
        relevant_events=[
            "global industrial shocks",
            "commodity volatility events",
            "global growth surprises",
        ],
    ),

    "Natural Gas": MarketCharacter(
        market="Natural Gas",
        character=(
            "Important energy-substitution character. Natural gas can compete "
            "with coal in power and industrial applications; its price can alter "
            "the relative economics of coal-fired and gas-fired generation and "
            "industrial fuel choice."
        ),
        exposure_character=(
            "Indirect-to-moderate energy-substitution and demand exposure, plus "
            "broader energy-market effects."
        ),
        impact_path=[
            "Natural-gas price",
            "gas-versus-coal generation/fuel economics",
            "power-sector fuel switching",
            "coal demand / dispatch",
            "Coal India revenue and earnings",
        ],
        calculation_logic=[
            "Calculate lagged natural-gas/Coal India relationships across multiple windows.",
            "Construct coal-versus-gas relative-price variables where data permits.",
            "Control for electricity demand, crude oil and NIFTY 50.",
            "Test whether gas-price shocks change coal dispatch with an operational lag.",
            "Separate global gas-price effects from India-specific gas availability and tariffs.",
        ],
        relevant_indicators=[
            "natural-gas return",
            "coal price",
            "coal/gas relative economics",
            "power generation",
            "coal dispatch",
            "coal stock at power plants",
        ],
        relevant_events=[
            "LNG/natural-gas supply disruptions",
            "large gas-price shocks",
            "power-sector fuel-switching events",
            "gas availability changes",
            "major energy-policy changes",
        ],
    ),

    "Copper": MarketCharacter(
        market="Copper",
        character=(
            "Industrial-cycle and mining-equipment input character. Copper is "
            "not Coal India's core product, but copper prices can signal industrial "
            "activity and can affect electrical/equipment supply costs in mining "
            "operations."
        ),
        exposure_character=(
            "Indirect industrial-demand and mining-input-cost exposure."
        ),
        impact_path=[
            "Copper price",
            "industrial-cycle signal / equipment input cost",
            "mining and infrastructure economics",
            "coal demand or operating cost",
            "Coal India earnings expectations",
        ],
        calculation_logic=[
            "Measure rolling and lagged copper/Coal India relationships.",
            "Separate industrial-demand signal from input-cost effects.",
            "Compare copper with aluminium and zinc as a common industrial-metals factor.",
            "Control for NIFTY 50 and electricity demand.",
            "Use mining capex/production data to test whether the relationship has an operating path.",
        ],
        relevant_indicators=[
            "copper return",
            "industrial-metals basket",
            "mining capex",
            "coal production",
            "coal dispatch",
            "operating margin",
        ],
        relevant_events=[
            "major copper supply shocks",
            "industrial-cycle shocks",
            "mining-equipment cost changes",
            "large Coal India capex events",
        ],
    ),

    "Aluminium": MarketCharacter(
        market="Aluminium",
        character=(
            "Industrial-cycle, mining-equipment and electricity-intensive-metals "
            "character. Aluminium is useful both as an industrial-demand signal "
            "and as a relative indicator for energy-intensive manufacturing."
        ),
        exposure_character=(
            "Indirect industrial-demand and mining-equipment cost exposure."
        ),
        impact_path=[
            "Aluminium price",
            "industrial activity / energy-intensive manufacturing signal",
            "power and industrial coal demand",
            "coal dispatch / production economics",
            "Coal India earnings expectations",
        ],
        calculation_logic=[
            "Measure rolling and lagged aluminium/Coal India relationships.",
            "Compare aluminium with copper and zinc to identify common industrial-cycle effects.",
            "Control for electricity demand and NIFTY 50.",
            "Test whether aluminium-price moves precede changes in industrial coal demand.",
            "Separate demand-signal effects from mining-equipment/input-cost effects.",
        ],
        relevant_indicators=[
            "aluminium return",
            "industrial-metals basket",
            "power demand",
            "industrial production proxy",
            "coal dispatch",
            "Coal India return",
        ],
        relevant_events=[
            "aluminium supply shocks",
            "industrial production changes",
            "large power-demand changes",
            "energy-intensive industry developments",
        ],
    ),

    "Zinc": MarketCharacter(
        market="Zinc",
        character=(
            "Industrial infrastructure and galvanising-cycle character. Zinc is "
            "not a direct Coal India product, but its industrial-cycle signal can "
            "reflect construction, infrastructure and manufacturing activity that "
            "affects electricity and coal demand."
        ),
        exposure_character=(
            "Indirect industrial-demand and mining-infrastructure exposure."
        ),
        impact_path=[
            "Zinc price",
            "construction / infrastructure / manufacturing activity",
            "electricity and industrial energy demand",
            "coal demand",
            "Coal India dispatch and earnings",
        ],
        calculation_logic=[
            "Measure rolling and lagged zinc/Coal India relationships.",
            "Compare zinc with copper and aluminium as a common industrial-cycle factor.",
            "Control for NIFTY 50 and electricity demand.",
            "Test whether zinc changes lead industrial/power coal demand.",
            "Use sector-level demand data to avoid treating correlation as direct causation.",
        ],
        relevant_indicators=[
            "zinc return",
            "industrial-metals basket",
            "construction/infrastructure proxy",
            "power demand",
            "coal dispatch",
            "Coal India return",
        ],
        relevant_events=[
            "zinc supply shocks",
            "infrastructure spending changes",
            "industrial-cycle events",
            "large power-demand changes",
        ],
    ),

    "Electricity": MarketCharacter(
        market="Electricity",
        character=(
            "Core demand-side character for Coal India. Coal is a major fuel for "
            "India's power system, so electricity demand, generation, peak load, "
            "plant utilisation and coal stock levels can directly affect coal "
            "dispatch requirements. This relationship is demand-side rather than "
            "an electricity cost input to Coal India."
        ),
        exposure_character=(
            "Direct-to-strong demand exposure through thermal-power generation, "
            "coal offtake, dispatch and power-sector fuel requirements."
        ),
        impact_path=[
            "Electricity demand / generation",
            "thermal power generation requirement",
            "coal consumption and plant stock position",
            "coal dispatch / offtake",
            "Coal India production and sales",
            "revenue / realization / earnings",
        ],
        calculation_logic=[
            "Measure electricity-demand changes against Coal India dispatch with appropriate lags.",
            "Use peak demand, total generation and thermal-generation share separately.",
            "Track coal stock at power plants and relate stock changes to future dispatch.",
            "Control for rainfall, hydro generation, renewable generation and seasonality where data permits.",
            "Separate electricity-demand effects from coal-price and policy effects.",
            "Test weekly, monthly and seasonal relationships because power demand is strongly time-dependent.",
        ],
        relevant_indicators=[
            "peak electricity demand",
            "total electricity generation",
            "thermal generation",
            "thermal utilisation",
            "coal consumption by power sector",
            "power-plant coal stocks",
            "Coal India production",
            "Coal India dispatch",
            "offtake",
            "coal realization",
        ],
        relevant_events=[
            "record peak-power demand",
            "heatwaves",
            "monsoon / rainfall changes",
            "hydro-generation changes",
            "renewable-generation changes",
            "thermal plant outages",
            "coal-stock shortages",
            "power-sector fuel-supply interventions",
            "government coal-stock directives",
        ],
    ),
}


COALINDIA_CHARACTER = CompanyCharacter(
    symbol="COALINDIA",
    company_name="Coal India Limited",
    sector="Coal Mining / Primary Energy",
    industry_character=(
        "Large-scale Indian coal mining and primary-energy company whose core "
        "economic character is production, dispatch and realization of coal. "
        "Its demand is strongly linked to thermal power generation and also to "
        "steel, cement and other industrial consumers. Its operating character "
        "is shaped by mine geology, production capacity, overburden removal, "
        "monsoon, rail/logistics, labour, environmental permissions, coal quality, "
        "customer demand and government energy policy."
    ),
    business_character=[
        "Open-cast coal mining",
        "Underground coal mining",
        "Thermal-power coal supply",
        "Non-power industrial coal supply",
        "Coking coal production and supply",
        "Non-coking coal production and supply",
        "Coal dispatch and marketing",
        "Mine development and expansion",
        "Exploration and mine planning",
        "Mining consultancy and technical services",
        "Coal washeries / coal-quality management",
        "Coal logistics and evacuation",
        "Coal gasification initiatives",
        "Diversification into energy and related businesses",
        "Subsidiary-led mining operations across multiple coalfields",
    ],
    demand_drivers=[
        "Indian electricity demand",
        "Thermal power generation",
        "Peak power demand",
        "Thermal plant utilisation",
        "Power-plant coal stock levels",
        "Steel production",
        "Cement production",
        "Industrial production",
        "Railway and logistics availability",
        "Domestic coal substitution for imports",
        "Coal-quality requirements",
        "Government energy policy",
        "Seasonality and weather",
        "Hydro and renewable generation",
    ],
    revenue_drivers=[
        "Coal production volume",
        "Coal offtake / dispatch volume",
        "Coal grade and quality",
        "Realized coal price",
        "E-auction realization",
        "Linkage / regulated sales",
        "Power-sector demand",
        "Non-power industrial demand",
        "Coking-coal demand",
        "Commercial coal initiatives",
        "Diversification / new-energy projects",
    ],
    cost_drivers=[
        "Employee and labour costs",
        "Overburden removal",
        "Diesel and fuel",
        "Explosives",
        "Heavy mining equipment",
        "Contract mining services",
        "Rail freight and evacuation",
        "Mine development",
        "Land and rehabilitation",
        "Environmental compliance",
        "Mine safety",
        "Power and mine electricity",
        "Maintenance",
        "Interest / financing where applicable",
        "Diversification and capex spending",
    ],
    supply_chain_character=[
        "Large network of mining subsidiaries",
        "Mine-to-rail logistics",
        "Railway evacuation",
        "Road transportation",
        "Mining equipment suppliers",
        "Heavy earth-moving machinery",
        "Explosives suppliers",
        "Contract mining ecosystem",
        "Power-sector customers",
        "Steel and cement customers",
        "Coal handling and preparation infrastructure",
        "Ports / coastal logistics where relevant",
        "Government and regulatory ecosystem",
    ],
    strategic_drivers=[
        "Coal production growth",
        "Production-capacity expansion",
        "Mine-opening and mine-development programme",
        "Rail evacuation capacity",
        "Domestic coal substitution",
        "Power-sector security of supply",
        "Coal-quality improvement",
        "Commercial mining / diversification",
        "Coal gasification",
        "Renewable-energy diversification",
        "Mining technology and mechanisation",
        "Mine safety",
        "Environmental and land-management improvements",
        "Operational efficiency",
        "Long-term energy-security role",
    ],
    key_indicators=[
        "coal production",
        "coal offtake",
        "coal dispatch",
        "production growth",
        "offtake growth",
        "inventory / pithead stock",
        "power-sector dispatch",
        "non-power dispatch",
        "e-auction volume",
        "e-auction realization",
        "average realization",
        "coal grade mix",
        "overburden removal",
        "employee cost",
        "fuel cost",
        "freight cost",
        "EBITDA",
        "EBITDA margin",
        "PAT",
        "operating cash flow",
        "capex",
        "receivables",
        "power-sector coal stock",
        "thermal generation",
        "peak electricity demand",
        "COALINDIA stock return",
        "COALINDIA volume",
        "relative strength versus NIFTY 50",
    ],
    key_events=[
        "monthly production updates",
        "monthly offtake / dispatch updates",
        "major mine openings",
        "mine expansion approvals",
        "production-target changes",
        "railway evacuation developments",
        "power-sector coal-stock shortages",
        "government coal-allocation changes",
        "e-auction policy changes",
        "coal-price changes",
        "coal-quality / grade changes",
        "commercial-mining policy",
        "coal-gasification projects",
        "renewable-energy diversification",
        "major capex announcements",
        "mine accidents",
        "safety-regulation changes",
        "environmental approvals",
        "land-acquisition developments",
        "labour / wage agreements",
        "major power-sector demand shocks",
        "heatwaves and extreme-weather events",
        "monsoon disruptions",
        "quarterly and annual results",
        "dividend announcements",
        "government ownership / policy decisions",
    ],
    market_characters=COALINDIA_MARKETS,
)


def get_company_character() -> CompanyCharacter:
    """Return the complete Coal India company character."""
    return COALINDIA_CHARACTER


def get_market_character(market: str) -> MarketCharacter:
    """Return Coal India's character for one of the nine tracked markets."""
    try:
        return COALINDIA_MARKETS[market]
    except KeyError as exc:
        raise ValueError(
            f"Unsupported market: {market!r}. "
            f"Expected one of: {', '.join(TRACKED_MARKETS)}"
        ) from exc


def get_all_market_characters() -> Dict[str, MarketCharacter]:
    """Return all nine Coal India market characters."""
    return dict(COALINDIA_MARKETS)


def validate_character() -> bool:
    """
    Validate the Coal India character contract.

    Historical result fields are deliberately excluded from this layer.
    """
    if COALINDIA_CHARACTER.symbol != "COALINDIA":
        return False

    if set(COALINDIA_MARKETS) != set(TRACKED_MARKETS):
        return False

    for market_name, character in COALINDIA_MARKETS.items():
        if character.market != market_name:
            return False
        if not character.character:
            return False
        if not character.exposure_character:
            return False
        if not character.impact_path:
            return False
        if not character.calculation_logic:
            return False

    forbidden_fields = {
        "RANK",
        "PCT_CHANGE",
        "LINKAGE_SCORE",
        "RELATION",
        "SCORE",
    }

    if forbidden_fields.intersection(COALINDIA_CHARACTER.__dataclass_fields__):
        return False

    return True


if __name__ == "__main__":
    print(f"{COALINDIA_CHARACTER.company_name} ({COALINDIA_CHARACTER.symbol})")
    print(f"Tracked markets: {len(COALINDIA_MARKETS)}")
    print(f"Character validation: {validate_character()}")

    for market_name in TRACKED_MARKETS:
        character = COALINDIA_MARKETS[market_name]
        print(f"- {market_name}: {character.character}")
