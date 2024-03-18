from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from pydantic import BaseModel
from app.constantes import ACCESS_TOKEN_EXPIRE_MINUTES
from app.login import authenticate_user, verify_password, get_password_hash, get_user, get_current_user, get_current_active_user, User, create_access_token

from app.constantes import db

class Token(BaseModel):
    access_token: str
    token_type: str


router = APIRouter()


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Usuário ou senha incorretos",
                            headers={"WWW-Authenticate": "Bearer"})
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={'sub': user.username}, expires_delta=access_token_expires)

    return {'access_token': access_token, 'token_type': 'bearer'}


@router.get('/users/me/', response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@router.get('/test')
async def testo(teste: str, current_user: User = Depends(get_current_active_user)):
    print(current_user)
    return {
        'item': teste
    }


# if __name__ == '__main__':
#     print(get_password_hash('123'))