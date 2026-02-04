"""Module création et gestion de la DB"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session, Generator

# SQLite local file. In CI, you can swap to Postgres later.
DATABASE_URL = "sqlite:///./taskmanager.db"

engine = create_engine(
    DATABASE_URL,
    # needed for SQLite + threads
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    """ Classe base non utilisée """
    pass


def get_db() -> Generator[Session, None, None]:
    """ Crée la db et gère proprement sa fermeture """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
