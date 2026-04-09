import os
import streamlit as st

from database import init_db, save_concept, get_concepts, get_concept_by_id, delete_concept
from services.concept_service import generate_concept
from config import CATEGORIES, DIFFICULTY, MATERIALS, USE_CASES
from utils import generate_dev_time, generate_investor_summary

st.set_page_config(
    page_title="Leonardo AI",
    page_icon="🎨",
    layout="wide"
)

init_db()

st.markdown(
    """
    <style>
    .main-title {
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 8px;
        color: #f9fafb;
    }
    .subtitle {
        font-size: 18px;
        color: #9ca3af;
        margin-bottom: 20px;
    }
    .topbar {
        background: linear-gradient(90deg, #111827, #1f2937);
        border: 1px solid #374151;
        border-radius: 18px;
        padding: 18px 22px;
        margin-bottom: 18px;
    }
    .topbar-title {
        font-size: 26px;
        font-weight: 700;
        color: #f9fafb;
        margin-bottom: 4px;
    }
    .topbar-subtitle {
        font-size: 14px;
        color: #9ca3af;
    }
    .profile-card {
        background: #111827;
        border: 1px solid #374151;
        border-radius: 16px;
        padding: 18px;
        margin-bottom: 14px;
        color: white;
    }
    .feature-box {
        padding: 14px;
        border-radius: 12px;
        background-color: #1f2937;
        border: 1px solid #374151;
        margin-bottom: 10px;
        color: white;
    }
    .result-box {
        padding: 18px;
        border-radius: 16px;
        background-color: #f8fafc;
        border: 1px solid #d1d5db;
        margin-top: 12px;
        margin-bottom: 12px;
        color: #111827;
    }
    .status-good {
        padding: 10px 14px;
        border-radius: 10px;
        background: #052e16;
        border: 1px solid #166534;
        color: #dcfce7;
        margin-bottom: 8px;
    }
    .status-warn {
        padding: 10px 14px;
        border-radius: 10px;
        background: #3f2a00;
        border: 1px solid #92400e;
        color: #fde68a;
        margin-bottom: 8px;
    }
    .mini-card {
        padding: 14px;
        border-radius: 14px;
        background: #111827;
        border: 1px solid #374151;
        color: white;
        margin-bottom: 10px;
    }
    .small-note {
        font-size: 13px;
        color: #9ca3af;
        margin-top: 6px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ----------------------------
# Helpers
# ----------------------------

# ----------------------------
# Session state
# ----------------------------
if "history" not in st.session_state:
    st.session_state.history = []

# ----------------------------
# Top bar
# ----------------------------
top1, top2, top3 = st.columns([2, 1, 1])

with top1:
    st.markdown(
        """
        <div class="topbar">
            <div class="topbar-title">🎨 Leonardo AI</div>
            <div class="topbar-subtitle">
                Renaissance Invention Generator with Modern Engineering Analysis
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with top2:
    selected_language = st.selectbox(
        "Language",
        ["English", "Русский", "Svenska"],
        index=0
    )

with top3:
    app_mode = st.selectbox(
        "Mode",
        ["Demo", "Presentation", "Prototype"],
        index=2
    )

# ----------------------------
# Layout
# ----------------------------
left, right = st.columns([1, 2])

with left:
    st.markdown(
        """
        <div class="profile-card">
            <h3 style="margin-top:0;">👤 User Panel</h3>
            <p style="margin-bottom:6px;"><b>Name:</b> Aleksei</p>
            <p style="margin-bottom:6px;"><b>Role:</b> Creator / Student</p>
            <p style="margin-bottom:0;"><b>Language:</b> Selected above</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("## Project Controls")

    category = st.selectbox(
    "Choose invention category",
    CATEGORIES
    )

    creativity_mode = st.selectbox(
        "Creativity mode",
        ["Classic", "Bold", "Experimental"]
    )

    audience = st.selectbox(
        "Target audience",
        ["Engineers", "Investors", "Students", "General Public"]
    )

    user_prompt = st.text_area(
        "Prompt / Idea",
        placeholder="Example: Create a Renaissance-inspired rescue glider for dangerous mountain missions...",
        height=120
    )

    st.markdown("### 🎤 Voice Prompt")
    st.button("🎙 Start Voice Prompt", use_container_width=True)
    st.caption("Demo UI ready. Real speech-to-text transcription can be connected later.")

    st.markdown("### AI Modules")
    image_module = st.toggle("Enable image generation concept", value=True)
    blueprint_module = st.toggle("Enable blueprint concept", value=True)
    voice_module = st.toggle("Enable voice assistant concept", value=True)

    generate = st.button("✨ Generate Full Concept", use_container_width=True)
    regenerate = st.button("🔄 Generate Again", use_container_width=True)

    st.markdown("## Included in Output")
    st.markdown(
        """
        <div class="feature-box">✅ Leonardo-style invention idea</div>
        <div class="feature-box">✅ Principle of operation</div>
        <div class="feature-box">✅ Leonardo sketch description</div>
        <div class="feature-box">✅ Modern implementation</div>
        <div class="feature-box">✅ Modern sketch description</div>
        <div class="feature-box">✅ Market demand estimate</div>
        <div class="feature-box">✅ ROI analysis</div>
        <div class="feature-box">✅ Difficulty level</div>
        <div class="feature-box">✅ Development timeline</div>
        <div class="feature-box">✅ Materials / technologies</div>
        <div class="feature-box">✅ Use cases</div>
        <div class="feature-box">✅ Investor summary</div>
        <div class="feature-box">✅ Voice assistant interaction concept</div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="small-note">For CS50 submission, core logic remains in project.py. Production mode uses OpenAI when API key is available.</div>',
        unsafe_allow_html=True
    )

with right:
    st.markdown("## About the System")
    st.write(
        "Leonardo AI generates invention concepts inspired by Renaissance engineering and "
        "translates them into modern product ideas with practical commercial potential."
    )

    st.info(
        "Use this app to demonstrate creative engineering thinking, concept generation, "
        "and product presentation for your final project and future product development."
    )

    st.markdown("## System Status")
    st.markdown('<div class="status-good">✅ Core Logic: Active</div>', unsafe_allow_html=True)
    st.markdown('<div class="status-good">✅ Interface Layer: Active</div>', unsafe_allow_html=True)

    if os.getenv("OPENAI_API_KEY"):
        st.markdown('<div class="status-good">✅ OpenAI Integration: Active</div>', unsafe_allow_html=True)
    else:
        st.markdown(
            '<div class="status-warn">🟡 OpenAI Integration: Not detected, fallback mode will be used</div>',
            unsafe_allow_html=True
        )

    st.markdown(
        '<div class="status-warn">🟡 Voice Prompt Transcription: Demo UI only (speech-to-text not connected yet)</div>',
        unsafe_allow_html=True
    )
    st.markdown('<div class="status-good">✅ Image Module: Concept Ready</div>', unsafe_allow_html=True)
    st.markdown('<div class="status-good">✅ Blueprint Engine: Concept Ready</div>', unsafe_allow_html=True)

    should_generate = generate or regenerate

    if should_generate:
        prompt_text = user_prompt.strip() if user_prompt.strip() else f"Create an invention in {category}"

        with st.spinner("Generating concept..."):
            concept_data = generate_concept(
                category=category,
                creativity_mode=creativity_mode,
                audience=audience,
                user_prompt=prompt_text,
            )

        title = concept_data["title"]
        principle = concept_data["principle"]
        leonardo_sketch_description = concept_data["leonardo_sketch_description"]
        difficulty = concept_data["difficulty"]
        modern_version = concept_data["modern_version"]
        modern_principle = concept_data.get(
            "modern_principle",
            "The modern operating principle is based on modular engineering, controlled actuation, structural stability, and maintainable subsystems."
        )
        modern_sketch_description = concept_data["modern_sketch_description"]
        materials = concept_data["materials"]
        use_cases = concept_data["use_cases"]
        dev_time = concept_data["dev_time"]
        modern_difficulty = concept_data["modern_difficulty"]
        demand = concept_data["demand"]
        roi = concept_data["roi"]
        startup_cost = concept_data.get(
            "startup_cost",
            "Estimated startup cost: $150,000-$300,000 depending on prototype complexity, testing, and early deployment requirements."
        )
        investor_summary = concept_data["investor_summary"]
        image_concept = concept_data["image_concept"]
        voice_assistant_concept = concept_data["voice_assistant_concept"]
        blueprint_concept = concept_data["blueprint_concept"]

        save_concept(
            title=title,
            category=category,
            prompt=prompt_text,
            principle=principle,
            modern_version=modern_version,
            demand=demand,
            roi=roi,
            materials=", ".join(materials),
            use_cases=", ".join(use_cases),
            investor_summary=investor_summary,
        )
        
        if not image_module:
            image_concept = "Image generation concept is currently disabled."
        if not blueprint_module:
            blueprint_concept = "Blueprint concept is currently disabled."
        if not voice_module:
            voice_assistant_concept = "Voice assistant module is currently disabled."

        if creativity_mode == "Bold":
            extra_note = "This concept emphasizes disruptive innovation and stronger commercial appeal."
        elif creativity_mode == "Experimental":
            extra_note = "This concept emphasizes unusual engineering ideas and speculative future applications."
        else:
            extra_note = "This concept stays close to classical engineering logic and historical inspiration."

        if audience == "Investors":
            audience_note = "Presentation focus: scalability, profitability, and market opportunity."
        elif audience == "Engineers":
            audience_note = "Presentation focus: mechanism design, functionality, materials, and architecture."
        elif audience == "Students":
            audience_note = "Presentation focus: clarity, learning value, and simple explanation."
        else:
            audience_note = "Presentation focus: accessibility, visual appeal, and easy understanding."

        st.session_state.history.insert(0, {"title": title, "category": category})
        st.session_state.history = st.session_state.history[:5]

        st.success("Concept generated successfully.")
        
        if user_prompt.strip():
            st.markdown("### User Prompt")
            st.markdown(
                f"""
                <div class="result-box">
                {user_prompt}
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("## 🎨 Leonardo Concept")

        st.markdown("### 📜 Generated Invention")
        st.markdown(
            f"""
            <div class="result-box">
            <b>{title}</b><br><br>
            {extra_note}<br><br>
            {audience_note}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("### ⚙️ Principle of Operation")
        st.markdown(f'<div class="result-box">{principle}</div>', unsafe_allow_html=True)

        st.markdown("### ✏️ Leonardo Sketch Description")
        st.markdown(
            f'<div class="result-box">{leonardo_sketch_description}</div>',
            unsafe_allow_html=True
        )

        st.markdown("### 🎯 Leonardo Concept Difficulty")
        st.markdown(f'<div class="result-box">{difficulty}</div>', unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("## 🚀 Modern Engineering")

        st.markdown("### 🚀 Modern Implementation")
        st.markdown(f'<div class="result-box">{modern_version}</div>', unsafe_allow_html=True)
        
        st.markdown("### ⚙️ Modern Principle of Operation")
        st.markdown(f'<div class="result-box">{modern_principle}</div>', unsafe_allow_html=True)
        
        st.markdown("### 🧩 Modern Sketch Description")
        st.markdown(
            f'<div class="result-box">{modern_sketch_description}</div>',
            unsafe_allow_html=True
        )

        st.markdown("### 🧱 Materials / Technologies")
        st.markdown(
            f'<div class="result-box">• ' + "<br>• ".join(materials) + "</div>",
            unsafe_allow_html=True
        )

        st.markdown("### 🧭 Use Cases")
        st.markdown(
            f'<div class="result-box">• ' + "<br>• ".join(use_cases) + "</div>",
            unsafe_allow_html=True
        )

        st.markdown("### ⏱ Development Timeline")
        st.markdown(f'<div class="result-box">{dev_time}</div>', unsafe_allow_html=True)

        st.markdown("### 🏗️ Modern Engineering Difficulty")
        st.markdown(
            f'<div class="result-box">{modern_difficulty}</div>',
            unsafe_allow_html=True
        )

        st.markdown("---")
        st.markdown("## 📈 Market & Business")

        st.markdown("### 📈 Market Demand")
        st.markdown(f'<div class="result-box">{demand}</div>', unsafe_allow_html=True)
        
        st.markdown("### 💵 Startup Cost Estimate")
        st.markdown(f'<div class="result-box">{startup_cost}</div>', unsafe_allow_html=True)
        
        st.markdown("### 💰 ROI Analysis")
        st.markdown(f'<div class="result-box">{roi}</div>', unsafe_allow_html=True)

        st.markdown("### 📊 Investor Summary")
        st.markdown(
            f'<div class="result-box">{investor_summary}</div>',
            unsafe_allow_html=True
        )

        st.markdown("---")
        st.markdown("## 🧠 AI System Features")

        st.markdown("### 🖼 Image Generation Concept")
        st.markdown(f'<div class="result-box">{image_concept}</div>', unsafe_allow_html=True)

        st.markdown("### 🎤 Voice Assistant Concept")
        st.markdown(
            f'<div class="result-box">{voice_assistant_concept}</div>',
            unsafe_allow_html=True
        )

        st.markdown("### 📐 Blueprint Concept")
        st.markdown(f'<div class="result-box">{blueprint_concept}</div>', unsafe_allow_html=True)

    
    st.markdown("## Previous Concepts")

    concepts = get_concepts()

    if concepts:
        for concept_id, title, category, created_at in concepts:
            col1, col2 = st.columns([5, 1])

            with col1:
                if st.button(f"Open: {title} ({category}) — {created_at}", key=f"open_{concept_id}"):
                    selected_concept = get_concept_by_id(concept_id)

                    if selected_concept:
                        (
                            concept_id,
                            saved_title,
                            saved_category,
                            saved_prompt,
                            saved_principle,
                            saved_modern_version,
                            saved_demand,
                            saved_roi,
                            saved_materials,
                            saved_use_cases,
                            saved_investor_summary,
                            saved_created_at,
                        ) = selected_concept

                        st.markdown("### Saved Concept Details")
                        st.write(f"**Title:** {saved_title}")
                        st.write(f"**Category:** {saved_category}")
                        st.write(f"**Prompt:** {saved_prompt}")
                        st.write(f"**Principle:** {saved_principle}")
                        st.write(f"**Modern Version:** {saved_modern_version}")
                        st.write(f"**Demand:** {saved_demand}")
                        st.write(f"**ROI:** {saved_roi}")
                        st.write(f"**Materials:** {saved_materials}")
                        st.write(f"**Use Cases:** {saved_use_cases}")
                        st.write(f"**Investor Summary:** {saved_investor_summary}")
                        st.write(f"**Created:** {saved_created_at}")

            with col2:
                if st.button("Delete", key=f"delete_{concept_id}"):
                    delete_concept(concept_id)
                    st.rerun()
    else:
        st.markdown("No previous concepts yet.")