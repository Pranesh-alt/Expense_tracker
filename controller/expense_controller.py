from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas import UserCreate, ExpenseCreate
# from services.user_services import create_user, authenticate_user
from database import get_db
from ..services.expense_services import get_all_expenses 

router = APIRouter()


@router.post("/", response_model=ExpenseCreate)
def get__all__expenses(user: UserCreate, db: Session = Depends(get_db)):
    return get_all_expenses(db, user)
