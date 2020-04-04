from typing import List

from pydantic import BaseModel
from .schema_item import Item

class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True

class TokenData(BaseModel):
    email: str = None
    is_active: bool = False

class Token(BaseModel):
    access_token: str
    token_type: str
