from fastapi import APIRouter, Request, Depends, status, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from sqlalchemy import insert, select, update, delete
from sqlalchemy.orm import Session
from typing import Annotated
from slugify import slugify

from mff_app.backend.db_depends import get_db
from mff_app.models.category import Category
from mff_app.schemas.category import CreateCategory

# Создание маршрутизаторов
router1 = APIRouter(prefix='', tags=['main', ])
router2 = APIRouter(prefix='/category', tags=['category', ])

# Подключение шаблонов
templates = Jinja2Templates(directory='templates')

# Установка связи с БД
DbSession = Annotated[Session, Depends(get_db)]


# Маршруты для шаблонов
# Главная страница: роутер без префикса
@router1.get('/')
async def main_page(request: Request, db: DbSession) -> HTMLResponse:
    """
    Главная страница: список категорий
    """
    categories = db.scalars(select(Category)).all()
    return templates.TemplateResponse('catalog/main.html', {'request': request, 'categories': categories})


# Маршруты для админки
# Страницы с префиксом /category для корректной работы с такими же endpoint в фильмах
@router2.post('/create')
async def create_category(db: DbSession, create_category: CreateCategory):
    """
    Добавление категории (для админки)
    """
    db.execute(insert(Category).values(name=create_category.name,
                                       slug=slugify(create_category.name)))
    db.commit()
    return {
        "status_code": status.HTTP_201_CREATED,
        "transaction": "Successful"
    }


@router2.put('/update')
async def update_category(db: DbSession, category_id: int, update_category: CreateCategory):
    """
    Редактирование категории (для админки)
    """
    category = db.scalar(select(Category).where(Category.id == category_id))
    if category is None:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Category not found")

    db.execute(update(Category).where(Category.id == category_id).values(
            name=update_category.name,
            slug=slugify(update_category.name)))
    db.commit()

    return {
        "status_code": status.HTTP_200_OK,
        "transaction": "Category updated successfully"
    }


@router2.delete('/delete')
async def delete_category(db: DbSession, category_id: int):
    """
    Удаление категории (для админки)
    """
    category = db.scalar(select(Category).where(Category.id == category_id))
    if category is None:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Category not found")

    db.execute(delete(Category).where(Category.id == category_id))
    db.commit()

    return {
        "status_code": status.HTTP_200_OK,
        "transaction": "Category deleted successfully"
    }
