import random

from utils import generate_dev_time, generate_investor_summary
from config import DIFFICULTY, MATERIALS, USE_CASES


CATEGORY_THEMES = {
    "transport": {
        "nouns": ["Transit Engine", "Mobility Frame", "Cargo Platform", "Rolling Mechanism"],
        "renaissance_focus": ["balanced motion", "wheel geometry", "mechanical traction", "load transfer"],
        "modern_focus": ["urban logistics", "autonomous delivery", "fleet efficiency", "smart mobility"],
    },
    "construction": {
        "nouns": ["StoneBridge System", "Lift Frame", "Builder Engine", "Support Mechanism"],
        "renaissance_focus": ["lifting arms", "counterweight balance", "movable supports", "modular assembly"],
        "modern_focus": ["rapid deployment", "infrastructure support", "construction safety", "site automation"],
    },
    "rescue": {
        "nouns": ["Rescue Wing", "Relief Engine", "Guardian Frame", "Emergency Mechanism"],
        "renaissance_focus": ["stabilized lifting", "rope-guided movement", "shock reduction", "secure extraction"],
        "modern_focus": ["disaster response", "hazard evacuation", "remote rescue", "emergency access"],
    },
    "military": {
        "nouns": ["Fortress Engine", "Defense Platform", "Shield Mechanism", "Tactical Frame"],
        "renaissance_focus": ["fortified structure", "protective motion", "impact resistance", "controlled deployment"],
        "modern_focus": ["defense support", "remote protection", "field mobility", "tactical durability"],
    },
    "exploration": {
        "nouns": ["TerraScout Engine", "Survey Frame", "Pathfinder Device", "Frontier Mechanism"],
        "renaissance_focus": ["terrain stability", "mechanical observation", "range extension", "direction control"],
        "modern_focus": ["terrain mapping", "remote missions", "field inspection", "autonomous scouting"],
    },
    "industrial": {
        "nouns": ["ForgeFlow Engine", "Workframe System", "Precision Mechanism", "Process Platform"],
        "renaissance_focus": ["repeatable motion", "force transfer", "mechanical timing", "durable structure"],
        "modern_focus": ["factory automation", "inspection workflows", "process efficiency", "industrial uptime"],
    },
    "energy": {
        "nouns": ["PowerCore Engine", "Heat Capture Frame", "Wind Motion System", "Energy Mechanism"],
        "renaissance_focus": ["rotary transfer", "wind capture", "heat concentration", "mechanical storage"],
        "modern_focus": ["energy balancing", "smart power systems", "renewable support", "efficient conversion"],
    },
    "architecture": {
        "nouns": ["Archimedes Build Frame", "Adaptive Pavilion", "Support Tower", "Structural Mechanism"],
        "renaissance_focus": ["load balance", "spiral support", "hinged geometry", "deployable structure"],
        "modern_focus": ["adaptive buildings", "temporary structures", "rapid shelters", "smart structural systems"],
    },
    "mechanical": {
        "nouns": ["Mechanica Engine", "Motion Assembly", "Gear Platform", "Precision Frame"],
        "renaissance_focus": ["gears and levers", "timed motion", "spring force", "mechanical sequence"],
        "modern_focus": ["engineering demos", "precision motion", "prototype systems", "mechanical education"],
    },
    "water": {
        "nouns": ["AquaLift Engine", "Marine Frame", "Subsurface Mechanism", "Water Motion System"],
        "renaissance_focus": ["sealed chambers", "water displacement", "propulsion balance", "pressure control"],
        "modern_focus": ["marine inspection", "underwater exploration", "water rescue", "ocean research"],
    },
    "flight": {
        "nouns": ["AeroGlide Engine", "Wing Frame", "Sky Mechanism", "Lift Platform"],
        "renaissance_focus": ["lift balance", "wing motion", "airflow direction", "stability in descent"],
        "modern_focus": ["aerial mapping", "rescue flight", "autonomous navigation", "high-altitude mobility"],
    },
    "space": {
        "nouns": ["AstroMechanica Engine", "Orbital Frame", "Celestial Rover", "Star Navigation System"],
        "renaissance_focus": ["direction by stars", "calibrated rings", "stable movement", "instrument alignment"],
        "modern_focus": ["orbital maintenance", "planetary missions", "autonomous robotics", "extreme-environment mobility"],
    },
    "agriculture": {
        "nouns": ["AgroLift Engine", "Harvest Frame", "Field Mechanism", "Crop Motion System"],
        "renaissance_focus": ["seed distribution", "water timing", "field traction", "mechanical cultivation"],
        "modern_focus": ["precision farming", "crop monitoring", "automated harvesting", "soil efficiency"],
    },
    "medicine": {
        "nouns": ["LifeAssist Engine", "Healing Frame", "Diagnostic Mechanism", "Care Support Platform"],
        "renaissance_focus": ["controlled measurement", "steady support", "protective enclosure", "precision handling"],
        "modern_focus": ["diagnostic support", "remote monitoring", "clinical assistance", "medical workflow efficiency"],
    },
    "robotics": {
        "nouns": ["AutoMechanica Engine", "Articulated Frame", "Logic Motion System", "Mechanical Assistant"],
        "renaissance_focus": ["joint coordination", "repeatable motion", "linked mechanisms", "guided articulation"],
        "modern_focus": ["automation", "inspection robotics", "modular systems", "intelligent assistance"],
    },
}


