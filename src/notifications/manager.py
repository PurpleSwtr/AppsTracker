from WinToastCreator.creator import toast


def send_notification(title: str | None, message: str | None):
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