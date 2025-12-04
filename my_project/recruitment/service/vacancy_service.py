from typing import List, Optional

from my_project.recruitment.dao.vacancy_dao import VacancyDAO
from my_project.recruitment.domain.models import Vacancy


class VacancyService:
    def __init__(self, dao: VacancyDAO | None = None):
        self.dao = dao or VacancyDAO()

    def get_all_vacancies(self) -> List[Vacancy]:
        return self.dao.get_all()

    def get_vacancy_by_id(self, vacancy_id: int) -> Optional[Vacancy]:
        return self.dao.get_by_id(vacancy_id)

    def create_vacancy(self, data: dict) -> Vacancy:
        return self.dao.create(
            project_id=data.get("project_id"),
            title=data.get("title"),
            description=data.get("description"),
            salary_from=data.get("salary_from"),
            salary_to=data.get("salary_to"),
        )

    def update_vacancy(self, vacancy_id: int, data: dict) -> Optional[Vacancy]:
        return self.dao.update(
            vacancy_id,
            project_id=data.get("project_id"),
            title=data.get("title"),
            description=data.get("description"),
            salary_from=data.get("salary_from"),
            salary_to=data.get("salary_to"),
        )

    def delete_vacancy(self, vacancy_id: int) -> bool:
        return self.dao.delete(vacancy_id)