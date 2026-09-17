"""
EICHERMOT (Eicher Motors Limited)
Company Character & 9-Market Relationship Engine

CHARACTER LAYER ONLY
--------------------
The company character is built from Eicher Motors' actual business structure:
    - Royal Enfield mid-size motorcycles
    - global motorcycle operations
    - VE Commercial Vehicles (VECV) joint venture
    - trucks, buses, engines, components and engineering
    - premium / lifestyle brand character
    - manufacturing, dealer and service ecosystem
    - exports and foreign-currency exposure

This module describes WHAT the historical research engine should calculate.
It does not hard-code historical outcomes.

Never hard-code:
    RANK
    PCT_CHANGE
    LINKAGE_SCORE
    RELATION

Those are calculated outputs of the later historical-analysis layer.
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


EICHERMOT_MARKETS: Dict[str, MarketCharacter] = {

    "NIFTY 50": MarketCharacter(
        market="NIFTY 50",
        character=(
            "Primary systematic equity-market character for Eicher Motors. "
            "Large-cap liquidity, consumer-discretionary sentiment, auto-sector "
            "flows and broad Indian risk appetite can influence valuation."
        ),
        exposure_character=(
            "Direct systematic equity exposure with additional auto, consumer "
            "discretionary, premiumisation and growth-factor exposure."
        ),
        impact_path=[
            "NIFTY 50 movement",
            "Indian equity liquidity and risk appetite",
            "auto / consumer-discretionary sector flows",
            "Eicher Motors valuation",
            "EICHERMOT relative performance",
        ],
        calculation_logic=[
            "Calculate EICHERMOT returns against NIFTY 50 over matched windows.",
            "Estimate rolling beta and rolling correlation instead of using the supplied fixed linkage.",
            "Calculate excess return after controlling for NIFTY 50.",
            "Where available, separately control for auto-sector returns.",
            "Test lead/lag effects across daily, weekly and monthly horizons.",
        ],
        relevant_indicators=[
            "EICHERMOT return",
            "NIFTY 50 return",
            "rolling beta",
            "rolling correlation",
            "relative strength",
            "volume",
            "volatility",
        ],
        relevant_events=[
            "broad-market risk-on/risk-off events",
            "Union Budget",
            "RBI rate decisions",
            "auto policy changes",
            "monthly Royal Enfield sales",
            "VECV sales",
            "quarterly results",
        ],
    ),

    "Crude Oil": MarketCharacter(
        market="Crude Oil",
        character=(
            "Important mobility-demand, fuel-cost, logistics and consumer-income "
            "character. Petrol prices can influence motorcycle usage economics, "
            "vehicle purchase decisions and household discretionary spending. "
            "Crude also affects freight and manufacturing costs."
        ),
        exposure_character=(
            "Indirect-to-moderate exposure through customer fuel economics, "
            "vehicle demand, logistics and manufacturing costs."
        ),
        impact_path=[
            "Crude oil price",
            "petrol / diesel price and inflation",
            "rider / fleet operating economics and household purchasing power",
            "motorcycle / commercial-vehicle demand",
            "Eicher sales, mix and earnings",
        ],
        calculation_logic=[
            "Measure contemporaneous and lagged crude/EICHERMOT relationships.",
            "Separate customer-demand effects from manufacturing/logistics cost effects.",
            "Control for NIFTY 50, inflation and interest rates where available.",
            "For Royal Enfield, test crude against motorcycle volumes and premium demand.",
            "For VECV, separately test crude against commercial-vehicle volumes and freight activity.",
            "Use event studies around unusually large crude shocks.",
        ],
        relevant_indicators=[
            "crude return",
            "petrol/diesel-price proxy",
            "inflation",
            "Royal Enfield volumes",
            "VECV volumes",
            "EICHERMOT margin",
        ],
        relevant_events=[
            "large crude shocks",
            "fuel-price changes",
            "fuel-tax changes",
            "major geopolitical energy events",
            "inflation shocks",
        ],
    ),

    "Gold": MarketCharacter(
        market="Gold",
        character=(
            "Indirect household-wealth, discretionary-spending, safe-haven and "
            "macro-liquidity character. Gold is not a core Eicher input; it can "
            "serve as a regime variable for household wealth, risk appetite and "
            "consumer discretionary behaviour."
        ),
        exposure_character=(
            "Indirect consumer-sentiment, wealth-effect and macro exposure."
        ),
        impact_path=[
            "Gold price",
            "household wealth / safe-haven / liquidity signal",
            "consumer confidence and discretionary spending",
            "premium motorcycle demand / equity sentiment",
            "EICHERMOT market response",
        ],
        calculation_logic=[
            "Measure rolling and lagged gold/EICHERMOT relationships.",
            "Control for NIFTY 50, rates and consumer-sentiment variables.",
            "Test the relationship separately during strong consumer and risk-off regimes.",
            "Compare gold with two-wheeler sales and premium-product demand where available.",
            "Do not infer causation from correlation alone.",
        ],
        relevant_indicators=[
            "gold return",
            "consumer-sentiment proxy",
            "two-wheeler sales",
            "premium motorcycle volumes",
            "EICHERMOT return",
        ],
        relevant_events=[
            "large gold-price moves",
            "household wealth shocks",
            "rate/liquidity events",
            "major risk-off events",
        ],
    ),

    "Silver": MarketCharacter(
        market="Silver",
        character=(
            "Indirect industrial-cycle and consumer-sentiment character. Silver "
            "can reflect global manufacturing activity and commodity risk, while "
            "having no major direct role in Eicher's core vehicle economics."
        ),
        exposure_character=(
            "Indirect industrial-cycle and macro exposure."
        ),
        impact_path=[
            "Silver price",
            "industrial / commodity-cycle signal",
            "manufacturing and consumer-demand environment",
            "motorcycle / commercial-vehicle demand",
            "Eicher market response",
        ],
        calculation_logic=[
            "Measure rolling and lagged silver/EICHERMOT relationships.",
            "Compare silver with copper to identify common industrial-cycle factors.",
            "Control for NIFTY 50 and broader commodity conditions.",
            "Test whether silver leads changes in auto demand during industrial expansions or slowdowns.",
        ],
        relevant_indicators=[
            "silver return",
            "copper return",
            "industrial-production proxy",
            "auto sales",
            "EICHERMOT return",
        ],
        relevant_events=[
            "global industrial shocks",
            "commodity-volatility events",
            "global growth surprises",
        ],
    ),

    "Natural Gas": MarketCharacter(
        market="Natural Gas",
        character=(
            "Indirect industrial-energy and manufacturing-cost character. "
            "Natural gas can influence energy costs, industrial activity and "
            "the broader manufacturing ecosystem rather than directly driving "
            "motorcycle demand."
        ),
        exposure_character=(
            "Indirect manufacturing-cost and industrial-cycle exposure."
        ),
        impact_path=[
            "Natural-gas price",
            "industrial energy economics",
            "supplier/manufacturing cost and industrial activity",
            "vehicle production / commercial demand",
            "EICHERMOT margins and earnings",
        ],
        calculation_logic=[
            "Measure lagged natural-gas/EICHERMOT relationships.",
            "Control for crude oil, electricity and NIFTY 50.",
            "Compare energy-price moves with manufacturing margins and production data.",
            "Separate industrial-demand effects from direct energy-cost effects.",
            "Use geography-specific energy data when available.",
        ],
        relevant_indicators=[
            "natural-gas return",
            "industrial-energy proxy",
            "EICHERMOT margin",
            "production volume",
            "VECV sales",
        ],
        relevant_events=[
            "energy supply disruptions",
            "natural-gas price shocks",
            "industrial-energy inflation",
            "major geopolitical energy events",
        ],
    ),

    "Copper": MarketCharacter(
        market="Copper",
        character=(
            "Important electrical, wiring, motor, electronics and industrial "
            "component character. Copper is relevant to motorcycles, commercial "
            "vehicles, wiring harnesses, electrical systems, motors and supplier "
            "costs, while also acting as an industrial-cycle signal."
        ),
        exposure_character=(
            "Moderate direct/indirect component-input and industrial-cycle exposure."
        ),
        impact_path=[
            "Copper price",
            "wiring / electrical / motor / component cost",
            "vehicle BOM and supplier economics",
            "manufacturing margin / vehicle pricing",
            "Eicher earnings",
        ],
        calculation_logic=[
            "Measure rolling and lagged copper/EICHERMOT relationships.",
            "Compare copper moves with vehicle input-cost and margin indicators.",
            "Control for aluminium, zinc and broader industrial-metal movement.",
            "Test procurement-to-production lags.",
            "Separate input-cost effects from copper's broader industrial-demand signal.",
            "Where possible, analyze Royal Enfield and VECV separately.",
        ],
        relevant_indicators=[
            "copper return",
            "industrial-metals basket",
            "vehicle input-cost proxy",
            "gross margin",
            "EBITDA margin",
            "Royal Enfield volumes",
            "VECV volumes",
        ],
        relevant_events=[
            "copper supply disruptions",
            "large supplier-cost changes",
            "new model launches",
            "major capacity expansion",
            "vehicle BOM changes",
        ],
    ),

    "Aluminium": MarketCharacter(
        market="Aluminium",
        character=(
            "Important vehicle lightweighting, casting, wheels, engine, chassis "
            "and component-cost character. Aluminium is materially relevant to "
            "motorcycle and commercial-vehicle manufacturing and can also signal "
            "industrial demand."
        ),
        exposure_character=(
            "Moderate direct component/input-cost exposure plus industrial-cycle exposure."
        ),
        impact_path=[
            "Aluminium price",
            "castings / wheels / engine / chassis / component costs",
            "vehicle BOM and supplier economics",
            "manufacturing cost and pricing",
            "Eicher margin / earnings",
        ],
        calculation_logic=[
            "Measure rolling and lagged aluminium/EICHERMOT relationships.",
            "Compare aluminium changes with vehicle input-cost and gross-margin indicators.",
            "Control for copper, zinc, crude and the broader industrial-metals basket.",
            "Use procurement and inventory lags.",
            "Test whether impact differs between Royal Enfield motorcycles and VECV.",
            "Separate metal-price effect from industrial-demand effect.",
        ],
        relevant_indicators=[
            "aluminium return",
            "industrial-metals basket",
            "vehicle input-cost proxy",
            "gross margin",
            "EBITDA margin",
            "motorcycle volumes",
            "commercial-vehicle volumes",
        ],
        relevant_events=[
            "aluminium supply shocks",
            "major raw-material price changes",
            "new product launches",
            "manufacturing-capacity expansion",
            "supplier-contract changes",
        ],
    ),

    "Zinc": MarketCharacter(
        market="Zinc",
        character=(
            "Vehicle steel, galvanising, corrosion-protection and component "
            "supply-chain character. Zinc is relevant indirectly through "
            "galvanised steel and fabricated vehicle/infrastructure components."
        ),
        exposure_character=(
            "Indirect-to-moderate vehicle material and supplier-cost exposure."
        ),
        impact_path=[
            "Zinc price",
            "galvanised steel / fabrication cost",
            "vehicle component and manufacturing cost",
            "vehicle pricing / margin",
            "Eicher earnings",
        ],
        calculation_logic=[
            "Measure rolling and lagged zinc/EICHERMOT relationships.",
            "Compare zinc with steel, aluminium and copper where data is available.",
            "Control for NIFTY 50 and the auto-sector cycle.",
            "Use procurement and inventory lags rather than same-day correlation only.",
            "Test separate effects on motorcycles and commercial vehicles.",
        ],
        relevant_indicators=[
            "zinc return",
            "steel proxy",
            "industrial-metals basket",
            "vehicle input-cost proxy",
            "EICHERMOT margin",
        ],
        relevant_events=[
            "zinc supply shocks",
            "steel-price changes",
            "vehicle-material cost changes",
            "new model / capacity events",
        ],
    ),

    "Electricity": MarketCharacter(
        market="Electricity",
        character=(
            "Direct manufacturing and industrial-energy character. Motorcycle "
            "and commercial-vehicle plants, machining, painting, welding, testing, "
            "warehousing and supplier operations require reliable power. Electricity "
            "also affects the economics of industrial production and VECV operations."
        ),
        exposure_character=(
            "Direct operating-cost and production-reliability exposure."
        ),
        impact_path=[
            "Electricity price / availability",
            "factory and supplier energy cost",
            "manufacturing operating expense",
            "production reliability / utilisation",
            "Eicher margin and cash flow",
        ],
        calculation_logic=[
            "Use electricity tariffs/market data relevant to major manufacturing geographies.",
            "Measure lagged electricity-cost sensitivity against margins and production.",
            "Separate electricity-price impact from outage/reliability impact.",
            "Control for natural-gas and broader industrial-inflation effects.",
            "Test sensitivity separately for Royal Enfield and VECV manufacturing.",
        ],
        relevant_indicators=[
            "electricity price",
            "industrial tariff proxy",
            "power availability",
            "plant utilisation",
            "manufacturing cost",
            "EBITDA margin",
            "free cash flow",
        ],
        relevant_events=[
            "electricity tariff changes",
            "power shortages/outages",
            "grid events",
            "plant expansion",
            "energy-efficiency initiatives",
            "new manufacturing facilities",
        ],
    ),
}


EICHERMOT_CHARACTER = CompanyCharacter(
    symbol="EICHERMOT",
    company_name="Eicher Motors Limited",
    sector="Automobiles / Motorcycles / Commercial Vehicles",
    industry_character=(
        "Premium-focused automotive group with two distinct economic engines: "
        "Royal Enfield's middleweight motorcycle business and the VECV joint "
        "venture with Volvo Group in commercial vehicles. The character is "
        "therefore split between premium consumer mobility and commercial/fleet "
        "transport. It is brand-led, product-cycle driven, manufacturing-intensive, "
        "dealer-network dependent and exposed to raw-material prices, fuel economics, "
        "interest rates, consumer income, freight activity and international markets."
    ),
    business_character=[
        "Royal Enfield middleweight motorcycles",
        "Classic family",
        "Bullet family",
        "Hunter family",
        "Himalayan / adventure motorcycles",
        "Interceptor / Continental GT 650 family",
        "Super Meteor / premium cruiser products",
        "Flying Flea / electric-mobility initiatives",
        "Motorcycle apparel",
        "Motorcycle riding accessories",
        "Motorcycle parts and after-sales",
        "Global Royal Enfield retail and dealer network",
        "VE Commercial Vehicles (VECV) joint venture",
        "Eicher trucks",
        "Eicher buses",
        "Volvo trucks in India through VECV",
        "Medium-duty engine manufacturing",
        "Engine exports / Volvo Group supply",
        "Components and aggregates",
        "Engineering design services",
        "Aftermarket support",
        "Connected / fleet and mobility solutions",
    ],
    demand_drivers=[
        "Motorcycle replacement demand",
        "Premiumisation",
        "Middleweight motorcycle segment growth",
        "Rider lifestyle / leisure demand",
        "Rural and urban income",
        "Consumer confidence",
        "Interest rates and vehicle financing",
        "Fuel economics",
        "New model launches",
        "International motorcycle demand",
        "Tourism and leisure activity",
        "Commercial vehicle freight demand",
        "Infrastructure activity",
        "Fleet replacement cycle",
        "Industrial production",
        "Construction activity",
    ],
    revenue_drivers=[
        "Royal Enfield motorcycle volumes",
        "Motorcycle average selling price",
        "Product mix",
        "Premium motorcycle mix",
        "International motorcycle volumes",
        "Accessories and apparel",
        "After-sales revenue",
        "VECV truck volumes",
        "VECV bus volumes",
        "Volvo truck business",
        "Engine sales and exports",
        "Components and aggregates",
        "Engineering services",
        "Fleet/aftermarket services",
    ],
    cost_drivers=[
        "Aluminium",
        "Steel",
        "Copper",
        "Zinc",
        "Rubber and tyres",
        "Plastics and polymers",
        "Electronic components",
        "Batteries",
        "Electricity",
        "Fuel / logistics",
        "Freight",
        "Employee costs",
        "R&D",
        "Tooling and manufacturing capex",
        "Dealer incentives",
        "Foreign-currency costs",
    ],
    supply_chain_character=[
        "Two-wheeler component suppliers",
        "Commercial-vehicle component suppliers",
        "Steel suppliers",
        "Aluminium and casting suppliers",
        "Copper/electrical suppliers",
        "Tyre and rubber suppliers",
        "Electronics suppliers",
        "Battery and EV suppliers",
        "Paint/coating suppliers",
        "Engine and transmission suppliers",
        "Tier-1 and Tier-2 automotive ecosystem",
        "Dealer and service network",
        "Global logistics providers",
        "Volvo Group technology and supply ecosystem",
    ],
    strategic_drivers=[
        "Royal Enfield premiumisation",
        "Middleweight motorcycle leadership",
        "Global market expansion",
        "Product-platform expansion",
        "New model launches",
        "Electric motorcycle development",
        "Manufacturing capacity expansion",
        "Dealer-network expansion",
        "Digital customer ecosystem",
        "VECV growth",
        "Commercial-vehicle product expansion",
        "Volvo technology collaboration",
        "Engine and component exports",
        "Aftermarket expansion",
        "Sustainability and energy efficiency",
    ],
    key_indicators=[
        "Royal Enfield monthly sales",
        "Royal Enfield domestic volumes",
        "Royal Enfield export volumes",
        "premium motorcycle mix",
        "average selling price",
        "product mix",
        "VECV monthly sales",
        "truck volumes",
        "bus volumes",
        "VECV market share",
        "dealer network",
        "after-sales revenue",
        "accessory revenue",
        "revenue growth",
        "EBITDA",
        "EBITDA margin",
        "PAT",
        "gross margin",
        "working capital",
        "inventory",
        "receivables",
        "operating cash flow",
        "capex",
        "capacity utilisation",
        "raw-material-cost index",
        "USD/INR",
        "EUR/INR",
        "GBP/INR",
        "international revenue",
        "EICHERMOT stock return",
        "EICHERMOT volume",
        "relative strength versus NIFTY 50",
    ],
    key_events=[
        "monthly Royal Enfield sales",
        "monthly VECV sales",
        "new motorcycle launches",
        "new engine/platform launches",
        "electric motorcycle launches",
        "major capacity additions",
        "new manufacturing facilities",
        "dealer-network expansion",
        "international market entry",
        "export growth events",
        "major VECV product launches",
        "Volvo technology / product events",
        "commercial-vehicle policy changes",
        "emission-norm changes",
        "EV policy changes",
        "GST / taxation changes",
        "interest-rate changes",
        "fuel-price changes",
        "raw-material price shocks",
        "major supplier disruptions",
        "labour / plant disruptions",
        "product recalls",
        "safety/regulatory events",
        "quarterly and annual results",
        "management guidance",
        "strategic partnerships",
        "VECV corporate events",
        "foreign-currency shocks",
    ],
    market_characters=EICHERMOT_MARKETS,
)


def get_company_character() -> CompanyCharacter:
    """Return the complete Eicher Motors company character."""
    return EICHERMOT_CHARACTER


def get_market_character(market: str) -> MarketCharacter:
    """Return Eicher Motors' character for one of the nine tracked markets."""
    try:
        return EICHERMOT_MARKETS[market]
    except KeyError as exc:
        raise ValueError(
            f"Unsupported market: {market!r}. "
            f"Expected one of: {', '.join(TRACKED_MARKETS)}"
        ) from exc


def get_all_market_characters() -> Dict[str, MarketCharacter]:
    """Return all nine Eicher Motors market characters."""
    return dict(EICHERMOT_MARKETS)


def validate_character() -> bool:
    """Validate the Eicher Motors character contract."""
    if EICHERMOT_CHARACTER.symbol != "EICHERMOT":
        return False

    if set(EICHERMOT_MARKETS) != set(TRACKED_MARKETS):
        return False

    for market_name, character in EICHERMOT_MARKETS.items():
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

    if forbidden_fields.intersection(EICHERMOT_CHARACTER.__dataclass_fields__):
        return False

    return True


if __name__ == "__main__":
    print(f"{EICHERMOT_CHARACTER.company_name} ({EICHERMOT_CHARACTER.symbol})")
    print(f"Tracked markets: {len(EICHERMOT_MARKETS)}")
    print(f"Character validation: {validate_character()}")

    for market_name in TRACKED_MARKETS:
        character = EICHERMOT_MARKETS[market_name]
        print(f"- {market_name}: {character.character}")
