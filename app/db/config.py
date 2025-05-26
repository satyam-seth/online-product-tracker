from pathlib import Path

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

# TODO: in future add support for other databases (MySQL, PostgreSQL etc)

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DB_PATH = BASE_DIR / "sqlite.db"

DATABASE_URL = f"sqlite+aiosqlite:///{DB_PATH}"

engine = create_async_engine(DATABASE_URL, echo=True)

async_session = async_sessionmaker(bind=engine, expire_on_commit=False)
