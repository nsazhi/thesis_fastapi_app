from mff_app.routers import *

# Создание маршрутизатора
router = APIRouter(prefix='/admin', tags=['admin', ])


@router.get('/login')
async def login(request: Request):
    """
    Страница входа для админа
    """
    return templates.TemplateResponse('admin/login.html', {'request': request})


@router.post('/login')
async def login_in(request: Request, db: DbSession, username: str = Form(), password: str = Form()):
    """
    Вход админа или регистрация нового
    """
    admin = db.scalar(select(Admin).where(Admin.username == username))
    if admin:
        try:
            admin.check_password(password, admin.password_hash)
            return RedirectResponse('category/create', status_code=status.HTTP_303_SEE_OTHER)
        except:
            raise HTTPException(401, 'Неверный пароль')
    else:
        admin = Admin()
        db.execute(insert(Admin).values(username=username,
                                        password_hash=admin.set_password(password)
                                        ))
        db.commit()
        return RedirectResponse('category/create', status_code=status.HTTP_303_SEE_OTHER)
