from mff_app.routers import *

# Создание маршрутизаторa
router = APIRouter(prefix='', tags=['main', ])


# Маршруты для шаблонов
@router.get('/')
async def main_page(request: Request, db: DbSession) -> HTMLResponse:
    """
    Главная страница: список категорий
    """
    categories = db.scalars(select(Category)).all()
    return templates.TemplateResponse('main.html', {'request': request, 'categories': categories})
