from mff_app.routers import *

# Создание маршрутизатора
router = APIRouter(prefix='/admin', tags=['admin', ])


@router.get('/login')
async def login(request: Request):
    """
    **Маршрут GET-запроса с префиксом /admin:** Пустая форма входа администратора.

    :return: Шаблон `admin/login.html`
    """
    return templates.TemplateResponse('admin/login.html', {'request': request})


@router.post('/')
async def add_admin(db: DbSession, create: CreateAdmin):
    """
    **Маршрут POST-запроса с префиксом /admin:** Регистрация администратора.

    :raise: Ошибка регистрации - username уже существует

    :return HTTP: 201, Успешная регистрация
    """
    try:
        admin = Admin()
        db.execute(insert(Admin).values(username=create.username,
                                        password_hash=admin.set_password(create.password)
                                        ))
        db.commit()
        return {
            'status_code': status.HTTP_201_CREATED,
            'transaction': 'Admin created successful'
        }
    except:
        raise HTTPException(409, 'Администратор с таким username уже существует')


@router.post('/login')
async def login_in(db: DbSession, username: str = Form(), password: str = Form()):
    """
    **Маршрут POST-запроса с префиксом /admin:** Вход администратора.

    :raise: Ошибка входа - неверный пароль\n
    :return redirect: Шаблон `admin/cat_panel.html`
    """
    admin = db.scalar(select(Admin).where(Admin.username == username))
    if admin:
        try:
            admin.check_password(password, admin.password_hash)
            return RedirectResponse('category/create', status_code=status.HTTP_303_SEE_OTHER)
        except:
            raise HTTPException(401, 'Неверный пароль')
