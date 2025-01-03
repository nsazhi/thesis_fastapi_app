from datetime import date

from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Date
from sqlalchemy.orm import relationship
from mff_app.backend.db import Base
from mff_app.models import *


class Film(Base):
    __tablename__ = "films"
    __table_args__ = {"keep_existing": True}
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    slug = Column(String, unique=True, index=True)
    release = Column(Integer)
    country = Column(String)
    genre = Column(String)
    director = Column(String)
    actors = Column(String)
    description = Column(String)
    img_url = Column(String)
    is_viewed = Column(Boolean, default=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False, index=True)
    category = relationship("Category", back_populates="films")
    created_at = Column(Date)
