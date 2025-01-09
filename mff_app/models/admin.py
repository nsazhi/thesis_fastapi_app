from mff_app.models import *


class Admin(Base):
    __tablename__ = "admins"
    __table_args__ = {"keep_existing": True}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)

    def set_password(self, password):
        self.password_hash = pwd_context.hash(password)
        return self.password_hash

    def check_password(self, password, password_hash):
        self.password_hash = password_hash
        return pwd_context.verify(password, self.password_hash)
