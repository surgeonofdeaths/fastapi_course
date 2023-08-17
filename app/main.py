from fastapi import FastAPI

from .database import engine
from . import models
from app.routers import post, user

# make migrations
models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
