from database import (
    delete_image_asset,
    get_images_for_concept,
    save_image_asset,
    toggle_image_favorite,
)
from services.image_service import (
    generate_blueprint_image_prompt,
    generate_leonardo_image_prompt,
)


def generate_leonardo_visual(prompt: str) -> dict:
    return generate_leonardo_image_prompt(prompt)


def generate_blueprint_visual(prompt: str) -> dict:
    return generate_blueprint_image_prompt(prompt)


def save_visual(concept_id, image_type, asset) -> None:
    save_image_asset(
        concept_id=concept_id,
        image_type=image_type,
        prompt=asset["prompt"],
        image_bytes=asset["image_bytes"],
    )


def list_concept_images(concept_id):
    return get_images_for_concept(concept_id)


def remove_visual(image_id) -> None:
    delete_image_asset(image_id)


def toggle_visual_favorite(image_id) -> None:
    toggle_image_favorite(image_id)
