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
    "The concept is based on mechanical efficiency and modular construction, applying {focus} to address practical challenges in {category}.",
    "This invention combines structural stability, controlled motion, and mechanical leverage to improve performance in {category}.",
    "Designed with practical engineering constraints in mind, the system uses {focus} to deliver reliable operation in {category}.",
    "The mechanism focuses on durability and maintainability, using simple engineering principles adapted for {category}.",
]

MODERN_PATTERNS = [
    "A modern implementation could integrate sensors, automation, and modular components to create a deployable solution for {modern_focus}.",
    "In a contemporary setting, the concept could evolve into an engineered product using lightweight materials, digital monitoring, and scalable architecture.",
    "Modern engineering could transform this idea into a field-ready system for {modern_focus}, emphasizing reliability, safety, and ease of maintenance.",
    "The modern version would likely use industrial components, embedded control systems, and standardized modules for practical deployment.",
]

DEMAND_PATTERNS = [
    "Market demand may emerge in sectors where operational efficiency and reliability are critical, particularly in {modern_focus}.",
    "The concept could attract interest in {modern_focus}, especially in environments requiring automation and reduced operational risk.",
    "Commercial adoption is plausible in {modern_focus}, where improved performance and reduced maintenance costs provide clear value.",
    "Demand may grow in industries focused on long-term operational efficiency and scalable engineering solutions in {modern_focus}.",
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

    modern_principle = (
        f"The modern operating principle is based on a modular engineering system designed for {modern_focus}. "
        f"It uses controlled actuation, structural stability, monitoring components, and maintainable subsystems "
        f"to deliver predictable performance in real operating conditions."
    )
    
    modern_principle = (
        f"The modern operating principle is based on a modular engineering system designed for {modern_focus}. "
        f"It uses controlled actuation, structural stability, monitoring components, and maintainable subsystems "
        f"to deliver predictable performance in real operating conditions."
    )
    
    demand = _pick(DEMAND_PATTERNS).format(
        modern_focus=modern_focus,
    )

    roi = _pick(ROI_PATTERNS)

    startup_cost = _pick([
        "Estimated startup cost: $80,000-$150,000 for early prototype development and initial validation.",
        "Estimated startup cost: $150,000-$300,000 depending on hardware complexity, prototyping needs, and testing.",
        "Estimated startup cost: $300,000-$600,000 for prototype, engineering validation, and first-stage market entry.",
    ])
    
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
    "title": f"{category.title()} Innovation System",

    "leonardo_concept": (
        f"A Renaissance-inspired mechanical concept designed by Leonardo da Vinci "
        f"to improve efficiency in {category} applications."
    ),

    "leonardo_sketch_description": (
        "A sepia-toned Renaissance notebook sketch featuring gears, pulleys, "
        "wooden frames, and handwritten annotations."
    ),

    "modern_product_name": f"{category.title()} Intelligent System",

    "modern_category": category,

    "executive_summary": (
        f"A modern engineering solution designed for {category} operations "
        f"with scalable deployment and automation capabilities."
    ),

    "problem_statement": (
        f"Organizations in {category} often struggle with efficiency, "
        f"safety, and automation limitations."
    ),

    "target_users": [
        "Engineering teams",
        "Industrial companies",
        "Technology organizations"
    ],

    "industries": [
        category,
        "Industrial",
        "Technology"
    ],

    "use_cases": [
        "Automation",
        "Operational efficiency",
        "Deployment optimization"
    ],

    "modern_principle": (
        "The system operates using modular architecture, automation logic, "
        "and scalable deployment strategy."
    ),

    "system_components": [
        "Control module",
        "Structural frame",
        "Sensors",
        "Automation system"
    ],

    "materials": [
        "Aluminum frame",
        "Composite materials",
        "Industrial electronics"
    ],

    "technical_requirements": [
        "Power supply",
        "Control software",
        "Safety system"
    ],

    "modern_sketch_description": (
        "Modern industrial blueprint with modular components and "
        "deployment-ready architecture."
    ),

    "implementation_roadmap": {
        "prototype": "Initial engineering prototype",
        "mvp": "Operational MVP deployment",
        "pilot": "Pilot deployment with partners",
        "production": "Full production deployment"
    },

    "implementation_guides": {
        "prototype": {
            "execution_plan": {
                "goal": "Create a working early-stage prototype to validate the core mechanism and operating logic.",
                "steps": [
                    "Define core functional scope for the prototype",
                    "Assemble a simplified engineering model",
                    "Test the main mechanism in controlled conditions"
                ],
                "specialists": [
                    "Mechanical engineer",
                    "Prototype engineer",
                    "Technical project lead"
                ],
                "technologies": [
                    "Rapid prototyping tools",
                    "Basic control systems",
                    "Testing equipment"
                ],
                "estimated_budget": "$25,000-$60,000",
                "stage_risks": [
                    "Core mechanism may fail under testing",
                    "Prototype may not reflect real operating conditions"
                ],
                "readiness_criteria": [
                    "Prototype performs core function",
                    "Main engineering assumptions are validated"
                ],
                "expected_output": "A testable prototype demonstrating the core concept."
            },
            "technical_architecture": {
                "system_schema": "Core control unit connected to the main mechanical structure and operating module.",
                "module_interaction": "The control logic triggers the mechanism, while the structural frame supports repeatable operation.",
                "process_flow": "Input signal → control action → mechanism activation → observed output.",
                "deployment_logic": "Prototype remains in lab or controlled pilot environment only."
            },
            "resources_budget": {
                "team": [
                    "Prototype engineer",
                    "Mechanical engineer",
                    "Technical assistant"
                ],
                "stack": [
                    "CAD tools",
                    "Basic embedded control",
                    "Testing software"
                ],
                "materials": [
                    "Prototype frame materials",
                    "Test components",
                    "Control hardware"
                ],
                "cost_notes": "Budget mainly covers prototyping, testing, and engineering labor."
            },
            "validation": {
                "tests": [
                    "Core functionality test",
                    "Stability test",
                    "Basic safety test"
                ],
                "kpi": [
                    "Functional reliability",
                    "Repeatability",
                    "Performance consistency"
                ],
                "success_criteria": [
                    "Prototype works in controlled testing",
                    "No critical design flaw blocks next phase"
                ]
            }
        },

        "mvp": {
            "execution_plan": {
                "goal": "Build a minimum viable product that performs the essential value proposition in realistic use conditions.",
                "steps": [
                    "Refine prototype into MVP architecture",
                    "Integrate essential modules",
                    "Test the MVP in limited operational scenarios"
                ],
                "specialists": [
                    "Product engineer",
                    "Software/controls engineer",
                    "Systems integrator"
                ],
                "technologies": [
                    "Embedded systems",
                    "Control software",
                    "Operational sensors"
                ],
                "estimated_budget": "$80,000-$180,000",
                "stage_risks": [
                    "Integration between modules may be unstable",
                    "MVP may be too limited for user validation"
                ],
                "readiness_criteria": [
                    "Essential system modules work together",
                    "MVP demonstrates clear user value"
                ],
                "expected_output": "A functional MVP ready for early external evaluation."
            },
            "technical_architecture": {
                "system_schema": "Integrated control, sensing, and actuation modules connected through a central logic layer.",
                "module_interaction": "Sensors collect input, control layer processes data, output modules perform the required action.",
                "process_flow": "Operational input → system analysis → module coordination → functional output.",
                "deployment_logic": "Deploy MVP in selected low-risk scenarios with close monitoring."
            },
            "resources_budget": {
                "team": [
                    "Systems engineer",
                    "Software engineer",
                    "Field testing specialist"
                ],
                "stack": [
                    "Embedded software",
                    "Sensor stack",
                    "Control platform"
                ],
                "materials": [
                    "Production-like components",
                    "Sensor modules",
                    "Protective housing"
                ],
                "cost_notes": "Budget expands due to integration work, iteration, and field validation."
            },
            "validation": {
                "tests": [
                    "Module integration test",
                    "Field functionality test",
                    "User scenario validation"
                ],
                "kpi": [
                    "Operational uptime",
                    "Accuracy",
                    "Task completion rate"
                ],
                "success_criteria": [
                    "MVP performs reliably in limited real-world use",
                    "Pilot customers can understand and evaluate product value"
                ]
            }
        },

        "pilot": {
            "execution_plan": {
                "goal": "Validate the system with real users or organizations in controlled but practical deployment scenarios.",
                "steps": [
                    "Select pilot partner environment",
                    "Deploy pilot units",
                    "Collect performance and user feedback data"
                ],
                "specialists": [
                    "Deployment manager",
                    "Field engineer",
                    "Customer success lead"
                ],
                "technologies": [
                    "Monitoring systems",
                    "Deployment tooling",
                    "Reporting dashboard"
                ],
                "estimated_budget": "$150,000-$350,000",
                "stage_risks": [
                    "Operational environment may expose unexpected failures",
                    "Users may require features not included in pilot version"
                ],
                "readiness_criteria": [
                    "Pilot partner can operate the system",
                    "Performance data supports scale-up decision"
                ],
                "expected_output": "Validated pilot results, field data, and implementation feedback."
            },
            "technical_architecture": {
                "system_schema": "Pilot deployment architecture adds monitoring, reporting, and support workflow layers.",
                "module_interaction": "Core system interacts with field environment while monitoring tools collect operational metrics.",
                "process_flow": "Deployment → live operation → monitoring → issue tracking → optimization cycle.",
                "deployment_logic": "Deploy to selected pilot sites with support and reporting processes in place."
            },
            "resources_budget": {
                "team": [
                    "Deployment engineer",
                    "Support specialist",
                    "Operations analyst"
                ],
                "stack": [
                    "Monitoring dashboard",
                    "Support workflow tools",
                    "Analytics layer"
                ],
                "materials": [
                    "Pilot-ready hardware",
                    "Deployment accessories",
                    "Support equipment"
                ],
                "cost_notes": "Pilot costs include support, logistics, deployment setup, and operational monitoring."
            },
            "validation": {
                "tests": [
                    "Field performance test",
                    "User acceptance test",
                    "Operational resilience test"
                ],
                "kpi": [
                    "User satisfaction",
                    "Deployment stability",
                    "Operational efficiency gain"
                ],
                "success_criteria": [
                    "Pilot users confirm value",
                    "System performs consistently in real operating conditions"
                ]
            }
        },

        "production": {
            "execution_plan": {
                "goal": "Scale the validated system into a production-ready solution with repeatable deployment and support model.",
                "steps": [
                    "Standardize final system design",
                    "Prepare manufacturing or deployment pipeline",
                    "Launch production rollout and support processes"
                ],
                "specialists": [
                    "Production engineer",
                    "Operations manager",
                    "Quality assurance lead"
                ],
                "technologies": [
                    "Production systems",
                    "QA processes",
                    "Deployment automation"
                ],
                "estimated_budget": "$300,000-$1,000,000+",
                "stage_risks": [
                    "Scaling may increase cost or reduce reliability",
                    "Operational support requirements may grow faster than expected"
                ],
                "readiness_criteria": [
                    "System is standardized for repeatable rollout",
                    "Support and QA processes are documented and active"
                ],
                "expected_output": "Production-ready solution with deployment, support, and scale model."
            },
            "technical_architecture": {
                "system_schema": "Production architecture includes final system design, monitoring, support, and maintenance processes.",
                "module_interaction": "Operational modules, support systems, and analytics layers work together in a repeatable deployment model.",
                "process_flow": "Production setup → deployment → operation → maintenance → performance optimization.",
                "deployment_logic": "Roll out through standardized deployment packages, trained teams, and documented operating procedures."
            },
            "resources_budget": {
                "team": [
                    "Production lead",
                    "QA engineer",
                    "Deployment operations team"
                ],
                "stack": [
                    "Production software stack",
                    "Monitoring platform",
                    "Support infrastructure"
                ],
                "materials": [
                    "Production-grade components",
                    "Standardized assemblies",
                    "Deployment kits"
                ],
                "cost_notes": "Costs shift toward scaling, QA, logistics, and operational support."
            },
            "validation": {
                "tests": [
                    "Production QA testing",
                    "Scalability test",
                    "Reliability regression testing"
                ],
                "kpi": [
                    "Deployment speed",
                    "Failure rate",
                    "Support efficiency"
                ],
                "success_criteria": [
                    "System can be deployed repeatedly at quality standard",
                    "Operational support model is sustainable"
                ]
            }
        }
    },
    
    "deployment_strategy": (
        "Phased deployment starting from pilot customers."
    ),

    "risks": [
        "Engineering complexity",
        "Integration challenges"
    ],

    "constraints": [
        "Budget limitations",
        "Technical integration"
    ],

    "market_demand": (
        f"Growing demand for automation solutions in {category} sector."
    ),

    "startup_cost": (
        "Estimated startup cost: $100,000-$300,000"
    ),

    "roi": (
        "Estimated ROI within 2-3 years."
    ),

    "investor_summary": (
        "Scalable engineering product with strong commercial potential."
    ),

    "difficulty": "High",

    "modern_difficulty": "High",

    "dev_time": "Prototype: 4-6 months • MVP: 8-12 months • Production: 1-2 years"
}