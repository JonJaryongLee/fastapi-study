from typing import Union
from pydantic import BaseModel


class Item(BaseModel):
    id: int
    name: str
    description: Union[str, None] = None
    price: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "name": "pen",
                    "description": None,
                    "price": 2000,
                },
                {
                    "id": 2,
                    "name": "eraser",
                    "price": 500,
                    "description": "잘 지워지는 지우개",
                },
            ],
        },
    }