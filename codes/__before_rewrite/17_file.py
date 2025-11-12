from typing import Annotated
from fastapi import FastAPI, UploadFile, Form
from pydantic import BaseModel

app = FastAPI()


class FormData(BaseModel):
    upload_file: UploadFile

@app.post("/files/")
async def create_file(data: Annotated[FormData, Form()]):
    contents = data.upload_file.file.read()
    print(contents)
    return {
        "filename": data.upload_file.filename,
        "file_size": data.upload_file.size,
        "file_content_type": data.upload_file.content_type
    }
