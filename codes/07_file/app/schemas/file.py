from fastapi import UploadFile
from pydantic import BaseModel

class FileFormData(BaseModel):
    upload_file: UploadFile