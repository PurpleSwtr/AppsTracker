import psutil

from src.notification_manager import send_notification
from src.tracker import ProcessTracker
from datetime import datetime


class TrackerManager:
    def __init__(self) -> None:
        self.tracked_applications: list[ProcessTracker] = []

    def add_application(self, app: ProcessTracker):
        self.tracked_applications.append(app)
    
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
        for app in self.tracked_applications:
            if self.watch_process(app.process_name) is not None:
                if not app.start_notificated:
                    app.start_triger()
                    send_notification(title=app.name, message=f"Приложение запущено в {self.get_time()}")
            else:
                if app.start_notificated:
                    app.end_triger()
                    send_notification(title=app.name, message=f"Приложение закрыто в {self.get_time()}")
                    app.start_notificated = False
                    app.end_notificated = False
