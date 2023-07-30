from fastapi import FastAPI

import uvicorn
from pydantic import BaseModel
from random import randrange

from utils import get_post_by_id

app = FastAPI()
posts = []


class Post(BaseModel):
    post_id: int | None = None
    title: str
    content: str
    rating: int | None = None


# @app.get('/')
# async def root():
#     return {'message': 'welcome to root'}


@app.get('/posts')
async def get_posts():
    return {'data': posts}


@app.get('/posts/{post_id}')
async def get_post(post_id):
    post = get_post_by_id(posts, str(post_id))
    return {'data': post}


@app.post('/posts')
async def create_post(post: Post):
    post = post.model_dump()
    if post['post_id'] is None:
        post['post_id'] = randrange(0, 1000)
    posts.append(post)
    return {'data': post}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
