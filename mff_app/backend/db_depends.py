from .db import SessionLocal

def get_db():
    """
    Функция для получения сессии
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()