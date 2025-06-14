from pydantic import BaseModel


class PostCreate(BaseModel):
    title: str
    content: str
    user_id: int


class PostRead(BaseModel):
    id: int
    title: str
    content: str
    user_id: int
