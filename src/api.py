from src import settings_manager

class Api:
    def set_notifications(self, enabled: bool):
        settings_manager.update_notifications_enabled(enabled)