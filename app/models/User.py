from sqlalchemy import *

from app.models.BaseModel import Base
from app.models.BaseModel import BaseModel


class User(Base):
    __tablename__ = "users"
    id = Column(String(10), primary_key=True)
    name = Column(String(20), nullable=False, unique=True, index=True)
    sex = Column(String(2), nullable=False)
    age = Column(Integer, nullable=False)

    def __init__(self, name, sex, age):
        BaseModel.initDb()
        self.name = name
        self.sex = sex
        self.age = age




