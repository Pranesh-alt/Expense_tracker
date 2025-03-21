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
class ExpenseCategory(str, Enum):
    FOOD = "FOOD"
    TRAVEL = "TRAVEL"
    ENTERTAINMENT = "ENTERTAINMENT"
    SHOPPING = "SHOPPING"
    OTHERS = "OTHERS"

    @classmethod
    def from_str(cls, value: str):
        try:
            return cls(value)
        except ValueError:
            raise ValueError(f"Invalid category: {value}.")

# Enum for Transaction Type
class TransactionType(str, Enum):
    DEBIT = "DEBIT"
    CREDIT = "CREDIT"

    @classmethod
    def from_str(cls, value: str):
        try:
            return cls(value)
        except ValueError:
            raise ValueError(f"Invalid transaction type: {value}.")
        
class Expense(Base):
    __tablename__ = "expenses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    amount: Mapped[float] = mapped_column(Float)
    category: Mapped[ExpenseCategory] = mapped_column(Enum(ExpenseCategory), nullable=False)
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
                # Validate category and transaction type
                category_type = ExpenseCategory.from_str(expense_data.category)
                transaction_type = TransactionType.from_str(expense_data.transaction)

                # Create new expense entry
                expense = Expense(
                    id=db.query(Expense).count() + 1,  # Generate ID dynamically
                    amount=expense_data.amount,
                    category=category_type.value,  # Store as string
                    transaction=transaction_type.value,  # Store as string
                    user_id=expense_data.user_id
                )

                # Add and commit transaction
                db.add(expense)
                db.commit()
                db.refresh(expense)
                return expense

            except Exception as e:
                db.rollback()
                raise e  # Re-raise exception for FastAPI to handle
             
        



