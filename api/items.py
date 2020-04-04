from fastapi import APIRouter, Depends, FastAPI, HTTPException
from typing import List

from cruds import crud_item
from schemas import schema_item
from sqlalchemy.orm import Session
from .db import get_db

router = APIRouter()

@router.get("/items/", response_model=List[schema_item.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud_item.get_items(db, skip=skip, limit=limit)
    return items