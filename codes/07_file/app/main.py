from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .dependencies import lifespan
from .internal import admin
from .routers import items, users, auth, files

app = FastAPI(lifespan=lifespan)

app.include_router(
    items.router,
    prefix="/api/v1/items",
    tags=["items"],
)
app.include_router(
    admin.router,
    prefix="/api/v1/admin",
    tags=["admin"],
)
app.include_router(
    users.router,
    prefix="/api/v1/users",
    tags=["user"],
)
app.include_router(
    auth.router,
    prefix="/api/v1/auth",
    tags=["auth"],
)
app.include_router(
    files.router,
    prefix="/api/v1/files",
    tags=["files"],
)

# 모든 출처 허용
origins = ['*']

# origins = [
#     "http://localhost",
#     "http://localhost:8080",
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/v1")
async def root():
    return {"message": "Hello World!"}
