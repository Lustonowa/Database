from my_project.recruitment.service.project_service import ProjectService

project_service = ProjectService()


# ----- CRUD -----

def get_all_projects():
    """
    DTO: всі проекти.
    """
    return [p.to_dict() for p in project_service.get_all_projects()]


def get_project(project_id: int):
    """
    DTO: один проект.
    """
    project = project_service.get_project_by_id(project_id)
    return project.to_dict() if project else None


def create_project(data: dict):
    """
    Створення проекту.
    Повинно включати company_id у data.
    """
    project = project_service.create_project(data)
    return project.to_dict()


def update_project(project_id: int, data: dict):
    """
    Оновлення проекту.
    """
    project = project_service.update_project(project_id, data)
    return project.to_dict() if project else None


def delete_project(project_id: int) -> bool:
    """
    Видалення проекту.
    """
    return project_service.delete_project(project_id)


# ----- 1:M Relationship (Project -> Vacancies) -----

def get_project_with_vacancies(project_id: int):
    """
    DTO: проект із вкладеним списком вакансій.
    Демонстрація зв'язку 1:M (One-to-Many).
    """
    project = project_service.get_project_with_vacancies(project_id)
    return project.to_dict(include_vacancies=True) if project else None


def get_all_projects_with_vacancies():
    """
    DTO: всі проекти з вакансіями.
    """
    return [
        p.to_dict(include_vacancies=True)
        for p in project_service.get_all_projects_with_vacancies()
    ]