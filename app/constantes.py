ORIGINS = [
    "http://localhost",
    "http://localhost:3000",
]


SECRET_KEY = "d5567c6aa69488baf1de094bee2dff2babb803c513e5785328105390da444444"
# secret key get with openssl rand -hex 32
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 200

db = {
    "lucas@gmail.com": {
        "username": "lucas@gmail.com",
        "full_name": "Lucas Goulart",
        "email": "lucas@gmail.com",
        "hashed_password": "$2b$12$tw/zZq3vmPOeYV1sJrKXTeJPp92sgppc9eDSWK0t5sD9YFOvKsi3q",
        "disabled": False
    }
}
# senha 123