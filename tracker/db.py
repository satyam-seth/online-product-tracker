import sqlite3
from datetime import datetime
from typing import List
from tracker.types import ProductData, ProductHistory, SourceConfig

# TODO: Make this configurable
DB_FILE = "products.db"


# TODO: in feature use SQLAlchemy
def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    # TODO: Add created_on and updated_on field
    # create source config table
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS sources (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        domain TEXT NOT NULL UNIQUE,
        title_selector TEXT NOT NULL,
        price_selector TEXT NOT NULL,
        rating_selector TEXT NOT NULL
        );
    """
    )

    # Create indexes on domain and url
    c.execute("CREATE INDEX IF NOT EXISTS idx_sources_domain ON sources (domain);")
    c.execute("CREATE INDEX IF NOT EXISTS idx_sources_name ON sources (name);")

    # TODO: source must be one to many field with on delete cascade
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
        );
    """
    )

    # Create indexes on url and title
    c.execute("CREATE INDEX IF NOT EXISTS idx_products_url ON products (url)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_products_title ON products (title)")

    conn.commit()
    conn.close()


def get_source_config(domain):
    # Connect to the database
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    # Query the sources table to get the configuration
    c.execute(
        """
        SELECT id, name, domain, title_selector, price_selector, rating_selector
        FROM sources
        WHERE domain = ?
        LIMIT 1;
    """,
        (domain,),
    )

    # Fetch the result
    source_config = c.fetchone()
    conn.close()

    if source_config:
        return SourceConfig(
            id=source_config[0],
            name=source_config[1],
            domain=source_config[2],
            title_selector=source_config[3],
            price_selector=source_config[4],
            rating_selector=source_config[5],
        )

    print(f"Source with name {domain} not found.")
    return None


# TODO: Remove query string from URL before saving
def save_product_data(product: ProductData):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    c.execute(
        """
        INSERT INTO products (url, title, amount, currency, rating, source, timestamp)
        VALUES (?, ?, ?, ?, ?, ?, ?);
    """,
        (
            product["url"],
            product["title"],
            float(product["amount"]) if product["amount"] else None,
            product["currency"],
            float(product["rating"]) if product["rating"] else None,
            product["source"],
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
        ORDER BY timestamp ASC;
    """,
        (url,),
    )

    rows = c.fetchall()
    conn.close()

    return [
        ProductHistory(
            id=row[0],
            url=url,
            title=row[0],
            amount=float(row[1]),
            currency=row[2],
            rating=float(row[3]),
            source=row[4],
            timestamp=row[5],
        )
        for row in rows
    ]
