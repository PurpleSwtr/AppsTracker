import time
import psutil
import sys
from enum import auto, Enum
from src.core.database import SessionLocal
from src.notifications.manager import send_notification

from src.config import config

from src.tracking.tracker import ProcessTracker
from src.tracking.manager import TrackerManager
from src.applications.services import ApplicationService

session = SessionLocal()

app_service = ApplicationService(session=session)

applications = app_service.repository.get_all()
tracker_manager = TrackerManager()
for app in applications:
    tracker = ProcessTracker(process_name=app.process_name, application_id=app.id)
    tracker_manager.add_application(tracker)

while True:
    tracker_manager.update()
    time.sleep(config.CHECK_INTERVAL)