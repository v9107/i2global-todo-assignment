from src.repository.base import BaseRepository
from src.database.tables.users import User
from sqlalchemy.orm import Session


class UserRepository[M: User](BaseRepository):
    def __init__(self, session: Session):
        super().__init__(User, session)

    def get_by_user_id(self, user_id: str) -> M:
        return (
            self._session.query(self._model_class)
            .filter(self._model_class.user_id == user_id)
            .first()
        )
