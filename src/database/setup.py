from sqlalchemy import create_engine
from contextlib import contextmanager
from src.database.base import Base
from sqlalchemy.orm import Session
from config import app_config

engine = create_engine(app_config.database_url, echo=True)


def create_tables():
    Base.metadata.create_all(engine)


def get_session():
    try:
        with Session(engine) as session:
            yield session
    except Exception:
        session.rollback()
        raise
    finally:
        session.commit()
