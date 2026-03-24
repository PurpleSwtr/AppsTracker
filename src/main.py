import sys
from pathlib import Path
from src.database import engine, SessionLocal
from src.models import Base, Application
import os
import json

config_file_path = 'config.json'
database_path = 'data.db'

def get_process_name(link: str) -> str:
    return link[link.rfind("\\") + 1 : ][:-1]

def save_application(app_name: str):
    file_path = config_file_path
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    new_entry = {"name": app_name}
    data['items'].append(new_entry)

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def create_db(database_path: str):
    if not os.path.exists(database_path):
        Base.metadata.create_all(bind=engine)



if __name__ == "__main__":
    create_db(database_path)
    l = input()
    app_name = get_process_name(l)
    save_application(app_name)
    try:
        if ".exe" in l:
            app_name = get_process_name(l)
            save_application(app_name)
        else:
            raise ValueError
    except ValueError:
        print("Недопустимое расширение приложения")

