from mff_app.routers import *

# Создание маршрутизаторa
router = APIRouter(prefix='', tags=['main', ])


@router.get('/')
async def main_page(request: Request, db: DbSession) -> HTMLResponse:
    """
    **Маршрут GET-запроса:** Главная страница — отображает список всех категорий.

    **Context**

    ``categories``
        Список объектов `category.Category`.

    :return: Шаблон `main.html`
    """
    categories = db.scalars(select(Category)).all()
    return templates.TemplateResponse('main.html', {'request': request, 'categories': categories})
