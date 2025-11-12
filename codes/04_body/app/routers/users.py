from fastapi import APIRouter, status

from ..schemas.user import UserCreate, UserPublic


router = APIRouter()

users = [
    {
        "id": 1,
        "username": "david123",
        "email": "david@gmail.com",
        "age": None,
        "password": "1q2w3e4r!",
        "disabled": False,
    },
    {
        "id": 2,
        "username": "sylvie456",
        "email": "sylvie@naver.com",
        "age": 30,
        "password": "asdfqwer1234@",
        "disabled": False,
    },
    {
        "id": 3,
        "username": "nana123",
        "email": "nana@hotmail.com",
        "age": 4,
        "password": "mypassword",
        "disabled": True,
    },
]

last_id = 3


# {
#     "username": "tommy111",
#     "email": "tommy@kakao.com",
#     "password": "secret123"
# }
@router.post("/", response_model=UserPublic, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate) -> UserPublic:
    global last_id

    user_dict = user.model_dump()
    last_id += 1
    user_dict.update({"id": last_id})
    return user_dict
