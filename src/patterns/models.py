
from datetime import datetime

from sqlalchemy import Boolean, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.database import Base


class Pattern(Base):
    __tablename__ = "patterns"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    notification_interval: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    title: Mapped[str] = mapped_column(String(20), nullable=False)
    message: Mapped[str] = mapped_column(String(100), nullable=False)
    repeat: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    applications = relationship("Application", secondary="application_patterns", back_populates="patterns")