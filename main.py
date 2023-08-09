from fastapi import FastAPI, Response, status, HTTPException

import uvicorn
import psycopg

from utils import get_post_by_id, delete_post_by_id, create_post_with_id
from models import Post

app = FastAPI()
posts: list[dict] = []

with psycopg.connect(
    host="localhost",
    database="fastapi_course",
    user="postgres",
    password="firethemonkey",
) as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM post")
        cur.fetchone()
        conn.commit()


@app.get("/posts")
async def get_posts():
    return {"data": posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_post(post: Post):
    post_data = create_post_with_id(posts, post)
    return {"data": post_data}


@app.get("/posts/{post_id}")
async def get_post(post_id: int):
    post = get_post_by_id(posts, post_id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="not found",
        )
    return {"data": post[1]}


@app.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post_id: int):
    deleted: bool = delete_post_by_id(posts, post_id)
    print(f"deleted {deleted}")
    if deleted:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"post with {post_id} doesn't exist",
    )


@app.put("/posts/{post_id}")
async def update_post(post_id: int, post: Post):
    deleted: bool = delete_post_by_id(posts, post_id)
    if deleted:
        post_data = create_post_with_id(posts, post)
        return {"data": post_data}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"post with post_id {post_id} not found",
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False)
