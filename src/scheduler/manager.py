import schedule
import threading
import time

from src.models import Pattern
from src.notifications.manager import  send_notification, progress_notification

class SchedulerManager():
    def __init__(self, pattern: Pattern) -> None:
        self.time_limit = pattern.time_limit

        self.notification_interval = pattern.notification_interval
        self.close_interval = pattern.close_interval
        
        self.repeat = pattern.repeat
        self.close = pattern.close

        self.title = pattern.title
        self.message = pattern.message


    def set_notification(self):
        schedule.every(self.notification_interval).minutes.do(...)
    
    def set_closing(self):
        ...

    def run_notification(self):
        ...

    def run_closing(self):
        ...
    
    def get_process_value(self, current_time):
        return float(self.time_limit - current_time * 60)