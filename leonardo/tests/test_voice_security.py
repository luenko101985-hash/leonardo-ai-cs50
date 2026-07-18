import json
import re

import pytest

from ui import voice


@pytest.mark.parametrize(
    "value",
    [
        "ordinary text",
        "кириллица",
        "emoji 🚀",
        "single ' quote",
        'double " quote',
        "slash / and backslash \\",
        "line one\nline two\rline three",
        "tab\tvalue",
        "</script>",
        "<script>",
        "A&B",
        "<!-- comment -->",
        "left\u2028right",
        "left\u2029right",
        "",
        None,
    ],
)
def test_safe_js_literal_round_trips_without_html_sensitive_characters(value):
    literal = voice._to_safe_js_string(value)

    assert json.loads(literal) == str(value)
    assert "</script>" not in literal.lower()
    assert "<" not in literal
    assert ">" not in literal
    assert "&" not in literal
    assert "\u2028" not in literal
    assert "\u2029" not in literal


def _capture_speech_html(monkeypatch, text, lang="en-US"):
    captured = {}

    def capture(html, height):
        captured["html"] = html
        captured["height"] = height

    monkeypatch.setattr(voice.components, "html", capture)
    voice._speak(text, lang)
    return captured


@pytest.mark.parametrize(
    "payload",
    [
        "</script><script>alert(1)</script>",
        '"</script><img src=x onerror=alert(1)>',
        "<!-- </script> -->",
    ],
)
def test_payload_remains_inside_one_script_block(monkeypatch, payload):
    captured = _capture_speech_html(monkeypatch, payload)
    html = captured["html"]

    assert captured["height"] == 0
    assert html.count("<script>") == 1
    assert html.count("</script>") == 1
    assert "<img" not in html.lower()

    text_literal = re.search(r"const text = (.*);", html).group(1)
    assert json.loads(text_literal) == payload


def test_language_uses_the_same_safe_literal_path(monkeypatch):
    dangerous_language = '</script><script>alert("lang")</script>'
    captured = _capture_speech_html(
        monkeypatch,
        "safe text",
        lang=dangerous_language,
    )

    language_literal = re.search(
        r"utterance\.lang = (.*);",
        captured["html"],
    ).group(1)
    assert json.loads(language_literal) == dangerous_language
    assert "</script><script>" not in captured["html"]


def test_voice_parameters_and_cancel_speak_order_are_unchanged(monkeypatch):
    html = _capture_speech_html(monkeypatch, "voice test")["html"]

    assert "const utterance = new SpeechSynthesisUtterance(text);" in html
    assert "utterance.rate = 1.0;" in html
    assert "utterance.pitch = 1.0;" in html
    assert "utterance.volume" not in html
    assert html.index("window.speechSynthesis.cancel();") < html.index(
        "window.speechSynthesis.speak(utterance);"
    )
