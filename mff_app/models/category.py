from mff_app.models import *


class Category(Base):
    """
    Создает в базе данных объект модели Категория, связанный с объектами films.Film
    """
    __tablename__ = "categories"
    __table_args__ = {"keep_existing": True}
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    slug = Column(String, unique=True, index=True)

    films = relationship("Film", back_populates="category")
