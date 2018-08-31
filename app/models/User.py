from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = "student2s"
    id = Column(String(10), primary_key=True)
    name = Column(String(20), nullable=False, unique=True, index=True)
    sex = Column(String(2), nullable=False)
    age = Column(Integer, nullable=False)

    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age


mysql_egnine = create_engine("mysql+pymysql://root:root@10.5.15.208:3306/test", max_overflow=5)
Base.metadata.create_all(mysql_egnine)
Session = sessionmaker()
session = Session()
session.commit()
session.close()


