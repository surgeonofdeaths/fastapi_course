from fastapi import FastAPI

from pydantic import BaseModel
from random import randrange

posts = [
    {'post_id': 1, 'title': 'sample title', 'content': 'sample content',
     'published': True, 'rating': 4}
]


class Post(BaseModel):
    post_id: int
    title: str
    content: str
    published: bool = True
    rating: int | None = None


app = FastAPI()


@app.get('/posts')
async def get_posts():
    return {'data': posts}


@app.post('/posts')
async def create_post(post: Post):
    new_post = post.model_dump()
    new_post.setdefault('post_id', randrange(0, 1000))
    posts.append(new_post)
    return {'data': new_post}


@app.get('/posts/{post_id}')
async def get_post(post_id: int):
    post = [item for item in posts if item['post_id'] == int(post_id)]
    return post[:1]


@app.get('/posts/latest')
async def latest():
    return {'data': posts[-1]}
