from mff_app.backend import SessionLocal


def get_db():
    """
    Функция для получения сессии подключения к БД
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
