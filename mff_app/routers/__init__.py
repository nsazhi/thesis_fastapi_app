from fastapi import APIRouter, Request, Depends, status, HTTPException, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from sqlalchemy import select, insert
from sqlalchemy.orm import Session

from typing import Annotated
from slugify import slugify

from mff_app.models import *
from mff_app.backend import get_db
from mff_app.schemas import *

# Подключение шаблонов
templates = Jinja2Templates(directory='templates')

# Установка связи с БД
DbSession = Annotated[Session, Depends(get_db)]

# Маршрутизаторы
from .main_page import router as main_router
from .admin import router as adm_router
from .category import router as cat_router
from .films import router1 as fil_router1
from .films import router2 as fil_router2
