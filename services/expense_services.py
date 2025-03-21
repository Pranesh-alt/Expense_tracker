from fastapi import HTTPException
from models import Expense
from schemas import ExpenseCreate, ExpenseUpdate

# Create Expense
def create_expense(expense_data: ExpenseCreate):
    expense = Expense.create_expense(expense_data)
    
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    
    return expense
    
    
    
# Get all Expenses
def get_all_expenses():
    expenses = Expense.get_expenses()
    
    return expenses if expenses else []  
    
def update_expense(expense_id:int,expense_data: ExpenseUpdate):
    expense = Expense.update_expense(expense_id,expense_data.model_dump())
    
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    
    return expense



    