TITLE_PATTERNS = [
    "Leonardo {noun}",
    "{noun} of {category}",
    "The {noun}",
    "{category} {noun}",
]

PRINCIPLE_PATTERNS = [
    "This concept uses {focus} to create a practical Renaissance mechanism for {category}.",
    "The invention relies on {focus}, combining structural balance and controlled motion for {category}.",
    "Built around {focus}, this machine solves a {category} problem through simple but disciplined engineering.",
]

MODERN_PATTERNS = [
    "A modern version could transform this idea into a product for {modern_focus}, using AI control, sensors, lightweight materials, and safer modular architecture.",
    "In modern engineering, this concept could evolve into a deployable system for {modern_focus}, with autonomous monitoring and data-assisted control.",
    "Today this invention could become a commercial platform for {modern_focus}, combining digital control systems, advanced materials, and scalable manufacturing.",
]

DEMAND_PATTERNS = [
    "Demand could be strong in {modern_focus}, especially where reliability, safety, and deployment speed matter.",
    "This concept could attract interest in {modern_focus}, particularly in markets that value automation and lower operating risk.",
    "Commercial demand is plausible in {modern_focus}, where performance improvements can justify premium engineering solutions.",
]

ROI_PATTERNS = [
    "Estimated ROI: 50% to 85% within 2-4 years depending on prototype quality, market fit, and production cost.",
    "Estimated ROI: 45% to 80% within 2-3 years if the concept achieves strong pilot results and efficient production.",
    "Estimated ROI: 55% to 90% within 3-5 years depending on adoption speed, technical validation, and deployment scale.",
]

SKETCH_PATTERNS = [
    "A sepia-toned Renaissance sketch of '{title}', with ink annotations, exposed mechanisms, sectional views, and notebook-style observations around the design.",
    "A Leonardo-style manuscript drawing of '{title}', showing gears, frames, motion arrows, and handwritten notes explaining the working principle.",
    "A detailed Renaissance engineering sheet for '{title}', with fine ink lines, mechanical labels, cross-sections, and balanced geometric construction.",
]

MODERN_SKETCH_PATTERNS = [
    "A clean modern engineering blueprint of '{title}', with labeled modules, structural framing, safety zones, material notes, and a presentation-ready technical layout.",
    "A product-design style technical sheet for '{title}', showing modular subsystems, manufacturing notes, digital control architecture, and deployment views.",
    "A modern concept blueprint for '{title}', with annotated components, system connections, protective housing, and investor-ready visual clarity.",
]

IMAGE_PATTERNS = [
    "Image generation concept enabled: the system can produce both a Leonardo-style invention sketch and a modern product concept image.",
    "Image generation concept enabled: the app can later generate a Renaissance drawing plus a separate modern industrial visualization.",
]

BLUEPRINT_PATTERNS = [
    "Blueprint concept enabled: the system can later output technical sketch descriptions for engineering slides and presentation visuals.",
    "Blueprint concept enabled: the app can generate detailed visual blueprint directions for both concept art and product presentation decks.",
]

