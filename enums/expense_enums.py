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


class Months:
    JANUARY = "JANUARY"
    FEBRAUARY = "FEBRAUARY"
    MARCH = "MARCH"
    APRIL = "APRIL"
    MAY = "MAY"
    JUNE = "JUNE"
    JULY = "JULY"
    AUGUST = "AUGUST"
    SEPTEMBER = "SEPTEMBER"
    OCTOBER = "OCTOBER"
    NOVEMBER = "NOVEMBER"
    DECEMBER = "DECEMBER"