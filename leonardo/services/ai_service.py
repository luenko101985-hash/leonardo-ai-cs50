from ai_generator import generate_leonardo_concept


def generate_ai_concept(category, creativity_mode, audience, user_prompt):
    return generate_leonardo_concept(
        category=category,
        prompt=user_prompt,
        creativity=creativity_mode,
        audience=audience,
    )