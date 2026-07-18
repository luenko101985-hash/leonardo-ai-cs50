import json

import streamlit as st
import streamlit.components.v1 as components


def _to_safe_js_string(value: object) -> str:
    literal = json.dumps(str(value), ensure_ascii=False)
    return (
        literal.replace("&", "\\u0026")
        .replace("<", "\\u003c")
        .replace(">", "\\u003e")
        .replace("\u2028", "\\u2028")
        .replace("\u2029", "\\u2029")
    )


def render_voice_prompt():
    speak = st.button("🎙 Voice Prompt", use_container_width=True)

    if speak:
        components.html(
            """
<script>
const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

if (SpeechRecognition) {
    const recognition = new SpeechRecognition();
    recognition.lang = "en-US";
    recognition.continuous = false;
    recognition.interimResults = false;

    recognition.onresult = function(event) {
        const text = event.results[0][0].transcript;
        const streamlitDoc = window.parent.document;
        const textarea = streamlitDoc.querySelector('textarea');

        if (textarea) {
            textarea.value = text;
            textarea.dispatchEvent(new Event('input', { bubbles: true }));
        }
    };

    recognition.start();
}
</script>
""",
            height=0,
        )


def _speak(text, lang):
    text_literal = _to_safe_js_string(text)
    lang_literal = _to_safe_js_string(lang)

    components.html(
        f"""
<script>
const text = {text_literal};
const utterance = new SpeechSynthesisUtterance(text);
utterance.rate = 1.0;
utterance.pitch = 1.0;
utterance.lang = {lang_literal};
window.speechSynthesis.cancel();
window.speechSynthesis.speak(utterance);
</script>
""",
        height=0,
    )


def render_voice_assistant(concept_data):
    st.markdown("## 🧠 Voice Assistant")

    title = concept_data.get("title", "")
    executive_summary = concept_data.get("executive_summary", "")
    market_demand = concept_data.get("market_demand", "")
    investor_summary = concept_data.get("investor_summary", "")
    modern_principle = concept_data.get("modern_principle", "")

    voice_language = st.selectbox(
        "Voice Language",
        ["English", "Русский"],
        key="voice_language_selector",
    )

    if voice_language == "Русский":
        summary_text = f"Название проекта: {title}. Краткое описание: {executive_summary}. Рыночный спрос: {market_demand}. Инвесторское резюме: {investor_summary}."
        investor_text = f"Инвесторская презентация проекта {title}. {investor_summary}. Рыночный спрос: {market_demand}."
        engineering_text = f"Инженерный обзор проекта {title}. {modern_principle}."
        speech_lang = "ru-RU"
    else:
        summary_text = f"Project title: {title}. Executive summary: {executive_summary}. Market demand: {market_demand}. Investor summary: {investor_summary}."
        investor_text = f"Investor pitch. {title}. {investor_summary}. Market demand: {market_demand}."
        engineering_text = f"Engineering overview for {title}. {modern_principle}."
        speech_lang = "en-US"

    top1, top2, top3 = st.columns(3)
    with top1:
        play_summary = st.button("▶ Summary", key="voice_summary", use_container_width=True)
    with top2:
        play_investor = st.button("🎧 Investor", key="voice_investor", use_container_width=True)
    with top3:
        play_engineering = st.button("⚙ Engineering", key="voice_engineering", use_container_width=True)

    bottom1, bottom2, bottom3 = st.columns(3)
    with bottom1:
        pause_voice = st.button("⏸ Pause", key="voice_pause", use_container_width=True)
    with bottom2:
        resume_voice = st.button("▶ Resume", key="voice_resume", use_container_width=True)
    with bottom3:
        stop_voice = st.button("⏹ Stop", key="voice_stop", use_container_width=True)


    if play_summary:
        _speak(summary_text, speech_lang)
    if play_investor:
        _speak(investor_text, speech_lang)
    if play_engineering:
        _speak(engineering_text, speech_lang)
    if pause_voice:
        components.html("<script>window.speechSynthesis.pause();</script>", height=0)
    if resume_voice:
        components.html("<script>window.speechSynthesis.resume();</script>", height=0)
    if stop_voice:
        components.html("<script>window.speechSynthesis.cancel();</script>", height=0)
