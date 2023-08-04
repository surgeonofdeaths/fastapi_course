def get_post_by_id(posts: list[dict], post_id: int):
    post = [
        (i, item) for i, item in enumerate(posts) if item["post_id"] == post_id
    ]
    return post[0] if post else {}
