from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base

class Borrow(Base):
    __tablename__ = 'borrows'

    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"), nullable=False)
    reader_id: Mapped[int] = mapped_column(ForeignKey("readers.id"), nullable=False)
    borrow_date: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    return_date: Mapped[datetime] = mapped_column(nullable=False)
