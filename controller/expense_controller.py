from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas import UserCreate, ExpenseCreate, ExpenseResponse
from database import get_db
from services.expense_services import get_all_expenses 

router = APIRouter()


@router.get("/", response_model=list[ExpenseResponse], status_code=status.HTTP_200_OK)
def get__all__expenses(db: Session = Depends(get_db)):
    return get_all_expenses(db)


