from typing import List, Optional

from my_project.recruitment.dao.project_dao import ProjectDAO
from my_project.recruitment.domain.models import Project


class ProjectService:
    """
    Сервісний шар для роботи з проектами.
    """

    def __init__(self, dao: ProjectDAO | None = None) -> None:
        self.dao = dao or ProjectDAO()

    # ----- CRUD -----

    def get_all_projects(self) -> List[Project]:
        return self.dao.get_all()

    def get_project_by_id(self, project_id: int) -> Optional[Project]:
        return self.dao.get_by_id(project_id)

    def create_project(self, data: dict) -> Project:
        return self.dao.create(
            company_id=data.get("company_id"),
            name=data.get("name"),
            description=data.get("description"),
        )

    def update_project(self, project_id: int, data: dict) -> Optional[Project]:
        return self.dao.update(
            project_id,
            company_id=data.get("company_id"),
            name=data.get("name"),
            description=data.get("description"),
        )

    def delete_project(self, project_id: int) -> bool:
        return self.dao.delete(project_id)

    # ----- 1:M Relationship (Project -> Vacancies) -----

    def get_project_with_vacancies(self, project_id: int) -> Optional[Project]:
        """
        Один проект + список його вакансій.
        """
        return self.dao.get_with_vacancies(project_id)

    def get_all_projects_with_vacancies(self) -> List[Project]:
        """
        Усі проекти з вкладеними вакансіями.
        """
        return self.dao.get_all_with_vacancies()