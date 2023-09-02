from fastapi import FastAPI

from app.routers import post, user, auth
from .config import get_settings
from .database import engine
from . import models

print(get_settings())
# make migrations
models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
