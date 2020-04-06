from sqlalchemy.orm import Session
from sqlalchemy import or_

from models.user import User
from schemas import schema

def cek_waktu_insert(db: Session, id: str, nfcId: str, username: str):
    return db.query(User).filter(or_(User.id == id, User.nfcId == nfcId, User.username == username)).first()

def cek_waktu_update(db: Session, id: str, nfcId: str, username: str):
    return db.query(User).filter(or_(User.nfcId == nfcId, User.username == username)).first()

def create_user(db: Session, user: schema.UserIn):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def cek_login(db: Session, username: str, password: str):
    return db.query(User).filter(User.username == username, User.password == password).first()

def get_users(db: Session, skip: int, limit: int):
    return db.query(User).offset(skip).limit(limit).all()

def get_user_by_id(db: Session, id: str):
    return db.query(User).filter(User.id == id).first()

def update_user_by_id(db: Session, id: str, user: schema.UserBase):
    user.id = id
    sql = db.query(User).filter(User.id == id).update(user.dict())
    db.commit()
    return user
