from fastapi import FastAPI

from .posts.routes import router as posts_router
from .users.routes import router as users_router

app = FastAPI()

app.include_router(users_router)
app.include_router(posts_router)
