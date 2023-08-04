from models import Post

from random import randrange


def get_post_by_id(posts: list[dict], post_id: int | str) -> tuple[int, dict] | dict:
    post = [
        (i, item) for i, item in enumerate(posts) if item["post_id"] == post_id
    ]
    return post[0] if post else {}


def create_post_with_id(posts: list[dict], post: Post) -> dict:
    post_data = post.model_dump()

    if post_data["post_id"] is None:
        post_data["post_id"] = randrange(0, 1000)
    posts.append(post_data)
    return post_data


def delete_post_by_id(posts: list[dict], post_id: int) -> bool:
    f"""
    returns False if post with post_id {post_id} doesn't exist
    returns True if post has been successfully deleted
    """

    post = get_post_by_id(posts, post_id)
    print(post)
    if post:
        remove_post_id = post[0]
        posts.pop(remove_post_id)
        return True

    return False
