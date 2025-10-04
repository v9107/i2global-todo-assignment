import datetime as dt
from sqlalchemy import DateTime
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


def datetime_now():
    return dt.datetime.now(dt.UTC)


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

    created_at: Mapped[dt.datetime] = mapped_column(
        DateTime(),
        default=datetime_now(),
    )
    last_update: Mapped[dt.datetime] = mapped_column(
        DateTime(), default=datetime_now(), onupdate=dt.datetime.now(dt.UTC)
    )
