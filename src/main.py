import sys
from pathlib import Path
from typing import Sequence
from sqlalchemy import func, select
from src.database import engine, SessionLocal
from src.models import Base, Application, AppSession
from enum import Enum, auto

class Action(Enum):
    ADD_APPLICATION = auto()
    ADD_PATTERN = auto()
    
    START_SESSION = auto()
    END_SESSION = auto()
    
    EXIT = auto()

actions_descriptions = {
    "ADD_APPLICATION": "Добавить приложение",
    "ADD_PATTERN": "Создать паттерн отслеживания",
    "START_SESSION": "Действие начала сессии",
    "END_SESSION": "Действие конец сессии",
    "EXIT": "Выход",
}    

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
    if app_id is not None:
        with SessionLocal() as session:
            app_session = AppSession(application_id=app_id, start_time=func.now())
            session.add(app_session)
            session.commit()
    else:
        raise ValueError("Запись не найдена")

def get_applications_process_names() -> list[str]:
    with SessionLocal() as session:
        names = session.scalars(select(Application.process_name)).all()
        return list(names)

def init_db() -> None:
    Base.metadata.create_all(bind=engine)


def dubug_menu() -> Action:
    for i, elem in enumerate(actions_descriptions.values()):
        print(f"{i+1}. {elem}")

    user_input = input().strip()

    if user_input.isdigit():
        user_input = int(user_input)
    else: return Action.EXIT
    
    if int(user_input) > len(actions_descriptions) + 1:
        print("Ошибка ввода")
    
    match int(user_input) - 1:
        case 0: 
            return Action.ADD_APPLICATION
        case 1: 
            return Action.ADD_PATTERN
        case 2: 
            return Action.START_SESSION
        case 3: 
            return Action.END_SESSION
        case 4: 
            return Action.EXIT
        case _:
            return Action.EXIT




if __name__ == "__main__":
    init_db()
    user_input = None
    while user_input != Action.EXIT:
        try:
            user_input = dubug_menu()
            match user_input:

                case Action.EXIT:
                    raise ValueError("Выход из программы")
                
                case Action.ADD_APPLICATION:
                    app = input("Перетащите приложение в окно программы...\n")
                    process_name = get_process_name(app)
                    save_application_to_db(process_name)

                case Action.START_SESSION:
                    app_name = input("Ожидание ввода названия приложения...\n")
                    print(get_app_id(app_name=app_name))
                    add_app_session(app_name=app_name)

        except ValueError as e:
            print(e)
        except KeyboardInterrupt:
            sys.exit(0)