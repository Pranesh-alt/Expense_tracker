from models.user_model import User
from schemas.user_schemas import UserCreate, UserUpdate
from fastapi import HTTPException


def create_user(user_data: UserCreate):
    return User.create_user(user_data)

def get_users():
    users = User.get_users()
    if not users:
        raise HTTPException(status_code=404, detail="Users not found")
    return users

def get_user(user_id: int):
    user = User.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def update_user(user_id: int , user_data: UserUpdate):
    user = User.update_user(user_id,user_data.model_dump())
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def delete_user(user_id: int):
    deleted = User.delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}





