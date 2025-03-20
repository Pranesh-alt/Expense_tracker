from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate, UserUpdate
from fastapi import HTTPException

def create_user(db: Session, user_data: UserCreate):
    return User.create_user(db, user_data)

def get_users(db: Session):
    users = User.get_users(db)
    if not users:
        raise HTTPException(status_code=404, detail="Users not found")
    return users

def get_user(db: Session, user_id: int):
    user = User.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def update_user(db: Session,user_id: int , user_data: UserUpdate):
    user = User.update_user(db, user_id,user_data)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def delete_user(db: Session, user_id: int):
    deleted = User.delete_user(db, user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}





