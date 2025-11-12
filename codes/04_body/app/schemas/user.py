from typing import Union
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    email: EmailStr
    age: Union[int, None] = None
    disabled: bool = False


class User(UserBase):
    id: int
    password: str
    

class UserCreate(UserBase):
    password: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "username": "david123",
                    "email": "david@gmail.com",
                    "password": "1q2w3e4r!",
                },
                {
                    "username": "sylvie456",
                    "email": "sylvie@naver.com",
                    "age": 30,
                    "password": "asdfqwer1234@",
                },
            ],
        },
    }


class UserPublic(UserBase):
    id: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "username": "david123",
                    "email": "david@gmail.com",
                    "age": None,
                },
                {
                    "id": 2,
                    "username": "sylvie456",
                    "email": "sylvie@naver.com",
                    "age": 30,
                },
            ],
        },
    }