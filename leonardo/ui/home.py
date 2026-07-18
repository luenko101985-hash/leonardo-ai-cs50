import os

import streamlit as st

from ui.assets import image_to_base64
from ui.components import render_section_heading


def render_banner():
    st.image("banner.png", use_container_width=True)


def render_system_status():
    openai_active = bool(os.getenv("OPENAI_API_KEY"))

    openai_title = "✅ OpenAI Integration: Active" if openai_active else "🟡 OpenAI Integration: Fallback"
    openai_desc = "Connected to OpenAI services and ready to generate." if openai_active else "API key not detected. Local fallback mode will be used."

    render_section_heading("System Status")

    st.markdown(
        f"""
<div class="status-grid">
    <div class="status-card">
        <div class="status-title">✅ Core Logic: Active</div>
        <div class="status-desc">The core reasoning engine is operational and ready.</div>
    </div>
    <div class="status-card">
        <div class="status-title">✅ Interface Layer: Active</div>
        <div class="status-desc">UI components are responsive and functioning.</div>
    </div>
    <div class="status-card">
        <div class="status-title">{openai_title}</div>
        <div class="status-desc">{openai_desc}</div>
    </div>
</div>
""",
        unsafe_allow_html=True,
    )


def render_empty_concept_area():
    render_section_heading("Generated Concept")

    concept_panel_base64 = image_to_base64("concept_panel.png")

    if concept_panel_base64:
        st.markdown(
            f"""
<div class="concept-empty-image-box">
    <img src="data:image/png;base64,{concept_panel_base64}" class="concept-empty-image">
    <div class="concept-empty-text">
        <p>Your invention concept will appear here.</p>
        <p>Leonardo AI will generate a complete Renaissance-inspired invention with modern engineering analysis.</p>
    </div>
</div>
""",
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
<div class="concept-empty">
    <p>Your idea concept will appear here.</p>
    <p>Leonardo AI will generate a complete idea with Renaissance-inspired vision and modern implementation analysis.</p>
</div>
""",
            unsafe_allow_html=True,
        )

    feature_cards = [
        ("🪶", "Title & Summary", "The name and brief overview of the idea."),
        ("⚙️", "Core Principle", "The fundamental principle behind how it works."),
        ("🖼️", "Leonardo Sketch", "A description of how Leonardo might have sketched it."),
        ("📦", "Blueprint Concept", "A modern engineering blueprint and structural concept."),
        ("⚗️", "Materials & Resources", "What materials are needed and how they are used."),
        ("🎯", "Use Cases", "Where and how this idea can be applied."),
    ]

    for row_start in range(0, len(feature_cards), 3):
        cols = st.columns(3)

        for col, card in zip(cols, feature_cards[row_start:row_start + 3]):
            icon, title, text = card

            with col:
                st.markdown(
                    f"""
<div class="feature-card">
    <div class="feature-title">
        <span class="feature-icon">{icon}</span>{title}
    </div>
    <div class="feature-text">{text}</div>
</div>
""",
                    unsafe_allow_html=True,
                )

    st.markdown(
        """
<div class="feature-card">
    <div class="feature-title">
        <span class="feature-icon">📊</span>Investor Summary
    </div>
    <div class="feature-text">A brief pitch for potential investors and backers.</div>
</div>
""",
        unsafe_allow_html=True,
    )
