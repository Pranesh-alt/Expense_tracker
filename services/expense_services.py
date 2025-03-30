from fastapi import HTTPException
from models.expense_model import Expense,ExpenseCategory, TransactionType, user_dependency
from schemas.expense_schemas import ExpenseCreate, ExpenseUpdate
from services.expense_services import user_dependency  # noqa: F811
from Validators.expense_validators import date_month_year_validator, month_year_validator,year_validator,user_validator

# Create Expense
def create_expense(user: user_dependency,expense_data: ExpenseCreate):
    
    user_validator(user)
    
    expense = Expense.create_expense(user,expense_data)
    
    return expense
       
# Get all Expenses
def get_all_expenses(user:user_dependency):
    
    user_validator(user)
    
    expenses = Expense.get_expenses(user)
    
    return expenses if expenses else []  
    
def get_expense_by_id(user: user_dependency,expense_id: int):
    
    user_validator(user)
    
    if expense_id is None:
        raise HTTPException(status_code=400, detail="Expense ID is required.")
    
    expense = Expense.get_expense_by_id(user,expense_id)
    
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    
    return expense
    
        
def update_expense(user: user_dependency,expense_id:int,expense_data: ExpenseUpdate):
    
    user_validator(user)
    
    if expense_id is None:
        raise HTTPException(status_code=400, detail="Expense ID is required.") 
    
    expense = Expense.update_expense(user,expense_id,expense_data.model_dump())
    
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    
    return expense


def delete_expense(user:user_dependency,expense_id: int):
    user_validator(user)
    
    if expense_id is None:
        raise HTTPException(status_code=400, detail="Expense ID is required.")
    
    expense = Expense.delete_expense(user,expense_id)
    
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    return expense

def expense_categories(user:user_dependency):
    
    user_validator(user)
    
    return {"categories": list(ExpenseCategory)}

def expense_transaction_types(user:user_dependency):
    user_validator(user)
    
    return {"transaction": list(TransactionType)}


def get_monthly_reports(user:user_dependency,month,year):
    
    user_validator(user)
    
    month_year_validator(month,year)
    
    report = Expense.get_monthly_reports(user,month,year)
    
    if report is None:
        raise HTTPException(status_code=404, detail="Report not found")
    
    return report

def get_yearly_reports(user:user_dependency,year):
    
    user_validator(user)
    
    year_validator(year)
    
    report = Expense.get_yearly_reports(user,year)
    
    if report is None:
        raise HTTPException(status_code=404, detail="Report not found")
    
    return report

def get_expenses_by_category(user: user_dependency,category):
    
    user_validator(user)
        
    if category is None:
        raise HTTPException(status_code=400, detail="Category is requird.")
    
    expenses = Expense.get_expenses_by_category(user,category)
    
    if expenses is None:
        raise HTTPException(status_code=404, detail="Category not found")
    
    return expenses

def get_expenses_by_transaction(user: user_dependency,transaction):
    
    user_validator(user)
             
    if transaction is None:
        raise HTTPException(status_code=400, detail="Transaction is requird.")        
    
    expenses = Expense.get_expenses_by_transaction(user,transaction)
    
    if expenses is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    
    return expenses

def get_monthly_amount(user:user_dependency,month,year):
    user_validator(user)
     
    month_year_validator(month,year) 

    report = Expense.get_monthly_amount(user,month,year)
    
    if report is None:
        raise HTTPException(status_code=404, detail="Amount not found")
    
    return report

def get_yearly_amount(user: user_dependency,year):
    user_validator(user)
    
    year_validator(year)
    
    amount = Expense.get_yearly_amount(user,year)
    
    if amount is None:
        raise HTTPException(status_code=404, detail="Amount not found")
    
    return amount


def get_daily_amount(user:user_dependency,year,month,date):
    user_validator(user)
        
    date_month_year_validator(date,month,year)
        
    report = Expense.get_daily_amount(user,year,month,date)
    
    if report is None:
        raise HTTPException(status_code=404, detail="Amount not found")
    
    return report

def get_daily_reports(user:user_dependency, day,month,year):
    
    user_validator(user)
    
    date_month_year_validator(day,month,year)
    
    report = Expense.get_daily_reports(user,day,month,year)
    
    if report is None:
        raise HTTPException(status_code=404, detail="Report not found")
    
    return report

def get_weekly_reports(user:user_dependency, day,month,year):
    
    user_validator(user)
    
    date_month_year_validator(day,month,year)
    
    report = Expense.get_weekly_report(user,day,month,year)
    
    if report is None:
        raise HTTPException(status_code=404, detail="Report not found")
    
    return report


def get_weekly_amount(user: user_dependency,year,month,date):
    user_validator(user)
     
    date_month_year_validator(date,month,year)
    
    amount = Expense.get_weekly_amount(user,year,month,date)
    
    return amount

