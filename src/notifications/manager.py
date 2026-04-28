from WinToastCreator.creator import toast
from src.settings_manager import settings

def send_notification(title: str | None, message: str | None):
    if settings.notifications:
        toast(
            title, 
            message, 
            duration="short"
            )
    
def progress_notification(title: str | None, message: str | None, progress: float):
        
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