from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# Создание приложения
app = FastAPI()

# Подключение статических файлов
app.mount('/static', StaticFiles(directory='static'))

# Подключение маршрутов
from mff_app.routers import main_router, adm_router, cat_router, fil_router1, fil_router2

app.include_router(main_router)  # Главная страница - "/"
app.include_router(adm_router)  # Вход админа - "/admin/login"
app.include_router(cat_router)  # Категории (админ) - "/admin/category"
app.include_router(fil_router1)  # Фильмы (пользовательские) - "/films"
app.include_router(fil_router2)  # Фильмы (админ) - "/admin/films"
