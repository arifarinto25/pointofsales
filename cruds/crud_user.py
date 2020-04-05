from sqlalchemy.orm import Session
from sqlalchemy import or_

from models.user import User
from schemas import schema


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def cek_login(db: Session, email: str, password: str):
    return db.query(User).filter(User.email == email, User.hashed_password == password).first()


def get_user_by_id(db: Session, id: str):
    return db.query(User).filter(User.id == id).first()


def cek_waktu_insert(db: Session, id: str, nfcId: str, username: str):
    return db.query(User).filter(or_(User.id == id, User.nfcId == nfcId, User.username == username)).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schema.UserIn):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
