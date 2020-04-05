import enum

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .database import Base

class paymentType(enum.Enum):
    cash = "uang tunai"
    card = "digital card"

class Product(Base):
    __tablename__ = "tbl_salesdata"

    id = Column(String(256), primary_key=True, index=True)
    memberType = Column(Boolean)
    customerId = Column(String(256), index=True)
    customerName = Column(String(256))
    customerBalance = Column(Integer)
    customerCardBalance = Column(Integer)
    customerNfcId = Column(String(100))
    createDate  = Column(DateTime(timezone=True), default=func.now())
    statusSync = Column(Boolean)
    syncDate = Column(DateTime(timezone=True), default=func.now())
    total = Column(Integer)
    discount = Column(Integer)
    finalPrice = Column(Integer)
    paymentType = Column(paymentType)
    bayar = Column(Integer)
    kembali = Column(Integer)