from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas import UserCreate, ExpenseCreate, ExpenseResponse
from services.expense_services import get_all_expenses 

router = APIRouter()


@router.get("/", response_model=list[ExpenseResponse], status_code=status.HTTP_200_OK)
def get__all__expenses():
    return get_all_expenses()


# @router.post("/", response_model=ExpenseCreate, status_code=status.HTTP_201_CREATED)
# def create_expense()

