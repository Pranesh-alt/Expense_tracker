from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Enum
from sqlalchemy.orm import session, relationship, Mapped, mapped_column, Session
from datetime import datetime
from typing import Optional, List
import enum
from database import Base, SessionLocal
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    password: Mapped[str] = mapped_column(String)
    expenses: Mapped["Expense"] = relationship("Expense", back_populates="user")

    # Data Access Object (DAO) Methods
    @staticmethod
    def create_user(user_credentials):
        with SessionLocal() as db:
           hashed_password = pwd_context.hash(user_credentials.password)
           db_user = User(id = db.query(User).count() + 1,username = user_credentials.username ,password = hashed_password)
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
         return True


class TransactionType(str, enum.Enum):
    CREDIT = "credit"
    DEBIT = "debit"

class Expense(Base):
    __tablename__ = "expenses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    amount: Mapped[float] = mapped_column(Float)
    category: Mapped[str] = mapped_column(String(255))
    transaction: Mapped[TransactionType] = mapped_column(Enum(TransactionType), nullable=False)
    time: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship("User", back_populates="expenses")
    
    
    @staticmethod
    def get_expenses():
        with SessionLocal() as db:
          return db.query(Expense).all()
    
    
    @staticmethod
    def create_expense(expense_data):
        with SessionLocal() as db:
         try:
             transaction_type = TransactionType(expense_data.transaction)
         finally: 
            expense = Expense(id = db.query(Expense).count() + 1,amount = expense_data.amount, category= expense_data.category,transaction = transaction_type)
            db.add(expense_data)
            db.commit()
            db.refresh(expense_data)
        
         return expense
        



