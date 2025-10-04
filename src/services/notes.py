import uuid
from sqlalchemy.orm import Session
from src.repository.notes import NotesRepository
from src.schemas.notes import CreateNote, UpdateNote
from src.database.tables.users import Notes


class NoteService:
    def __init__(self, session: Session):
        self._note_repo = NotesRepository(session=session)

    def create(self, note: CreateNote):
        data = note.model_dump(exclude_unset=True)
        note_id = str(uuid.uuid4)
        data["note_id"] = note_id
        return self._note_repo.create(data=data)

    def retrive(self):
        return self._note_repo.get_by([])

    def retrive_by_note_id(self, note_id: str) -> Notes:
        note = self._note_repo.get_by([Notes.note_id == note_id], limit=1)
        if len(note) > 0:
            return note[0]
        else:
            raise Exception

    def update(self, pk: str | int, note: UpdateNote) -> Notes:
        note_dict = note.model_dump(exclude_unset=True)
        note: Notes | None = self._note_repo.update_one(pk, note_dict)
        if not note:
            raise Exception
        else:
            return note
