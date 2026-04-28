from sqlalchemy import func, select
from src.models import Application, AppSession
from src.core.repository import BaseRepository
from sqlalchemy.orm import Session
from sqlalchemy import case

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
    
    def save_application_to_db(self, process_name: str) -> None:
        app_name = process_name.replace(".exe", "")
        app = Application(name=app_name, process_name=process_name)
        self.session.add(app)
        self.session.commit()
    
    def stats_per_day(self):
        ...
    
    def stats_all_time(self, name: str | None = None):
    
        duration_min = (
            func.coalesce(func.julianday(AppSession.end_time), func.julianday(func.now()))
            - func.julianday(AppSession.start_time)
        ) * 24 * 60

        safe_duration = case(
            (duration_min < 0, 0),
            else_=duration_min
        )

        stmt = (
            select(
                Application.name,
                func.sum(safe_duration).label("total_time")
            )
            .join(AppSession, Application.id == AppSession.application_id)
            .group_by(Application.id, Application.name)
        )

        if name:
            stmt = stmt.where(func.lower(Application.name) == func.lower(name))

        stmt = stmt.order_by(
            func.sum(safe_duration).desc()
        )

        result = self.session.execute(stmt)
        
        return [
            {"name": row.name, "total_time": round(row.total_time or 0, 1)}
            for row in result.mappings()
        ]