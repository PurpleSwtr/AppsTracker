from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base

class Application(Base):
    __tablename__ = "applications"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    process_name: Mapped[str] = mapped_column(String(100), nullable=False)

    def __repr__(self) -> str:
        return f"<User(id={self.id}, name='{self.name}')>"