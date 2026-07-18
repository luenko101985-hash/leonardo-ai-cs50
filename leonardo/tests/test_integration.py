import json

import pytest

import database
from application.concepts import ConceptLoadError, load_concept
from pdf_export import export_project_plan_pdf
from services.concept_schema import validate_concept_data
from services.fallback_service import build_fallback_concept


def _fallback_concept():
    return build_fallback_concept(
        category="robotics",
        prompt_text="сервис прогнозирования спроса для магазина",
        creativity_mode="Experimental",
        audience="Small business owners",
    )


def test_fallback_validate_save_load_validate(temporary_database):
    generated = validate_concept_data(_fallback_concept())
    concept_id = database.save_concept(
        title=generated["title"],
        category="robotics",
        prompt="сервис прогнозирования спроса для магазина",
        concept_data=generated,
    )

    loaded = load_concept(concept_id)

    assert loaded == generated
    assert validate_concept_data(loaded) == loaded


def test_fallback_exports_through_pdf_bytes_pipeline():
    concept = validate_concept_data(_fallback_concept())

    pdf_bytes = export_project_plan_pdf(concept)

    assert isinstance(pdf_bytes, bytes)
    assert pdf_bytes.startswith(b"%PDF")
    assert len(pdf_bytes) > 100


def test_malformed_stored_concept_raises_without_raw_payload_leak(insert_raw_concept):
    raw_payload = "RAW_PRIVATE_PROMPT SELECT secret FROM concepts"
    concept_id = insert_raw_concept(
        json.dumps({"title": raw_payload}),
        prompt=raw_payload,
    )

    with pytest.raises(ConceptLoadError) as exc_info:
        load_concept(concept_id)

    message = str(exc_info.value)
    assert raw_payload not in message
    assert "SELECT" not in message
    assert "{" not in message
