from typing import Union
from sqlmodel import select
from ..schemas.user import UserInDB
from ..dependencies import SessionDep


def find_user_by_username(username: str, session: SessionDep) -> Union[UserInDB, None]:
    # PK 기반으로 찾기
    # user = session.get(User, username)

    stmt = select(UserInDB).where(UserInDB.username == username)
    user = session.exec(stmt).first()
    return user