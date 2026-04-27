import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

class Config:
    BASE_DIR = Path(__file__).resolve().parent.parent
    
    DATA_DIR = BASE_DIR / "data"
    DB_PATH = DATA_DIR / "data.db"
    ICONS_PATH = BASE_DIR / "frontend" / "public" / "icons"
    SETTINGS_FILE = "settings.json"

    CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", 30))
    SQLALCHEMY_ECHO = os.getenv("SQLALCHEMY_ECHO", "False").lower() == "true"
    DEBUG_PYWEBVIEW_MODE = True

config = Config() 