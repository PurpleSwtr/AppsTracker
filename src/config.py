import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

class Config:
    BASE_DIR = Path(__file__).resolve().parent.parent
    
    DATA_DIR = BASE_DIR / "data"
    DB_PATH = DATA_DIR / "data.db"
    ICONS_PATH = DATA_DIR / "icons"
    
    CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", 30))
    SQLALCHEMY_ECHO = os.getenv("SQLALCHEMY_ECHO", "False").lower() == "true"

config = Config() 