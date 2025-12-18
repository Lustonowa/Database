from flask import Blueprint, jsonify, request

from my_project.recruitment.controller import candidate_controller as controller

candidate_bp = Blueprint("candidates", __name__, url_prefix="/api/candidates")


@candidate_bp.get("/")
def list_candidates():
    return jsonify(controller.get_all_candidates())


@candidate_bp.get("/<int:candidate_id>")
def get_candidate(candidate_id: int):
    c = controller.get_candidate(candidate_id)
    if not c:
        return jsonify({"message": "Candidate not found"}), 404
    return jsonify(c)


@candidate_bp.post("/")
def create_candidate():
    """
    Body: {"full_name": "...", "email": "...", "english_level_id": 1, ...}
    """
    data = request.get_json() or {}
    c = controller.create_candidate(data)
    return jsonify(c), 201


@candidate_bp.put("/<int:candidate_id>")
def update_candidate(candidate_id: int):
    data = request.get_json() or {}
    c = controller.update_candidate(candidate_id, data)
    if not c:
        return jsonify({"message": "Candidate not found"}), 404
    return jsonify(c)


@candidate_bp.delete("/<int:candidate_id>")
def delete_candidate(candidate_id: int):
    ok = controller.delete_candidate(candidate_id)
    if not ok:
        return jsonify({"message": "Candidate not found"}), 404
    return "", 204