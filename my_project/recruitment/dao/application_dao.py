from typing import List

from sqlalchemy.orm import selectinload

from my_project.recruitment.utils import db
from my_project.recruitment.domain.models import Application


def get_all() -> List[Application]:
    """Повертає всі записи з таблиці applications."""
    with db.SessionLocal() as session:
        return (
            session.query(Application)
            # Вантажимо і кандидата, і вакансію, щоб уникнути помилок при повному списку
            .options(
                selectinload(Application.candidate),
                selectinload(Application.vacancy)
            )
            .all()
        )


def get_by_candidate(candidate_id: int) -> List[Application]:
    """
    Усі заявки конкретного кандидата.
    Тут нам важливо підтягнути VACANCY, щоб показати, куди він подався.
    """
    with db.SessionLocal() as session:
        return (
            session.query(Application)
            .options(selectinload(Application.vacancy))  # <--- Завантажуємо вакансію
            .filter(Application.candidate_id == candidate_id)
            .all()
        )


def get_by_vacancy(vacancy_id: int) -> List[Application]:
    """
    Усі заявки на конкретну вакансію.
    Тут нам важливо підтягнути CANDIDATE, щоб показати, хто подався.
    """
    with db.SessionLocal() as session:
        return (
            session.query(Application)
            .options(selectinload(Application.candidate)) # <--- Завантажуємо кандидата (це фіксить твою помилку)
            .filter(Application.vacancy_id == vacancy_id)
            .all()
        )


def create_application(application: Application) -> Application:
    """
    Створення нового запису в таблиці заявок.
    """
    with db.SessionLocal() as session:
        session.add(application)
        session.commit()
        session.refresh(application)
        
        # Перечитуємо об'єкт із завантаженням зв'язків, щоб можна було безпечно викликати to_dict()
        return (
            session.query(Application)
            .options(
                selectinload(Application.candidate),
                selectinload(Application.vacancy)
            )
            .filter(Application.application_id == application.application_id)
            .one()
        )