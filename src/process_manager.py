import time
import psutil
import sys
from enum import auto, Enum
from src.notification_manager import send_notification

from src.config import config

from src.tracker import ProcessTracker
from src.tracker_manager import TrackerManager

class ProcessStatus(Enum):
    NOT_RUNNING = auto(),
    RUNNING = auto(),
    CLOSED = auto(),


def check_process_exist(pid: int | None) -> bool:
    if not pid is None:
        return psutil.pid_exists(pid)
    else: return False

def watch_process(app_name: str) -> int | None:
    for p in psutil.process_iter(['name', 'pid']):
        if p.info['name'] == app_name:
            return p.info['pid']
    return None

def get_name_by_pid(pid: int) -> str | None:
    try:
        process = psutil.Process(pid)
        return process.name()
    except psutil.NoSuchProcess:
        return None
    except psutil.AccessDenied:
        return None


process_status = ProcessStatus.NOT_RUNNING
app_name = ''
pid = None

apps = ['obs64.exe', 'Godot 4.6.exe', 'qbittorrent.exe', 'Brotato.exe', '7 Billion Humans.exe', 'Cuphead.exe']

tracker_manager = TrackerManager()

for app in apps:
    application = ProcessTracker(process_name=app)
    tracker_manager.add_application(application)

while True:
    tracker_manager.update()
    time.sleep(config.CHECK_INTERVAL)


# while True:
#     match process_status:
#         case ProcessStatus.NOT_RUNNING:
#             for app in apps:
#                 pid = watch_process(app_name=app)
#                 if not pid is None:
#                     process_status = ProcessStatus.RUNNING
#                     app_name = get_name_by_pid(pid)
#                     send_notification(title=app_name, message=f"Приложение запущено в {get_time()}")
#         case ProcessStatus.RUNNING:
#             if not check_process_exist(pid):
#                 process_status = ProcessStatus.CLOSED
#                 send_notification(title=app_name, message=f"Приложение запущено в {get_time()}")
#         case ProcessStatus.CLOSED:
#             process_status = ProcessStatus.NOT_RUNNING
#             # sys.exit(0)
#     print(process_status)
#     time.sleep(config.CHECK_INTERVAL)
