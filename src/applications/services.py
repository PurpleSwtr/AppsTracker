from pathlib import Path

from sqlalchemy.orm import Session
from src.applications.repository import ApplicationRepository
from src.models import Application, AppSession
from src.utils.iconextract import save_icon
from src.config import config

class ApplicationService:
    def __init__(self, session: Session):
        self.repository = ApplicationRepository(session)
        self.session = session
    
    @staticmethod
    def _get_process_name(link: str) -> str:
        link = link.strip('"').strip("'")
        return Path(link).name

    def get_all_applications_names(self) -> list[str]:
        apps = self.repository.get_all()
        apps_names = []
        for app in apps:
            apps_names.append(app.process_name)
        return apps_names

    def get_or_create_application(self, process_name: str) -> Application:
        app = self.repository.get_by_process_name(process_name)
        if not app:
            app = self.repository.create_from_process(process_name)
        return app

    def start_session(self, process_name: str) -> AppSession:
        app = self.get_or_create_application(process_name)
        return self.repository.add_session(app.id)

    def end_session(self, app_session_id: int) -> None:
        session_obj = self.session.get(AppSession, app_session_id)
        if session_obj:
            from datetime import datetime
            session_obj.end_time = datetime.now()
            self.session.commit()
    
    def add_application(self, application_path: str):
        process_name = self._get_process_name(application_path)
        self.repository.save_application_to_db(process_name)
        save_icon(Path(application_path), config.ICONS_PATH)