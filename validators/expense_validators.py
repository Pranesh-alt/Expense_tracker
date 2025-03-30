from fastapi import HTTPException

def date_month_year_validator(date,month,year):
    if year is None:
        raise HTTPException(status_code=400, detail="Year is required.")
    if month is None:
        raise HTTPException(status_code=400, detail="Month is required.")
    if date is None:
        raise HTTPException(status_code=400, detail="Date is required.")
    
    
def month_year_validator(month,year):
    if month is None or year is None:
            raise HTTPException(status_code=400, detail="Month and year are required.")

def year_validator(year):
    if year is None:
        raise HTTPException(status_code=400, detail="Year is required.")
    
def user_validator(user):
    if user is None:
        raise HTTPException(status_code=401, detail='authentication failed')
    
def expense_id_validator(expense_id):
    if expense_id is None:
        raise HTTPException(status_code=400, detail="Expense ID is required.")
