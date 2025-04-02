from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    username: str
    password: str

class UserUpdate(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None

class UserResponse(BaseModel):
    id: int
    username: str
    password: str

    class Config:
        orm_mode = True

class DeleteResponse(BaseModel):
    message: str

class Token(BaseModel):
    access_token: str
    token_type: str