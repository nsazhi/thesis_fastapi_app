from datetime import date

from pydantic import BaseModel, Field


class CreateFilm(BaseModel):
    title: str = Field(..., min_length=2, max_length=100, description='Название фильма')
    release: int = Field(..., ge=1900, description='Год выхода')
    country: str = Field(..., min_length=2, max_length=100, description='Страна')
    genre: str = Field(..., min_length=2, max_length=100, description='Жанр')
    director: str = Field(..., min_length=2, max_length=100, description='Режиссер')
    actors: str = Field(..., min_length=2, max_length=200, description='Актеры')
    description: str = Field(..., min_length=50, max_length=300, description='Страна')
    img_url: str = Field(default='/static/images/placeholder.png',
                         min_length=2, max_length=300, description='Страна')
    is_viewed: bool = Field(default=False)
    created_at: date = Field(default=date.today().isoformat())
