from typing import List
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from fastapi.websockets import WebSocketState
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
import json
from typing import Optional
from pydantic import BaseModel
from app.constantes import ORIGINS
from app.routes import authentication


app = FastAPI()

# Configuração do CORS


app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(authentication.router)

