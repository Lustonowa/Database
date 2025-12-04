from my_project.recruitment.service.company_service import CompanyService

# Ініціалізація сервісу для роботи з компаніями
company_service = CompanyService()


def get_all_companies():
    """
    Отримати список усіх компаній (DTO).
    """
    return [c.to_dict() for c in company_service.get_all_companies()]


def get_company(company_id: int):
    """
    Отримати одну компанію за ID.
    """
    company = company_service.get_company_by_id(company_id)
    return company.to_dict() if company else None


def create_company(data: dict):
    """
    Створити нову компанію.
    """
    company = company_service.create_company(data)
    return company.to_dict()


def update_company(company_id: int, data: dict):
    """
    Оновити дані компанії.
    """
    company = company_service.update_company(company_id, data)
    return company.to_dict() if company else None


def delete_company(company_id: int) -> bool:
    """
    Видалити компанію.
    """
    return company_service.delete_company(company_id)


# ----- 1:M Relationship (Company -> Projects) -----

def get_company_with_projects(company_id: int):
    """
    DTO: Компанія разом зі списком її проектів.
    Демонстрація зв'язку 1:M (One-to-Many).
    """
    company = company_service.get_company_with_projects(company_id)
    # Передбачається, що метод to_dict має параметр include_projects
    return company.to_dict(include_projects=True) if company else None


def get_all_companies_with_projects():
    """
    DTO: Всі компанії з вкладеними списками проектів.
    """
    return [
        c.to_dict(include_projects=True)
        for c in company_service.get_all_companies_with_projects()
    ]