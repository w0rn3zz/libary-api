from fastapi import APIRouter, Depends

from src.users.models import User
from src.users.dependencies import get_current_user
from src.borrows.dao import BorrowDAO


router = APIRouter(tags=["Borrows"], prefix="/borrows")

@router.post("/take")
async def borrow_book(reader_id: int, book_id: int, current_user: User = Depends(get_current_user)):
    await BorrowDAO.borrow_book(book_id=book_id, reader_id=reader_id)
    return {"message": "Книга выдана"}

@router.post("/return")
async def return_book(book_id: int, reader_id: int, current_user: User = Depends(get_current_user)):
    await BorrowDAO.return_book(book_id, reader_id)
    return {"message": "Книга возвращена"}
    
    