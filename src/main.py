# uvicorn socialmedia.main:app --reload

from fastapi import FastAPI
from src.routers.posts import router as post_router

app = FastAPI()

app.include_router(post_router)
