from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# /items?skip=1&limit=1
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

# 필수로 요청하고 싶을 경우? 기본값을 안 주면 됨
# @app.get("/items/")
# async def read_item(skip: int, limit: int = 10):
#     return fake_items_db[skip : skip + limit]
