from typing import List, Optional

from sqlalchemy.orm import selectinload

# Імпортуємо BaseDAO та session_scope з твого base.py
from my_project.recruitment.dao.base import BaseDAO, session_scope
from my_project.recruitment.domain.models import Company


class CompanyDAO(BaseDAO[Company]):
    def __init__(self):
        super().__init__(Company)

    def get_all_with_projects(self) -> List[Company]:
        """
        Отримати всі компанії разом із їхніми проектами.
        Використовуємо selectinload для оптимізації (Eager Loading).
        """
        with session_scope() as s:
            return (
                s.query(Company)
                .options(selectinload(Company.projects))
                .all()
            )

    def get_with_projects(self, company_id: int) -> Optional[Company]:
        """
        Отримати одну компанію разом із проектами.
        """
        with session_scope() as s:
            return (
                s.query(Company)
                .options(selectinload(Company.projects))
                .filter(Company.company_id == company_id)
                .one_or_none()
            )