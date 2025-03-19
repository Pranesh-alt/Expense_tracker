from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.user_services import update_user, get_user, get_users, delete_user, create_user
from schemas import UserCreate, UserUpdate, UserResponse
from database import get_db

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse)
def create__user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get("/", response_model=list[UserResponse])
def get__users(db: Session = Depends(get_db)):
    return get_users(db)

@router.get("/{user_id}", response_model=UserResponse)
def get__user(user_id: int, db: Session = Depends(get_db)):
    return get_user(db, user_id)

@router.put("/", response_model=UserResponse)
def update__user(user: UserUpdate, db: Session = Depends(get_db)):
    return update_user(db, user)

@router.delete("/{user_id}")
def delete__user(user_id: int, db: Session = Depends(get_db)):
    return delete_user(db, user_id)
