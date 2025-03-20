from pydantic import BaseModel
from typing import Optional, List

class ExpenseCreate(BaseModel):
    amount: float  # Ensure amount is always a float
    category: str  # Ensure category is a string

class ExpenseResponse:
    

class UserCreate(BaseModel):
    username: str
    password: str

class UserUpdate(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None

class UserResponse(BaseModel):
    id: int
    username: str



    class Config:
        orm_mode = True

