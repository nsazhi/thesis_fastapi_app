from mff_app.schemas import *


class CreateFilm(BaseModel):
    category_id: int = Field(..., description='Категория')
    title: str = Field(..., min_length=2, max_length=100, description='Название фильма')
    release: int = Field(..., ge=1900, description='Год выхода')
    country: str = Field(..., min_length=2, max_length=100, description='Страна')
    genre: str = Field(..., min_length=2, max_length=100, description='Жанр')
    director: str = Field(..., min_length=2, max_length=100, description='Режиссер')
    actors: str = Field(..., min_length=2, max_length=200, description='Актеры')
    description: str = Field(..., max_length=300, description='Страна')
    img_url: str = Field(default='/static/images/placeholder.png')
    is_viewed: bool = Field(default=False)
    created_at: date = Field(default=date.today().isoformat())
