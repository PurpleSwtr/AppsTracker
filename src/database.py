from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

class Base(DeclarativeBase):
    pass

engine = create_engine(
    "sqlite:///instance/data.db",
    echo=True,
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)