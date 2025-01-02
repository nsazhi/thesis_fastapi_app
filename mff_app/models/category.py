from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from mff_app.backend.db import Base
from mff_app.models import *


class Category(Base):
    __tablename__ = "categories"
    __table_args__ = {"keep_existing": True}
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    slug = Column(String, unique=True, index=True)

    films = relationship("Film", back_populates="category")

# from sqlalchemy.schema import CreateTable
# print(CreateTable(Category.__table__))
