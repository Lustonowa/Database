from my_project.recruitment.service.vacancy_service import VacancyService

vacancy_service = VacancyService()


def get_all_vacancies():
    return [v.to_dict() for v in vacancy_service.get_all_vacancies()]


def get_vacancy(vacancy_id: int):
    vacancy = vacancy_service.get_vacancy_by_id(vacancy_id)
    return vacancy.to_dict() if vacancy else None


def create_vacancy(data: dict):
    """
    Створення вакансії.
    data має містити project_id.
    """
    vacancy = vacancy_service.create_vacancy(data)
    return vacancy.to_dict()


def update_vacancy(vacancy_id: int, data: dict):
    vacancy = vacancy_service.update_vacancy(vacancy_id, data)
    return vacancy.to_dict() if vacancy else None


def delete_vacancy(vacancy_id: int) -> bool:
    return vacancy_service.delete_vacancy(vacancy_id)