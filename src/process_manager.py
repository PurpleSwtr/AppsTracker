import time
import psutil
import sys
from enum import auto, Enum
from src.core.database import SessionLocal
from src.notifications.notification_manager import send_notification

from src.config import config

from src.tracking.tracker import ProcessTracker
from src.tracking.manager import TrackerManager
from src.applications.services import ApplicationService

session = SessionLocal()

app_service = ApplicationService(session=session)

apps = app_service.get_all_applications()

tracker_manager = TrackerManager()

for app in apps:
    application = ProcessTracker(process_name=app)
    tracker_manager.add_application(application)

while True:
    tracker_manager.update()
    time.sleep(config.CHECK_INTERVAL)