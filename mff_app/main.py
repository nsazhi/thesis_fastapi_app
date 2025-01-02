from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from mff_app.routers import category, films

# Создание приложения
app = FastAPI()

# Подключение статических файлов
app.mount("/static", StaticFiles(directory="static"))

# Подключение маршрутов
app.include_router(category.router1)
app.include_router(category.router2)
app.include_router(films.router)
