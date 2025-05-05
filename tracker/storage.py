import sqlite3
from datetime import datetime
from typing import List, Dict
from tracker.types import ProductData

# TODO: Make this configurable
DB_FILE = "products.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    # Create the products table
    c.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL,
            title TEXT,
            amount REAL,
            currency TEXT,
            rating REAL,
            source INTEGER NOT NULL,
            timestamp TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Create indexes on url and title
    c.execute("CREATE INDEX IF NOT EXISTS idx_products_url ON products (url)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_products_title ON products (title)")

    conn.commit()
    conn.close()

def save_product_data(product: ProductData):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    c.execute("""
        INSERT INTO products (url, title, amount, currency, rating, source, timestamp)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        product["url"],
        product["title"],
        float(product["amount"]),
        product["currency"],
        float(product["rating"]),
        int(product["source"].value),
        datetime.now().isoformat()
    ))

    conn.commit()
    conn.close()
