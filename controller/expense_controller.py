from fastapi import APIRouter, Depends, HTTPException, status
from schemas.expense_schemas import ExpenseCreate, ExpenseResponse, ExpenseUpdate,ExpenseCategoryResponse,ExpenseTransactionRespone
from services import expense_services
router = APIRouter()


@router.get("/", response_model=list[ExpenseResponse], status_code=status.HTTP_200_OK)
def get__all__expenses():
    return expense_services.get_all_expenses()


@router.post("/", response_model=ExpenseResponse, status_code=status.HTTP_201_CREATED)
def create__expense(expense: ExpenseCreate):
    return expense_services.create_expense(expense)
    

@router.put("/{expense_id}",response_model=ExpenseResponse, status_code=status.HTTP_201_CREATED)
def update__expense(expense_id:int,expense_data: ExpenseUpdate):
    return expense_services.update_expense(expense_id,expense_data)


@router.delete("/{expense_id}", response_model=ExpenseResponse, status_code=status.HTTP_200_OK)
def delete__expense(expense_id: int):
    return expense_services.delete_expense(expense_id)

@router.get("/categories", response_model=ExpenseCategoryResponse, status_code=status.HTTP_200_OK)
def expenses__categories():
    return expense_services.expense_categories()
    
@router.get("/transaction", response_model=ExpenseTransactionRespone, status_code=status.HTTP_200_OK)
def expenses_transaction_types():
    return expense_services.expense_transaction_types()    

@router.get("/monthlyreport/{year}/{month}",response_model=ExpenseResponse, status_code=status.HTTP_200_OK)
def get_monthly__reports(user_id,month,year):
    return expense_services.get_monthly_reports(user_id,month,year)


@router.get("/monthlyreport/{year}",response_model=ExpenseResponse, status_code=status.HTTP_200_OK)
def get_yearly__reports(user_id,year):
    return expense_services.get_yearly_reports(user_id,year)