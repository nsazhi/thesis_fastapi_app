from fastapi import APIRouter, Request, Depends, status, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from sqlalchemy import insert, select, update, delete
from sqlalchemy.orm import Session
from typing import Annotated
from slugify import slugify

from mff_app.backend.db_depends import get_db
from mff_app.models import Film, Category
from mff_app.schemas.films import CreateFilm

# Создание маршрутизатора
router = APIRouter(prefix='/films', tags=['films', ])

# Подключение шаблонов
templates = Jinja2Templates(directory='templates')

# Установка связи с БД
DbSession = Annotated[Session, Depends(get_db)]


# Маршруты для шаблонов
@router.get('/')
async def get_films_by_category(request: Request, db: DbSession, slug: str='') -> HTMLResponse:
    """
    Получение всех фильмов или списка фильмов по категории при параметре запроса
    """
    if slug:
        category = db.scalar(select(Category).where(Category.slug == slug))
        films = db.scalars(select(Film).where(Film.category_id == category.id)).all()
        return templates.TemplateResponse('films_by_category.html', {'request': request,
                                                                     'category': category, 'films': films})
    else:
        films = db.scalars(select(Film)).all()
        return templates.TemplateResponse('films.html', {'request': request, 'films': films})



@router.get('/{category_slug}')
async def get_films_by_category(request: Request, db: DbSession, category_slug: str) -> HTMLResponse:
    """
    Получение списка фильмов по категории - динамические URL
    """
    category = db.scalar(select(Category).where(Category.slug == category_slug))
    films = db.scalars(select(Film).where(Film.category_id == category.id)).all()
    return templates.TemplateResponse('films_by_category.html', {'request': request,
                                                                 'category': category, 'films': films})


# Маршруты для админки
@router.get('/film_id')
async def get_film_by_id(db: DbSession, film_id: int):
    """
    Получение фильма по ID (для админки)
    """
    film = db.scalar(select(Film).where(Film.id == film_id))
    return film


@router.post('/create')
async def create_film(db: DbSession, create_film: CreateFilm, category_id: int):
    """
    Добавление фильма (для админки)
    """
    category = db.scalar(select(Category).where(Category.id == category_id))
    db.execute(insert(Film).values(title=create_film.title,
                                   slug=slugify(create_film.title),
                                   release=create_film.release,
                                   country=create_film.country,
                                   genre=create_film.genre,
                                   director=create_film.director,
                                   actors=create_film.actors,
                                   description=create_film.description,
                                   img_url=create_film.img_url,
                                   category_id=category.id
                                   ))
    db.commit()
    return {
        "status_code": status.HTTP_201_CREATED,
        "transaction": "Successful"
    }


@router.put('/update')
async def update_film(db: DbSession, film_id: int, update_film: CreateFilm):
    """
    Редактирование фильма (для админки)
    """
    film = db.scalar(select(Film).where(Film.id == film_id))
    if film is None:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Film not found")

    db.execute(update(Film).where(Film.id == film_id).values(
            title=update_film.title,
            slug=slugify(update_film.title),
            release=update_film.release,
            country=update_film.country,
            genre=update_film.genre,
            director=update_film.director,
            actors=update_film.actors,
            description=update_film.description,
            img_url=update_film.img_url,
    ))
    db.commit()

    return {
        "status_code": status.HTTP_200_OK,
        "transaction": "Film updated successfully"
    }


@router.delete('/delete')
async def delete_film(db: DbSession, film_id: int):
    """
    Удаление фильма (для админки)
    """
    film = db.scalar(select(Film).where(Film.id == film_id))
    if film is None:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Film not found")

    db.execute(delete(Film).where(Film.id == film_id))
    db.commit()

    return {
        "status_code": status.HTTP_200_OK,
        "transaction": "Film deleted successfully"
    }
