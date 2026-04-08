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
            title TEXT NOT NULL,
            category TEXT NOT NULL,
            prompt TEXT,
            principle TEXT,
            modern_version TEXT,
            demand TEXT,
            roi TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def save_concept(title, category, prompt, principle, modern_version, demand, roi):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO concepts (title, category, prompt, principle, modern_version, demand, roi)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (title, category, prompt, principle, modern_version, demand, roi))

    conn.commit()
    conn.close()


def get_concepts(limit=10):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT title, category, created_at
        FROM concepts
        ORDER BY created_at DESC
        LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()
    conn.close()

    return rows