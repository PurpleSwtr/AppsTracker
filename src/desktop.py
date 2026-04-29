import threading
import webview
from datetime import datetime
from sqlalchemy import update
from src.api import Api
from src.core.database import init_db, SessionLocal
from src.applications.services import ApplicationService
from src.models import AppSession
from src.tracking.manager import TrackerManager
from src.tracking.tracker import ProcessTracker
from src.config import config

_tracker_running = threading.Event()
_tracker_running.set()

def run_tracker():
    session = SessionLocal()
    try:
        app_service = ApplicationService(session)
        
        from sqlalchemy import update
        from src.models import AppSession
        from datetime import datetime
        
        session.execute(
            update(AppSession)
            .where(AppSession.end_time == None)
            .values(end_time=datetime.now())
        )
        session.commit()
        
        applications = app_service.repository.get_all()
        
        tracker_manager = TrackerManager()
        for app in applications:
            tracker = ProcessTracker(process_name=app.process_name, application_id=app.id)
            tracker_manager.add_application(tracker)

        while _tracker_running.is_set():
            tracker_manager.update()
            _tracker_running.wait(config.CHECK_INTERVAL)
    except KeyboardInterrupt:
        pass
    finally:
        session.close()

def on_closing():
    _tracker_running.clear()

    session = SessionLocal()
    try:
        stmt = (
            update(AppSession)
            .where(AppSession.end_time == None)
            .values(end_time=datetime.now())
        )
        session.execute(stmt)
        session.commit()
    except Exception as e:
        print(e)
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

    if window is None:
        raise RuntimeError("Ошибка создания окна")

    window.events.closing += on_closing
    webview.start(debug=config.DEBUG_PYWEBVIEW_MODE)


if __name__ == "__main__":
    main()