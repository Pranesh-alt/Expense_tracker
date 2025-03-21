from pydantic import BaseModel, field_validator, Field, ValidationInfo
from typing import Optional, List
from datetime import datetime
from models import TransactionType, ExpenseCategory

class ExpenseCreate(BaseModel):
    amount: float  
    category: ExpenseCategory  
    transaction: TransactionType
    user_id : int
    

class ExpenseResponse(BaseModel):
    id: int
    amount: float
    category: ExpenseCategory
    transaction: TransactionType
    time: datetime
    user_id: int
    
    
    class Config:
        from_attributes = True  # Enables ORM serialization in FastAPI
    
class ExpenseUpdate(BaseModel):
    amount: Optional[float] = Field(None, gt=0) 
    category: Optional[ExpenseCategory] = None
    transaction: Optional[TransactionType] = None



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

