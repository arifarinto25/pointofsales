import enum

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .database import Base

class VolType(enum.Enum):
    mg = "miligram"
    kg = "kilogram"
    ml = "mililiter / cc"
    lt = "liter"

class Product(Base):
    __tablename__ = "tbl_product"

    id = Column(String(256), primary_key=True, index=True)
    name = Column(String, index=True)
    volume = Column(Integer)
    volType =  Column(Enum(VolType))
    description = Column(String)
    code = Column(String)
    barCode = Column(String)
    price = Column(Integer)
    stock = Column(Integer)
    isNew = Column(Boolean)
    stockable = Column(Boolean)
    lastSync =  Column(DateTime(timezone=True), default=func.now())
    status = Column(Boolean)
    imageName = Column(String)