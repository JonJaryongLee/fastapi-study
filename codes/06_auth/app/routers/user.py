from fastapi import APIRouter, HTTPException, status
from sqlmodel import select
from ..services.user import find_user_by_username
from ..dependencies import SessionDep
from ..schemas.user import UserInDB, UserPublic, UserUpdate


router = APIRouter()

@router.get("/", response_model=list[UserPublic], status_code=status.HTTP_200_OK)
def read_users(session: SessionDep):
    users = session.exec(select(UserInDB)).all()
    return users


@router.get("/{username}", response_model=UserPublic, status_code=status.HTTP_200_OK)
def read_user(username: str, session: SessionDep):
    user = find_user_by_username(username, session)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# email 또는 age 만 변경 가능
@router.patch(
    "/{username}", response_model=UserPublic, status_code=status.HTTP_201_CREATED
)
def update_user(username: str, user: UserUpdate, session: SessionDep) -> UserPublic:
    user_db = find_user_by_username(username, session)
    if not user_db:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = user.model_dump(exclude_unset=True)
    user_db.sqlmodel_update(user_data)
    session.add(user_db)
    session.commit()
    session.refresh(user_db)
    return user_db


@router.delete("/{username}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(username: str, session: SessionDep) -> None:
    user_db = find_user_by_username(username, session)
    if not user_db:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user_db)
    session.commit()
    return
