from starlette.config import Config

config = Config('.env')

SECRET_KEY = config('SECRET_KEY', default='you-will-never-guess')
SQLALCHEMY_DATABASE_URI = config('DATABASE_URL', default='sqlite:///./ mff.db')
