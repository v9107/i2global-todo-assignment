import datetime as dt

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from src.services.auth import auth_service
from src.dependencies import SessionDeps
from src.schemas.user import CreateUser, UserDetails
from src.services.user import UserService
from src.config import app_config


router = APIRouter(tags=["Auth"], prefix="/auth")


@router.post("/login")
async def login(session: SessionDeps, payload: OAuth2PasswordRequestForm = Depends()):
    user_service = UserService(session)

    user = user_service.retrive_by_email(email=payload.username)

    if not user or not auth_service.verify_password(payload.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )

    access_token_expires = dt.timedelta(minutes=app_config.access_token_expire_minutes)
    access_token = auth_service.create_access_token(
        data={"sub": str(user.user_id)}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/register")
def create_users(session: SessionDeps, payload: CreateUser) -> UserDetails:
    user_repo = UserService(session=session)
    return user_repo.register(user=payload)
