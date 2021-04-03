import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URL, echo=settings.SQLALCHEMY_ECHO)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

metadados = sa.MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }
)

Base = declarative_base(metadata=metadados)


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
