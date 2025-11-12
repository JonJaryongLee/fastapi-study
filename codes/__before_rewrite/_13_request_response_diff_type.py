from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None

# {
#     "username": "david123",
#     "password": "1q2w3e4r!",
#     "email": "david@gmail.com"
# }
@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn) -> UserOut:
    return user
