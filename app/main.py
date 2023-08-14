import uvicorn
from fastapi import FastAPI, Response, status, HTTPException, Depends
from sqlalchemy.orm import Session

from .database import engine, get_db
from . import models
from . import schemas


# make migrations
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# while True:
#     try:
#         conn = psycopg.connect(
#             host="localhost",
#             dbname="fastapi_course",
#             user="postgres",
#             password="firethemonkey",
#             row_factory=dict_row,
#         )
#         cur = conn.cursor()
#         break
#     except Exception as err:
#         print("connecting to the database failed")
#         print(err)
#         time.sleep(2)


@app.get("/posts")
async def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return {"data": posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    new_post = models.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"data": new_post}


@app.get("/posts/{post_id}")
async def get_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id {post_id} doesn't exist",
        )
    return {"post_detail": post}


@app.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == post_id)

    if not post.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id {post_id} doesn't exist",
        )
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{post_id}")
async def update_post(post_id: int, post: schemas.PostCreate, db: Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == post_id)
    return_post = post_query.first()

    if not return_post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with post_id {post_id} not found",
        )
    post_query.update(
        post.model_dump(),
        synchronize_session=False,
    )
    db.commit()
    db.refresh(return_post)
    return {'updated_post': return_post}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False)
