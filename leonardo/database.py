import sqlite3


DB_NAME = "leonardo.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS concepts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            category TEXT,
            prompt TEXT,
            principle TEXT,
            modern_version TEXT,
            demand TEXT,
            roi TEXT,
            materials TEXT,
            use_cases TEXT,
            investor_summary TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def save_concept(
    title,
    category,
    prompt,
    principle,
    modern_version,
    demand,
    roi,
    materials,
    use_cases,
    investor_summary,
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO concepts (
            title, category, prompt, principle, modern_version,
            demand, roi, materials, use_cases, investor_summary
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        title,
        category,
        prompt,
        principle,
        modern_version,
        demand,
        roi,
        materials,
        use_cases,
        investor_summary,
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
        SELECT id, title, category, prompt, principle, modern_version,
               demand, roi, materials, use_cases, investor_summary, created_at
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