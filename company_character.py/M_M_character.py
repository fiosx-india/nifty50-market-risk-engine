"""
M_M_9_MARKETS_CHARACTER
Mahindra & Mahindra Limited (M&M)

Character layer for the focused NIFTY 50 / 9-market research engine.

The company character is deliberately based on M&M's actual business mix:
Automotive, Farm Equipment and the wider Services/Industrial portfolio.
The nine market characters describe mechanisms to be tested later with
historical data; they are NOT fixed scores or trading signals.

No RANK, PCT_CHANGE, LINKAGE_SCORE or fixed RELATION values are hard-coded.
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


COMPANY_CHARACTER = CompanyCharacter(
    symbol="M&M",
    company_name="Mahindra & Mahindra Limited",
    sector="Automotive, Farm Equipment & Diversified Services",
    industry_character=(
        "Diversified operating and holding-company character centred on "
        "Automotive and Farm Equipment, with additional exposure through "
        "Financial Services and Industrial/Consumer Services. The core "
        "economic engine is vehicle and tractor volumes, product mix, rural "
        "income, financing, commodity costs, manufacturing capacity, exports "
        "and new-product execution."
    ),
    business_character=[
        "Automotive: SUVs, passenger vehicles, pickups, light commercial vehicles, three-wheelers, electric vehicles, two-wheelers, construction equipment, spares and related services.",
        "Farm Equipment: tractors, implements, spares and related farm-power products across Mahindra, Swaraj and Trakstar brands.",
        "Electric mobility: electric three-wheelers and electric four-wheelers, with EV product development and manufacturing capability.",
        "Construction equipment and powertrain businesses add industrial-cycle and infrastructure exposure.",
        "Financial Services provides retail/other loans, SME finance, housing finance, mutual funds and insurance-broking services.",
        "The wider Services/Industrial portfolio includes IT services, real estate, hospitality, logistics, renewables, defence, agri and other businesses.",
        "Global operations create export, FX, freight and country-specific demand exposure.",
        "R&D, design, connected vehicles and software-defined vehicle capabilities make technology execution an important long-term driver.",
    ],
    demand_drivers=[
        "Indian SUV and passenger-vehicle demand.",
        "Light commercial vehicle and last-mile mobility demand.",
        "Rural income, crop prices and farm cash flows.",
        "Tractor replacement and farm mechanisation cycle.",
        "Interest rates and vehicle/tractor financing availability.",
        "Government infrastructure and construction activity.",
        "EV adoption and policy support.",
        "Export-market demand.",
        "New model launches and product acceptance.",
        "Fleet replacement and commercial activity.",
    ],
    revenue_drivers=[
        "Automotive volumes.",
        "SUV/product mix.",
        "LCV and commercial-vehicle volumes.",
        "Electric three-wheeler and four-wheeler volumes.",
        "Tractor volumes.",
        "Average selling price and premiumisation.",
        "Exports.",
        "Spare-parts revenue.",
        "Financial Services assets under management and loan growth.",
        "Industrial/consumer-services portfolio performance.",
    ],
    cost_drivers=[
        "Steel and ferrous-metal prices.",
        "Aluminium prices.",
        "Copper and electrical-component costs.",
        "Rubber, plastics, glass and other automotive materials.",
        "Crude-linked petrochemical and logistics costs.",
        "Electricity and plant energy costs.",
        "Natural-gas/industrial-energy costs.",
        "Imported components and foreign exchange.",
        "Freight and logistics.",
        "Employee and engineering costs.",
        "Battery and power-electronics costs as EV volumes increase.",
        "Interest and funding costs in Financial Services.",
    ],
    supply_chain_character=[
        "Large automotive and farm-equipment supplier ecosystem.",
        "Tiered suppliers for metals, electronics, tyres, castings, forgings and components.",
        "Semiconductor and electronic-component availability can affect vehicle production.",
        "Tractor production is exposed to agricultural component and machinery supply chains.",
        "EV growth increases battery, power-electronics and specialised-component dependencies.",
        "Exports add port, shipping, customs and FX dependencies.",
        "Manufacturing capacity and supplier continuity determine the ability to convert demand into sales.",
    ],
    strategic_drivers=[
        "SUV portfolio growth and product leadership.",
        "Farm mechanisation and tractor market leadership.",
        "EV product expansion.",
        "Capacity expansion and manufacturing efficiency.",
        "R&D and software-defined/connected vehicle capabilities.",
        "Global automotive expansion.",
        "Rural and semi-urban financial-services penetration.",
        "Renewables and other growth businesses.",
        "Capital allocation across the wider Mahindra portfolio.",
    ],
    key_indicators=[
        "Automotive monthly sales",
        "SUV volume",
        "LCV volume",
        "Electric 3-wheeler volume",
        "Electric 4-wheeler volume",
        "Export volume",
        "Tractor volume",
        "Domestic tractor market share",
        "Automotive market share",
        "Average selling price",
        "Material cost",
        "Operating margin",
        "Capacity utilisation",
        "Production volume",
        "Financial Services AUM",
        "Loan growth",
        "Asset quality",
        "Capex",
        "R&D expenditure",
        "FX exposure",
    ],
    key_events=[
        "Monthly automotive sales",
        "Monthly tractor sales",
        "Quarterly and annual results",
        "New SUV launches",
        "New tractor launches",
        "EV launches",
        "Capacity additions",
        "Plant commissioning",
        "Major export-market expansion",
        "Government auto/EV policy changes",
        "Agricultural policy changes",
        "Rural income/crop-price changes",
        "Major commodity-cost shocks",
        "Supplier/semiconductor disruptions",
        "Major acquisitions, demergers or strategic investments",
    ],
    market_characters={},
)


MARKET_CHARACTERS: Dict[str, MarketCharacter] = {

    "NIFTY 50": _mc(
        "NIFTY 50",
        "Indian equity-market, liquidity and domestic economic-cycle character.",
        "Direct market-beta and valuation channel, plus an indirect signal for "
        "consumer confidence, credit conditions and capex.",
        [
            "NIFTY regime -> equity risk appetite -> M&M valuation",
            "Macro/liquidity regime -> financing conditions -> auto demand",
            "Economic cycle -> industrial/rural activity -> auto and tractor demand",
        ],
        [
            "Calculate M&M returns versus NIFTY.",
            "Estimate rolling correlation and beta.",
            "Estimate downside beta during market stress.",
            "Separate NIFTY effect from company-specific residual returns.",
            "Test multiple lead/lag windows.",
        ],
        [
            "M&M return",
            "NIFTY return",
            "Rolling beta",
            "Rolling correlation",
            "Volatility",
            "Relative strength",
        ],
        [
            "Major NIFTY regime changes",
            "RBI/liquidity events",
            "Budget and policy events",
            "Large macro shocks",
            "Risk-off episodes",
        ],
        ["intraday", "1D", "1W", "1M", "3M", "6M", "1Y"],
    ),

    "Crude Oil": _mc(
        "Crude Oil",
        "Fuel, petrochemical, logistics, inflation and rural-income character.",
        "Mixed exposure: cost pressure through fuel/plastics/logistics and demand "
        "effects through consumer affordability and farm economics.",
        [
            "Crude -> fuel price -> vehicle running cost -> demand",
            "Crude -> petrochemical/plastic/rubber inputs -> vehicle cost",
            "Crude -> freight/logistics -> supply-chain cost",
            "Crude -> inflation -> household/rural purchasing power -> vehicle/tractor demand",
        ],
        [
            "Measure lagged M&M/crude sensitivity.",
            "Use domestic petrol/diesel prices separately from crude.",
            "Test whether crude affects volumes, margins or both.",
            "Control for NIFTY and rural-demand variables.",
            "Use event studies around large oil shocks.",
        ],
        [
            "Brent/WTI return",
            "Petrol/diesel price",
            "Freight-cost proxy",
            "Petrochemical input proxy",
            "Auto volume",
            "Tractor volume",
            "Operating margin",
        ],
        [
            "OPEC+ decisions",
            "Large crude shocks",
            "Domestic fuel-price changes",
            "Inflation shocks",
            "Logistics disruptions",
        ],
        ["1D", "1W", "1M", "3M", "6M", "1Y"],
    ),

    "Gold": _mc(
        "Gold",
        "Safe-haven, wealth, real-rate and risk-aversion character.",
        "Indirect macro and household-wealth exposure; gold is not a core "
        "manufacturing input for M&M.",
        [
            "Gold/risk regime -> household wealth sentiment -> vehicle demand",
            "Gold/rates -> financial conditions -> vehicle/tractor financing",
            "Gold/USD/global risk -> export and equity-market regime",
        ],
        [
            "Test M&M/gold rolling correlation after controlling for NIFTY.",
            "Use gold as a macro regime indicator rather than an input cost.",
            "Test high-risk-off periods separately.",
            "Compare auto and tractor responses.",
        ],
        [
            "Gold return",
            "Gold volatility",
            "Real-rate proxy",
            "USD index",
            "Auto-sector return",
            "M&M volume",
        ],
        [
            "Safe-haven shocks",
            "Rate decisions",
            "Global geopolitical stress",
            "Liquidity stress",
        ],
        ["1D", "1W", "1M", "3M", "6M"],
    ),

    "Silver": _mc(
        "Silver",
        "Precious-metal plus industrial-cycle character.",
        "Indirect industrial and risk-sentiment exposure; limited direct input "
        "importance relative to steel, aluminium and copper.",
        [
            "Silver industrial demand -> manufacturing cycle -> auto demand",
            "Silver/risk regime -> market sentiment -> valuation",
            "Silver/electronics cycle -> component supply conditions",
        ],
        [
            "Calculate rolling M&M/silver relationship.",
            "Compare silver with copper as industrial-cycle indicators.",
            "Control for NIFTY and auto-sector returns.",
            "Test whether silver leads industrial/auto-cycle changes.",
        ],
        [
            "Silver return",
            "Gold/silver ratio",
            "Industrial-metal index",
            "Auto-sector return",
            "M&M volumes",
        ],
        [
            "Industrial-cycle shocks",
            "Silver volatility events",
            "Global manufacturing changes",
        ],
        ["1D", "1W", "1M", "3M", "6M"],
    ),

    "Natural Gas": _mc(
        "Natural Gas",
        "Industrial energy, manufacturing and farm/industrial input character.",
        "Mostly indirect through plant energy costs, supplier economics, "
        "industrial activity and the broader energy regime.",
        [
            "Gas -> industrial energy cost -> manufacturing/supplier cost",
            "Gas -> electricity/energy system -> plant operating cost",
            "Gas/inflation -> household/rural affordability -> demand",
            "Gas industrial cycle -> machinery/industrial activity",
        ],
        [
            "Measure lagged M&M/gas sensitivity.",
            "Use electricity data alongside gas.",
            "Test operating-margin and volume responses separately.",
            "Control for crude and NIFTY.",
        ],
        [
            "Natural-gas return",
            "Gas volatility",
            "Industrial energy-cost proxy",
            "Production volume",
            "Operating margin",
        ],
        [
            "Gas-price shocks",
            "Energy disruptions",
            "Industrial production shocks",
            "LNG/global gas events",
        ],
        ["1D", "1W", "1M", "3M", "6M"],
    ),

    "Copper": _mc(
        "Copper",
        "Electrical, electronic, wiring and vehicle-electrification character.",
        "Meaningful input exposure through vehicle electrical systems, electronics "
        "and increasingly EV power/electrical architecture.",
        [
            "Copper -> electrical/component cost -> vehicle cost",
            "Copper -> EV electrical intensity -> EV input cost",
            "Copper demand -> industrial cycle -> auto/farm demand",
            "Copper supply shock -> component availability -> production risk",
        ],
        [
            "Estimate lagged M&M/copper sensitivity.",
            "Compare copper moves with material-cost and margin data.",
            "Separate conventional vehicle and EV exposure where possible.",
            "Control for steel, aluminium, crude and NIFTY.",
        ],
        [
            "Copper return",
            "Copper volatility",
            "Electrical-component cost",
            "EV volume",
            "Material-cost ratio",
            "Operating margin",
        ],
        [
            "Copper supply disruptions",
            "Large copper price shocks",
            "EV production ramps",
            "Electronics/component shortages",
        ],
        ["1D", "1W", "1M", "3M", "6M", "1Y"],
    ),

    "Aluminium": _mc(
        "Aluminium",
        "Vehicle lightweighting, castings, body/components and industrial-input character.",
        "Direct-to-meaningful input exposure across automotive and farm equipment, "
        "with additional relevance to EV lightweighting.",
        [
            "Aluminium -> body/casting/component cost -> vehicle margin",
            "Aluminium -> supplier economics -> procurement cost",
            "Aluminium demand -> auto/industrial cycle -> M&M volumes",
            "EV/lightweighting -> aluminium intensity -> longer-term input sensitivity",
        ],
        [
            "Calculate rolling and lagged M&M/aluminium sensitivity.",
            "Test margin response around major aluminium shocks.",
            "Compare exposure across Automotive and Farm Equipment.",
            "Control for steel, copper, crude and NIFTY.",
        ],
        [
            "Aluminium return",
            "Aluminium volatility",
            "Material-cost ratio",
            "Vehicle production",
            "Tractor production",
            "Operating margin",
        ],
        [
            "Aluminium price shocks",
            "Smelter/supply disruptions",
            "Major auto-material inflation",
            "EV/lightweighting changes",
        ],
        ["1D", "1W", "1M", "3M", "6M", "1Y"],
    ),

    "Zinc": _mc(
        "Zinc",
        "Galvanised steel, corrosion protection and automotive/construction-cycle character.",
        "Indirect-to-moderate input exposure through coated steel and industrial "
        "components, with a broader manufacturing-cycle signal.",
        [
            "Zinc -> galvanised/coated steel -> vehicle input cost",
            "Zinc -> industrial/construction cycle -> commercial-vehicle demand",
            "Zinc supply shock -> supplier costs -> production economics",
        ],
        [
            "Measure lagged M&M/zinc sensitivity.",
            "Compare zinc with steel as a vehicle-material proxy.",
            "Test margin response after controlling for steel.",
            "Control for NIFTY and industrial-demand variables.",
        ],
        [
            "Zinc return",
            "Zinc volatility",
            "Steel price",
            "Coated-steel proxy",
            "Material-cost ratio",
            "Production volume",
        ],
        [
            "Zinc supply disruptions",
            "Steel/metal price shocks",
            "Supplier disruptions",
            "Industrial-cycle changes",
        ],
        ["1D", "1W", "1M", "3M", "6M"],
    ),

    "Electricity": _mc(
        "Electricity",
        "Manufacturing, plant-utilisation and industrial-energy character.",
        "Direct operating-cost exposure for vehicle/tractor plants and suppliers, "
        "plus a broader industrial-activity signal.",
        [
            "Electricity cost -> plant operating cost -> margin",
            "Power reliability -> plant uptime -> production volume",
            "Electricity/industrial demand -> economic cycle -> auto/farm demand",
            "Power transition -> EV manufacturing/charging ecosystem",
        ],
        [
            "Use reliable industrial/commercial electricity data.",
            "Measure lagged electricity-cost sensitivity to margins.",
            "Test outages/disruptions as event variables.",
            "Separate price effects from power-availability effects.",
            "Compare Automotive and Farm Equipment manufacturing exposure.",
        ],
        [
            "Industrial electricity price",
            "Power demand",
            "Peak demand",
            "Plant production",
            "Capacity utilisation",
            "Energy cost",
            "Operating margin",
        ],
        [
            "Power shortages",
            "Electricity-price shocks",
            "Plant disruptions",
            "New manufacturing capacity",
            "Renewable/captive-power projects",
        ],
        ["intraday", "1D", "1W", "1M", "3M", "6M", "1Y"],
    ),
}


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
    """Return the complete M&M company character."""
    return COMPANY_CHARACTER


def get_market_character(market: str) -> MarketCharacter:
    """Return one market character for M&M."""
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
    """Structural validation only; no market scores are calculated."""
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
