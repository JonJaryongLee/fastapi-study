from fastapi import APIRouter, status

router = APIRouter()


@router.get("/", status_code=status.HTTP_401_UNAUTHORIZED)
async def update_admin() -> dict:
    return {"message": "This API is for admin."}