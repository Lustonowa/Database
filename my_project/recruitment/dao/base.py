from contextlib import contextmanager
from typing import Type, TypeVar, Generic, List, Optional

from sqlalchemy.orm import Session

# Зверни увагу: шлях змінено на recruitment
from my_project.recruitment.utils.db import get_session

T = TypeVar("T")


@contextmanager
def session_scope():
    """
    Контекстний менеджер для роботи з сесією.
    Автоматично робить commit, якщо все добре, або rollback при помилці.
    """
    session: Session = get_session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


class BaseDAO(Generic[T]):
    """
    Базовий клас DAO, що реалізує стандартні CRUD-операції.
    Інші DAO можуть наслідувати його, щоб не дублювати код.
    """
    def __init__(self, model: Type[T]):
        self.model = model

    def get_all(self) -> List[T]:
        with session_scope() as s:
            return s.query(self.model).all()

    def get_by_id(self, obj_id: int) -> Optional[T]:
        with session_scope() as s:
            return s.get(self.model, obj_id)

    def create(self, **kwargs) -> T:
        with session_scope() as s:
            obj = self.model(**kwargs)
            s.add(obj)
            s.flush() # flush щоб отримати ID, але коміт буде в session_scope
            s.refresh(obj)
            return obj

    def update(self, obj_id: int, **kwargs) -> Optional[T]:
        with session_scope() as s:
            obj = s.get(self.model, obj_id)
            if obj is None:
                return None
            for key, value in kwargs.items():
                setattr(obj, key, value)
            s.flush()
            s.refresh(obj)
            return obj

    def delete(self, obj_id: int) -> bool:
        with session_scope() as s:
            obj = s.get(self.model, obj_id)
            if obj is None:
                return False
            s.delete(obj)
            return True