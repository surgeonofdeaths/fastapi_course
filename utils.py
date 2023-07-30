def get_post_by_id(posts: list[dict], post_id: str | int):
    post = [item for item in posts if item["post_id"] == str(post_id)]
    return post[0] if post else {}
