from flask import Blueprint, jsonify, request

# Імпортуємо контролер компаній
from my_project.recruitment.controller import company_controller as controller

company_bp = Blueprint("companies", __name__, url_prefix="/api/companies")


@company_bp.get("/")
def list_companies():
    """
    GET /api/companies/
    Отримати список всіх компаній.
    """
    return jsonify(controller.get_all_companies())


@company_bp.get("/<int:company_id>")
def get_company(company_id: int):
    """
    GET /api/companies/<id>
    Отримати одну компанію.
    """
    company = controller.get_company(company_id)
    if not company:
        return jsonify({"message": "Company not found"}), 404
    return jsonify(company)


@company_bp.post("/")
def create_company():
    """
    POST /api/companies/
    Створити нову компанію.
    JSON Body: {"name": "...", "location": "..."}
    """
    data = request.get_json() or {}
    company = controller.create_company(data)
    return jsonify(company), 201


@company_bp.put("/<int:company_id>")
def update_company(company_id: int):
    """
    PUT /api/companies/<id>
    Оновити дані компанії.
    """
    data = request.get_json() or {}
    company = controller.update_company(company_id, data)
    if not company:
        return jsonify({"message": "Company not found"}), 404
    return jsonify(company)


@company_bp.delete("/<int:company_id>")
def delete_company(company_id: int):
    """
    DELETE /api/companies/<id>
    Видалити компанію.
    """
    ok = controller.delete_company(company_id)
    if not ok:
        return jsonify({"message": "Company not found"}), 404
    return "", 204


# ----- 1:M Relationship Endpoints -----

@company_bp.get("/with-projects")
def list_companies_with_projects():
    """
    GET /api/companies/with-projects
    Отримати всі компанії разом зі списком їхніх проектів.
    """
    return jsonify(controller.get_all_companies_with_projects())


@company_bp.get("/<int:company_id>/projects")
def get_company_projects(company_id: int):
    """
    GET /api/companies/<id>/projects
    Отримати конкретну компанію разом з її проектами.
    """
    data = controller.get_company_with_projects(company_id)
    if not data:
        return jsonify({"message": "Company not found"}), 404
    return jsonify(data)