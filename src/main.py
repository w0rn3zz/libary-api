from fastapi import FastAPI

from src.users.router import router as router_users
from src.config import settings

app = FastAPI()


app.include_router(router_users)