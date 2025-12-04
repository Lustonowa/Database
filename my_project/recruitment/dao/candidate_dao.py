from typing import List, Optional
from sqlalchemy.orm import selectinload

from my_project.recruitment.dao.base import BaseDAO, session_scope
from my_project.recruitment.domain.models import Candidate


class CandidateDAO(BaseDAO[Candidate]):
    def __init__(self):
        super().__init__(Candidate)

    def get_all(self) -> List[Candidate]:
        """
        Перевизначаємо get_all, щоб одразу підтягувати (selectinload)
        дані про рівні англійської та технічні навички.
        Це запобігає DetachedInstanceError.
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
        Те саме для пошуку одного кандидата.
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