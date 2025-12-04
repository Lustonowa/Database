from typing import Optional, List

from sqlalchemy.orm import selectinload

from my_project.recruitment.dao.base import BaseDAO, session_scope
from my_project.recruitment.domain.models import Project


class ProjectDAO(BaseDAO[Project]):
    """
    DAO для роботи з таблицею projects.
    Додаємо методи, які одразу підтягують вакансії (vacancies).
    """

    def __init__(self) -> None:
        super().__init__(Project)

    def get_with_vacancies(self, project_id: int) -> Optional[Project]:
        """
        Один проект разом з усіма вакансіями.
        """
        with session_scope() as s:
            return (
                s.query(Project)
                .options(selectinload(Project.vacancies))
                .filter(Project.project_id == project_id)
                .one_or_none()
            )

    def get_all_with_vacancies(self) -> List[Project]:
        """
        Усі проекти з їхніми вакансіями.
        """
        with session_scope() as s:
            return (
                s.query(Project)
                .options(selectinload(Project.vacancies))
                .all()
            )