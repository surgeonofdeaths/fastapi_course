from sqlalchemy import create_engine
from sqlalchemy.orm.decl_api import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import get_settings

settings = get_settings()

SQLALCHEMY_DATABASE_URL = (
    f"postgresql+psycopg://{settings.DB_USERNAME}:"
    f"{settings.DB_PASSWORD}@{settings.DB_HOSTNAME}:"
    f"{settings.DB_PORT}/{settings.DB_NAME}"
)
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine, autoflush=False)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
