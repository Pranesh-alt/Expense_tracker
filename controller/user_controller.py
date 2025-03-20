from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.user_services import update_user, get_user, get_users, delete_user, create_user
from schemas import UserCreate, UserUpdate, UserResponse

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse)
def create__user(user: UserCreate):
    return create_user(user)

@router.get("/", response_model=list[UserResponse])
def get__users():
    return get_users()

@router.get("/{user_id}", response_model=UserResponse)
def get__user(user_id: int):
    return get_user(user_id)

@router.put("/{user_id}", response_model=UserResponse)
def update__user(user_id:int,user_data: UserUpdate):
    return update_user(user_id, user_data)

@router.delete("/{user_id}")
def delete__user(user_id: int):
    return delete_user(user_id)
