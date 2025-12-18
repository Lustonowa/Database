from my_project.recruitment.service.lab5_service import Lab5Service
from sqlalchemy.exc import OperationalError, DatabaseError

service = Lab5Service()

def insert_note_controller(data: dict):
    try:
        service.add_note(data.get("candidate_id"), data.get("note_text"))
        return {"status": "success", "message": "Note added via Procedure 2a"}
    except DatabaseError as e:
        # Тут ми можемо зловити помилку від ТРИГЕРА (пункт 1), якщо ID не існує
        return {"status": "error", "message": str(e.orig)}

def add_application_smart_controller(data: dict):
    try:
        service.add_application_smart(data.get("email"), data.get("vacancy_title"))
        return {"status": "success", "message": "Application added via Procedure 2b"}
    except DatabaseError as e:
        return {"status": "error", "message": str(e.orig)}

def create_dummies_controller():
    service.create_dummies()
    return {"status": "success", "message": "10 Dummy companies created via Procedure 2c"}

def get_top_candidates_controller():
    data = service.get_top_candidates()
    return data

def run_cursor_controller():
    tables = service.run_cursor_migration()
    return {
        "status": "success", 
        "message": "Cursor executed. Tables created.",
        "tables": tables
    }

def get_audit_logs_controller():
    return service.get_logs()