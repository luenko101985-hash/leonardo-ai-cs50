import base64
from pathlib import Path

import streamlit as st


APP_ROOT = Path(__file__).resolve().parents[1]


def image_to_base64(filename):
    image_path = APP_ROOT / filename

    if not image_path.exists():
        st.error(f"Image not found: {image_path}")
        return None

    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()
