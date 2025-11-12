from fastapi import FastAPI

app = FastAPI()

# ===========================================
@app.get("/")
async def root():
    return {"message": "Hello World"}

# ===========================================
# 만약 int 가 아닌 것을 전달하면 자동으로 에러 발생
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

# ===========================================
# 여러 개 주고싶은 경우
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: str):
    return {"item_id": item_id, "owner_id": user_id}

# ===========================================
# 아래 두 경우를 어떻게 구분하는가?
# 선언 순서에 따라 구분함. `users/me` 를 먼저 선언해야 인식함
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}
