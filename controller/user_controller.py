from fastapi import APIRouter, status
from services.user_services import update_user, get_user, get_users, delete_user, create_user
from schemas.user_schemas import UserResponse
router = APIRouter()

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create__user(user):
    return create_user(user)

@router.get("/", response_model=list[UserResponse], status_code=status.HTTP_200_OK)
def get__users():
    return get_users()

@router.get("/{user_id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
def get__user(user_id: int):
    return get_user(user_id)

@router.put("/{user_id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
def update__user(user_data:dict,user_id:int):
    return update_user(user_data,user_id)

@router.delete("/{user_id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
def delete__user(user_id: int):
    return delete_user(user_id)



