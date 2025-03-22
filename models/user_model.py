from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime,Boolean, Enum
from sqlalchemy.orm import session, relationship, Mapped, mapped_column, Session
from datetime import datetime
from typing import Optional, List
import enum
from sqlalchemy import Enum
from database import Base, SessionLocal
from passlib.context import CryptContext
from models.expense_model import Expense

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    password: Mapped[str] = mapped_column(String)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    # Data Access Object (DAO) Methods
    @staticmethod
    def create_user(user_credentials):
        with SessionLocal() as db:
           hashed_password = pwd_context.hash(user_credentials.password)
           db_user = User(id = db.query(User).count() + 1,
                          username = user_credentials.username ,
                          password = hashed_password,
                          )
           db.add(db_user)
           db.commit()
           db.refresh(db_user)
           return db_user

    @staticmethod
    def get_users():
        with SessionLocal() as db:
         return db.query(User).all() or []

    @staticmethod
    def get_user(user_id: int):
        with SessionLocal() as db: 
           return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def update_user(user_id: int, user_credentials: dict):
        with SessionLocal() as db:
         user = db.query(User).filter(User.id == user_id).first()
         if not user:
             return None  
                
         if 'username' in user_credentials:
            user.username = user_credentials['username']
         if 'password' in user_credentials:
            user.password = pwd_context.hash(user_credentials['password'])
            
         db.commit()
         db.refresh(user)
        
         return user


    @staticmethod
    def delete_user(user_id: int):
        with SessionLocal() as db:
         user = db.query(User).filter(User.id == user_id).first()
         if not user:
             return None

         db.delete(user)
         db.commit()
    
    
    @staticmethod
    def authenticate_user(username: str, password: str):
        with SessionLocal() as db:
            user = db.query(User).filter(User.username == username).first()
            
            if not user:
                return False
            if not pwd_context.verify(password,user.password):
                return False
            return user