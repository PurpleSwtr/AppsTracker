from pathlib import Path
from src.database import engine, SessionLocal
from src.models import Base, Application

def get_process_name(link: str) -> str:
    link = link.strip('"').strip("'")
    return Path(link).name

def save_application_to_db(app_name: str, process_name: str) -> None:
    with SessionLocal() as session:
        app = Application(name=app_name, process_name=process_name)
        session.add(app)
        session.commit()

def init_db() -> None:
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()

    user_input = input().strip()
    try:
        process_name = get_process_name(user_input)
        app_name = process_name
        save_application_to_db(app_name, process_name)

    except ValueError as e:
        print(e)