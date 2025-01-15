from mff_app.routers import *

# Создание маршрутизатора
router = APIRouter(prefix='/admin/category', tags=['admin', ])


@router.get('/create')
async def category_form(request: Request):
    """
    **Маршрут GET-запроса с префиксом /admin/category:** Пустая форма создания категории.

    :return: Шаблон `admin/cat_panel.html`
    """
    return templates.TemplateResponse('admin/cat_panel.html', {'request': request})


@router.post('/create')
async def create_category(db: DbSession, create: CreateCategory = Form()):
    """
    **Маршрут POST-запроса с префиксом /admin/category:** Создание категории.

    :raise: Ошибка создания - категория уже существует\n
    :return redirect: GET-запрос на текущую страницу `admin/cat_panel.html`
    """
    try:
        db.execute(insert(Category).values(name=create.name,
                                           slug=slugify(create.name)))
        db.commit()
        return RedirectResponse('#', status_code=status.HTTP_303_SEE_OTHER)
    except:
        raise HTTPException(409, 'Категория уже существует')
