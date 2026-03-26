from sqlalchemy import func, select
from src.applications.models import Application, AppSession
from src.core.repository import BaseRepository
from sqlalchemy.orm import Session

class ApplicationRepository(BaseRepository[Application]):
    def __init__(self, session: Session):
        super().__init__(session, Application)

    def get_by_name(self, name: str) -> Application | None:
        stmt = select(Application).where(func.lower(Application.name) == func.lower(name))
        return self.session.execute(stmt).scalar_one_or_none()

    def get_by_process_name(self, process_name: str) -> Application | None:
        stmt = select(Application).where(Application.process_name == process_name)
        return self.session.execute(stmt).scalar_one_or_none()

    def create_from_process(self, process_name: str) -> Application:
        app_name = process_name.replace(".exe", "")
        return self.create(name=app_name, process_name=process_name)

    def add_session(self, application_id: int) -> AppSession:
        from datetime import datetime
        session_obj = AppSession(
            application_id=application_id,
            start_time=datetime.now()
        )
        self.session.add(session_obj)
        self.session.commit()
        return session_obj