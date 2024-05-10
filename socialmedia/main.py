# uvicorn socialmedia.main:app --reload

from fastapi import FastAPI
from socialmedia.routers.post import router as post_router

app = FastAPI()

app.include_router(post_router)
