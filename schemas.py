from pydantic import BaseModel
from typing import Optional, List

class ExpenseCreate(BaseModel):
    amount: float  # Ensure amount is always a float
    category: str  # Ensure category is a string

class UserCreate(BaseModel):
    username: str
    password: str
    expenses: Optional[List[ExpenseCreate]] = []

class UserUpdate(BaseModel):
    id: int
    username: Optional[str] = None
    password: Optional[str] = None
    expenses: Optional[float] = None

class UserResponse(BaseModel):
    id: int
    username: str
    expenses: float

    class Config:
        orm_mode = True

