from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import SQLALCHEMY_DATABASE_URI

# Создание движка
engine = create_engine(SQLALCHEMY_DATABASE_URI)

# Создание сессии
SessionLocal = sessionmaker(bind=engine)

from .db import Base
from .db_depends import get_db
