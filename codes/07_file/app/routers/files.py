from typing import Annotated
from fastapi import APIRouter, Form

from ..schemas.file import FileFormData

router = APIRouter()

@router.post("/")
async def create_file(data: Annotated[FileFormData, Form()]):
    contents = data.upload_file.file.read()
    print(contents)
    return {
        "filename": data.upload_file.filename,
        "file_size": data.upload_file.size,
        "file_content_type": data.upload_file.content_type
    }