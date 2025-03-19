from fastapi import FastAPI 
from controller import user_controller, expense_controller
from database import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

# FastAPI instance
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to Expense Tracker"}



# Include controllers
app.include_router(user_controller.router, prefix="/users", tags=["Users"])
app.include_router(expense_controller.router, prefix="/expenses", tags=["Expenses"])
