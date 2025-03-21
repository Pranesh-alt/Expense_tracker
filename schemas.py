from pydantic import BaseModel, field_validator, Field, ValidationInfo
from typing import Optional, List
from datetime import datetime
from models import TransactionType, ExpenseCategory

class ExpenseCreate(BaseModel):
    amount: float  # Ensure amount is always a float
    category: str  # Ensure category is a string
    transaction: str
    user_id : int
    
    @field_validator("transaction", "category", mode="before")
    @classmethod
    def convert_to_enum(cls, value: str, info: ValidationInfo):
        field_name = info.field_name  # Gets the field being validated
        
        if field_name == "category":
            value_upper = value.upper()
            if value_upper not in ExpenseCategory.__members__:
                raise ValueError(f"Invalid category type: {value}. Must be one of {list(ExpenseCategory.__members__.keys())}")
            return value_upper
        
        if field_name == "transaction":
            value_upper = value.upper()
            if value_upper not in TransactionType.__members__:
                raise ValueError(f"Invalid transaction type: {value}. Must be one of {list(TransactionType.__members__.keys())}")
            return value_upper  # Ensures it's stored
    
    

class ExpenseResponse(BaseModel):
    id: int
    amount: float
    category: str
    transaction: str
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

