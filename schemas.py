from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from models import TransactionType

class ExpenseCreate(BaseModel):
    amount: float  # Ensure amount is always a float
    category: str  # Ensure category is a string
    transaction: Optional[str] = None
    user_id : int

class ExpenseResponse(BaseModel):
    id: int
    amount: float
    category: str
    transaction: TransactionType
    time: datetime
    user_id: int

    class Config:
        from_attributes = True  # Enables ORM serialization in FastAPI
    

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

