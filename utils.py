def get_post_by_id(posts: list[dict], post_id: str):
    post = [item for item in posts if item['post_id'] == post_id]
    return post
