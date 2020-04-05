import enum

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .database import Base

class Product(Base):
    __tablename__ = "tbl_salestempdetail"

    id = Column(String(256), primary_key=True, index=True)
    salesId = Column(String(256), index=True)
    productId = Column(String(256), index=True)
    name = Column(String(256))
    price = Column(Integer)
    jumlah = Column(Integer)