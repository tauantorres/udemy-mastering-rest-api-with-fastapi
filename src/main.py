# uvicorn src.main:app --reload

from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.database import database
from src.routers.posts import router as post_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)

app.include_router(post_router)
