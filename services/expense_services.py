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
def get_all_expenses():
    expenses = Expense.get_expenses()
    
    return expenses if expenses else []  
    
def update_expense(expense_id:int,expense_data: ExpenseUpdate):
    expense = Expense.update_expense(expense_id,expense_data.model_dump())
    
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    
    return expense


def delete_expense(expense_id: int):
    expense = Expense.delete_expense(expense_id)
    
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    return expense

def expense_categories():
    return {"categories": list(ExpenseCategory)}

def expense_transaction_types():
    return {"transaction": list(TransactionType)}


def get_monthly_reports(user_id,month,year):
    report = Expense.get_monthly_reports(user_id,month,year)
    
    if report is None:
        raise HTTPException(status_code=404, detail="Report not found")
    
    return report

def get_yearly_reports(user_id,year):
    report = Expense.get_yearly_reports(user_id,year)
    
    if report is None:
        raise HTTPException(status_code=404, detail="Report not found")
    
    return report