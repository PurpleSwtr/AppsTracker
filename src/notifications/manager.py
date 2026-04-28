from WinToastCreator.creator import toast
from src.settings_manager import settings

from enum import Enum, auto

class Notification(Enum):
    DEFAULT = auto()
    PROGRESS = auto()
    ALERT = auto()
    TIMER = auto()
    CLOSE_ACTION = auto()

class NotificationManager():
    
    @staticmethod
    def send_notification(title: str | None, message: str | None):
        if settings.notifications:
            if settings.start_end_notification:
                toast(
                    title, 
                    message, 
                    duration="short"
                    )
    
    @staticmethod
    def progress_notification(title: str | None, message: str | None, progress: float):
        if settings.notifications:

            status = f'{int(progress * 100)} мин.'

            toast(
            title, 
            message, 
            # button="Открыть папку",
            # on_click=lambda e: print("Клик по кнопке"),
            progress={
                'value': progress,
                'title': 'Прогресс',
                'status': status
            },
            duration="short"
            )