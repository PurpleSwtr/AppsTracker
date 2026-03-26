from sqlalchemy import Float, ForeignKey, String, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.core.database import Base

class ApplicationPattern(Base):
    __tablename__ = "application_patterns"

    id: Mapped[int] = mapped_column(primary_key=True)
    application_id: Mapped[int] = mapped_column(ForeignKey("applications.id"))
    pattern_id: Mapped[int] = mapped_column(ForeignKey("patterns.id"))
    enabled: Mapped[bool] = mapped_column(default=True)