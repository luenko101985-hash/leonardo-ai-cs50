from pathlib import Path

import pytest

import application.project_export as project_export
import pdf_export
from ui.concept_page import _safe_pdf_filename


def _assert_pdf_bytes(value):
    assert isinstance(value, bytes)
    assert value.startswith(b"%PDF")
    assert len(value) > 100


def test_pdf_export_without_images_returns_bytes(valid_concept):
    _assert_pdf_bytes(pdf_export.export_project_plan_pdf(valid_concept))


def test_pdf_export_with_images_returns_bytes(valid_concept, saved_images):
    _assert_pdf_bytes(
        pdf_export.export_project_plan_pdf(
            valid_concept,
            saved_images=saved_images,
        )
    )


def test_repeated_pdf_exports_are_independent_and_leave_no_files(
    valid_concept,
    tmp_path,
    monkeypatch,
):
    monkeypatch.chdir(tmp_path)
    before = set(tmp_path.iterdir())

    first = pdf_export.export_project_plan_pdf(valid_concept)
    first_signature = first[:8]
    second = pdf_export.export_project_plan_pdf(valid_concept)

    _assert_pdf_bytes(first)
    _assert_pdf_bytes(second)
    assert first is not second
    assert first[:8] == first_signature
    assert set(tmp_path.iterdir()) == before


def test_pdf_export_exception_leaves_no_temporary_files(
    valid_concept,
    tmp_path,
    monkeypatch,
):
    monkeypatch.chdir(tmp_path)
    before = set(tmp_path.iterdir())

    def fail_export(*args, **kwargs):
        raise RuntimeError("mock PDF failure")

    monkeypatch.setattr(pdf_export, "_write_project_plan_pdf", fail_export)

    with pytest.raises(RuntimeError, match="mock PDF failure"):
        pdf_export.export_project_plan_pdf(valid_concept)

    assert set(tmp_path.iterdir()) == before


def test_application_project_export_returns_bytes(valid_concept, monkeypatch):
    monkeypatch.setattr(
        project_export,
        "list_concept_images",
        lambda concept_id: [],
    )

    result = project_export.export_project_package(valid_concept, concept_id=42)

    _assert_pdf_bytes(result)


@pytest.mark.parametrize(
    ("title", "expected"),
    [
        ("Ordinary Project", "Ordinary_Project.pdf"),
        ("folder/name\\draft", "folder_name_draft.pdf"),
        ("../secret", "secret.pdf"),
        ("..", "leonardo_project.pdf"),
        ("", "leonardo_project.pdf"),
        ("safe\x00name\n", "safename.pdf"),
        ("Проект Леонардо", "Проект_Леонардо.pdf"),
    ],
)
def test_safe_pdf_filename(title, expected):
    assert _safe_pdf_filename(title) == expected


def test_safe_pdf_filename_limits_long_names():
    result = _safe_pdf_filename("a" * 250)

    assert result == f"{'a' * 100}.pdf"
    assert len(Path(result).stem) == 100
