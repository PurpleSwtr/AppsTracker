import json
import os

from src.config import config

default_settings = {
    "notifications": True,
    "start_end_notification": True
}

def load_settings():
    if not os.path.exists(config.SETTINGS_FILE):
        save_settings(default_settings)
        return default_settings
    
    with open(config.SETTINGS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_settings(settings):
    with open(config.SETTINGS_FILE, 'w', encoding='utf-8') as f:
        json.dump(settings, f, indent=4)

# def update_notifications_enabled(enabled: bool):
#     settings = load_settings()
#     settings['notifications'] = enabled
#     save_settings(settings)

class Settings:
    def __init__(self):
        self._data = load_settings()

    @property
    def notifications(self):
        return self._data.get('notifications')

    @property
    def start_end_notification(self):
        return self._data.get('start_end_notification')
    
    @start_end_notification.setter
    def start_end_notification(self, value: bool):
        self._data['start_end_notification'] = value
        save_settings(self._data)

    @notifications.setter
    def notifications(self, value: bool):
        self._data['notifications'] = value
        save_settings(self._data)

settings = Settings()