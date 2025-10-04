from src.database.base import Base
from sqlalchemy.orm import Session
from typing import Type, Any


class BaseRepository[M: Base]:
    def __init__(self, model: Type[M], session: Session):
        self._model_class = model
        self._session = session

    def create(self, data: dict[str, Any]) -> M:
        row = self._model_class(**data)
        self._session.add(row)
        self._session.commit()
        self._session.refresh(row)
        return row

    def update_one(self, pk: str | int, values: dict[str, any]) -> M:
        self._session.query(self._model_class).filter(
            self._model_class.id == pk
        ).update(values)

        return self.get_by_id(pk)

    def delete(self, filters: list):
        self._session.query(self._model_class).filter(*filters).delete()
        return None

    def get_by_id(self, pk: str | None) -> M | None:
        return (
            self._session.query(self._model_class)
            .filter(self._model_class.id == pk)
            .first()
        )

    def get_by(self, filters: list, *, skip: int = 0, limit: int = 100) -> list[M]:
        return self._session.query(self._model_class).filter(*filters).all()
