from typing import List, Optional

from my_project.recruitment.dao.company_dao import CompanyDAO
from my_project.recruitment.domain.models import Company


class CompanyService:
    def __init__(self, dao: CompanyDAO | None = None):
        self.dao = dao or CompanyDAO()

    def get_all_companies(self) -> List[Company]:
        return self.dao.get_all()

    def get_company_by_id(self, company_id: int) -> Optional[Company]:
        return self.dao.get_by_id(company_id)

    def create_company(self, data: dict) -> Company:
        return self.dao.create(
            name=data.get("name"),
            location=data.get("location"),
        )

    def update_company(self, company_id: int, data: dict) -> Optional[Company]:
        return self.dao.update(
            company_id,
            name=data.get("name"),
            location=data.get("location"),
        )

    def delete_company(self, company_id: int) -> bool:
        return self.dao.delete(company_id)

    # ----- Специфічні методи для 1:M -----

    def get_company_with_projects(self, company_id: int) -> Optional[Company]:
        return self.dao.get_with_projects(company_id)

    def get_all_companies_with_projects(self) -> List[Company]:
        return self.dao.get_all_with_projects()