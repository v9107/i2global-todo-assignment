from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from src.config import app_config
from passlib.context import CryptContext


class AuthService:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(AuthService, cls).__new__(cls)
        return cls.instance

    def create_access_token(self, data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + (
            expires_delta or timedelta(minutes=app_config.access_token_expire_minutes)
        )
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(
            to_encode, app_config.secret_key, algorithm=app_config.algorithm
        )
        return encoded_jwt

    def verify_access_token(self, token: str):
        try:
            payload = jwt.decode(
                token, app_config.secret_key, algorithms=[app_config.algorithm]
            )
            return payload
        except JWTError:
            return None

    def hash_password(self, password: str) -> str:
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(plain_password, hashed_password)


auth_service = AuthService()
