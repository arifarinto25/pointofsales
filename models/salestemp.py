import enum

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .database import Base

class Product(Base):
    __tablename__ = "tbl_salestemp"

    id = Column(String(256), primary_key=True, index=True)
    memberType = Column(Boolean)
    customerId = Column(String(256), index=True)
    customerName = Column(String(256))
    createDate  = Column(DateTime(timezone=True), default=func.now())
    salesStatus = Column(Boolean)
    total = Column(Integer)
    discount = Column(Integer)
    finalPrice = Column(Integer)
    bayar = Column(Integer)
    kembali = Column(Integer)
