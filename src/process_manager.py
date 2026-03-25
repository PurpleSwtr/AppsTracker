import time
import psutil
import sys
from enum import auto, Enum
from src.notification_manager import send_notification

from src.config import config
from datetime import datetime

def get_time() -> str:
    now = datetime.now()
    return now.strftime("%H:%M:%S")


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

while process_status != ProcessStatus.CLOSED:
    pid = watch_process(app_name='Godot 4.exe')
    match process_status:
        case ProcessStatus.NOT_RUNNING:
            if not pid is None:
                process_status = ProcessStatus.RUNNING
                app_name = get_name_by_pid(pid)
                send_notification(title=app_name, message=f"Приложение запущено в {get_time()}")
        case ProcessStatus.RUNNING:
            if not check_process_exist(pid):
                process_status = ProcessStatus.CLOSED
                send_notification(title=app_name, message=f"Приложение запущено в {get_time()}")
        case ProcessStatus.CLOSED:
            sys.exit(0)
    print(process_status)
    time.sleep(config.CHECK_INTERVAL)
