import sqlite3
from datetime import datetime
from typing import List
from tracker.types import ProductData, ProductHistory, Source

# TODO: Make this configurable
DB_FILE = "products.db"


def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    # Create the products table
    c.execute(
        """
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
    """
    )

    # Create indexes on url and title
    c.execute("CREATE INDEX IF NOT EXISTS idx_products_url ON products (url)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_products_title ON products (title)")

    conn.commit()
    conn.close()


# TODO: Remove query string from URL before saving
def save_product_data(product: ProductData):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    c.execute(
        """
        INSERT INTO products (url, title, amount, currency, rating, source, timestamp)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """,
        (
            product["url"],
            product["title"],
            float(product["amount"]) if product["amount"] else None,
            product["currency"],
            float(product["rating"]) if product["rating"] else None,
            int(product["source"].value),
            datetime.now().isoformat(),
        ),
    )

    conn.commit()
    conn.close()


def get_product_history(url: str) -> List[ProductHistory]:
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    c.execute(
        """
        SELECT title, amount, currency, rating, source, timestamp
        FROM products
        WHERE url = ?
        ORDER BY timestamp ASC
    """,
        (url,),
    )

    rows = c.fetchall()
    conn.close()

    return [
        ProductHistory(
            id=row[0],
            # url=url,
            title=row[0],
            amount=float(row[1]),
            currency=row[2],
            rating=float(row[3]),
            source=Source(row[4]),
            timestamp=row[5],
        )
        for row in rows
    ]
