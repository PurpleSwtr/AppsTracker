from pathlib import Path
from sqlalchemy import func, select
from src.database import engine, SessionLocal
from src.models import Base, Application, AppSession

def get_process_name(link: str) -> str:
    link = link.strip('"').strip("'")
    return Path(link).name

def save_application_to_db(process_name: str) -> None:
    with SessionLocal() as session:
        app_name = process_name.replace(".exe", "")
        app = Application(name=app_name, process_name=process_name)
        session.add(app)
        session.commit()

def get_app_id(app_name: str) -> int | None:
    with SessionLocal() as session:
        stmt = select(Application.id).where(func.lower(Application.name) == func.lower(app_name))
        return session.execute(stmt).scalar_one_or_none()

def add_app_session(app_name: str):
    app_id = get_app_id(app_name=app_name)
    with SessionLocal() as session:
        app_session = AppSession(application_id=app_id, start_time=func.now())
        session.add(app_session)
        session.commit()

def init_db() -> None:
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
    user_input = ''
    while user_input != '*':
        user_input = input().strip()
        try:
            if "*" in user_input:
                raise ValueError("Выход из программы")
            # process_name = get_process_name(user_input)
            # save_application_to_db(process_name)
            print(get_app_id(app_name=user_input))
            add_app_session(app_name=user_input)

        except ValueError as e:
            print(e)