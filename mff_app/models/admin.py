from mff_app.models import *


class Admin(Base):
    """
    Создает в базе данных объект модели Администратор.
    """
    __tablename__ = "admins"
    __table_args__ = {"keep_existing": True}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)

    def set_password(self, password):
        """
        Устанавливает хэшированный пароль для объекта модели Admin.

        :param password: Пароль, введенный при регистрации
        :return: Хэш пароля
        """
        self.password_hash = pwd_context.hash(password)
        return self.password_hash

    def check_password(self, password, password_hash):
        """
        Проверяет пароль на соответствие сохраненному хэшу.

        :param password: Пароль, введенный в форме входа `admin/login.html`
        :param password_hash: Сохраненный хэш пароля
        :return bool: Соответствует ли введенный пароль сохраненному
        """
        self.password_hash = password_hash
        return pwd_context.verify(password, self.password_hash)
