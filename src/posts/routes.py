from fastapi import APIRouter
from sqlmodel import select

from ..db import SessionDep
from ..users.dependencies import get_user_by_id
from .models import Post
from .schemas import PostCreate, PostRead

router = APIRouter(prefix="/posts", tags=["posts"])


@router.post("/", response_model=PostRead)
def create_post(post: PostCreate, session: SessionDep):
    get_user_by_id(post.user_id, session)
    db_post = Post.model_validate(post)
    session.add(db_post)
    session.commit()
    session.refresh(db_post)
    return db_post


@router.get("/", response_model=list[PostRead])
def list_posts(session: SessionDep):
    posts = session.exec(select(Post)).all()
    return posts
