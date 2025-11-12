from typing import List, Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# 기본값 넣기
class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

# /items/foo
@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str) -> Item:
    return items[item_id]
