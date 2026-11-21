import sqlite3
from app.parser import parse_file
from app.incident_rules import find_incidents

DB_PATH = "sentinel.db"


def get_connection() -> sqlite3.Connection:
    return sqlite3.connect(DB_PATH)

def init_db() -> None:
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            severity TEXT,
            service TEXT,
            message TEXT
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            service TEXT,
            error_count INTEGER,
            detected_at TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_log(entry: dict) -> None:
    conn = get_connection()
    conn.execute(
        "INSERT INTO logs (timestamp, severity, service, message) VALUES (?, ?, ?, ?)",
        (entry["timestamp"], entry["severity"], entry["service"], entry["message"]),
    )
    conn.commit()
    conn.close()


def save_incident(incident: dict) -> None:
    conn = get_connection()
    conn.execute(
        "INSERT INTO incidents (service, error_count, detected_at) VALUES (?, ?, ?)",
        (incident["service"], incident["error_count"], incident["detected_at"]),
    )
    conn.commit()
    conn.close()

def get_logs(limit: int = 100) -> list[dict]:
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        "SELECT timestamp, severity, service, message FROM logs ORDER BY id DESC LIMIT ?",
        (limit,),
    ).fetchall()
    conn.close()
    return [dict(row) for row in rows]

def get_incidents() -> list[dict]:
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        "SELECT service, error_count, detected_at FROM incidents ORDER BY id DESC"
    ).fetchall()
    conn.close()
    return [dict(row) for row in rows]

if __name__ == "__main__":
    init_db()

    entries = parse_file()
    for entry in entries:
        save_log(entry)

    incidents = find_incidents(entries)
    for incident in incidents:
        save_incident(incident)

    print(f"Saved {len(entries)} logs and {len(incidents)} incidents to {DB_PATH}")