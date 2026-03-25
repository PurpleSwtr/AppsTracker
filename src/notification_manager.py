from WinToastCreator.creator import toast

def send_notification(title: str | None, message: str | None):
    toast(
        title, 
        message, 
        # image=r"C:\Users\User\Desktop\GameTracker\assets\info.svg",
        # button="Открыть папку",
        # on_click=lambda e: print("Клик по кнопке"),
        #     progress={
        #     'value': 0.3,
        #     'title': 'Прогресс',
        #     'status': '30 мин.'
        # },
        duration="short"
        )