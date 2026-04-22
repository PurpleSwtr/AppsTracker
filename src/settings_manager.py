import json
import os

SETTINGS_FILE = "settings.json"

default_settings = {
    "notifications": True,
}

def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        save_settings(default_settings)
        return default_settings
    
    with open(SETTINGS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_settings(settings):
    with open(SETTINGS_FILE, 'w', encoding='utf-8') as f:
        json.dump(settings, f, indent=4)

def update_notifications_enabled(enabled: bool):
    settings = load_settings()
    settings['notifications'] = enabled
    save_settings(settings)