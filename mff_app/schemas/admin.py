from mff_app.schemas import *


class CreateAdmin(BaseModel):
    """
    Валидирует входящие данные и создает объект Администратор.
    """
    username: str = Field(..., min_length=3, description='Логин админа')
    password: str = Field(..., description='Пароль админа')
