from sqlalchemy.orm import Session
from models import Expense

# Create Expense
def create_expense(db: Session, expense_data):
    expense = Expense(amount=expense_data.amount, category=expense_data.category, user_id=expense_data.user_id)
    db.add(expense)
    db.commit()
    db.refresh(expense)
    return {"message": "Expense added successfully"}

# Get all Expenses
def get_all_expenses(db: Session):
    return Expense.get_users(db)
    



