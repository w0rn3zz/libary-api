from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class BookBaseSchema(BaseModel):
    title: str
    author: str
    publication_year: Optional[int] = None
    isbn: Optional[str] = None
    copies: int = Field(default=1, ge=0)


class BookResponseSchema(BookBaseSchema):
    id: int


class BookUpdateSchema(BookBaseSchema):
    title: Optional[str] = None
    author: Optional[str] = None
    publication_year: Optional[int] = None
    isbn: Optional[str] = None
    copies: Optional[int] = Field(default=None, ge=0)


class BookAddSchema(BookBaseSchema):
    pass
