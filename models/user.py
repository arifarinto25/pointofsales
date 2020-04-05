from sqlalchemy import Column, Boolean, ForeignKey, Integer, String, DateTime, BLOB
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .database import Base

class User(Base):
    __tablename__ = "tbl_user"

    id = Column(String(256), primary_key=True, index=True)
    name = Column(String(256))
    username = Column(String(256), unique=True, index=True)
    password = Column(String)
    userBalance = Column(Integer, default=0)
    limitKartu = Column(Integer, default=0)
    saldoKartu = Column(Integer, default=0)
    nfcId = Column(String(20), unique=True, index=True)
    imageUser = Column(String(256))
    lastSync = Column(DateTime(timezone=True), default=func.now())
