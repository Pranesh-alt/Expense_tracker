from fastapi import HTTPException
from models.expense_model import Expense,ExpenseCategory, TransactionType, user_dependency
from schemas.expense_schemas import ExpenseCreate, ExpenseUpdate

# Create Expense
def create_expense(user: user_dependency,expense_data: ExpenseCreate):
    
    if user is None:
                 raise HTTPException(status_code=401, detail='authentication failed')
    
    expense = Expense.create_expense(user,expense_data)
    
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    
    return expense
       
    
# Get all Expenses
def get_all_expenses(user:user_dependency):
    
    if user is None:
        raise HTTPException(status_code=401, detail='authentication failed')
    
    expenses = Expense.get_expenses(user)
    
    return expenses if expenses else []  
    
def get_expense_by_id(user: user_dependency,expense_id: int):
    
    if user is None:
        raise HTTPException(status_code=401, detail='authentication failed')
    
    expense = Expense.get_expense_by_id(user,expense_id)
    
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    
    return expense
    
        
def update_expense(user: user_dependency,expense_id:int,expense_data: ExpenseUpdate):
    
    if user is None:
        raise HTTPException(status_code=401, detail='authentication failed')
    
    expense = Expense.update_expense(user,expense_id,expense_data.model_dump())
    
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    
    return expense


def delete_expense(user:user_dependency,expense_id: int):
    
    if user is None:
        raise HTTPException(status_code=401, detail='authentication failed')
    expense = Expense.delete_expense(user,expense_id)
    
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    return expense

def expense_categories(user:user_dependency):
    
    if user is None:
        raise HTTPException(status_code=401, detail='authentication failed')
    
    return {"categories": list(ExpenseCategory)}

def expense_transaction_types(user:user_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='authentication failed')
    return {"transaction": list(TransactionType)}


def get_monthly_reports(user:user_dependency,month,year):
    
    if user is None:
        raise HTTPException(status_code=401, detail='authentication failed')

    
    report = Expense.get_monthly_reports(user,month,year)
    
    if report is None:
        raise HTTPException(status_code=404, detail="Report not found")
    
    return report

def get_yearly_reports(user:user_dependency,year: int):
    
    if user is None:
         raise HTTPException(status_code=401, detail='authentication failed')
    
    if year is None:
        raise HTTPException(status_code=400, detail="Year is required.")
    
    report = Expense.get_yearly_reports(user,year)
    
    if report is None:
        raise HTTPException(status_code=404, detail="Report not found")
    
    return report

def get_expenses_by_category(user: user_dependency,category):
    
    if user is None:
                 raise HTTPException(status_code=401, detail='authentication failed')
    
    expenses = Expense.get_expenses_by_category(user,category)
    
    if expenses is None:
        raise HTTPException(status_code=404, detail="Category not found")
    
    return expenses

def get_expenses_by_transaction(user: user_dependency,transaction):
    
    if user is None:
                 raise HTTPException(status_code=401, detail='authentication failed')
    
    expenses = Expense.get_expenses_by_transaction(user,transaction)
    
    if expenses is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    
    return expenses

def get_monthly_amount(user:user_dependency,month,year):
    if user is None:
            raise HTTPException(status_code=401, detail='Authentication failed')

    if month is None or year is None:
            raise HTTPException(status_code=400, detail="Month and year are required.")

    report = Expense.get_monthly_amount(user,month,year)
    
    if report is None:
        raise HTTPException(status_code=404, detail="Amount not found")
    
    return report

def get_daily_amount(user:user_dependency,year,month,date):
        if user is None:
            raise HTTPException(status_code=401, detail='Authentication failed')
        if year is None:
            raise HTTPException(status_code=400, detail="Year is required.")
        if month is None:
            raise HTTPException(status_code=400, detail="Month is required.")
        if date is None:
            raise HTTPException(status_code=400, detail="Date is required.")
        
    
        report = Expense.get_daily_amount(user,year,month,date)
    
        if report is None:
          raise HTTPException(status_code=404, detail="Amount not found")
    
        return report

def get_daily_reports(user:user_dependency, day,month,year):
    
    if user is None:
                 raise HTTPException(status_code=401, detail='authentication failed')
    
    report = Expense.get_daily_reports(user,day,month,year)
    
    if report is None:
        raise HTTPException(status_code=404, detail="Report not found")
    
    return report