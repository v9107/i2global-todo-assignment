from typing import List

from src.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey


class User(Base):
    __tablename__ = "user"

    user_id: Mapped[str] = mapped_column(unique=True)
    user_name: Mapped[str] = mapped_column(String(120))
    user_email: Mapped[str] = mapped_column(String(120), unique=True)
    password: Mapped[str] = mapped_column(String(120))

    notes: Mapped[List["Notes"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )


class Notes(Base):
    __tablename__ = "notes"

    note_id: Mapped[str] = mapped_column(unique=True)
    note_title: Mapped[str] = mapped_column(String(120))
    note_content: Mapped[str] = mapped_column(String(240))
    created_by: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))

    user: Mapped[User] = relationship(back_populates="notes")
