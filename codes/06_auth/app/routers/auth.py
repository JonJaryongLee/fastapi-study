from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from ..dependencies import ACCESS_TOKEN_EXPIRE_MINUTES, SessionDep
from ..schemas.auth import Token
from ..schemas.user import UserCreate, UserInDB, UserPublic
from ..services.auth import (
    authenticate_user,
    create_access_token,
    get_current_active_user,
    get_password_hash,
)

router = APIRouter()


# {
#     "username": "tommy111",
#     "email": "tommy@kakao.com",
#     "password": "secret123"
# }
@router.post(
    "/register", response_model=UserPublic, status_code=status.HTTP_201_CREATED
)
def register_user(user_data: UserCreate, session: SessionDep) -> UserPublic:

    hashed_password = get_password_hash(user_data.password)

    db_user = UserInDB(
        username=user_data.username,
        email=user_data.email,
        age=user_data.age,
        hashed_password=hashed_password,
        disabled=user_data.disabled,
    )

    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return UserPublic.model_validate(db_user)


@router.post("/token", response_model=Token, status_code=status.HTTP_201_CREATED)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: SessionDep,
) -> Token:
    user = authenticate_user(session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@router.get("/users/me/", response_model=UserPublic)
async def read_users_me(
    current_user: Annotated[UserPublic, Depends(get_current_active_user)],
) -> UserPublic:
    return current_user
