from datetime import datetime, timedelta, timezone

import bcrypt
import jwt

from pydantic import EmailStr

from src.config import settings
from src.users.dao import UserDAO
from src.users.models import User

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))

def get_password_hash(password: str) -> str:
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    return hashed_password.decode("utf-8")

async def authenticate_user(email: EmailStr, password: str):
    user: User = await UserDAO.find_one_or_none(email=email)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(days=360)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.app.SECRET_KEY, algorithm=settings.app.ALGORITHM)
    return encoded_jwt