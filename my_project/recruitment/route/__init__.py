from .company_route import company_bp
from .project_route import project_bp
from .vacancy_route import vacancy_bp
from .candidate_route import candidate_bp
from .application_route import application_bp

# Збираємо всі блюпринти в список для зручної реєстрації в app.py
all_blueprints = [
    company_bp,
    project_bp,
    vacancy_bp,
    candidate_bp,
    application_bp,
]