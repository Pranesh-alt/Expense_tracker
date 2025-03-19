from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas import UserCreate
# from services.user_services import create_user, authenticate_user
from database import get_db

router = APIRouter()



