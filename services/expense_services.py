from fastapi import HTTPException
from models.expense_model import Expense,ExpenseCategory, TransactionType, user_dependency
from schemas.expense_schemas import ExpenseCreate, ExpenseUpdate

# Create Expense
def create_expense(user: user_dependency,expense_data: ExpenseCreate):
    expense = Expense.create_expense(user,expense_data)
    
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    
    return expense
       
    
# Get all Expenses
def get_all_expenses(user:user_dependency):
    expenses = Expense.get_expenses(user)
    
    return expenses if expenses else []  
    
def get_expense_by_id(user: user_dependency,expense_id: int):
    expense = Expense.get_expense_by_id(user,expense_id)
    
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    
    return expense
    
        
def update_expense(user: user_dependency,expense_id:int,expense_data: ExpenseUpdate):
    expense = Expense.update_expense(user,expense_id,expense_data.model_dump())
    
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    
    return expense


def delete_expense(user:user_dependency,expense_id: int):
    expense = Expense.delete_expense(user,expense_id)
    
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    return expense

def expense_categories(user:user_dependency):
    return {"categories": list(ExpenseCategory)}

def expense_transaction_types(user:user_dependency):
    return {"transaction": list(TransactionType)}


def get_monthly_reports(user:user_dependency,month,year):
    report = Expense.get_monthly_reports(user,month,year)
    
    if report is None:
        raise HTTPException(status_code=404, detail="Report not found")
    
    return report

def get_yearly_reports(user:user_dependency,year: int):
    report = Expense.get_yearly_reports(user,year)
    
    if report is None:
        raise HTTPException(status_code=404, detail="Report not found")
    
    return report

def get_expenses_by_category(user: user_dependency,category):
    expenses = Expense.get_expenses_by_category(user,category)
    
    return expenses