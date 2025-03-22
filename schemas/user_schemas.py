from pydantic import BaseModel, field_validator, Field, ValidationInfo
from typing import Optional, List




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

