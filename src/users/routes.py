from fastapi import APIRouter, Depends
from sqlmodel import select

from ..db import SessionDep
from .dependencies import get_user_by_id
from .models import User
from .schemas import UserCreate, UserRead

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserRead)
def create_user(user: UserCreate, session: SessionDep):
    db_user = User.model_validate(user)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


@router.get("/", response_model=list[UserRead])
def list_users(session: SessionDep):
    users = session.exec(select(User)).all()
    return users


@router.get("/{user_id}", response_model=UserRead)
def get_user(user: User = Depends(get_user_by_id)):
    return user
