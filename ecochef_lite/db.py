import sqlite3
import os

DB_FILE = "pantry.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT NOT NULL,
            quantity TEXT,
            days_until_expiry INTEGER,
            category TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_item(item_name, quantity, days_until_expiry, category):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO inventory (item_name, quantity, days_until_expiry, category) VALUES (?, ?, ?, ?)",
              (item_name, quantity, days_until_expiry, category))
    conn.commit()
    conn.close()

def get_all_items():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM inventory ORDER BY days_until_expiry ASC")
    items = c.fetchall()
    conn.close()
    return items

def delete_item(item_id):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("DELETE FROM inventory WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    # Example usage:
    # add_item("Avocado", "1", 2, "Fruit")
    # add_item("Pasta", "500g", 30, "Grain")
    # print(get_all_items())
