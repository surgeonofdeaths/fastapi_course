from fastapi import FastAPI, Response, status, HTTPException

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


@app.get("/posts")
async def get_posts():
    return {"data": posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_post(post: Post):
    post_data = post.model_dump()

    if post_data["post_id"] is None:
        post_data["post_id"] = randrange(0, 1000)
    posts.append(post_data)
    return {"data": post_data}


@app.get("/posts/{post_id}")
async def get_post(post_id: str):
    post = get_post_by_id(posts, int(post_id))
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="not found"
        )
    return {"data": post[1]}


@app.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post_id: int):
    post = get_post_by_id(posts, post_id)
    if post:
        remove_post_id = post[0]
        posts.pop(remove_post_id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with {post_id} doesn't exist",
        )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False)
