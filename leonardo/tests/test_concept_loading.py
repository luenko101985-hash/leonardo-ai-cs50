import copy
import json

import pytest

import database
from application.concepts import ConceptLoadError, load_concept
from services.concept_schema import ConceptData


def _save_concept(concept):
    return database.save_concept(
        title="Stored test concept",
        category="robotics",
        prompt="test prompt",
        concept_data=concept,
    )


def test_valid_concept_loads_with_full_contract(temporary_database, valid_concept):
    concept_id = _save_concept(valid_concept)

    loaded = load_concept(concept_id)

    assert loaded == valid_concept
    assert len(loaded) == 27
    assert set(loaded) == set(ConceptData.model_fields)


def test_nested_optional_defaults_are_filled(temporary_database, valid_concept):
    concept = copy.deepcopy(valid_concept)
    concept["implementation_roadmap"] = {}
    concept["implementation_guides"] = {}
    concept_id = _save_concept(concept)

    loaded = load_concept(concept_id)

    assert loaded["implementation_roadmap"] == {
        "prototype": "",
        "mvp": "",
        "pilot": "",
        "production": "",
    }
    assert set(loaded["implementation_guides"]) == {
        "prototype",
        "mvp",
        "pilot",
        "production",
    }
    assert loaded["implementation_guides"]["prototype"]["execution_plan"]["steps"] == []


def test_missing_record_returns_none(temporary_database):
    assert load_concept(999_999) is None


@pytest.mark.parametrize(
    "mutation",
    [
        lambda concept: concept.pop("title"),
        lambda concept: concept.__setitem__("title", ["wrong type"]),
        lambda concept: concept.__setitem__("title", "   "),
    ],
    ids=["missing-required-field", "wrong-type", "empty-required-string"],
)
def test_invalid_required_data_raises_concept_load_error(
    temporary_database,
    valid_concept,
    mutation,
):
    concept = copy.deepcopy(valid_concept)
    mutation(concept)
    concept_id = _save_concept(concept)

    with pytest.raises(ConceptLoadError):
        load_concept(concept_id)


@pytest.mark.parametrize(
    "raw_json",
    [
        "{malformed-json",
        "null",
        "[]",
    ],
    ids=["malformed-json", "null", "list"],
)
def test_invalid_json_shapes_raise_concept_load_error(insert_raw_concept, raw_json):
    concept_id = insert_raw_concept(raw_json)

    with pytest.raises(ConceptLoadError):
        load_concept(concept_id)


def test_extra_fields_follow_ignore_policy(temporary_database, valid_concept):
    concept = copy.deepcopy(valid_concept)
    concept["unexpected_extra_field"] = "ignored"
    concept_id = _save_concept(concept)

    loaded = load_concept(concept_id)

    assert "unexpected_extra_field" not in loaded
    assert set(loaded) == set(ConceptData.model_fields)


def test_load_error_does_not_leak_raw_payload_sql_or_prompt(insert_raw_concept):
    secret = "SUPER_SECRET_PROMPT SELECT * FROM concepts"
    concept_id = insert_raw_concept(
        json.dumps({"title": secret}),
        prompt=secret,
    )

    with pytest.raises(ConceptLoadError) as exc_info:
        load_concept(concept_id)

    message = str(exc_info.value)
    assert secret not in message
    assert "SELECT" not in message
    assert "concepts" not in message
    assert "{" not in message
