from fastapi import APIRouter, Depends

from src.books.schemas import BookAddSchema, BookResponseSchema, BookUpdateSchema
from src.exceptions import (
    BookNotFoundException,
    BookDeleteFailedException,
    BookAddFailedException,
    BookUpdateFailedException,
)
from src.books.dao import BookDAO
from src.users.dependencies import get_current_user
from src.users.models import User


router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/{book_id}")
async def get_book_by_id(
    book_id: int, current_user: User = Depends(get_current_user)
) -> BookResponseSchema:
    book = await BookDAO.find_by_id(book_id)
    if not book:
        raise BookNotFoundException
    return book


@router.post("/add")
async def add_book(data: BookAddSchema, current_user: User = Depends(get_current_user)):
    try:
        await BookDAO.add(**data.model_dump())
        return {"status": "ok", "message": "success"}
    except Exception:
        raise BookAddFailedException


@router.delete("/delete/{book_id}")
async def delete_book_by_id(
    book_id: int, current_user: User = Depends(get_current_user)
):
    try:
        await BookDAO.delete_by_id(book_id)
        return {"status": "ok", "message": "success"}
    except ValueError:
        raise BookDeleteFailedException


@router.patch("/update/{book_id}")
async def update_book_by_id(
    book_id: int, data: BookUpdateSchema, current_user: User = Depends(get_current_user)
) -> BookResponseSchema:
    try:
        return await BookDAO.update_by_id(book_id, **data.model_dump())
    except ValueError:
        raise BookUpdateFailedException
