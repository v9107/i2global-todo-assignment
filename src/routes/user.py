from fastapi import APIRouter
from src.dependencies import CurrentUser, SessionDeps
from src.schemas.user import UserDetails, UpdateUser
from src.services.user import UserService

router = APIRouter(tags=["User"], prefix="/user")


@router.get("/all")
def users(
    session: SessionDeps, user: CurrentUser, skip: int = 0, limit: int = 100
) -> list[UserDetails]:
    user_service = UserService(session=session)
    return user_service.retrive()


@router.patch("/{user_id}")
def update_user(
    session: SessionDeps, user: CurrentUser, user_id: str, payload: UpdateUser
) -> UserDetails:
    user_service = UserService(session)
    user = user_service.update(user_id, payload)
    return user


@router.get("/{user_id}")
def retrive_user(session: SessionDeps, user: CurrentUser, user_id: str) -> UserDetails:
    user_service = UserService(session)
    user = user_service.retrive_by_user_id(user_id=user_id)
    return user
