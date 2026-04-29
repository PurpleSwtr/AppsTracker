import psutil

from datetime import datetime
from src.applications.services import ApplicationService
from src.core.database import SessionLocal
from src.notifications.manager import NotificationManager
from src.tracking.tracker import ProcessTracker
from src.session_rules.service import SessionRulesService

class TrackerManager:
    def __init__(self) -> None:
        self.tracked_applications: list[ProcessTracker] = []
        self.notification_manager: NotificationManager = NotificationManager()
        self.rules_service: SessionRulesService = SessionRulesService()

    def add_application(self, app: ProcessTracker):
        self.tracked_applications.append(app)
    
    @staticmethod
    def check_process_exist(pid: int | None) -> bool:
        if not pid is None:
            return psutil.pid_exists(pid)
        else: return False

    @staticmethod
    def get_name_by_pid(pid: int) -> str | None:
        try:
            process = psutil.Process(pid)
            return process.name()
        except psutil.NoSuchProcess:
            return None
        except psutil.AccessDenied:
            return None

    @staticmethod
    def get_time() -> str:
        now = datetime.now()
        return now.strftime("%H:%M:%S")
    
    @staticmethod
    def watch_process(app_name: str) -> int | None:
        for p in psutil.process_iter(['name', 'pid']):
            if p.info['name'] == app_name:
                return p.info['pid']
        return None

    def update(self):


        session = SessionLocal()
        try:
            app_service = ApplicationService(session)
            rules_service = SessionRulesService()

            for app in self.tracked_applications[:]:
                pid = self.watch_process(app.process_name)
                if pid is not None:
                    if not app.start_notificated:
                        app.start_triger()
                        app.end_notificated = False
                        self.notification_manager.send_notification(title=app.name, message=f"Приложение запущено в {self.get_time()}")
                        cur_session = app_service.start_session(app.process_name)
                        app.current_session_id = cur_session.id
                        self.rules_service.start_session(
                            session=session,
                            session_id=cur_session.id,
                            app_id=app.application_id,
                            process_name=app.process_name,
                            start_time=datetime.now()
                        )
                    else:
                        if app.current_session_id != -1:
                            rules_service.update_session(app.current_session_id, datetime.now())
                else:
                    if app.start_notificated:
                        app.end_triger()
                        app.start_notificated = False
                        self.notification_manager.send_notification(title=app.name, message=f"Приложение закрыто в {self.get_time()}")
                        if app.current_session_id != -1:
                            app_service.end_session(app_session_id=app.current_session_id)
                            rules_service.end_session(app.current_session_id)
                        app.current_session_id = -1
        finally:
            session.close()