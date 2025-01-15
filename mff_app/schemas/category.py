from mff_app.schemas import *


class CreateCategory(BaseModel):
    """
    Валидирует входящие данные и создает объект Категория.
    """
    name: str = Field(..., min_length=5, max_length=20, description='Название категории')
