def generate_dev_time(difficulty):
    mapping = {
        "Medium": "Prototype: 2-4 months • MVP: 6-8 months • Product: 1 year",
        "High": "Prototype: 4-6 months • MVP: 8-12 months • Product: 1-2 years",
        "Extreme": "Prototype: 6-10 months • MVP: 12-18 months • Product: 2+ years"
    }
    return mapping.get(difficulty, "Prototype: 3-6 months • MVP: 8-12 months • Product: 1-2 years")


def generate_investor_summary(title, category, demand, roi):
    return (
        f"{title} is a {category} innovation concept inspired by Leonardo da Vinci. "
        f"It targets practical engineering value, visual uniqueness, and product potential. "
        f"{demand} {roi}"
    )