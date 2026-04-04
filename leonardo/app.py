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
        padding: 18px;
        border-radius: 14px;
        background-color: #f7f4ef;
        border: 1px solid #ddd;
        margin-bottom: 12px;
    }
    .result-box {
        padding: 20px;
        border-radius: 16px;
        background-color: #faf8f3;
        border: 1px solid #d8d2c4;
        margin-top: 15px;
        margin-bottom: 15px;
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

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### Project Controls")
    category = st.selectbox(
        "Choose invention category",
        ["flight", "water", "war", "transport"]
    )

    creativity_mode = st.selectbox(
        "Creativity mode",
        ["Classic", "Bold", "Experimental"]
    )

    audience = st.selectbox(
        "Target audience",
        ["Engineers", "Investors", "Students", "General Public"]
    )

    generate = st.button("Generate Full Concept", use_container_width=True)

    st.markdown("### Included in Output")
    st.markdown(
        """
        <div class="feature-box">✅ Leonardo-style invention idea</div>
        <div class="feature-box">✅ Principle of operation</div>
        <div class="feature-box">✅ Modern implementation</div>
        <div class="feature-box">✅ Market demand estimate</div>
        <div class="feature-box">✅ ROI analysis</div>
        <div class="feature-box">✅ Sketch description for slides/video</div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown("### About the System")
    st.write(
        "Leonardo AI generates an invention concept inspired by the engineering "
        "spirit of Leonardo da Vinci, then translates it into a modern product idea "
        "with practical commercial potential."
    )

    st.info(
        "Use this app to demonstrate creative engineering thinking, concept generation, "
        "and product presentation for your final project."
    )

    if generate:
        if validate_category(category):
            invention = generate_invention(category)

            sketch_description = (
                f"A sepia-toned Renaissance sketch of '{invention['title']}', drawn with "
                f"fine ink lines, annotations in the style of Leonardo da Vinci, visible "
                f"mechanical parts, wooden gears, and engineering notes in the margins."
            )

            modern_sketch = (
                f"A modern engineering concept illustration of '{invention['title']}', "
                f"showing sleek materials, labeled components, functional modules, and "
                f"a presentation-ready product design."
            )

            if creativity_mode == "Bold":
                extra_note = (
                    "This concept emphasizes disruptive innovation and stronger commercial appeal."
                )
            elif creativity_mode == "Experimental":
                extra_note = (
                    "This concept emphasizes unusual engineering ideas and speculative future applications."
                )
            else:
                extra_note = (
                    "This concept stays close to classical engineering logic and historical inspiration."
                )

            if audience == "Investors":
                audience_note = (
                    "Presentation focus: scalability, profitability, commercial value, and market opportunity."
                )
            elif audience == "Engineers":
                audience_note = (
                    "Presentation focus: mechanism design, functionality, materials, and system architecture."
                )
            elif audience == "Students":
                audience_note = (
                    "Presentation focus: clarity, learning value, and simple explanation of technical ideas."
                )
            else:
                audience_note = (
                    "Presentation focus: accessibility, visual appeal, and easy understanding."
                )

            st.success("Concept generated successfully.")

            st.markdown("## 📜 Generated Invention")
            st.markdown(
                f"""
                <div class="result-box">
                <b>{invention['title']}</b><br><br>
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
                    {invention['principle']}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown("### 📈 Market Demand")
                st.markdown(
                    f"""
                    <div class="result-box">
                    {invention['demand']}
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

            with c2:
                st.markdown("### 🚀 Modern Implementation")
                st.markdown(
                    f"""
                    <div class="result-box">
                    {invention['modern_version']}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown("### 💰 ROI Analysis")
                st.markdown(
                    f"""
                    <div class="result-box">
                    {invention['roi']}
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

            with st.expander("Show formatted text output"):
                st.text(format_invention(invention))

        else:
            st.error("Invalid category selected.")
    else:
        st.markdown("### Demo Preview")
        st.write(
            "Choose a category, select creativity mode, and generate a full invention concept "
            "for your presentation, screenshots, or final project video."
        )