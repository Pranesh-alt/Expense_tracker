from fastapi import APIRouter, Depends, HTTPException, status
from schemas.expense_schemas import ExpenseCreate, ExpenseResponse, ExpenseUpdate,ExpenseCategoryResponse,ExpenseTransactionRespone,ExpenseReport,MonthlyExpenseAmount,DailyExpenseAmount, YearlyExpenseAmount
from services import expense_services
from models.expense_model import user_dependency
from datetime import datetime
from typing import List
router = APIRouter()


@router.get("/", response_model=list[ExpenseResponse], status_code=status.HTTP_200_OK)
def get__all__expenses(user:user_dependency):
    return expense_services.get_all_expenses(user)


@router.get("/{expense_id}",response_model=ExpenseResponse, status_code=status.HTTP_200_OK)
def get__expense__by__id(user: user_dependency,expense_id:int):
    return expense_services.get_expense_by_id(user,expense_id)


@router.post("/", response_model=ExpenseResponse, status_code=status.HTTP_201_CREATED)
def create__expense(user:user_dependency, expense: ExpenseCreate):
    return expense_services.create_expense(user,expense)
    

@router.put("/{expense_id}",response_model=ExpenseResponse, status_code=status.HTTP_201_CREATED)
def update__expense(user: user_dependency,expense_id:int,expense_data: ExpenseUpdate):
    return expense_services.update_expense(user,expense_id,expense_data)


@router.delete("/{expense_id}", response_model=ExpenseResponse, status_code=status.HTTP_200_OK)
def delete__expense(user:user_dependency,expense_id: int):
    return expense_services.delete_expense(user,expense_id)

@router.get("/categories", response_model=ExpenseCategoryResponse, status_code=status.HTTP_200_OK)
def expenses__categories(user:user_dependency):
    return expense_services.expense_categories(user)
    
@router.get("/transaction", response_model=ExpenseTransactionRespone, status_code=status.HTTP_200_OK)
def expenses_transaction_types(user:user_dependency):
    return expense_services.expense_transaction_types(user)    

@router.get("/monthlyreport/{year}/{month}",response_model=List[ExpenseReport], status_code=status.HTTP_200_OK)
def get_monthly__reports(user:user_dependency,month: int,year: int):
    expense = expense_services.get_monthly_reports(user,month,year)
    return expense

@router.get("/monthlyreport/{year}",response_model=List[ExpenseReport], status_code=status.HTTP_200_OK)
def get_yearly__reports(user:user_dependency,year:int):
    expense = expense_services.get_yearly_reports(user,year)
    return expense

@router.get("/dailyreport/{year}/{month}/{day}", response_model=List[ExpenseReport], status_code=status.HTTP_200_OK)
def get__daily__report(user:user_dependency,day: int,month:int,year: int):
    amount = expense_services.get_daily_reports(user,day,month,year)
    return amount
    

@router.get("/transactions/{transaction}", response_model=List[ExpenseResponse], status_code=status.HTTP_200_OK)
def get__expenses__by__transaction(user: user_dependency,transaction: str):
    expense = expense_services.get_expenses_by_transaction(user,transaction)
    return expense

@router.get("/categories/{category}", response_model=List[ExpenseResponse], status_code=status.HTTP_200_OK)
def get__expenses_by_category(user: user_dependency,category: str):
    expense = expense_services.get_expenses_by_category(user,category)
    return expense

@router.get("/monthlyreport/{year}/{month}/amount", response_model=MonthlyExpenseAmount, status_code=status.HTTP_200_OK)
def get__monthly__amount(user:user_dependency,month: int,year: int):
    amount = expense_services.get_monthly_amount(user,month,year)
    return amount
    
@router.get("/dailyreport/{year}/{month}/{day}/amount", response_model=DailyExpenseAmount, status_code=status.HTTP_200_OK)
def get__daily__amount(user:user_dependency,year: int,month:int,day: int):
    amount = expense_services.get_daily_amount(user,year,month,day)
    return amount
    
    
@router.get("/yearlyreport/{year}/amount",response_model=YearlyExpenseAmount, status_code=status.HTTP_200_OK)
def get_yearly__amount(user:user_dependency,year:int):
    expense = expense_services.get_yearly_amount(user,year)
    return expense