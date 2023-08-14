from sqlalchemy import create_engine
from sqlalchemy.orm.decl_api import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg://postgres:root@localhost/fastapi_course"

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
