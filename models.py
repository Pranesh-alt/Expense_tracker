from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Enum
from sqlalchemy.orm import session, relationship, Mapped, mapped_column, Session
from datetime import datetime
from typing import Optional, List
import enum
from database import Base
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    password: Mapped[str] = mapped_column(String)
    expenses: Mapped[float] = relationship("Expense", back_populates="user")  # Ensure this line exists
    

    # Data Access Object (DAO) Methods
    @staticmethod
    def create_user( db: Session, username: str, password: str,  expenses: Optional[List[dict]] = None):
        hashed_password = pwd_context.hash(password)
        
        # Check if expenses exist and are in the correct format
        db_expenses = []
        if expenses:
             db_expenses = [Expense(**expense) for expense in expenses]  # Convert dictionaries to Expense models
        
        db_user = User(username=username, password=hashed_password, expenses=db_expenses)
        
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def get_users(db: Session):
        return db.query(User).all()

    @staticmethod
    def get_user(db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def update_user(db: Session, user_id: int, username: Optional[str] = None, password: Optional[str] = None, expenses: Optional[float] = None):
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            return None

        if username:
            user.username = username
        if password:
            user.password = pwd_context.hash(password)
        if expenses is not None:
            user.expenses = expenses

        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def delete_user(db: Session, user_id: int):
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            return None

        db.delete(user)
        db.commit()
        return True


class TransactionType(str, enum.Enum):
    credit = "credit"
    debit = "debit"

class Expense(Base):
    __tablename__ = "expenses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    amount: Mapped[float] = mapped_column(Float)
    category: Mapped[str] = mapped_column(String(255))
    transaction: Mapped[TransactionType] = mapped_column(Enum(TransactionType), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship("User", back_populates="expenses")
