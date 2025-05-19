from sqlmodel import SQLModel, Field


class Post(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(max_length=100)
    content: str = Field(max_length=255)
    user_id: int = Field(foreign_key="user.id")
