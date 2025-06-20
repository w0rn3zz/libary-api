from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class BorrowResponseSchema(BaseModel):
    id: int
    book_id: int
    reader_id: int
    borrow_date: datetime
    return_date: Optional[datetime] = None
