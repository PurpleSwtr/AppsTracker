import threading
import time
import webview

from src.api import Api
from src.core.database import init_db, SessionLocal
from src.applications.services import ApplicationService
from src.tracking.manager import TrackerManager
from src.tracking.tracker import ProcessTracker
from src.config import config


def run_tracker():
    session = SessionLocal()
    try:
        app_service = ApplicationService(session)
        applications = app_service.repository.get_all()
        
        tracker_manager = TrackerManager()
        for app in applications:
            tracker = ProcessTracker(process_name=app.process_name, application_id=app.id)
            tracker_manager.add_application(tracker)

        while True:
            tracker_manager.update()
            time.sleep(config.CHECK_INTERVAL)
    except KeyboardInterrupt:
        pass
    finally:
        session.close()


def main():
    init_db()

    tracker_thread = threading.Thread(target=run_tracker, daemon=True)
    tracker_thread.start()

    FRONTEND_URL = "http://localhost:5173"
    
    # Когда сделаю билд
    # frontend_dist = Path(__file__).resolve().parent.parent / "frontend" / "dist"
    # FRONTEND_URL = str(frontend_dist / "index.html")
    api = Api()

    window = webview.create_window(
        title="AppsTracker",
        url=FRONTEND_URL,
        width=520,
        height=500,
        resizable=False,
        min_size=(520, 500),
        on_top=True,
        frameless=False,
        js_api=api
    )

    webview.start(debug=config.DEBUG_PYWEBVIEW_MODE)


if __name__ == "__main__":
    main()