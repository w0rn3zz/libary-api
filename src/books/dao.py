from src.dao.base import BaseDAO
from src.books.models import Book

class BookDAO(BaseDAO):
    model = Book