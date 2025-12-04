from flask import Blueprint, jsonify, request

from my_project.recruitment.controller import application_controller as controller

application_bp = Blueprint("applications", __name__, url_prefix="/api/applications")


@application_bp.get("/")
def list_applications():
    """
    Отримати всі заявки (всі зв'язки Кандидат-Вакансия).
    """
    return jsonify(controller.get_all_applications())


@application_bp.get("/by-candidate/<int:candidate_id>")
def list_applications_by_candidate(candidate_id: int):
    """
    Отримати всі вакансії, на які подався конкретний кандидат.
    """
    data = controller.get_applications_for_candidate(candidate_id)
    return jsonify(data)


@application_bp.get("/by-vacancy/<int:vacancy_id>")
def list_applications_by_vacancy(vacancy_id: int):
    """
    Отримати всіх кандидатів, які подалися на конкретну вакансію.
    """
    data = controller.get_applications_for_vacancy(vacancy_id)
    return jsonify(data)


@application_bp.post("/")
def create_application():
    """
    Створити нову заявку (подати кандидата на вакансію).
    Body: {"candidate_id": 1, "vacancy_id": 2, "applied_date": "2025-05-20"}
    """
    data = request.get_json() or {}
    # Створюємо через контролер (додай метод create_application у контролер, якщо його там ще немає, 
    # або використовуй логіку сервісу)
    app = controller.create_application(data)
    return jsonify(app), 201