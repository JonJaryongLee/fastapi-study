from contextlib import asynccontextmanager
import os
from typing import Annotated
from dotenv import load_dotenv
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from pwdlib import PasswordHash
from sqlmodel import SQLModel, Session, create_engine

load_dotenv(".env.local")

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

password_hash = PasswordHash.recommended()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}

engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


SessionDep = Annotated[Session, Depends(get_session)]
