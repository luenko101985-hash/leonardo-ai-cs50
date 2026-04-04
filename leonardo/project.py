import random


INVENTIONS = {
    "flight": [
        {
            "title": "Mechanical Flying Machine with Rotating Wings",
            "principle": (
                "This invention imitates the motion of bird wings and uses "
                "rotating wooden mechanisms to create lift and forward movement."
            ),
            "modern_version": (
                "A lightweight drone with flapping composite wings, onboard sensors, "
                "and AI-assisted flight stabilization."
            ),
            "demand": "High demand in robotics, research, and surveillance.",
            "roi": "Estimated ROI: 70% within 2-3 years if developed commercially."
        },
        {
            "title": "Wind-Powered Glider",
            "principle": (
                "The machine captures wind energy and uses a curved wing structure "
                "to maintain stable gliding over long distances."
            ),
            "modern_version": (
                "An autonomous glider using carbon fiber materials, GPS, and "
                "environmental data analysis."
            ),
            "demand": "Moderate to high demand in environmental monitoring.",
            "roi": "Estimated ROI: 55% within 3 years."
        },
        {
            "title": "Ornithopter Inspired by Birds",
            "principle": (
                "A wing-flapping mechanism recreates the biomechanics of birds "
                "to generate lift and directional control."
            ),
            "modern_version": (
                "A bio-inspired aerial robot with servo-controlled wings and "
                "computer vision navigation."
            ),
            "demand": "High demand in experimental aviation and defense technology.",
            "roi": "Estimated ROI: 80% within 2-4 years."
        }
    ],
    "water": [
        {
            "title": "Underwater Breathing Device",
            "principle": (
                "The device stores air in a sealed system and distributes it "
                "through tubes to allow a person to stay underwater longer."
            ),
            "modern_version": (
                "A modern diving apparatus with compressed air tanks, pressure "
                "regulators, and digital monitoring."
            ),
            "demand": "High demand in marine exploration and rescue operations.",
            "roi": "Estimated ROI: 65% within 2 years."
        },
        {
            "title": "Mechanical Submarine",
            "principle": (
                "A sealed underwater vessel moves using manual propulsion and "
                "controlled ballast for diving and resurfacing."
            ),
            "modern_version": (
                "A compact autonomous underwater vehicle for exploration and inspection."
            ),
            "demand": "High demand in ocean research and industrial inspection.",
            "roi": "Estimated ROI: 75% within 3 years."
        },
        {
            "title": "Water Propulsion System",
            "principle": (
                "Rotating blades transfer force into water, producing controlled "
                "movement for boats or underwater machines."
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
                "A protected mobile structure carries defensive equipment while "
                "shielding its operators from enemy attacks."
            ),
            "modern_version": (
                "An AI-assisted armored ground vehicle with remote navigation "
                "and surveillance systems."
            ),
            "demand": "High demand in defense and security sectors.",
            "roi": "Estimated ROI: 85% within 2-3 years."
        },
        {
            "title": "Defensive Rotating Shield",
            "principle": (
                "A rotating shield mechanism disperses impact and provides a moving "
                "protective barrier."
            ),
            "modern_version": (
                "A portable ballistic defense system using lightweight alloys and "
                "stabilized deployment."
            ),
            "demand": "Moderate demand in tactical defense applications.",
            "roi": "Estimated ROI: 45% within 3 years."
        },
        {
            "title": "Mechanical Crossbow System",
            "principle": (
                "A tension-based firing mechanism stores energy and releases it "
                "with improved precision and force."
            ),
            "modern_version": (
                "A robotic launching system with targeting software and "
                "electromechanical control."
            ),
            "demand": "Moderate demand in defense research and simulation systems.",
            "roi": "Estimated ROI: 40% within 3-4 years."
        }
    ],
    "transport": [
        {
            "title": "Self-Propelled Cart",
            "principle": (
                "A gear-driven cart stores mechanical energy and releases it "
                "to move without animal power."
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
                "across difficult terrain."
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
                "to improve movement efficiency over land."
            ),
            "modern_version": (
                "A compact electric transport platform with intelligent motion control."
            ),
            "demand": "High demand in urban mobility and industrial transport.",
            "roi": "Estimated ROI: 70% within 2-3 years."
        }
    ]
}


def main():
    print("Leonardo AI - Renaissance Invention Generator")
    category = input("Choose category (flight, water, war, transport): ").strip().lower()

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