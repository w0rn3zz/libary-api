from pydantic import BaseModel, EmailStr
from typing import Optional

class UserRegisterSchema(BaseModel):
    email: EmailStr
    password: str
    username: str

class UserAuthSchema(BaseModel):
    email: EmailStr
    password: str
    
class UserResponseSchema(BaseModel):
    id: int
    email: str
    username: str

class UserUpdateSchema(BaseModel):
    email: Optional[str] = None
    username: Optional[str] = None
    