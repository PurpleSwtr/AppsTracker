from sqlalchemy import Float, ForeignKey, String, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.core.database import Base
from datetime import datetime

class Application(Base):
    __tablename__ = "applications"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    process_name: Mapped[str] = mapped_column(String(100), nullable=False)
    total_time: Mapped[float] = mapped_column(Float(10), nullable=False, default=0.0)

    sessions = relationship("AppSession", back_populates="application")
    patterns = relationship("Pattern", secondary="application_patterns", back_populates="applications")

class AppSession(Base):
    __tablename__ = "apps_sessions"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    application_id: Mapped[int] = mapped_column(ForeignKey('applications.id'))
    process_id: Mapped[int] = mapped_column(nullable=True)
    start_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    end_time: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    application = relationship("Application", back_populates="sessions")