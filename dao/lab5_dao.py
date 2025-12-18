from sqlalchemy import text
from my_project.recruitment.dao.base import session_scope

class Lab5DAO:
    """
    DAO для виклику збережених процедур та роботи з таблицями Лабораторної №5.
    Використовуємо 'execute(text(...))' для виклику процедур.
    """

    def call_insert_candidate_note(self, candidate_id: int, note_text: str):
        """2a. Параметризована вставка"""
        with session_scope() as s:
            s.execute(
                text("CALL insert_candidate_note(:p1, :p2)"),
                {"p1": candidate_id, "p2": note_text}
            )

    def call_add_application_by_names(self, email: str, vacancy_title: str):
        """2b. M:M вставка за значеннями"""
        with session_scope() as s:
            s.execute(
                text("CALL add_application_by_email_and_title(:p1, :p2)"),
                {"p1": email, "p2": vacancy_title}
            )

    def call_insert_dummy_companies(self):
        """2c. Пакетна вставка 10 стрічок"""
        with session_scope() as s:
            s.execute(text("CALL insert_dummy_companies()"))

    def call_get_candidates_above_avg(self):
        """2d. Процедура з SELECT (використовує функцію)"""
        with session_scope() as s:
            result = s.execute(text("CALL get_candidates_above_avg()"))
            # Перетворюємо результат (Row objects) у список словників
            return [
                {"full_name": row.full_name, "experience_years": row.experience_years}
                for row in result.mappings().all()
            ]

    def call_cursor_random_copy(self):
        """2e. Курсор: динамічні таблиці"""
        with session_scope() as s:
            result = s.execute(text("CALL cursor_copy_candidates_randomly()"))
            # Отримуємо імена створених таблиць
            row = result.mappings().one_or_none()
            return dict(row) if row else None
            
    def get_audit_logs(self):
        """Для перевірки тригерів"""
        with session_scope() as s:
            result = s.execute(text("SELECT * FROM audit_log ORDER BY created_at DESC LIMIT 20"))
            return [dict(row) for row in result.mappings().all()]