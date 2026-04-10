import sqlite3
import json


DB_NAME = "leonardo.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS concepts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            category TEXT NOT NULL,
            prompt TEXT,
            concept_json TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def save_concept(title, category, prompt, concept_data):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO concepts (
            title, category, prompt, concept_json
        )
        VALUES (?, ?, ?, ?)
    """, (
        title,
        category,
        prompt,
        json.dumps(concept_data, ensure_ascii=False),
    ))

    conn.commit()
    conn.close()


def get_concepts(limit=10):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, title, category, created_at
        FROM concepts
        ORDER BY created_at DESC
        LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()
    conn.close()
    return rows


def get_concept_by_id(concept_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, title, category, prompt, concept_json, created_at
        FROM concepts
        WHERE id = ?
    """, (concept_id,))

    row = cursor.fetchone()
    conn.close()
    return row


def delete_concept(concept_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM concepts WHERE id = ?", (concept_id,))

    conn.commit()
    conn.close()

def get_concept_by_id(concept_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT concept_json FROM concepts WHERE id = ?",
        (concept_id,)
    )

    row = cursor.fetchone()
    conn.close()

    if row:
        import json
        return json.loads(row[0])

    return None