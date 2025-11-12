from typing import Union

from fastapi import FastAPI, Query

app = FastAPI()


# query 인 q 를 안 넣어도 상관없지만,
# 만약 넣을 경우 5글자를 넘으면 에러
# min_length 도 가능
# pattern="^fixedquery$" 식으로 정규표현식도 가능하다고 함...
@app.get("/items/")
async def read_items(q: Union[str, None] = Query(default=None, max_length=5)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
