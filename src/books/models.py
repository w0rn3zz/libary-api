from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import validates

from src.database import Base

class Book(Base):
    __tablename__ = 'books'

    title: Mapped[str] = mapped_column(nullable=False)
    author: Mapped[str] = mapped_column(nullable=False)
    publication_year: Mapped[int] = mapped_column(nullable=True)
    isbn: Mapped[str] = mapped_column(unique=True, nullable=True)
    copies: Mapped[int]= mapped_column(default=1, nullable=False)

    @validates('copies')
    def validate_copies(self, key, value):
        if value < 0:
            raise ValueError("Количество экземпляров не может быть меньше 0")
        return value
