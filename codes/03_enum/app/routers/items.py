from typing import List
from fastapi import APIRouter, Query, status, HTTPException
from ..schemas.item import Item, SortOrder

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
    sort_by: str = Query(default="id", alias="sort-by"),
    sort_order: SortOrder = Query(default=SortOrder.asc, alias="sort-order"),
) -> List[Item]:
    filtered_items = items
    valid_sort_fields = Item.model_fields.keys()
    if sort_by not in valid_sort_fields:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"{sort_by} 는 정렬 기준이 될 수 없습니다. 다음 중 하나여야 합니다: {list(valid_sort_fields)}",
        )
    reverse_sort = sort_order == SortOrder.desc
    filtered_items = sorted(
        filtered_items,
        key=lambda item: item.get(sort_by),
        reverse=reverse_sort,
    )

    return filtered_items
