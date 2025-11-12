from typing import Union
from pydantic import EmailStr
from sqlmodel import SQLModel, Field


class UserBase(SQLModel):
    username: str = Field(index=True, unique=True)
    email: EmailStr = Field(index=True, unique=True)
    age: Union[int, None] = Field(default=None)
    disabled: bool = Field(default=False)


class UserInDB(UserBase, table=True):
    __tablename__ = "users"
    id: Union[int, None] = Field(default=None, primary_key=True)
    hashed_password: str = Field()


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


class UserUpdate(SQLModel):
    email: Union[EmailStr, None] = Field(default=None, index=True, unique=True)
    age: Union[int, None] = Field(default=None)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "email": "david@gmail.com",
                },
                {
                    "age": 30,
                },
                {
                    "email": "david@gmail.com",
                    "age": 30,
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
