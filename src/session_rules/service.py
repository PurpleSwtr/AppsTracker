from datetime import datetime
from sqlalchemy.orm import Session
from src.patterns.repository import PatternRepository
from src.notifications.manager import send_notification, progress_notification
from src.session_rules.session_state import ActiveSession, PatternState
import psutil

class SessionRulesService:
    def __init__(self, session: Session):
        self.session = session
        self.pattern_repo = PatternRepository(session)
        self._active_sessions: dict[int, ActiveSession] = {}  # session_id -> ActiveSession

    def start_session(self, session_id: int, app_id: int, process_name: str, start_time: datetime):
        patterns = self.pattern_repo.get_patterns_for_application(app_id)
        if not patterns:
            return  # нет правил – не отслеживаем

        pattern_states = {}
        for pattern in patterns:
            pattern_states[pattern.id] = PatternState(
                pattern=pattern,
                last_notification_time=start_time
            )

        active = ActiveSession(
            session_id=session_id,
            app_id=app_id,
            process_name=process_name,
            start_time=start_time,
            pattern_states=pattern_states
        )
        self._active_sessions[session_id] = active

    def update_session(self, session_id: int, current_time: datetime):
        active = self._active_sessions.get(session_id)
        if not active:
            return

        elapsed_min = (current_time - active.start_time).total_seconds() / 60.0

        for state in active.pattern_states.values():
            pattern = state.pattern
            # 1. Проверка превышения лимита
            if elapsed_min >= pattern.time_limit:
                if not state.limit_exceeded:
                    # Первое превышение
                    self._notify_limit_exceeded(pattern, elapsed_min)
                    state.limit_exceeded = True
                    if pattern.close:
                        self._close_process(active.process_name)
                elif pattern.repeat:
                    # Повторные уведомления после превышения
                    last = state.last_notification_time
                    if (current_time - last).total_seconds() / 60.0 >= pattern.notification_interval:
                        self._notify_limit_exceeded(pattern, elapsed_min, repeat=True)
                        state.last_notification_time = current_time
                # Если repeat=False, больше ничего не делаем
                continue  # переходим к следующему паттерну (лимит уже превышен)

            # 2. Лимит не превышен – проверяем интервал напоминаний
            last = state.last_notification_time
            if (current_time - last).total_seconds() / 60.0 >= pattern.notification_interval:
                progress = elapsed_min / pattern.time_limit if pattern.time_limit > 0 else 0
                self._send_progress_notification(pattern, elapsed_min, progress)
                state.last_notification_time = current_time

    def end_session(self, session_id: int):
        self._active_sessions.pop(session_id, None)

    # ---- Приватные вспомогательные методы ----
    def _send_progress_notification(self, pattern, elapsed_min: float, progress: float):
        # Можно форматировать сообщение, добавляя elapsed_min, но для простоты используем как есть
        progress_notification(pattern.title, pattern.message, progress)

    def _notify_limit_exceeded(self, pattern, elapsed_min: float, repeat: bool = False):
        if repeat:
            msg = f"Лимит {pattern.time_limit} мин. превышен! Вы работаете {int(elapsed_min)} мин."
        else:
            msg = f"Лимит времени ({pattern.time_limit} мин.) превышен!"
            if pattern.close:
                msg += " Приложение будет закрыто."
        send_notification(pattern.title, msg)

    def _close_process(self, process_name: str):
        for proc in psutil.process_iter(['name', 'pid']):
            if proc.info['name'] == process_name:
                try:
                    proc.terminate()
                except Exception as e:
                    print(f"Не удалось закрыть {process_name}: {e}")
                break