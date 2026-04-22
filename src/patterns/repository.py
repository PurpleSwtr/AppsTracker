from sqlalchemy.orm import Session
from sqlalchemy import select
from src.models import Pattern, ApplicationPattern

class PatternRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_patterns_for_application(self, app_id: int) -> list[Pattern]:
        stmt = select(Pattern).join(ApplicationPattern).where(
            ApplicationPattern.application_id == app_id,
            ApplicationPattern.enabled == True
        )
        return list(self.session.execute(stmt).scalars().all())