from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Date
from sqlalchemy.orm import relationship
from mff_app.backend import Base
from passlib.context import CryptContext

#  Хэширование пароля
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

from .category import Category
from .films import Film
from .admin import Admin
