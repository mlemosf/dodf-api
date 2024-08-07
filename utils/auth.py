# Funcionalidades de autenticação
from fastapi import Security, HTTPException, status
from fastapi.security import APIKeyHeader
from utils.crud import get_user_by_api_key
from utils.db import SessionLocal

api_key_header = APIKeyHeader(name='X-API-Key')
session = SessionLocal()

def get_user(api_key_header : str = Security(api_key_header)):
    user = get_user_by_api_key(session, api_key_header)
    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Chave de API não encontrada'
    )
