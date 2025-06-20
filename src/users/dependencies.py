from datetime import datetime
from fastapi import Request, Depends
from jose import jwt, JWTError

from src.config import settings
from src.users.dao import UserDAO
from src.users.models import User
from src.exceptions import (
    TokenAbsentException,
    TokenExpiredException,
    IncorrectTokenFormatException,
    UserIsNotPresentException,
)


def get_token(request: Request):
    token = request.cookies.get("libary_access_token")
    if not token:
        raise TokenAbsentException
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(token, settings.app.SECRET_KEY, settings.app.ALGORITHM)
    except JWTError:
        IncorrectTokenFormatException
    expire: str = payload.get("exp")
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise TokenExpiredException
    user_id: str = payload.get("sub")
    if not user_id:
        UserIsNotPresentException
    user = await UserDAO.find_by_id(int(user_id))
    if not user:
        raise UserIsNotPresentException
    return user
