from fastapi import Depends, HTTPException
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime,Boolean, Enum, func
from sqlalchemy.orm import session, relationship, Mapped, mapped_column, Session, joinedload
from datetime import datetime
from typing import Optional, List, Annotated
from sqlalchemy import Enum
from database import Base, SessionLocal
from passlib.context import CryptContext
from enums.expense_enums import ExpenseCategory,TransactionType
from auth import get_current_user



user_dependency = Annotated[dict, Depends(get_current_user)]
        
class Expense(Base):
    __tablename__ = "expenses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    amount: Mapped[float] = mapped_column(Float)
    category: Mapped[ExpenseCategory] = mapped_column(Enum(ExpenseCategory), default=ExpenseCategory.FOOD, nullable=False)
    transaction: Mapped[TransactionType] = mapped_column(Enum(TransactionType), default=TransactionType.CREDIT, nullable=False)
    time: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    
    
    # Use a string reference instead of direct import
    user = relationship("User", back_populates="expenses")
    
    @staticmethod
    def get_expenses(user:user_dependency):
        with SessionLocal() as db:
            if user is None:
                 raise HTTPException(status_code=401, detail='authentication failed')
        
            return db.query(Expense).filter(Expense.user_id == user.get('id')).all()
    
    
    @staticmethod
    def get_expense_by_id(user: user_dependency,expense_id: int):
        with SessionLocal() as db:
            if user is None:
                 raise HTTPException(status_code=401, detail='authentication failed')
             
            expense = db.query(Expense).filter(Expense.id == expense_id).first()
            
            return expense
    
    @staticmethod
    def create_expense(user: user_dependency,expense_data):
        with SessionLocal() as db:
         try:
             if user is None:
                 raise HTTPException(status_code=401, detail='authentication failed')
        
        
             last_expense = db.query(Expense).order_by(Expense.id.desc()).first()
             new_id = last_expense.id + 1 if last_expense else 1 
 
             expense = Expense(id = new_id,
                              amount = expense_data.amount,
                              category= expense_data.category,
                              transaction = expense_data.transaction,
                              user_id=user.get('id')
                              )
             db.add(expense)
             db.commit()
             db.refresh(expense)
             return expense
        
        
         except Exception as e:
             db.rollback()
             raise e
    
    @staticmethod
    def update_expense(user: user_dependency,expense_id:int,expense_data:dict):
        with SessionLocal() as db:
            
            if user is None:
                 raise HTTPException(status_code=401, detail='authentication failed')
        
            expense = db.query(Expense).filter(Expense.id == expense_id).filter(Expense.user_id == user.get('id')).first()
            
            if not expense:
                return None
            
            if 'amount' in expense_data:
                expense.amount = expense_data['amount']
            
            if 'category' in expense_data:
                expense.category = expense_data['category']
            
            db.commit()
            db.refresh(expense)
            
            return expense
            
    @staticmethod
    def delete_expense(user: user_dependency,expense_id:int):
        with SessionLocal() as db:
            
            if user is None:
                 raise HTTPException(status_code=401, detail='authentication failed')
        
            expense = db.query(Expense).filter(Expense.id == expense_id).first()
            
            if not expense:
                return None
            
            db.delete(expense)
            db.commit()
            
            return {"message" : "successfully Deleted"}
            
                          
    @staticmethod
    def get_expense_category(user: user_dependency):
        with SessionLocal() as db:
            if user is None:
                 raise HTTPException(status_code=401, detail='authentication failed')
        
            return db.query(Expense.category).all()
            
    
    
    @staticmethod
    def get_monthly_reports(user: user_dependency, month, year):
        with SessionLocal() as db:
           if user is None:
                 raise HTTPException(status_code=401, detail='authentication failed')
        
            
           start_date = datetime(year, month, 1)
           if month == 12:
            end_date = datetime(year + 1, 1, 1)
           else:
            end_date = datetime(year, month + 1, 1)

           report = db.query(Expense).filter(
            Expense.time >= start_date,
            Expense.time < end_date
             ).filter(Expense.user_id == user.get('id')).all()

           return report        
       
       
       
    @staticmethod
    def get_yearly_reports(user: user_dependency, year: int):
        with SessionLocal() as db:
          if user is None:
                 raise HTTPException(status_code=401, detail='authentication failed')
          
            
          start_date = datetime(year, 1, 1) 
          end_date = datetime(year + 1, 1, 1)  

          report = (
            db.query(Expense)
            .filter(Expense.time >= start_date, Expense.time < end_date).filter(Expense.user_id == user.get('id'))
            .all()
        )

        return  report  
    
    @staticmethod
    def get_expenses_by_category(user: user_dependency,category: str):
        with SessionLocal() as db:
            expenses = db.query(Expense).filter(Expense.category == category).all()
        return expenses if expenses else []
     
    @staticmethod
    def get_expenses_by_transaction(user: user_dependency,transaction: str):
        with SessionLocal() as db:
            expenses = db.query(Expense).filter(Expense.transaction == transaction).all()
        return expenses if expenses else []
    
    
    @staticmethod
    def get_monthly_amount(user: user_dependency, month, year):
        if user is None:
            raise HTTPException(status_code=401, detail='Authentication failed')

        if month is None or year is None:
            raise HTTPException(status_code=400, detail="Month and year are required.")

        start_date = datetime(year, month, 1)
        end_date = datetime(year + 1, 1, 1) if month == 12 else datetime(year, month + 1, 1)

        with SessionLocal() as db:
            total = db.query(func.sum(Expense.amount)).filter(
                Expense.time >= start_date,
                Expense.time < end_date,
                Expense.user_id == user.get('id')  
            ).scalar() or 0  
    