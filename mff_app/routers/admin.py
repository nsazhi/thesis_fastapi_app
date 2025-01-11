from mff_app.routers import *

# Создание маршрутизатора
router = APIRouter(prefix='/admin', tags=['admin', ])


@router.get('/login')
async def login(request: Request):
    """
    Страница входа для админа
    """
    return templates.TemplateResponse('admin/login.html', {'request': request})


@router.post('/')
async def add_admin(db: DbSession, create: CreateAdmin):
    """
    Регистрация админа
    """
    admin = Admin()
    db.execute(insert(Admin).values(username=create.username,
                                    password_hash=admin.set_password(create.password)
                                    ))
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Admin created successful'
    }


@router.post('/login')
async def login_in(db: DbSession, username: str = Form(), password: str = Form()):
    """
    Вход админа
    """
    admin = db.scalar(select(Admin).where(Admin.username == username))
    if admin:
        try:
            admin.check_password(password, admin.password_hash)
            return RedirectResponse('category/create', status_code=status.HTTP_303_SEE_OTHER)
        except:
            raise HTTPException(401, 'Неверный пароль')
