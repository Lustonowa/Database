from flask import Blueprint, jsonify, request

from my_project.recruitment.controller import project_controller as controller

project_bp = Blueprint("projects", __name__, url_prefix="/api/projects")


@project_bp.get("/")
def list_projects():
    """
    GET /api/projects/
    Отримати всі проекти (без вакансій).
    """
    return jsonify(controller.get_all_projects())


@project_bp.get("/<int:project_id>")
def get_project(project_id: int):
    """
    GET /api/projects/<id>
    """
    project = controller.get_project(project_id)
    if not project:
        return jsonify({"message": "Project not found"}), 404
    return jsonify(project)


@project_bp.post("/")
def create_project():
    """
    POST /api/projects/
    Body: {"company_id": 1, "name": "...", "description": "..."}
    """
    data = request.get_json() or {}
    project = controller.create_project(data)
    return jsonify(project), 201


@project_bp.put("/<int:project_id>")
def update_project(project_id: int):
    data = request.get_json() or {}
    project = controller.update_project(project_id, data)
    if not project:
        return jsonify({"message": "Project not found"}), 404
    return jsonify(project)


@project_bp.delete("/<int:project_id>")
def delete_project(project_id: int):
    ok = controller.delete_project(project_id)
    if not ok:
        return jsonify({"message": "Project not found"}), 404
    return "", 204


# ----- 1:M Relationship Endpoints (Project -> Vacancies) -----

@project_bp.get("/with-vacancies")
def list_projects_with_vacancies():
    """
    GET /api/projects/with-vacancies
    Всі проекти з вкладеними списками вакансій.
    """
    return jsonify(controller.get_all_projects_with_vacancies())


@project_bp.get("/<int:project_id>/with-vacancies")
def get_project_with_vacancies(project_id: int):
    """
    GET /api/projects/<id>/with-vacancies
    """
    data = controller.get_project_with_vacancies(project_id)
    if not data:
        return jsonify({"message": "Project not found"}), 404
    return jsonify(data)