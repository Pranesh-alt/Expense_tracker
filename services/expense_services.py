from sqlalchemy.orm import Session
from models import Expense
from schemas import ExpenseCreate, ExpenseUpdate

# Create Expense
def create_expense(expense_data: ExpenseCreate):
    return Expense.create_expense(expense_data)
    
    
    
# Get all Expenses
def get_all_expenses():
    return Expense.get_expenses()


def update_expense(expense_data: ExpenseUpdate):
    return Expense.update_expense(expense_data)
    
    



    