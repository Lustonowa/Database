import yaml
from flask import Flask, jsonify

from my_project.recruitment.utils.db import init_db, Base, engine
from my_project.recruitment.route import all_blueprints


def create_app(config_path: str = "config/app.yml") -> Flask:
    app = Flask(__name__)

    # 1. читаємо конфіг
    with open(config_path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    app.config["APP_CONFIG"] = cfg

    # 2. ініціалізація БД
    db_cfg = cfg["db"]
    init_db(db_cfg)

    # 3. створюємо таблиці (якщо треба)
    if engine is not None:
        Base.metadata.create_all(bind=engine)

    # 4. реєструємо всі blueprints (/api/brands, /api/products, ...)
    for bp in all_blueprints:
        app.register_blueprint(bp)

    # 5. health-check: ОЦЕЙ маршрут ти зараз тестуєш
    @app.get("/api/health")
    def health():
        return jsonify({"status": "ok"}), 200

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
