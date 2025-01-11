from mff_app.routers import *

# Создание маршрутизатора
router = APIRouter(prefix='/admin/category', tags=['category', ])


# Маршруты для шаблонов
# Маршруты для админки с префиксом /admin
# и с префиксом /category для корректной работы с такими же endpoint в фильмах
@router.get('/create')
async def category_form(request: Request):
    """
    Пустая форма для добавления категории (для админа)
    """
    return templates.TemplateResponse('admin/cat_panel.html', {'request': request})


@router.post('/create')
async def create_category(db: DbSession, create: CreateCategory = Form()):
    """
    Добавление категории (для админа)
    """
    try:
        db.execute(insert(Category).values(name=create.name,
                                           slug=slugify(create.name)))
        db.commit()
        return RedirectResponse('#', status_code=status.HTTP_303_SEE_OTHER)
    except:
        raise HTTPException(409, 'Категория уже существует')
