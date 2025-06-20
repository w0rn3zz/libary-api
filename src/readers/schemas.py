from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class ReaderBaseSchema(BaseModel):
    email: EmailStr
    name: str
    
class ReaderResponseSchema(ReaderBaseSchema): 
    id: int

class ReaderUpdateSchema(ReaderBaseSchema):
    email: Optional[EmailStr] = None
    name: Optional[str] = None

class ReaderAddSchema(ReaderBaseSchema):
    pass
    