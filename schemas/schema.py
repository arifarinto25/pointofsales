from typing import List
from datetime import datetime
from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str = None
    userId: str = False

class UserBase(BaseModel):
    id: str
    name: str
    username: str
    userBalance: int
    limitKartu: int
    saldoKartu: int
    nfcId: str
    imageUser: str
    lastSync: datetime

class UserIn(UserBase):
    password: str

class UserOut(UserBase):
    pass
