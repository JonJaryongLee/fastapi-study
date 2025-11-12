from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/token")
async def get_token(authorization: str = Header(default=None)):
    token = None
    # 'Bearer ' 부분을 제거하고 실제 토큰 값만 추출
    if authorization and authorization.startswith("Bearer "):
        token = authorization.split(" ")[1]
    return {"token": token}

