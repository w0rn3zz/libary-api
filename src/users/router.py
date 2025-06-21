from fastapi import APIRouter, Response, Depends


from src.users.schemas import (
    UserRegisterSchema,
    UserAuthSchema,
    UserUpdateSchema,
    UserResponseSchema,
)
from src.users.dao import UserDAO
from src.exceptions import (
    IncorrectEmailOrPasswordException,
    UserAlreadyExistsException,
    UserIsNotPresentException,
)
from src.users.auth import get_password_hash, authenticate_user, create_access_token
from src.users.dependencies import get_current_user
from src.users.models import User
from src.config import settings

router = APIRouter(prefix="/auth", tags=["Auth & Users"])


@router.post("/register")
async def register_user(user_data: UserRegisterSchema):
    existing_user = await UserDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise UserAlreadyExistsException

    hashed_password = get_password_hash(user_data.password)
    await UserDAO.add(
        email=user_data.email,
        username=user_data.username,
        hashed_password=hashed_password,
    )
    return {"status": "ok", "message": "success"}


@router.post("/login")
async def login_user(response: Response, user_data: UserAuthSchema):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise IncorrectEmailOrPasswordException
    access_token = create_access_token(
        data={"sub": str(user.id)},
    )
    response.set_cookie("libary_access_token", access_token, httponly=True)
    return access_token


@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("libary_access_token")


@router.get("/me", response_model=UserResponseSchema)
async def read_user_me(current_user: User = Depends(get_current_user)):
    if not current_user:
        raise UserIsNotPresentException
    return current_user


@router.delete("/me")
async def delete_user_me(current_user: User = Depends(get_current_user)):
    if not current_user:
        raise UserIsNotPresentException
    await UserDAO.delete_by_id(current_user.id)
    return {"status": "ok", "message": "success"}


@router.patch("/me", response_model=UserResponseSchema)
async def update_user_me(
    user_data: UserUpdateSchema,
    current_user: User = Depends(get_current_user),
):
    update_data = user_data.model_dump(exclude_unset=True)

    if update_data:
        updated_user = await UserDAO.update_user_by_id(
            user_id=current_user.id, **update_data
        )

    return updated_user
