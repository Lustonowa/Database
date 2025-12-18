from flask import Blueprint, jsonify, request
from my_project.recruitment.controller import lab5_controller as controller

lab5_bp = Blueprint("lab5", __name__, url_prefix="/api/lab5")

@lab5_bp.post("/notes")
def add_note():
    """2a. Insert Note (Test Trigger for integrity)"""
    data = request.get_json() or {}
    res = controller.insert_note_controller(data)
    if res.get("status") == "error":
        return jsonify(res), 400
    return jsonify(res), 201

@lab5_bp.post("/applications/smart")
def add_app_smart():
    """2b. M:M Insert by names"""
    data = request.get_json() or {}
    res = controller.add_application_smart_controller(data)
    if res.get("status") == "error":
        return jsonify(res), 400
    return jsonify(res), 201

@lab5_bp.post("/companies/dummies")
def create_dummies():
    """2c. Insert 10 companies loop"""
    return jsonify(controller.create_dummies_controller()), 201

@lab5_bp.get("/candidates/top")
def get_top():
    """2d. Function usage (Above AVG experience)"""
    return jsonify(controller.get_top_candidates_controller())

@lab5_bp.post("/migration/random")
def run_cursor():
    """2e. Cursor execution"""
    return jsonify(controller.run_cursor_controller()), 201

@lab5_bp.get("/logs")
def get_logs():
    """Check audit logs (Trigger 3a result)"""
    return jsonify(controller.get_audit_logs_controller())