from mff_app.routers import *

# Создание маршрутизаторов
router1 = APIRouter(prefix='/films', tags=['films', ])
router2 = APIRouter(prefix='/admin/films', tags=['admin', ])


@router1.get('/')
async def get_films_by_category(request: Request, db: DbSession, slug: str = '') -> HTMLResponse:
    """
    **Маршрут GET-запроса с префиксом /films:** Отображает весь список фильмов или по категориям.

    **Если есть параметр запроса:**

    :param request: `slug`

    **Context**

    ``category``
        Объект category.Category с Category.slug == slug

    ``films``
        Список объектов `films.Film` с фильтром по Film.category_id.

    :return: Шаблон `films/films_by_category.html`

    **Если нет параметра запроса:**

    **Context**

    ``films``
        Список объектов `films.Film`.

    :return: Шаблон `films/films.html`
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
    **Маршрут GET-запроса с префиксом /films:** Отображает список фильмов по категориям.

    :param request: `category_slug`

    **Context**

    ``category``
        Объект category.Category с Category.slug == category_slug.

    ``films``
        Список объектов `films.Film` с фильтром по Film.category_id.

    :return: Шаблон `films/films_by_category.html`
    """
    category = db.scalar(select(Category).where(Category.slug == category_slug))
    films = db.scalars(select(Film).where(Film.category_id == category.id)).all()
    return templates.TemplateResponse('films/films_by_category.html', {'request': request,
                                                                       'category': category, 'films': films})


@router2.get('/create')
async def film_form(request: Request):
    """
    **Маршрут GET-запроса с префиксом /admin/films:** Пустая форма создания фильма.

    :return: Шаблон `admin/film_panel.html`
    """
    return templates.TemplateResponse('admin/film_panel.html', {'request': request})


@router2.post('/create')
async def create_film(db: DbSession, create: CreateFilm = Form()):
    """
    **Маршрут POST-запроса с префиксом /admin/films:** Создание фильма.

    :raise: Ошибка создания.

    :return redirect: GET-запрос на текущую страницу `admin/film_panel.html`
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
