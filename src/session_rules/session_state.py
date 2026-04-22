from dataclasses import dataclass, field
from datetime import datetime
from src.models import Pattern

@dataclass
class PatternState:
    pattern: Pattern
    last_notification_time: datetime
    limit_exceeded: bool = False

@dataclass
class ActiveSession:
    session_id: int
    app_id: int
    process_name: str
    start_time: datetime
    pattern_states: dict[int, PatternState] = field(default_factory=dict)