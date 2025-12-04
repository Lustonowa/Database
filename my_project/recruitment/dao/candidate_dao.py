from typing import List, Optional
from sqlalchemy.orm import selectinload

from my_project.recruitment.dao.base import BaseDAO, session_scope
from my_project.recruitment.domain.models import Candidate


class CandidateDAO(BaseDAO[Candidate]):
    def __init__(self):
        super().__init__(Candidate)

    def get_all(self) -> List[Candidate]:
        """
        GET: Вантажимо всіх разом з рівнями (english_level, tech_level).
        Це запобігає помилці DetachedInstanceError при читанні списку.
        """
        with session_scope() as s:
            return (
                s.query(Candidate)
                .options(
                    selectinload(Candidate.english_level),
                    selectinload(Candidate.tech_level)
                )
                .all()
            )

    def get_by_id(self, candidate_id: int) -> Optional[Candidate]:
        """
        GET ONE: Вантажимо одного кандидата разом з рівнями.
        """
        with session_scope() as s:
            return (
                s.query(Candidate)
                .options(
                    selectinload(Candidate.english_level),
                    selectinload(Candidate.tech_level)
                )
                .filter(Candidate.candidate_id == candidate_id)
                .one_or_none()
            )

    def create(self, **kwargs) -> Candidate:
        """
        POST: Створюємо кандидата, а потім ПЕРЕЧИТУЄМО його з БД.
        Це найважливіша частина фіксу помилки DetachedInstanceError при створенні.
        """
        # 1. Використовуємо базовий метод для фізичної вставки в БД
        new_candidate_simple = super().create(**kwargs)
        
        # 2. Одразу робимо запит get_by_id, який підтягує всі зв'язки.
        # Це гарантує, що ми повернемо повний об'єкт, готовий для to_dict().
        return self.get_by_id(new_candidate_simple.candidate_id)

    def update(self, obj_id: int, **kwargs) -> Optional[Candidate]:
        """
        PUT: Оновлюємо і одразу перечитуємо повні дані.
        """
        updated_candidate_simple = super().update(obj_id, **kwargs)
        
        if updated_candidate_simple:
            return self.get_by_id(obj_id)
        return None