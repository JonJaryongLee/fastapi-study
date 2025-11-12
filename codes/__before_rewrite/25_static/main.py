from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# /static/abc.png
app.mount("/static", StaticFiles(directory="static"), name="static")