from my_project.recruitment.dao.base import BaseDAO
from my_project.recruitment.domain.models import Vacancy


class VacancyDAO(BaseDAO[Vacancy]):
    def __init__(self):
        super().__init__(Vacancy)