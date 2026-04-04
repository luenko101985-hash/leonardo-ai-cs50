import random


INVENTIONS = {
    "flight": [
        {
            "title": "Mechanical Flying Machine with Rotating Wings",
            "principle": (
                "This invention imitates the motion of bird wings and uses rotating "
                "mechanisms to create lift and directional movement."
            ),
            "modern_version": (
                "A lightweight autonomous drone with flapping composite wings, "
                "AI-assisted flight stabilization, and onboard sensors."
            ),
            "demand": "High demand in robotics, surveillance, and environmental research.",
            "roi": "Estimated ROI: 70% within 2-3 years."
        },
        {
            "title": "Wind-Powered Glider",
            "principle": (
                "The design captures wind energy and uses a curved wing structure "
                "to maintain balance and glide efficiently."
            ),
            "modern_version": (
                "An autonomous glider using carbon fiber materials, GPS guidance, "
                "and weather-response software."
            ),
            "demand": "Moderate to high demand in environmental monitoring and aviation research.",
            "roi": "Estimated ROI: 55% within 3 years."
        },
        {
            "title": "Ornithopter Inspired by Birds",
            "principle": (
                "A wing-flapping mechanism recreates the natural biomechanics of birds "
                "to generate lift and controlled navigation."
            ),
            "modern_version": (
                "A bio-inspired aerial robot with servo-controlled wings and computer vision."
            ),
            "demand": "High demand in experimental aviation and defense technology.",
            "roi": "Estimated ROI: 80% within 2-4 years."
        }
    ],
    "water": [
        {
            "title": "Underwater Breathing Device",
            "principle": (
                "This system stores air in a sealed chamber and distributes it through "
                "tubes to extend underwater breathing time."
            ),
            "modern_version": (
                "A modern diving apparatus with compressed air tanks, pressure control, "
                "and digital monitoring."
            ),
            "demand": "High demand in marine exploration and rescue operations.",
            "roi": "Estimated ROI: 65% within 2 years."
        },
        {
            "title": "Mechanical Submarine",
            "principle": (
                "A sealed underwater vessel uses controlled ballast and propulsion "
                "to dive, navigate, and resurface safely."
            ),
            "modern_version": (
                "A compact autonomous underwater vehicle for research and inspection."
            ),
            "demand": "High demand in ocean research and industrial inspection.",
            "roi": "Estimated ROI: 75% within 3 years."
        },
        {
            "title": "Water Propulsion System",
            "principle": (
                "Rotating blades transfer mechanical force into water to produce "
                "controlled movement in a marine environment."
            ),
            "modern_version": (
                "An electric marine propulsion system with efficient turbines and "
                "smart control software."
            ),
            "demand": "Moderate demand in marine transport and green engineering.",
            "roi": "Estimated ROI: 50% within 3-4 years."
        }
    ],
    "war": [
        {
            "title": "Armored Mechanical Vehicle",
            "principle": (
                "A protected mobile structure carries defensive systems while shielding "
                "its operators from external attacks."
            ),
            "modern_version": (
                "An AI-assisted armored ground vehicle with remote navigation and surveillance."
            ),
            "demand": "High demand in defense and security sectors.",
            "roi": "Estimated ROI: 85% within 2-3 years."
        },
        {
            "title": "Defensive Rotating Shield",
            "principle": (
                "A rotating shield system disperses impact and forms a moving protective barrier."
            ),
            "modern_version": (
                "A portable ballistic defense system using lightweight alloys and smart deployment."
            ),
            "demand": "Moderate demand in tactical defense applications.",
            "roi": "Estimated ROI: 45% within 3 years."
        },
        {
            "title": "Mechanical Crossbow System",
            "principle": (
                "A tension-based launch mechanism stores and releases force "
                "with enhanced precision and consistency."
            ),
            "modern_version": (
                "A robotic launch platform with targeting software and electromechanical control."
            ),
            "demand": "Moderate demand in defense research and simulation systems.",
            "roi": "Estimated ROI: 40% within 3-4 years."
        }
    ],
    "transport": [
        {
            "title": "Self-Propelled Cart",
            "principle": (
                "A gear-driven cart stores mechanical energy and releases it to move "
                "without animal power."
            ),
            "modern_version": (
                "An autonomous delivery vehicle powered by batteries and guided by AI."
            ),
            "demand": "High demand in logistics and smart city infrastructure.",
            "roi": "Estimated ROI: 90% within 2 years."
        },
        {
            "title": "Mechanical Bridge System",
            "principle": (
                "A movable bridge uses hinges and leverage to deploy quickly "
                "across terrain or obstacles."
            ),
            "modern_version": (
                "A rapid-deployment smart bridge for emergency and military engineering."
            ),
            "demand": "Moderate demand in civil engineering and disaster response.",
            "roi": "Estimated ROI: 60% within 3 years."
        },
        {
            "title": "Rotating Wheel Transport Machine",
            "principle": (
                "The machine combines rotational motion and balanced structure "
                "to improve transport efficiency on land."
            ),
            "modern_version": (
                "A compact electric mobility platform with intelligent motion control."
            ),
            "demand": "High demand in urban mobility and industrial transport.",
            "roi": "Estimated ROI: 70% within 2-3 years."
        }
    ],
    "energy": [
        {
            "title": "Mechanical Wind Energy Tower",
            "principle": (
                "Rotating blades capture wind power and transfer the motion "
                "through gears into usable mechanical energy."
            ),
            "modern_version": (
                "A smart wind turbine integrated with grid analytics and energy storage."
            ),
            "demand": "High demand in renewable infrastructure and sustainable engineering.",
            "roi": "Estimated ROI: 75% within 3 years."
        },
        {
            "title": "Thermal Power Storage Engine",
            "principle": (
                "The device collects heat, stores it in insulated chambers, "
                "and converts it into mechanical output."
            ),
            "modern_version": (
                "A thermal battery system for industrial energy balancing and clean storage."
            ),
            "demand": "Moderate to high demand in industrial energy optimization.",
            "roi": "Estimated ROI: 68% within 3-4 years."
        },
        {
            "title": "Solar Mirror Concentrator",
            "principle": (
                "Reflective surfaces focus sunlight onto a central point to amplify heat energy."
            ),
            "modern_version": (
                "A concentrated solar power unit with automated mirror tracking and AI controls."
            ),
            "demand": "High demand in green technology and solar energy innovation.",
            "roi": "Estimated ROI: 72% within 3 years."
        }
    ],
    "medicine": [
        {
            "title": "Mechanical Diagnostic Analyzer",
            "principle": (
                "A sequence of controlled measurements is used to identify changes "
                "in body state through mechanical indicators."
            ),
            "modern_version": (
                "An AI-assisted diagnostic device with biosensors and real-time data analysis."
            ),
            "demand": "High demand in healthcare, diagnostics, and preventive medicine.",
            "roi": "Estimated ROI: 88% within 2-3 years."
        },
        {
            "title": "Precision Surgical Support Arm",
            "principle": (
                "An articulated mechanism stabilizes tools and enhances precise movement during procedures."
            ),
            "modern_version": (
                "A robotic surgical assistant with motion tracking and intelligent control."
            ),
            "demand": "High demand in hospitals and advanced clinical centers.",
            "roi": "Estimated ROI: 82% within 3 years."
        },
        {
            "title": "Portable Healing Chamber",
            "principle": (
                "An enclosed mechanical system creates a controlled recovery environment "
                "for treatment and observation."
            ),
            "modern_version": (
                "A smart portable medical pod for patient monitoring and emergency support."
            ),
            "demand": "Moderate to high demand in emergency medicine and remote care.",
            "roi": "Estimated ROI: 64% within 3 years."
        }
    ],
    "architecture": [
        {
            "title": "Adaptive Bridge Pavilion",
            "principle": (
                "A modular structure uses hinges, supports, and balance principles "
                "to adapt to changing spatial needs."
            ),
            "modern_version": (
                "A deployable smart pavilion with lightweight materials and structural sensors."
            ),
            "demand": "Moderate demand in temporary architecture and event engineering.",
            "roi": "Estimated ROI: 58% within 3 years."
        },
        {
            "title": "Self-Supporting Spiral Tower",
            "principle": (
                "The tower distributes load through a spiral geometry that improves vertical stability."
            ),
            "modern_version": (
                "A parametric high-rise design using advanced structural simulation and smart materials."
            ),
            "demand": "Moderate to high demand in experimental architecture.",
            "roi": "Estimated ROI: 62% within 4 years."
        },
        {
            "title": "Rapid-Deployment Shelter Frame",
            "principle": (
                "A foldable frame uses mechanical locking joints to create shelter quickly and securely."
            ),
            "modern_version": (
                "An emergency smart shelter for disaster response and humanitarian operations."
            ),
            "demand": "High demand in disaster response and emergency engineering.",
            "roi": "Estimated ROI: 70% within 2-3 years."
        }
    ],
    "agriculture": [
        {
            "title": "Mechanical Seed Distribution System",
            "principle": (
                "A rotating distribution mechanism spreads seeds evenly while reducing manual labor."
            ),
            "modern_version": (
                "An AI-guided precision seeding machine with smart soil analysis."
            ),
            "demand": "High demand in precision agriculture and farm automation.",
            "roi": "Estimated ROI: 76% within 2 years."
        },
        {
            "title": "Automatic Irrigation Regulator",
            "principle": (
                "A timed valve mechanism controls water flow according to field conditions."
            ),
            "modern_version": (
                "A sensor-based irrigation system with climate feedback and mobile control."
            ),
            "demand": "High demand in water-efficient farming systems.",
            "roi": "Estimated ROI: 73% within 2-3 years."
        },
        {
            "title": "Harvest Assistance Cart",
            "principle": (
                "A mechanically supported cart improves carrying efficiency and reduces labor intensity."
            ),
            "modern_version": (
                "An autonomous field support vehicle for harvesting and crop logistics."
            ),
            "demand": "Moderate to high demand in agricultural logistics.",
            "roi": "Estimated ROI: 61% within 3 years."
        }
    ],
    "robotics": [
        {
            "title": "Articulated Mechanical Assistant",
            "principle": (
                "A system of coordinated joints and gears reproduces useful repetitive motion."
            ),
            "modern_version": (
                "A collaborative robot with AI control, vision systems, and industrial manipulators."
            ),
            "demand": "High demand in automation, manufacturing, and education.",
            "roi": "Estimated ROI: 89% within 2-3 years."
        },
        {
            "title": "Autonomous Inspection Automaton",
            "principle": (
                "A guided mobile machine follows a planned route and mechanically records conditions."
            ),
            "modern_version": (
                "An inspection robot with cameras, AI analytics, and predictive maintenance tools."
            ),
            "demand": "High demand in infrastructure and industrial maintenance.",
            "roi": "Estimated ROI: 84% within 2 years."
        },
        {
            "title": "Mechanical Learning Demonstrator",
            "principle": (
                "Visible moving parts illustrate logic, sequence, and interaction between mechanisms."
            ),
            "modern_version": (
                "An educational robot platform for STEM learning and interactive engineering training."
            ),
            "demand": "Moderate to high demand in education and robotics labs.",
            "roi": "Estimated ROI: 59% within 2-3 years."
        }
    ],
    "space": [
        {
            "title": "Orbital Observation Platform",
            "principle": (
                "A stable rotating frame maintains directional alignment for observation and measurement."
            ),
            "modern_version": (
                "A compact orbital research satellite with AI-assisted navigation and autonomous diagnostics."
            ),
            "demand": "High demand in aerospace research and commercial observation systems.",
            "roi": "Estimated ROI: 83% within 3-5 years."
        },
        {
            "title": "Planetary Exploration Rover",
            "principle": (
                "A resilient movement system crosses uneven terrain while preserving stability and control."
            ),
            "modern_version": (
                "A smart exploration rover with terrain mapping, robotic sampling, and autonomous decisions."
            ),
            "demand": "High demand in space exploration and extreme-environment robotics.",
            "roi": "Estimated ROI: 78% within 4 years."
        },
        {
            "title": "Mechanical Star Navigation Device",
            "principle": (
                "Rotating calibrated rings align with celestial bodies to determine direction and motion."
            ),
            "modern_version": (
                "A modern stellar navigation module for spacecraft guidance and deep-space positioning."
            ),
            "demand": "Moderate to high demand in aerospace guidance systems.",
            "roi": "Estimated ROI: 66% within 4 years."
        }
    ]
}


def main():
    print("Leonardo AI - Renaissance Invention Generator")
    category = input(
        "Choose category (flight, water, war, transport, energy, medicine, "
        "architecture, agriculture, robotics, space): "
    ).strip().lower()

    if not validate_category(category):
        print("Invalid category.")
        return

    invention = generate_invention(category)
    result = format_invention(invention)

    print("\nGenerated Invention:\n")
    print(result)


def validate_category(category):
    return category in INVENTIONS


def generate_invention(category):
    if not validate_category(category):
        raise ValueError("Invalid category")
    return random.choice(INVENTIONS[category])


def format_invention(invention):
    return (
        f"Title: {invention['title']}\n"
        f"Principle: {invention['principle']}\n"
        f"Modern Version: {invention['modern_version']}\n"
        f"Market Demand: {invention['demand']}\n"
        f"ROI Analysis: {invention['roi']}"
    )


if __name__ == "__main__":
    main()