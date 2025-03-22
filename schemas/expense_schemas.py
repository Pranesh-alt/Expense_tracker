from pydantic import BaseModel, field_validator, Field, ValidationInfo
from typing import Optional, List
from datetime import datetime
from models.expense_model import TransactionType, ExpenseCategory



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



class ExpenseCategoryResponse(BaseModel):
    categories: list[ExpenseCategory]

class ExpenseTransactionRespone(BaseModel):
    transaction: list[TransactionType]
