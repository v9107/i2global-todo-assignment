from src.repository.base import BaseRepository
from src.database.tables.users import Notes
from sqlalchemy.orm import Session


class NotesRepository[M: Notes](BaseRepository):
    def __init__(self, session: Session):
        super().__init__(Notes, session)

    def get_by_note_id(self, note_id: str) -> M:
        return (
            self._session.query(self._model_class)
            .filter(self._model_class.note_id == note_id)
            .first()
        )
