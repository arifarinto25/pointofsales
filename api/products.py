from fastapi import APIRouter, Depends, FastAPI, HTTPException
from typing import List

from cruds import crud_product
from schemas import schema
from sqlalchemy.orm import Session
from .db import get_db

router = APIRouter()

@router.get("/product/", response_model=List[schema.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud_product.get_items(db, skip=skip, limit=limit)
    return items