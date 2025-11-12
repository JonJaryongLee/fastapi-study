from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# model_config
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ]
        }
    }


@app.post("/items")
async def update_item(item: Item):
    results = {"item": item}
    return results

