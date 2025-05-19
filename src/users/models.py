from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(max_length=50)
    email: str = Field(max_length=100, index=True, unique=True)
    age: int = Field(default=18, ge=0, le=120)
