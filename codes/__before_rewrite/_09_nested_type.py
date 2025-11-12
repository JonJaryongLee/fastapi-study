from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Image(BaseModel):
    url: str
    name: str


# nested type
class Item(BaseModel):
    name: str
    image: Image


# {
#     "name": "apple",
#     "image": {
#         "url": "/imgs/apple.jpg",
#         "name": "apple.jpg"
#     }
# }
@app.post("/items")
async def update_item(item: Item):
    results = {"item": item}
    return results

