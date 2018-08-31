from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    @staticmethod
    def __init__(self):
        mysql_egnine = create_engine("mysql+pymysql://root:root@10.5.15.208:3306/test", max_overflow=5)
        Base.metadata.create_all(mysql_egnine)
        Session = sessionmaker()
        session = Session()
        session.commit()
        session.close()
