from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.auth.schemas import RefreshRequest, RegisterRequest, TokenResponse
from app.auth.service import authenticate_user, create_tokens, refresh_access_token, register_user
from app.dependencies import DbSession
from app.users.schemas import UserResponse

router = APIRouter()


@router.post("/register", response_model=UserResponse, status_code=201)
async def register(db: DbSession, data: RegisterRequest):
    return await register_user(db, data)


@router.post("/login", response_model=TokenResponse)
async def login(db: DbSession, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = await authenticate_user(db, form_data.username, form_data.password)
    return create_tokens(str(user.id))


@router.post("/refresh", response_model=TokenResponse)
async def refresh(db: DbSession, data: RefreshRequest):
    return await refresh_access_token(db, data.refresh_token)
