from my_project.recruitment.service import application_service as service

# Цей контролер відповідає за таблицю 'applications' (зв'язок М:М)
# Вона зв'язує Candidates та Vacancies

def get_all_applications():
    """DTO для всієї таблиці applications."""
    apps = service.get_all()
    return [app.to_dict() for app in apps]


def get_applications_for_candidate(candidate_id: int):
    """
    DTO для М:М – усі заявки (вакансії) конкретного кандидата.
    """
    apps = service.get_by_candidate(candidate_id)
    # Повертаємо, наприклад, інформацію про вакансію для цього кандидата
    return [app.to_vacancy_info_dict() for app in apps]


def get_applications_for_vacancy(vacancy_id: int):
    """
    DTO для М:М – усі кандидати, що подалися на конкретну вакансію.
    """
    apps = service.get_by_vacancy(vacancy_id)
    # Повертаємо інформацію про кандидата
    return [app.to_candidate_info_dict() for app in apps]


def create_application(data: dict):
    """
    Створити нову заявку (зв'язати кандидата і вакансію).
    data: { "candidate_id": 1, "vacancy_id": 2, "applied_date": "2025-01-01" }
    """
    app = service.create_application(data)
    return app.to_dict()