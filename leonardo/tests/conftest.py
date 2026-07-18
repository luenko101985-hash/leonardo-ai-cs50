import base64
import socket

import pytest

import database
from services.concept_schema import validate_concept_data
from services.fallback_service import build_fallback_concept


@pytest.fixture(autouse=True)
def block_network_connections(monkeypatch):
    def blocked_connection(*args, **kwargs):
        raise AssertionError("Network access is forbidden in the regression test suite")

    monkeypatch.setattr(socket, "create_connection", blocked_connection)


@pytest.fixture
def valid_concept():
    return validate_concept_data(
        build_fallback_concept(
            category="robotics",
            prompt_text="умная кормушка для домашних животных",
            creativity_mode="Bold",
            audience="Small business owners",
        )
    )


@pytest.fixture
def temporary_database(tmp_path, monkeypatch):
    database_path = tmp_path / "test-leonardo.db"
    monkeypatch.setattr(database, "DB_PATH", database_path)
    database.init_db()
    return database_path


@pytest.fixture
def insert_raw_concept(temporary_database):
    def insert(concept_json, prompt="test prompt"):
        connection = database.get_connection()
        try:
            cursor = connection.execute(
                """
                INSERT INTO concepts (title, category, prompt, concept_json)
                VALUES (?, ?, ?, ?)
                """,
                ("Stored test concept", "robotics", prompt, concept_json),
            )
            connection.commit()
            return cursor.lastrowid
        finally:
            connection.close()

    return insert


@pytest.fixture
def png_bytes():
    return base64.b64decode(
        "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII="
    )


@pytest.fixture
def saved_images(png_bytes):
    return [
        (1, "leonardo", "Renaissance sketch", png_bytes, "test-date", 0),
        (2, "blueprint", "Modern blueprint", png_bytes, "test-date", 0),
    ]
