from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError

from my_project.recruitment.controller import vacancy_controller as controller

vacancy_bp = Blueprint("vacancies", __name__, url_prefix="/api/vacancies")


@vacancy_bp.get("/")
def list_vacancies():
    return jsonify(controller.get_all_vacancies())


@vacancy_bp.get("/<int:vacancy_id>")
def get_vacancy(vacancy_id: int):
    v = controller.get_vacancy(vacancy_id)
    if not v:
        return jsonify({"status": "error", "message": "Vacancy not found"}), 404
    return jsonify(v)


@vacancy_bp.post("/")
def create_vacancy():
    """
    POST /api/vacancies/
    Body: {"project_id": 1, "title": "...", "salary_from": 1000, ...}
    """
    data = request.get_json() or {}
    try:
        v = controller.create_vacancy(data)
        return jsonify(v), 201
    except IntegrityError:
         return jsonify({"message": "Project ID required or invalid"}), 400


@vacancy_bp.put("/<int:vacancy_id>")
def update_vacancy(vacancy_id: int):
    data = request.get_json() or {}
    v = controller.update_vacancy(vacancy_id, data)
    if not v:
        return jsonify({"status": "error", "message": "Vacancy not found"}), 404
    return jsonify(v)


@vacancy_bp.delete("/<int:vacancy_id>")
def delete_vacancy(vacancy_id: int):
    try:
        ok = controller.delete_vacancy(vacancy_id)
    except IntegrityError:
        # Вакансію не можна видалити, якщо на неї є подані заявки (applications)
        return (
            jsonify(
                {
                    "status": "error",
                    "message": "Неможливо видалити вакансію, оскільки на неї є подані заявки (applications).",
                }
            ),
            409,
        )

    if not ok:
        return jsonify({"status": "error", "message": "Vacancy not found"}), 404

    return jsonify({"status": "success", "message": "Vacancy deleted"}), 200