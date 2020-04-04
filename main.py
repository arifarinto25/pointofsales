from fastapi import Depends, FastAPI, Header, HTTPException

from api import items, users, token

app = FastAPI()

app.include_router(token.router, prefix="/token", tags=["token"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(items.router, prefix="/items", tags=["items"])
