from fastapi import FastAPI, Response, status, HTTPException

import uvicorn
import psycopg
from psycopg.rows import dict_row
import time

# from utils import get_post_by_id, delete_post_by_id, create_post_with_id
from models import Post

app = FastAPI()
posts: list[dict] = []

while True:
    try:
        conn = psycopg.connect(
            host="localhost",
            dbname="fastapi_course",
            user="postgres",
            password="firethemonkey",
            row_factory=dict_row,
        )
        cur = conn.cursor()
        break
    except Exception as err:
        print("connecting to the database failed")
        print(err)
        time.sleep(2)


@app.get("/posts")
async def get_posts():
    cur.execute(query="SELECT * FROM posts")
    posts = cur.fetchall()
    return {"data": posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_post(post: Post):
    cur.execute(
        """
        INSERT INTO posts (title, content, published)
        VALUES (%s, %s, %s)
        RETURNING *
        """,
        (post.title, post.content, post.published),
    )
    created_post = cur.fetchone()
    conn.commit()
    return {"data": created_post}


@app.get("/posts/{post_id}")
async def get_post(post_id: int):
    cur.execute("""SELECT * FROM posts WHERE id = %s""", (post_id,))
    post = cur.fetchone()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="not found",
        )
    return {"data": post}


@app.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post_id: int):
    cur.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (post_id,))
    deleted: bool = cur.fetchone()
    if deleted:
        conn.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"post with id {post_id} doesn't exist",
    )


@app.put("/posts/{post_id}")
async def update_post(post_id: int, post: Post):
    cur.execute(
        """UPDATE posts
           SET title = %s,
               content = %s,
               published = %s
           WHERE id = %s
           RETURNING *;
        """,
        (post.title, post.content, post.published, post_id),
    )
    updated_post = cur.fetchone()

    if updated_post:
        conn.commit()
        return {"data": updated_post}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"post with post_id {post_id} not found",
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False)