VOICE_PATTERNS = [
    "The voice assistant could explain how '{title}' works, guide the user through the modern implementation, and answer questions about demand and ROI.",
    "The voice assistant could present '{title}' step by step, translating the invention from Renaissance logic into a modern engineering product.",
]


def generate_difficulty(category, creativity_mode):
    base = DIFFICULTY.get(category, "High")
    if creativity_mode == "Experimental" and base == "Medium":
        return "High"
    return base


def generate_modern_difficulty(category):
    return DIFFICULTY.get(category, "High")


def generate_materials(category):
    return MATERIALS.get(
        category,
        ["modular frame", "sensors", "AI controller", "lightweight materials"]
    )


def generate_use_cases(category):
    return USE_CASES.get(
        category,
        ["education", "engineering demos", "research", "commercial prototypes"]
    )


def _get_theme(category):
    return CATEGORY_THEMES.get(
        category,
        {
            "nouns": ["Concept Engine", "Adaptive Frame", "Motion Platform"],
            "renaissance_focus": ["mechanical balance", "controlled motion", "structural discipline"],
            "modern_focus": ["commercial engineering", "practical deployment", "modern automation"],
        },
    )


def _pick(items):
    return random.choice(items)


def _build_title(category):
    theme = _get_theme(category)
    noun = _pick(theme["nouns"])
    pattern = _pick(TITLE_PATTERNS)
    return pattern.format(
        noun=noun,
        category=category.title(),
    )


def build_fallback_concept(category, prompt_text, creativity_mode, audience):
    theme = _get_theme(category)

    title = _build_title(category)
    renaissance_focus = _pick(theme["renaissance_focus"])
    modern_focus = _pick(theme["modern_focus"])

    principle = _pick(PRINCIPLE_PATTERNS).format(
        focus=renaissance_focus,
        category=category,
    )

    if prompt_text.strip():
        principle += f" It is additionally adapted to the user's scenario: {prompt_text.strip()}."

    modern_version = _pick(MODERN_PATTERNS).format(
        modern_focus=modern_focus,
    )

    demand = _pick(DEMAND_PATTERNS).format(
        modern_focus=modern_focus,
    )

    roi = _pick(ROI_PATTERNS)

    difficulty = generate_difficulty(category, creativity_mode)
    modern_difficulty = generate_modern_difficulty(category)
    materials = generate_materials(category)
    use_cases = generate_use_cases(category)
    dev_time = generate_dev_time(modern_difficulty)
    investor_summary = generate_investor_summary(title, category, demand, roi)

    leonardo_sketch_description = _pick(SKETCH_PATTERNS).format(title=title)
    modern_sketch_description = _pick(MODERN_SKETCH_PATTERNS).format(title=title)
    image_concept = _pick(IMAGE_PATTERNS)
    blueprint_concept = _pick(BLUEPRINT_PATTERNS)
    voice_assistant_concept = _pick(VOICE_PATTERNS).format(title=title)

    if creativity_mode == "Bold":
        modern_version += " The final product should prioritize strong visual identity and commercial differentiation."
    elif creativity_mode == "Experimental":
        principle += " The mechanism may also explore an unconventional arrangement of motion, balance, or deployment."
        modern_version += " The modern system can include more speculative product directions if they remain technically believable."

    if audience == "Investors":
        investor_summary += " Investor angle: scalability, market visibility, and product positioning are central."
    elif audience == "Engineers":
        principle += " Engineering angle: emphasize mechanism clarity, force transfer, and structural feasibility."
    elif audience == "Students":
        principle += " Educational angle: the system should remain easy to explain and visually memorable."
    else:
        modern_version += " Public-facing angle: the concept should stay understandable and visually compelling."

    return {
        "title": title,
        "principle": principle,
        "leonardo_sketch_description": leonardo_sketch_description,
        "difficulty": difficulty,
        "modern_version": modern_version,
        "modern_sketch_description": modern_sketch_description,
        "materials": materials,
        "use_cases": use_cases,
        "dev_time": dev_time,
        "modern_difficulty": modern_difficulty,
        "demand": demand,
        "roi": roi,
        "investor_summary": investor_summary,
        "image_concept": image_concept,
        "voice_assistant_concept": voice_assistant_concept,
        "blueprint_concept": blueprint_concept,
    }