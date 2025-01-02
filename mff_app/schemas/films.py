from pydantic import BaseModel

class CreateFilm(BaseModel):
    title: str
    release: int
    country: str
    genre: str
    director: str
    actors: str
    description: str
    img_url: str
    is_viewed: bool
