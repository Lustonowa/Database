from typing import Any, Dict

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session

# Базовий клас для моделей
Base = declarative_base()

engine = None
SessionLocal: sessionmaker | None = None


def build_connection_url(cfg: Dict[str, Any]) -> str:
    """
    Генерує рядок підключення до MySQL.
    Приклад: mysql+pymysql://user:password@localhost:3306/it_recruitment?charset=utf8mb4
    """
    user = cfg["user"]
    password = cfg.get("password", "")
    host = cfg.get("host", "localhost")
    port = cfg.get("port", 3306)
    db_name = cfg["database"]
    return f"mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}?charset=utf8mb4"


def init_db(db_cfg: Dict[str, Any]) -> None:
    """
    Ініціалізує глобальний engine та фабрику сесій.
    Викликається один раз при старті додатку.
    """
    global engine, SessionLocal

    url = build_connection_url(db_cfg)
    
    engine = create_engine(
        url,
        echo=db_cfg.get("echo", False),           # Логування SQL запитів
        pool_pre_ping=db_cfg.get("pool_pre_ping", True), # Перевірка з'єднання перед запитом
        future=True,
    )

    SessionLocal = sessionmaker(
        bind=engine,
        autoflush=False,
        autocommit=False,
        expire_on_commit=False,
        future=True,
    )


def get_session() -> Session:
    """
    Повертає нову сесію.
    Викидає помилку, якщо БД ще не ініціалізована.
    """
    if SessionLocal is None:
        raise RuntimeError("DB is not initialized, call init_db() first")
    return SessionLocal()