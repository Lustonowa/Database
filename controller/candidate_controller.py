from my_project.recruitment.service.candidate_service import CandidateService

candidate_service = CandidateService()


def get_all_candidates():
    return [c.to_dict() for c in candidate_service.get_all_candidates()]


def get_candidate(candidate_id: int):
    candidate = candidate_service.get_candidate_by_id(candidate_id)
    return candidate.to_dict() if candidate else None


def create_candidate(data: dict):
    """
    Створення кандидата.
    Може включати english_level_id та tech_level_id.
    """
    candidate = candidate_service.create_candidate(data)
    return candidate.to_dict()


def update_candidate(candidate_id: int, data: dict):
    candidate = candidate_service.update_candidate(candidate_id, data)
    return candidate.to_dict() if candidate else None


def delete_candidate(candidate_id: int) -> bool:
    return candidate_service.delete_candidate(candidate_id)