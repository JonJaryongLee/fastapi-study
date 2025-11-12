from typing import List
from fastapi import APIRouter, status, HTTPException
from ..schemas.item import Item

router = APIRouter()

items = [
    {
        "id": 1,
        "name": "pen",
        "price": 2000,
    },
    {
        "id": 2,
        "name": "eraser",
        "price": 500,
        "description": "잘 지워지는 지우개",
    },
    {
        "id": 3,
        "name": "note",
        "price": 1500,
    },
]

@router.get("/", response_model=List[Item], status_code=status.HTTP_200_OK)
async def read_items() -> List[Item]:
    return items


# 타입일치 안하면 에러
@router.get("/{item_id}", response_model=Item, status_code=status.HTTP_200_OK)
async def read_item(item_id: int) -> Item:
    for item in items:
        if item.get("id") == item_id:
            return item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
