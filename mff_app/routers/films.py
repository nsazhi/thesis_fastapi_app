from mff_app.routers import *

# Создание маршрутизаторов
router1 = APIRouter(prefix='/films', tags=['films', ])
router2 = APIRouter(prefix='/admin/films', tags=['admin_films'])


# Маршруты для пользовательских шаблонов с префиксом /films
@router1.get('/')
async def get_films_by_category(request: Request, db: DbSession, slug: str = '') -> HTMLResponse:
    """
    Получение всех фильмов или списка фильмов по категории при параметре запроса
    """
    if slug:
        category = db.scalar(select(Category).where(Category.slug == slug))
        films = db.scalars(select(Film).where(Film.category_id == category.id)).all()
        return templates.TemplateResponse('films/films_by_category.html',
                                          {'request': request,
                                           'category': category, 'films': films})
    else:
        films = db.scalars(select(Film)).all()
        return templates.TemplateResponse('films/films.html', {'request': request, 'films': films})


@router1.get('/{category_slug}')
async def get_films_by_category(request: Request, db: DbSession, category_slug: str) -> HTMLResponse:
    """
    Получение списка фильмов по категории - динамические URL
    """
    category = db.scalar(select(Category).where(Category.slug == category_slug))
    films = db.scalars(select(Film).where(Film.category_id == category.id)).all()
    return templates.TemplateResponse('films/films_by_category.html', {'request': request,
                                                                       'category': category, 'films': films})


# Маршруты для админки с префиксом /admin
@router2.get('/create')
async def film_form(request: Request):
    """
    Пустая форма для добавления фильма (для админа)
    """
    return templates.TemplateResponse('admin/film_panel.html', {'request': request})


@router2.post('/create')
async def create_film(db: DbSession, create: CreateFilm = Form()):
    """
    Добавление фильма (для админа)
    """
    try:
        category = db.scalar(select(Category).where(Category.id == create.category_id))
        db.execute(insert(Film).values(title=create.title,
                                       slug=slugify(create.title),
                                       release=create.release,
                                       country=create.country,
                                       genre=create.genre,
                                       director=create.director,
                                       actors=create.actors,
                                       description=create.description,
                                       img_url=create.img_url,
                                       category_id=category.id
                                       ))
        db.commit()
        return RedirectResponse('#', status_code=status.HTTP_303_SEE_OTHER)
    except Exception as e:
        raise HTTPException(409, 'Что-то пошло не так.')
