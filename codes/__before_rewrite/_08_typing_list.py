from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# typing 의 List 를 사용해 str 배열을 받도록 강제함
class Item(BaseModel):
    tags: List[str] = []


# {
#     "tags": ["abc","def","fff"]
# }
@app.post("/items")
async def update_item(item: Item):
    results = {"item": item}
    return results

