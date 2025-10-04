from fastapi import APIRouter
from src.services.notes import NoteService
from src.schemas.notes import NoteDetails, CreateNote, UpdateNote
from src.dependencies import SessionDeps

router = APIRouter(tags=["Note"], prefix="/note")


@router.post("")
def create_notes(session: SessionDeps, payload: CreateNote) -> NoteDetails:
    note_service = NoteService(session=session)
    return note_service.create(payload)


@router.get("/all")
def notes(session: SessionDeps, skip: int = 0, limit: int = 100) -> list[NoteDetails]:
    note_service = NoteService(session=session)
    return note_service.retrive()


@router.patch("/{note_id}")
def update_user(session: SessionDeps, note_id: str, payload: UpdateNote) -> NoteDetails:
    note_service = NoteService(session)
    note = note_service.update(note_id, payload)
    return note


@router.get("/{note_id}")
def retrive_user(session: SessionDeps, note_id: str) -> NoteDetails:
    note_service = NoteService(session)
    note = note_service.retrive_by_note_id(note_id=note_id)
    return note
