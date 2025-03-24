from pydantic import BaseModel, field_validator, Field, ValidationInfo, ConfigDict
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
        model_config = ConfigDict(from_attributes=True)
    
class ExpenseUpdate(BaseModel):
    amount: Optional[float] = Field(None, gt=0) 
    category: Optional[ExpenseCategory] = None
    transaction: Optional[TransactionType] = None



class ExpenseCategoryResponse(BaseModel):
    categories: list[ExpenseCategory]

class ExpenseTransactionRespone(BaseModel):
    transaction: list[TransactionType]


class ExpenseReport(BaseModel):
    id: int
    amount: float
    category: str
    transaction: str
    time: datetime

class MonthlyExpenseAmount(BaseModel):
    month: int
    year: int
    total_expense: float
    
class DailyExpenseAmount(BaseModel):
    month: int
    year: int
    date: int
    total_expense: float
    
class YearlyExpenseAmount(BaseModel):
    year: int
    total_expense: float