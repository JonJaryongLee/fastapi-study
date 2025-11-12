from typing import Union

from fastapi import FastAPI, Query

app = FastAPI()

# /items?item-query=foobaritems
# item-query 는 python 변수가 될 수 없는 이름
# 따라서, alias 를 설정해 안전하게 처리함
@app.get("/items")
async def read_items(q: Union[str, None] = Query(default=None, alias="item-query")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
