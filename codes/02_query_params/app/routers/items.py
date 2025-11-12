from typing import List, Union
from fastapi import APIRouter, Query, status, HTTPException
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
async def read_items(
    min_price: Union[int, None] = Query(default=None, alias="min-price"),
    max_price: Union[int, None] = Query(default=None, alias="max-price"),
    q: Union[str, None] = Query(default=None, max_length=5),
) -> List[Item]:
    filtered_items = items

    if q is not None:
        search_term = q.lower()

        def matches_keyword(item, search_term):
            if search_term in item["name"].lower():
                return True
            if item.get("description") and search_term in item["description"].lower():
                return True
            return False

        filtered_items = [
            item for item in filtered_items if matches_keyword(item, search_term)
        ]
    if min_price is not None and max_price is not None:
        if min_price > max_price:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="min_price 는 max_price 보다 작거나 같아야 합니다.",
            )
    if min_price is not None:
        filtered_items = [item for item in filtered_items if item["price"] >= min_price]

    if max_price is not None:
        filtered_items = [item for item in filtered_items if item["price"] <= max_price]

    return filtered_items
