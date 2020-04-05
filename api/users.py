from fastapi import APIRouter, Depends, FastAPI, HTTPException
from typing import List

from cruds import crud_user
from schemas import schema
from models.database import SessionLocal,engine
from models import user
from sqlalchemy.orm import Session
from .db import get_db
from .token import get_current_user

user.Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.post("/user/", response_model=schema.UserOut)
def create_user(user: schema.UserIn, db: Session = Depends(get_db)):
    db_user = crud_user.cek_waktu_insert(db, id=user.id, nfcId=user.nfcId, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="userID or username or nfcId already registered")
    crud_user.create_user(db=db, user=user)
    return user


# @router.get("/user/", response_model=List[schema.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     # print(current_user) , current_user: schema.TokenData = Depends(get_current_user)
#     users = crud_user.get_users(db, skip=skip, limit=limit)
#     return users


# @router.get("/user/{user_id}", response_model=schema.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud_user.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user


# @router.post("/user/{user_id}/items/", response_model=schema.Item)
# def create_item_for_user(
#     user_id: int, item: schema.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud_product.create_user_item(db=db, item=item, user_id=user_id)
