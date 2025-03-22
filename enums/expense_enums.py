import enum
from sqlalchemy import Enum


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

