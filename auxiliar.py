from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

# SECRET_KEY = 'd5567c6aa69488baf1de094bee2dff2babb803c513e5785328105390da444444'
# secret key get with openssl rand -hex 32
#
# ALGORITHM = 'HS256'
# ACCESS_TOKEN_EXPIRE_MINUTES = 30
#
#


db = {
    "nomeprologin": {
        "username": "Lucas",
        "full_name": "Lucas Goulart",
        "email": "lucas@gmail.com",
        "hashed_password": "$2b$12$tw/zZq3vmPOeYV1sJrKXTeJPp92sgppc9eDSWK0t5sD9YFOvKsi3q",
        "disabled": False
    }
}




app = FastAPI()


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Usuário ou senha incorretos",
                            headers={"WWW-Authenticate": "Bearer"})
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={'sub': user.username}, expires_delta=access_token_expires)

    return {'access_token': access_token, 'token_type': 'bearer'}


@app.get('/users/me/', response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@app.get('/test')
async def testo(teste: str, current_user: User = Depends(get_current_active_user)):
    print(current_user)
    return {
        'item': teste
    }


# if __name__ == '__main__':
#     print(get_password_hash('123'))