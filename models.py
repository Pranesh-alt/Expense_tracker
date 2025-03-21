from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Enum
from sqlalchemy.orm import session, relationship, Mapped, mapped_column, Session
from datetime import datetime
from typing import Optional, List
import enum
from sqlalchemy import Enum
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


# Enum for Expense Category
class ExpenseCategory(str, enum.Enum):
    FOOD = "FOOD"
    TRAVEL = "TRAVEL"
    ENTERTAINMENT = "ENTERTAINMENT"
    SHOPPING = "SHOPPING"
    OTHERS = "OTHERS"

    

# Enum for Transaction Type
class TransactionType(str, enum.Enum):
    DEBIT = "DEBIT"
    CREDIT = "CREDIT"

        
class Expense(Base):
    __tablename__ = "expenses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    amount: Mapped[float] = mapped_column(Float)
    category: Mapped[ExpenseCategory] = mapped_column(Enum(ExpenseCategory), default=ExpenseCategory.FOOD, nullable=False)
    transaction: Mapped[TransactionType] = mapped_column(Enum(TransactionType), default=TransactionType.CREDIT, nullable=False)
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
            
        
             expense = Expense(id = db.query(Expense).count() + 1,
                              amount = expense_data.amount,
                              category= expense_data.category,
                              transaction = expense_data.transaction,
                              user_id=expense_data.user_id
                              )
             db.add(expense)
             db.commit()
             db.refresh(expense)
             return expense
        
        
         except Exception as e:
             db.rollback()
             raise e
    
    @staticmethod
    def update_expense(expense_data:dict):
        with SessionLocal() as db:
            expense = db.query(Expense).filter(Expense.id == expense_data["expense_id"]).first()
            
            if not expense:
                return None
            
            if 'amount' in expense_data:
                expense.amount = expense_data['amount']
            
            if 'category' in expense_data:
                expense.category = expense_data['category']
            
        
            db.commit()
            db.refresh(expense)
            
            return expense
            
                  
            



