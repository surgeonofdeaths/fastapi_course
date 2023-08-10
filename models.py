from pydantic import BaseModel


class Post(BaseModel):
    post_id: int | None = None
    title: str
    published: bool
    content: str
