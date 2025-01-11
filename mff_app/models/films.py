from datetime import date

from mff_app.models import *


class Film(Base):
    __tablename__ = "films"
    __table_args__ = {"keep_existing": True}
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    slug = Column(String, unique=True, index=True)
    release = Column(Integer, nullable=False)
    country = Column(String, nullable=False, index=True)
    genre = Column(String, nullable=False, index=True)
    director = Column(String, nullable=False)
    actors = Column(String, nullable=False)
    description = Column(String, nullable=False)
    img_url = Column(String)
    is_viewed = Column(Boolean, default=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False, index=True)
    category = relationship("Category", back_populates="films")
    created_at = Column(Date, default=lambda: date.today().isoformat())
