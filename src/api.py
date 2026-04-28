import webview

from src.applications.services import ApplicationService
from src.core.database import SessionLocal
from src.settings_manager import settings

class Api:
    def set_notifications(self, enabled: bool):
        settings.notifications = enabled

    def set_start_end_notifications(self, enabled: bool):
        settings.start_end_notification = enabled

    def get_all_applications(self):
        session = SessionLocal()
        try:
            app_service = ApplicationService(session)
            apps = app_service.repository.get_all()
            
            return [
                {
                    "id": app.id,
                    "title": app.name,
                    "process_name": app.process_name,
                    "icon": f"/icons/{app.name}.ico",
                    "value": int(app.total_time)
                }
                for app in apps
            ]
        finally:
            session.close()

    def open_file_dialog(self):
        result = webview.windows[0].create_file_dialog(
            dialog_type=webview.FileDialog.OPEN,
            allow_multiple=False,
            file_types=['Executables (*.exe)']
        )
        return list(result) if result else []


    def add_new_application(self, application_path):
        session = SessionLocal()
        try:
            app_service = ApplicationService(session)
            app_service.add_application(application_path=application_path)
        finally:
            session.close()