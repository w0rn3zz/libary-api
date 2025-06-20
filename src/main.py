from fastapi import FastAPI

from src.users.router import router as router_users
from src.books.router import router as router_books
from src.readers.router import router as router_readers
from src.borrows.router import router as router_borrows

app = FastAPI()


app.include_router(router_users)
app.include_router(router_books)
app.include_router(router_readers)
app.include_router(router_borrows)
