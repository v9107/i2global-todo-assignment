from typing import Optional
from pydantic import BaseModel, ConfigDict
import datetime as dt


class BaseSchema(BaseModel):
    id: int
    created_at: dt.datetime
    last_update: dt.datetime


class CreateUser(BaseModel):
    user_name: str
    user_email: str
    password: str


class UpdateUser(BaseModel):
    user_name: Optional[str]
    user_email: Optional[str]
    password: Optional[str]


class UserDetails(BaseSchema):
    user_name: str
    user_email: str

    model_config = ConfigDict(from_attributes=True)


class LoginPayload(BaseModel):
    email: str
    password: str
