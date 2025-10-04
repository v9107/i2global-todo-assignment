from typing import Optional
from pydantic import BaseModel, ConfigDict
import datetime as dt


class BaseSchema(BaseModel):
    id: int
    created_at: dt.datetime
    last_update: dt.datetime


class CreateNote(BaseModel):
    note_title: str
    note_content: str
    created_by: int


class UpdateNote(BaseModel):
    note_title: Optional[str]
    note_content: Optional[str]
    created_by: Optional[int]


class NoteDetails(BaseSchema, CreateNote):
    model_config = ConfigDict(from_attributes=True)
