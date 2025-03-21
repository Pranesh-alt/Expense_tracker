from fastapi import APIRouter, Depends, HTTPException, status
from schemas import UserCreate, ExpenseCreate, ExpenseResponse, ExpenseUpdate
from services.expense_services import get_all_expenses , create_expense, update_expense

router = APIRouter()


@router.get("/", response_model=list[ExpenseResponse], status_code=status.HTTP_200_OK)
def get__all__expenses():
    return get_all_expenses()


@router.post("/", response_model=ExpenseResponse, status_code=status.HTTP_201_CREATED)
def create__expense(expense: ExpenseCreate):
    return create_expense(expense)
    


@router.put("/{expense_id}", status_code=status.HTTP_201_CREATED)
def update__expense(expense_id: int, expense_data: ExpenseUpdate):
    return update_expense(expense_data)