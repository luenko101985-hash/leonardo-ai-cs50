import pytest
from project import validate_category, generate_invention, format_invention


def test_validate_category_valid():
    assert validate_category("flight") is True
    assert validate_category("water") is True
    assert validate_category("war") is True
    assert validate_category("transport") is True


def test_validate_category_invalid():
    assert validate_category("music") is False
    assert validate_category("") is False
    assert validate_category("Flight") is False


def test_generate_invention_valid():
    invention = generate_invention("flight")
    assert isinstance(invention, dict)
    assert "title" in invention
    assert "principle" in invention
    assert "modern_version" in invention
    assert "demand" in invention
    assert "roi" in invention


def test_generate_invention_invalid():
    with pytest.raises(ValueError):
        generate_invention("invalid")


def test_format_invention():
    invention = {
        "title": "Test Machine",
        "principle": "Test principle",
        "modern_version": "Test modern version",
        "demand": "Test demand",
        "roi": "Test ROI"
    }

    formatted = format_invention(invention)

    assert "Title: Test Machine" in formatted
    assert "Principle: Test principle" in formatted
    assert "Modern Version: Test modern version" in formatted
    assert "Market Demand: Test demand" in formatted
    assert "ROI Analysis: Test ROI" in formatted