from my_project.recruitment.dao.lab5_dao import Lab5DAO

class Lab5Service:
    def __init__(self):
        self.dao = Lab5DAO()

    def add_note(self, candidate_id: int, text: str):
        self.dao.call_insert_candidate_note(candidate_id, text)

    def add_application_smart(self, email: str, vacancy_title: str):
        self.dao.call_add_application_by_names(email, vacancy_title)

    def create_dummies(self):
        self.dao.call_insert_dummy_companies()

    def get_top_candidates(self):
        return self.dao.call_get_candidates_above_avg()

    def run_cursor_migration(self):
        return self.dao.call_cursor_random_copy()
        
    def get_logs(self):
        return self.dao.get_audit_logs()