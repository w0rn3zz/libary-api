from datetime import datetime
from sqlalchemy import select

from src.books.models import Book
from src.database import async_session
from src.dao.base import BaseDAO
from src.borrows.models import Borrow
from src.readers.dao import ReaderDAO
from src.exceptions import (
    BookNotFoundException,
    BookUnavailableException,
    BorrowLimitExceededException,
    BorrowNotFoundOrAlreadyReturnedException,
    ReaderNotFoundException,
)


class BorrowDAO(BaseDAO):
    model = Borrow

    @classmethod
    async def return_book(cls, book_id: int, reader_id: int):
        async with async_session() as session:
            # Найти активную запись о выдаче (без return_date)
            result = await session.execute(
                select(Borrow)
                .where(
                    Borrow.book_id == book_id,
                    Borrow.reader_id == reader_id,
                    Borrow.return_date == None,
                )
                .order_by(Borrow.borrow_date.desc())
                .limit(1)
            )
            borrow = result.scalar_one_or_none()
            if not borrow:
                raise BorrowNotFoundOrAlreadyReturnedException

            book = await session.get(Book, book_id)
            if not book:
                raise BookNotFoundException

            borrow.return_date = datetime.utcnow()
            book.copies += 1

            await session.commit()

    @classmethod
    async def borrow_book(cls, book_id: int, reader_id: int):
        async with async_session() as session:
            # Загружаем объекты напрямую в этой же сессии
            book = await session.get(Book, book_id)
            if not book:
                raise BookNotFoundException
            if book.copies <= 0:
                raise BookUnavailableException

            reader = await ReaderDAO.find_by_id(reader_id)
            if not reader:
                raise ReaderNotFoundException

            active_borrows = await session.execute(
                select(Borrow).where(
                    Borrow.reader_id == reader_id, Borrow.return_date == None
                )
            )
            active_borrow_list = active_borrows.scalars().all()

            if len(active_borrow_list) >= 3:
                raise BorrowLimitExceededException

            borrow = Borrow(book_id=book.id, reader_id=reader.id)
            session.add(borrow)

            book.copies -= 1

            await session.commit()
            return borrow

    @classmethod
    async def get_reader_active_borrows(cls, reader_id: int):
        async with async_session() as session:
            query = select(Borrow).where(
                    Borrow.reader_id == reader_id, Borrow.return_date == None
                )
            active_borrows = await session.execute(query)
            return active_borrows.scalars().all()
            