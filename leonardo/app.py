import streamlit as st
from project import validate_category, generate_invention, format_invention


st.set_page_config(
    page_title="Leonardo AI",
    page_icon="🎨",
    layout="wide"
)

st.markdown(
    """
    <style>
    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 10px;
    }
    .subtitle {
        font-size: 20px;
        color: #555;
        margin-bottom: 25px;
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
        padding: 20px;
        border-radius: 16px;
        background-color: #faf8f3;
        border: 1px solid #d8d2c4;
        margin-top: 15px;
        margin-bottom: 15px;
        color: #111827;
    }
    .small-note {
        font-size: 14px;
        color: #9ca3af;
        margin-top: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="main-title">🎨 Leonardo AI</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Renaissance Invention Generator with Modern Engineering Analysis</div>',
    unsafe_allow_html=True
)

# Expanded categories for interface
display_categories = [
    "flight",
    "water",
    "war",
    "transport",
    "energy",
    "medicine",
    "architecture",
    "agriculture",
    "robotics",
    "space"
]

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("## Project Controls")

    category = st.selectbox(
        "Choose invention category",
        display_categories
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
        placeholder="Example: Create an invention for agriculture, rescue missions, smart transport, underwater exploration, or medical diagnostics...",
        height=120
    )

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
        <div class="feature-box">✅ Modern implementation</div>
        <div class="feature-box">✅ Market demand estimate</div>
        <div class="feature-box">✅ ROI analysis</div>
        <div class="feature-box">✅ Sketch description for slides/video</div>
        <div class="feature-box">✅ Voice assistant interaction concept</div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="small-note">For CS50 submission, core logic remains in project.py.</div>',
        unsafe_allow_html=True
    )

with col2:
    st.markdown("## About the System")
    st.write(
        "Leonardo AI generates an invention concept inspired by the engineering spirit "
        "of Leonardo da Vinci, then translates it into a modern product idea with "
        "practical commercial potential."
    )

    st.info(
        "Use this app to demonstrate creative engineering thinking, concept generation, "
        "and product presentation for your final project."
    )

    should_generate = generate or regenerate

    if should_generate:
        # If category exists in project.py, use existing logic
        if validate_category(category):
            invention = generate_invention(category)
            title = invention["title"]
            principle = invention["principle"]
            modern_version = invention["modern_version"]
            demand = invention["demand"]
            roi = invention["roi"]
        else:
            # Fallback generation for new interface-only categories
            prompt_text = user_prompt.strip() if user_prompt.strip() else f"an invention in {category}"
            title = f"Leonardo Concept for {category.title()}: {prompt_text[:60]}"
            principle = (
                f"This invention applies Renaissance engineering logic to {category}. "
                f"It combines mechanical motion, structural balance, and practical design "
                f"to solve the problem described by the user prompt: '{prompt_text}'."
            )
            modern_version = (
                f"A modern implementation could combine AI, sensors, lightweight materials, "
                f"automation, and data analysis to turn this {category} concept into a real product."
            )
            demand = (
                f"Potential demand is moderate to high in the {category} sector, especially if "
                f"the solution improves efficiency, safety, or cost reduction."
            )
            roi = (
                "Estimated ROI: 50% to 85% within 2-4 years depending on prototype quality, "
                "market fit, and production cost."
            )

        sketch_description = (
            f"A sepia-toned Renaissance sketch of '{title}', drawn with fine ink lines, "
            f"mechanical annotations, visible gears, cross-sections, and Leonardo-style notes "
            f"in the margins."
        )

        modern_sketch = (
            f"A modern engineering concept illustration of '{title}', showing labeled components, "
            f"smart materials, functional modules, and a presentation-ready product design."
        )

        if voice_module:
            voice_assistant_concept = (
                f"The voice assistant module could explain how '{title}' works, guide the user through "
                f"its modern implementation, answer questions about market demand, and describe the concept "
                f"step by step in an educational style."
            )
        else:
            voice_assistant_concept = "Voice assistant module is currently disabled."

        if image_module:
            image_concept = (
                "Image generation concept enabled: the system can later produce Leonardo-style visual ideas "
                "and modern concept art for the invention."
            )
        else:
            image_concept = "Image generation concept is currently disabled."

        if blueprint_module:
            blueprint_concept = (
                "Blueprint concept enabled: the system can later output a technical sketch description "
                "for engineering slides and presentation visuals."
            )
        else:
            blueprint_concept = "Blueprint concept is currently disabled."

        if creativity_mode == "Bold":
            extra_note = "This concept emphasizes disruptive innovation and stronger commercial appeal."
        elif creativity_mode == "Experimental":
            extra_note = "This concept emphasizes unusual engineering ideas and speculative future applications."
        else:
            extra_note = "This concept stays close to classical engineering logic and historical inspiration."

        if audience == "Investors":
            audience_note = "Presentation focus: scalability, profitability, commercial value, and market opportunity."
        elif audience == "Engineers":
            audience_note = "Presentation focus: mechanism design, functionality, materials, and system architecture."
        elif audience == "Students":
            audience_note = "Presentation focus: clarity, learning value, and simple explanation of technical ideas."
        else:
            audience_note = "Presentation focus: accessibility, visual appeal, and easy understanding."

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

        st.markdown("## 📜 Generated Invention")
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

        c1, c2 = st.columns(2)

        with c1:
            st.markdown("### ⚙️ Principle of Operation")
            st.markdown(
                f"""
                <div class="result-box">
                {principle}
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown("### 📈 Market Demand")
            st.markdown(
                f"""
                <div class="result-box">
                {demand}
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown("### ✏️ Leonardo-Style Sketch Description")
            st.markdown(
                f"""
                <div class="result-box">
                {sketch_description}
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown("### 🖼️ Image Generation Concept")
            st.markdown(
                f"""
                <div class="result-box">
                {image_concept}
                </div>
                """,
                unsafe_allow_html=True
            )

        with c2:
            st.markdown("### 🚀 Modern Implementation")
            st.markdown(
                f"""
                <div class="result-box">
                {modern_version}
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown("### 💰 ROI Analysis")
            st.markdown(
                f"""
                <div class="result-box">
                {roi}
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown("### 🧩 Modern Concept Illustration")
            st.markdown(
                f"""
                <div class="result-box">
                {modern_sketch}
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown("### 🎤 Voice Assistant Concept")
            st.markdown(
                f"""
                <div class="result-box">
                {voice_assistant_concept}
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("### 📐 Blueprint / Technical Concept")
        st.markdown(
            f"""
            <div class="result-box">
            {blueprint_concept}
            </div>
            """,
            unsafe_allow_html=True
        )

        with st.expander("Show formatted core text output"):
            if validate_category(category):
                st.text(format_invention(generate_invention(category)))
            else:
                st.text(
                    f"Title: {title}\n"
                    f"Principle: {principle}\n"
                    f"Modern Version: {modern_version}\n"
                    f"Market Demand: {demand}\n"
                    f"ROI Analysis: {roi}"
                )

    else:
        st.markdown("## Demo Preview")
        st.write(
            "Choose a category, write your own prompt, select creativity mode, and generate "
            "a full invention concept for your presentation, screenshots, or final project video."
        )