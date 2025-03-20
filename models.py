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
    expenses: Mapped["Expense"] = relationship("Expense", back_populates="user")

    # Data Access Object (DAO) Methods
    @staticmethod
    def create_user( db: Session, user_credentials):
        hashed_password = pwd_context.hash(user_credentials.password)
        db_user = User(username = user_credentials.username ,password = hashed_password)
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
    def update_user(db: Session, user_id: int, user_credentials: dict):
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
    time: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship("User", back_populates="expenses")
    
    
    @staticmethod
    def get_users(db: Session):
        return db.query(Expense).all()



