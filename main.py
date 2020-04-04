from fastapi import Depends, FastAPI, Header, HTTPException

from api import items, users

app = FastAPI()

async def get_token_header(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")

app.include_router(users.router, prefix="/items", tags=["users"])
app.include_router(items.router, prefix="/items", tags=["items"])
