"""
RELIANCE Character Engine
-------------------------
Character layer for Reliance Industries Limited (RIL).

The company is modeled as a diversified business system rather than as a
single oil/telecom/retail company.

Primary character layers:
    1. Oil-to-Chemicals (O2C)
    2. Oil & Gas / E&P
    3. Retail
    4. Digital Services / Jio
    5. Media & Entertainment
    6. New Energy & New Materials

The nine tracked markets are structural inputs/signals. Actual linkage,
correlation, beta, lag, impact magnitude and probability must be calculated
later from observed data.

No RANK, PCT_CHANGE, LINKAGE_SCORE or RELATION values are hard-coded.
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
    symbol="RELIANCE",
    company_name="Reliance Industries Limited",
    business_character=(
        "Reliance is a diversified Indian conglomerate whose economic character "
        "is built from multiple large business engines rather than a single "
        "commodity exposure. Its current structure combines Oil-to-Chemicals, "
        "Oil & Gas exploration and production, Retail, Digital Services/Jio, "
        "Media & Entertainment, and New Energy & New Materials. This creates "
        "a multi-channel character in which crude and natural gas directly affect "
        "energy businesses, while consumption, telecom/digital adoption, media, "
        "manufacturing, petrochemical margins, capital expenditure and new-energy "
        "execution create additional independent drivers."
    ),
    core_businesses=(
        "Oil-to-Chemicals (O2C)",
        "Transportation fuels",
        "Petrochemicals",
        "Polymers and elastomers",
        "Intermediates and polyesters",
        "Oil and Gas exploration and production",
        "KG-D6 and CBM operations",
        "Reliance Retail",
        "Consumer electronics retail",
        "Grocery retail",
        "Fashion and lifestyle retail",
        "Digital commerce and new commerce",
        "Jio digital services and connectivity",
        "5G and broadband",
        "Cloud, IoT and enterprise digital services",
        "Media and Entertainment",
        "Sports, news, OTT and content",
        "New Energy and New Materials",
        "Solar manufacturing",
        "Battery manufacturing",
        "Electrolysers and green-energy ecosystem",
    ),
    operating_model=(
        "Vertically integrated energy and materials ecosystem",
        "Large-scale O2C manufacturing",
        "Upstream oil and gas production",
        "Omnichannel physical and digital retail",
        "Telecom network plus digital-platform ecosystem",
        "Media/content creation and distribution",
        "Advanced manufacturing and new-energy development",
        "Large capital-expenditure programme",
        "Technology-led platform businesses",
        "Long-term supply-chain partnerships",
    ),
    revenue_and_cashflow_drivers=(
        "O2C refining and petrochemical margins",
        "Transportation-fuel sales",
        "Petrochemical product volumes",
        "Crude/feedstock economics",
        "Oil and gas production volumes",
        "Realised oil and gas prices",
        "Retail sales and customer transactions",
        "Store footprint and productivity",
        "Digital subscriber base",
        "ARPU and tariff realisation",
        "Broadband and enterprise digital services",
        "Media advertising/subscription/engagement",
        "New-energy manufacturing scale-up",
        "Project commissioning",
        "Domestic consumption growth",
    ),
    cost_drivers=(
        "Crude and feedstock costs",
        "Energy and utilities",
        "Petrochemical feedstock",
        "Logistics and transportation",
        "Retail store operating costs",
        "Telecom network and spectrum-related costs",
        "Content and media costs",
        "Digital infrastructure",
        "Manufacturing capex and depreciation",
        "Solar/battery manufacturing inputs",
        "Interest and financing costs",
        "Employee and technology costs",
    ),
    supply_chain_dependencies=(
        "Crude oil and hydrocarbon feedstocks",
        "Petrochemical raw materials",
        "Ports and marine logistics",
        "Refinery and petrochemical equipment",
        "Retail suppliers and brands",
        "Consumer-product supply chains",
        "Telecom network equipment",
        "Spectrum and network infrastructure",
        "Data centres and cloud infrastructure",
        "Media/content partners",
        "Solar manufacturing equipment",
        "Battery materials and technology",
        "Engineering and EPC contractors",
    ),
    demand_dependencies=(
        "Indian transportation-fuel demand",
        "Global petrochemical demand",
        "Industrial materials demand",
        "Indian household consumption",
        "Consumer electronics demand",
        "Grocery and fashion demand",
        "Mobile-data consumption",
        "5G and broadband adoption",
        "Enterprise digital demand",
        "Media consumption and advertising",
        "Renewable-energy investment",
        "Battery and energy-storage demand",
    ),
    strategic_themes=(
        "O2C integration and higher-value chemicals",
        "Oil and gas production growth",
        "Retail scale and omnichannel expansion",
        "Jio digital ecosystem",
        "5G and broadband expansion",
        "Media and Entertainment scale",
        "AI and digital platforms",
        "Solar and battery manufacturing",
        "New Energy and New Materials",
        "Advanced manufacturing",
        "Supply-chain security",
        "Capital productivity",
        "Energy transition",
        "Technology-led diversification",
    ),
    key_indicators=(
        "O2C EBITDA and margins",
        "Refining margins/crack spreads",
        "Petrochemical margins",
        "Feedstock cost",
        "Oil and gas production",
        "Realised hydrocarbon prices",
        "Retail gross revenue",
        "Retail EBITDA",
        "Store count",
        "Customer base",
        "Digital subscribers",
        "5G subscribers",
        "ARPU",
        "Broadband additions",
        "Media engagement",
        "New-energy manufacturing capacity",
        "Capex",
        "Net debt",
        "Operating cash flow",
    ),
    event_signals=(
        "Crude/feedstock price shocks",
        "Major O2C margin changes",
        "New refinery/petrochemical capacity",
        "KG-D6 or CBM production changes",
        "Oil/gas discoveries and field milestones",
        "Retail expansion",
        "Major brand/partnership changes",
        "Jio tariff revisions",
        "Spectrum developments",
        "5G/broadband milestones",
        "Major media/content transactions",
        "New-energy plant commissioning",
        "Solar/battery/electrolyser milestones",
        "Large capex announcements",
        "Regulatory/tax changes",
        "Major financing/debt developments",
    ),
    risk_channels=(
        "Crude-price volatility",
        "Refining-margin volatility",
        "Petrochemical-cycle weakness",
        "Feedstock availability",
        "Oil and gas production risk",
        "Retail demand weakness",
        "Competitive pressure in telecom",
        "Spectrum/regulatory risk",
        "Media/content execution risk",
        "New-energy project execution",
        "Large capital requirements",
        "Interest-rate/financing risk",
        "Geopolitical energy risk",
        "Environmental/transition regulation",
    ),
)


MARKET_CHARACTERS: Dict[str, MarketCharacter] = {
    "NIFTY 50": _mc(
        "NIFTY 50",
        "Broad Indian equity-market and macro character. Because Reliance has "
        "large consumer, digital and energy businesses, the NIFTY relationship "
        "can reflect both valuation/liquidity and the Indian growth cycle.",
        direct=("Equity-market valuation and market beta",),
        indirect=(
            "Indian GDP/consumption cycle",
            "Institutional risk appetite",
            "Interest-rate expectations",
            "Infrastructure and investment cycle",
        ),
        channels=(
            "Market-wide repricing",
            "Valuation multiple changes",
            "Domestic-growth transmission",
        ),
        demand=(
            "Consumer spending",
            "Telecom/digital usage",
            "Industrial energy demand",
        ),
        strategy=("Capital-market valuation across diversified business segments",),
        indicators=(
            "RELIANCE return",
            "NIFTY 50 return",
            "Rolling beta",
            "Rolling correlation",
            "Relative volatility",
            "Segment-level valuation",
        ),
        events=("Major Indian macro events", "Budget/rate/policy events"),
        logic=(
            "Calculate RELIANCE versus NIFTY returns from observed data.",
            "Estimate rolling beta/correlation rather than hard-coding a linkage.",
            "Decompose market movement into O2C, consumer, digital and company-specific events.",
        ),
    ),
    "Crude Oil": _mc(
        "Crude Oil",
        "Major direct and multi-layer commodity character. Crude is a feedstock "
        "for O2C/refining and a revenue driver for upstream oil and gas, while "
        "also influencing fuel retail, petrochemical economics, inflation and "
        "consumer demand.",
        direct=(
            "O2C feedstock",
            "Refining economics",
            "Upstream oil realisation",
            "Fuel business economics",
        ),
        indirect=(
            "Petrochemical margins",
            "Logistics/freight",
            "Inflation",
            "Consumer purchasing power",
            "Energy-sector sentiment",
        ),
        channels=(
            "Feedstock-cost transmission",
            "Refining-margin transmission",
            "Upstream revenue transmission",
            "Fuel-price transmission",
            "Inflation/consumption transmission",
        ),
        supply=(
            "Crude procurement",
            "Ports and marine logistics",
            "Refinery supply chain",
            "Petrochemical feedstock chain",
        ),
        demand=(
            "Transportation-fuel demand",
            "Petrochemical demand",
            "Industrial energy demand",
            "Consumer demand through inflation",
        ),
        cost=(
            "Crude feedstock",
            "Logistics",
            "Working capital",
        ),
        strategy=(
            "O2C integration",
            "Higher-value chemicals",
            "Fuel retail",
            "Energy transition",
        ),
        indicators=(
            "Brent/WTI or relevant crude benchmark",
            "Crude procurement cost",
            "Refining margins",
            "Petrochemical margins",
            "Oil production",
            "Realised oil price",
            "Fuel retail volumes",
        ),
        events=(
            "OPEC+ decisions",
            "Global supply disruptions",
            "Large crude shocks",
            "Domestic fuel/tax changes",
        ),
        logic=(
            "Separate O2C feedstock effects from upstream revenue effects.",
            "Use refining-margin and realised-price data instead of crude alone.",
            "Test same-day and lagged effects on segment and consolidated results.",
            "Control for NIFTY when measuring equity-price transmission.",
        ),
    ),
    "Natural Gas": _mc(
        "Natural Gas",
        "Direct upstream commodity exposure plus an O2C/energy-system input. "
        "Gas affects E&P revenue, KG-D6/CBM production economics and the broader "
        "energy/materials ecosystem.",
        direct=(
            "Natural gas production revenue",
            "Realised gas price",
            "Gas-field economics",
        ),
        indirect=(
            "Energy costs",
            "Petrochemical economics",
            "Industrial gas demand",
            "Power-sector demand",
        ),
        channels=(
            "Upstream revenue",
            "Production-volume transmission",
            "Energy-input transmission",
            "Industrial-demand transmission",
        ),
        supply=(
            "Gas processing",
            "Gas gathering",
            "Pipeline infrastructure",
            "Field equipment",
        ),
        demand=(
            "Power generation",
            "Fertiliser/industrial gas demand",
            "City-gas ecosystem",
            "Industrial users",
        ),
        cost=(
            "Gas-field development",
            "Processing",
            "Energy and utilities",
        ),
        strategy=(
            "Domestic gas production",
            "Energy security",
            "New-energy transition",
        ),
        indicators=(
            "Natural-gas benchmark prices",
            "Gas production",
            "Realised gas price",
            "KG-D6 output",
            "CBM output",
            "Gas revenue",
        ),
        events=(
            "Gas-price policy changes",
            "KG-D6 production milestones",
            "CBM production changes",
            "Major global gas shocks",
        ),
        logic=(
            "Separate gas-price effects from production-volume effects.",
            "Use realised-price and field-level production data.",
            "Test lagged relationships around new-field commissioning.",
        ),
    ),
    "Electricity": _mc(
        "Electricity",
        "Mixed operating-cost, manufacturing and demand character. Electricity "
        "is important to RIL's refineries, petrochemicals, retail infrastructure, "
        "digital networks/data infrastructure and new-energy manufacturing.",
        indirect=(
            "O2C manufacturing utilities",
            "Digital infrastructure power consumption",
            "Retail/store utilities",
            "New-energy manufacturing",
            "Industrial demand",
        ),
        channels=(
            "Manufacturing-cost transmission",
            "Data-centre/network operating cost",
            "Retail operating cost",
            "Industrial-demand transmission",
        ),
        supply=(
            "Grid electricity",
            "Captive/backup power",
            "Data centres",
            "Manufacturing facilities",
        ),
        demand=(
            "Industrial electricity demand",
            "Digital-services usage",
            "New-energy manufacturing",
            "Consumer activity",
        ),
        cost=(
            "Refinery/petrochemical electricity",
            "Network/data infrastructure",
            "Retail utilities",
            "Manufacturing power",
        ),
        strategy=(
            "Energy efficiency",
            "New-energy manufacturing",
            "Digital infrastructure",
            "Industrial scale-up",
        ),
        indicators=(
            "Industrial electricity prices",
            "O2C energy cost",
            "Data/network energy use",
            "New-energy manufacturing output",
            "Industrial demand",
        ),
        events=("Power-price shocks", "Major industrial electricity-demand changes"),
        logic=(
            "Model electricity separately by business segment.",
            "Do not treat electricity as a single homogeneous company-wide factor.",
            "Test segment margins and operating costs against electricity data.",
        ),
    ),
    "Gold": _mc(
        "Gold",
        "Indirect macro, wealth and risk-regime signal. Gold has no major "
        "physical input relationship with Reliance, but it can reflect inflation, "
        "real rates, liquidity and consumer wealth conditions.",
        indirect=(
            "Inflation expectations",
            "Real rates",
            "Risk sentiment",
            "Consumer wealth",
        ),
        channels=(
            "Macro-regime transmission",
            "Consumer-confidence transmission",
            "Valuation/liquidity transmission",
        ),
        demand=(
            "Retail consumption",
            "Premium consumer spending",
        ),
        strategy=("Macro and consumer-regime monitoring",),
        indicators=(
            "Gold return",
            "RELIANCE return",
            "NIFTY return",
            "Real-rate proxy",
            "Retail-sales indicators",
        ),
        events=("Major real-rate changes", "Large macro risk events"),
        logic=(
            "Treat gold as a macro-state variable.",
            "Test incremental information after controlling for crude and NIFTY.",
        ),
    ),
    "Silver": _mc(
        "Silver",
        "Indirect industrial, electrification and macro signal. Silver has no "
        "primary Reliance revenue linkage but can provide information about "
        "industrial activity and energy-transition sentiment.",
        indirect=(
            "Industrial cycle",
            "Electrification",
            "Commodity sentiment",
            "Macro risk regime",
        ),
        channels=(
            "Industrial-cycle transmission",
            "Energy-transition signal",
        ),
        demand=(
            "Industrial investment",
            "Consumer/economic cycle",
        ),
        strategy=("Industrial and new-energy regime monitoring",),
        indicators=(
            "Silver return",
            "RELIANCE return",
            "Copper return",
            "Industrial-cycle proxies",
        ),
        events=("Industrial-metal shocks", "Global macro shocks"),
        logic=(
            "Test silver after controlling for crude and NIFTY.",
            "Check whether any relationship changes across industrial-cycle regimes.",
        ),
    ),
    "Copper": _mc(
        "Copper",
        "Multi-channel indirect industrial and new-energy input. Copper is "
        "relevant to telecom/digital infrastructure, electrical equipment, "
        "manufacturing, power systems and renewable-energy projects.",
        indirect=(
            "Electrical equipment",
            "Telecom infrastructure",
            "Data centres",
            "Solar/battery ecosystem",
            "Industrial capex",
        ),
        channels=(
            "Equipment procurement",
            "Infrastructure-capex transmission",
            "Industrial-cycle transmission",
            "New-energy input transmission",
        ),
        supply=(
            "Cables",
            "Electrical equipment",
            "Telecom equipment",
            "Renewable-energy equipment",
        ),
        demand=(
            "5G/network expansion",
            "Data centres",
            "Solar manufacturing",
            "Battery/energy infrastructure",
            "Industrial electrification",
        ),
        cost=(
            "Electrical equipment",
            "Telecom infrastructure",
            "New-energy manufacturing",
        ),
        strategy=(
            "Digital infrastructure",
            "5G",
            "Data centres",
            "New Energy",
            "Advanced manufacturing",
        ),
        indicators=(
            "Copper price",
            "Telecom capex",
            "Data-centre capex",
            "New-energy capex",
            "Equipment-cost proxies",
        ),
        events=("Copper shocks", "Global electrification-capex changes"),
        logic=(
            "Model copper mainly through capex and equipment channels.",
            "Use lagged windows because infrastructure procurement is delayed.",
        ),
    ),
    "Aluminium": _mc(
        "Aluminium",
        "Indirect manufacturing, packaging, electrical and new-energy input. "
        "Its importance spans O2C downstream products, equipment, packaging, "
        "retail supply chains and renewable-energy manufacturing.",
        indirect=(
            "Manufacturing inputs",
            "Electrical applications",
            "Packaging",
            "Solar/new-energy equipment",
            "Industrial capex",
        ),
        channels=(
            "Input-cost transmission",
            "Manufacturing-margin transmission",
            "Project-capex transmission",
        ),
        supply=(
            "Industrial materials",
            "Packaging",
            "Electrical components",
            "Renewable-energy equipment",
        ),
        demand=(
            "Industrial investment",
            "Consumer goods",
            "Solar/new-energy deployment",
        ),
        cost=(
            "Manufacturing inputs",
            "Packaging",
            "Equipment procurement",
        ),
        strategy=(
            "Advanced manufacturing",
            "New Energy",
            "Materials integration",
        ),
        indicators=(
            "Aluminium price",
            "O2C margins",
            "Manufacturing costs",
            "New-energy capex",
            "Equipment-cost proxies",
        ),
        events=("Aluminium shocks", "Large manufacturing-capex changes"),
        logic=(
            "Separate O2C material exposure from retail/new-energy procurement.",
            "Test segment-level margins rather than assuming one company-wide effect.",
        ),
    ),
    "Zinc": _mc(
        "Zinc",
        "Indirect industrial and infrastructure input. Zinc is connected mainly "
        "through galvanised steel, equipment, construction and infrastructure "
        "used across manufacturing, telecom, retail facilities and new-energy "
        "projects.",
        indirect=(
            "Galvanised steel",
            "Infrastructure",
            "Industrial construction",
            "Telecom/network structures",
        ),
        channels=(
            "Construction-input transmission",
            "Project-cost transmission",
            "Industrial-cycle signal",
        ),
        supply=(
            "Galvanised structures",
            "Steel equipment",
            "Telecom infrastructure",
            "Manufacturing facilities",
        ),
        demand=(
            "Infrastructure expansion",
            "Industrial capex",
            "Telecom expansion",
            "New-energy projects",
        ),
        cost=(
            "Construction inputs",
            "Steel structures",
            "Project equipment",
        ),
        strategy=("Large-scale infrastructure and manufacturing expansion",),
        indicators=(
            "Zinc price",
            "Steel-price proxies",
            "Capex",
            "Project pipeline",
            "Equipment costs",
        ),
        events=("Zinc/steel shocks", "Infrastructure-cycle changes"),
        logic=(
            "Treat zinc as an indirect project and industrial-cost variable.",
            "Test its incremental effect after controlling for NIFTY and industrial metals.",
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
    """Return the complete Reliance company character."""
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

    print("RELIANCE CHARACTER VALIDATION")
    print("=" * 36)
    print(f"Company: {result['company_name']}")
    print(f"Markets: {result['market_character_count']}/9")
    print(f"Valid: {result['valid']}")

    if result["missing_markets"]:
        print("Missing:", result["missing_markets"])
    if result["extra_markets"]:
        print("Extra:", result["extra_markets"])

    print("\nMARKET CHARACTERS")
    print("=" * 36)

    for market in TRACKED_MARKETS:
        mc = MARKET_CHARACTERS[market]
        print(f"\n[{market}]")
        print(mc.character)
        print("Direct:", ", ".join(mc.direct_exposure) or "None")
        print("Indirect:", ", ".join(mc.indirect_exposure) or "None")
