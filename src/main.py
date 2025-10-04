from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routes.base import router as base_router
from src.routes.user import router as user_router
from src.routes.auth import router as auth_router
from src.routes.note import router as note_router
from src.database.setup import create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield


app = FastAPI(
    title="ToDo",
    root_path="/api/v1",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(base_router)
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(note_router)


def start():
    host = "localhost"
    port = 8080

    uvicorn.run("main:app", host=host, port=port, reload=True)


if __name__ == "__main__":
    start()
