from typing import List, Optional

from my_project.recruitment.dao.candidate_dao import CandidateDAO
from my_project.recruitment.domain.models import Candidate


class CandidateService:
    def __init__(self, dao: CandidateDAO | None = None):
        self.dao = dao or CandidateDAO()

    def get_all_candidates(self) -> List[Candidate]:
        return self.dao.get_all()

    def get_candidate_by_id(self, candidate_id: int) -> Optional[Candidate]:
        return self.dao.get_by_id(candidate_id)

    def create_candidate(self, data: dict) -> Candidate:
        return self.dao.create(
            full_name=data.get("full_name"),
            email=data.get("email"),
            phone=data.get("phone"),
            english_level_id=data.get("english_level_id"),
            tech_level_id=data.get("tech_level_id"),
            experience_years=data.get("experience_years"),
        )

    def update_candidate(self, candidate_id: int, data: dict) -> Optional[Candidate]:
        return self.dao.update(
            candidate_id,
            full_name=data.get("full_name"),
            email=data.get("email"),
            phone=data.get("phone"),
            english_level_id=data.get("english_level_id"),
            tech_level_id=data.get("tech_level_id"),
            experience_years=data.get("experience_years"),
        )

    def delete_candidate(self, candidate_id: int) -> bool:
        return self.dao.delete(candidate_id)