from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from src.config import config

config.DATA_DIR.mkdir(exist_ok=True)

class Base(DeclarativeBase):
    pass

engine = create_engine(
    f"sqlite:///{config.DB_PATH}",
    echo=config.SQLALCHEMY_ECHO,
)

def init_db() -> None:
    Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)