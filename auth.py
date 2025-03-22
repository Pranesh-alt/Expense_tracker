from fastapi import APIRouter, Depends, status, HTTPException, Request
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from typing import Annotated
from passlib.context import CryptContext
from models.user_model import User

router = APIRouter()

SECRET_KEY = 'ocewmpowmpomv'
ALGORITHM = 'HS256'


bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

def create_access_token(username: str, user_id: int, expires_delta: timedelta):
    encode = {'sub': username, 'id': user_id}
    expires = datetime.now(timezone.utc) + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm = ALGORITHM)
        
        
        
async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub', '')
        user_id: int = payload.get('id', 0)
        user_role: str = payload.get('role', '')
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user')
        
        return {'username': username, 'id': user_id, 'role': user_role}
    
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate token')


@router.post("/token")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm,Depends()]):
    
    user = User.authenticate_user(form_data.username, form_data.password)
    
    if not user:
        return "Failed Authentication"
    
    token = create_access_token(user.username, user.id, timedelta(minutes=20))
    
    return  token