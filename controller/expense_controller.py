from fastapi import APIRouter, Depends, HTTPException, status
from schemas.expense_schemas import ExpenseCreate, ExpenseResponse, ExpenseUpdate,ExpenseCategoryResponse,ExpenseTransactionRespone,ExpenseReport
from services import expense_services
from models.expense_model import user_dependency,Expense
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
    
    return expense_services.get_monthly_reports(user,month,year)


@router.get("/monthlyreport/{year}",response_model=List[ExpenseReport], status_code=status.HTTP_200_OK)
def get_yearly__reports(user:user_dependency,year:int):
    expense = expense_services.get_yearly_reports(user,year)
    return expense


@router.get("/categories/{category}", response_model=List[ExpenseResponse], status_code=status.HTTP_200_OK)
def get__expenses_by_category(user: user_dependency,category: str):
    expense = expense_services.get_expenses_by_category(user,category)
    return expense