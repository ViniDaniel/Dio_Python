from fastapi import APIRouter, HTTPException, status

from auth.auth import LoginIn
from security import sign_jwt, verify_password
from services.account import AccountService
from views.auth import LoginOut


router = APIRouter(prefix="/auth")

account_service = AccountService()


@router.post("/login", response_model=LoginOut)
async def login(data: LoginIn):
    user = await account_service.get_by_username(data.username)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials.",
        )

    if not verify_password(data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials.",
        )

    return sign_jwt(user_id=user["user_id"])