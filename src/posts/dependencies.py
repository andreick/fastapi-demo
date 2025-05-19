from fastapi import HTTPException

from ..db import SessionDep
from .models import Post


def get_post_by_id(post_id: int, session: SessionDep) -> Post:
    post = session.get(Post, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post
