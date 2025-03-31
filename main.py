from fastapi import FastAPI , Request
from controller import user_controller, expense_controller
from database import engine, Base
import auth
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os

# Create database tables
Base.metadata.create_all(bind=engine)

# FastAPI instance
app = FastAPI()

# Set the correct template directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})



# Include controllers
app.include_router(user_controller.router, prefix="/users", tags=["Users"])
app.include_router(expense_controller.router, prefix="/expenses", tags=["Expenses"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])