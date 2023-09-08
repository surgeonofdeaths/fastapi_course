from fastapi import FastAPI

from app.routers import post, user, auth
from .database import engine
from . import models

# make migrations
models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
