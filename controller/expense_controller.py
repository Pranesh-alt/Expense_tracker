from fastapi import APIRouter, Depends, HTTPException, status
from schemas.expense_schemas import ExpenseCreate, ExpenseResponse, ExpenseUpdate,ExpenseCategoryResponse,ExpenseTransactionRespone
from services.expense_services import get_all_expenses , create_expense, update_expense, delete_expense, expense_categories, expense_transaction_types
router = APIRouter()


@router.get("/", response_model=list[ExpenseResponse], status_code=status.HTTP_200_OK)
def get__all__expenses():
    return get_all_expenses()


@router.post("/", response_model=ExpenseResponse, status_code=status.HTTP_201_CREATED)
def create__expense(expense: ExpenseCreate):
    return create_expense(expense)
    


@router.put("/{expense_id}",response_model=ExpenseResponse, status_code=status.HTTP_201_CREATED)
def update__expense(expense_id:int,expense_data: ExpenseUpdate):
    return update_expense(expense_id,expense_data)


@router.delete("/{expense_id}", response_model=ExpenseResponse, status_code=status.HTTP_200_OK)
def delete__expense(expense_id: int):
    return delete_expense(expense_id)

@router.get("/categories", response_model=ExpenseCategoryResponse, status_code=status.HTTP_200_OK)
def expenses__categories():
    return expense_categories()
    
@router.get("/transaction", response_model=ExpenseTransactionRespone, status_code=status.HTTP_200_OK)
def expenses_transaction_types():
    return expense_transaction_types()    
