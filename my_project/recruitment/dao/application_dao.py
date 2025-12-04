from typing import List

from my_project.recruitment.utils import db
from my_project.recruitment.domain.models import Application


def get_all() -> List[Application]:
    """Повертає всі записи з таблиці applications."""
    with db.SessionLocal() as session:
        return session.query(Application).all()


def get_by_candidate(candidate_id: int) -> List[Application]:
    """
    Усі заявки конкретного кандидата.
    """
    with db.SessionLocal() as session:
        return (
            session.query(Application)
            .filter(Application.candidate_id == candidate_id)
            .all()
        )


def get_by_vacancy(vacancy_id: int) -> List[Application]:
    """
    Усі заявки на конкретну вакансію.
    """
    with db.SessionLocal() as session:
        return (
            session.query(Application)
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
        return application