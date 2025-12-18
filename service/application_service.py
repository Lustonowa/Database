from typing import List

from my_project.recruitment.dao import application_dao as dao
from my_project.recruitment.domain.models import Application


def get_all() -> List[Application]:
    return dao.get_all()


def get_by_candidate(candidate_id: int) -> List[Application]:
    """
    Отримати всі заявки конкретного кандидата.
    """
    return dao.get_by_candidate(candidate_id)


def get_by_vacancy(vacancy_id: int) -> List[Application]:
    """
    Отримати всі заявки на конкретну вакансію.
    """
    return dao.get_by_vacancy(vacancy_id)


def create_application(data: dict) -> Application:
    """
    Створення заявки.
    Потрібні candidate_id, vacancy_id, applied_date
    """
    # Створюємо об'єкт моделі
    app = Application(
        candidate_id=data.get("candidate_id"),
        vacancy_id=data.get("vacancy_id"),
        applied_date=data.get("applied_date")
    )
    # Передаємо в DAO для збереження
    return dao.create_application(app)