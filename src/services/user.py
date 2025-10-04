import uuid
from sqlalchemy.orm import Session
from src.services.auth import auth_service
from src.database.tables.users import User
from src.repository.users import UserRepository
from src.schemas.user import CreateUser, UpdateUser


class UserService:
    def __init__(self, session: Session):
        self._user_repo = UserRepository(session=session)

    def register(self, user: CreateUser):
        user_id = str(uuid.uuid4())
        data = user.model_dump()

        raw_psswd = data.pop("password")
        hashed_psswd = self._hash_password(raw_psswd)
        data["user_id"] = user_id
        data["password"] = hashed_psswd
        return self._user_repo.create(data=data)

    def retrive(self):
        return self._user_repo.get_by([])

    def retrive_by_user_id(self, user_id: str) -> User:
        user = self._user_repo.get_by([User.user_id == user_id], limit=1)
        if len(user) > 0:
            return user[0]
        else:
            raise Exception

    def retrive_by_email(self, email: str) -> User:
        users = self._user_repo.get_by([User.user_email == email], limit=1)
        if len(users) == 0:
            raise Exception

        return users[0]

    def update(self, pk: str | int, user: UpdateUser) -> User:
        user_dict = user.model_dump(exclude_unset=True)
        user: User | None = self._user_repo.update_one(pk, user_dict)
        if not user:
            raise Exception
        else:
            return user

    def _hash_password(self, raw_psswd: str):
        return auth_service.hash_password(raw_psswd)

    def verify_password(self, raw_psswd: str, hashed_psswd: str) -> bool:
        return auth_service.verify_password(raw_psswd, hashed_psswd)
