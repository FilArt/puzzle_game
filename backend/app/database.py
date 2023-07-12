from sqlalchemy import create_engine
from sqlmodel import Session, SQLModel

from .settings import settings


def create_engine_and_db():
    engine = create_engine(url=settings.DATABASE_URL, echo=settings.DEBUG)
    SQLModel.metadata.create_all(bind=engine)


def get_session():
    engine = create_engine(url=settings.DATABASE_URL, echo=settings.DEBUG)
    with Session(engine) as session:
        yield session
