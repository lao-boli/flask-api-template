from flask_sqlalchemy import SQLAlchemy
from .serializer import Serializer

db = SQLAlchemy()


class Base(db.Model, Serializer):
    # 忽略基类的主键
    __abstract__ = True

    @classmethod
    def get_db(cls):
        return db

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @classmethod
    def filter_dict(cls, data: dict, exclude=[]):
        return {k: v for k, v in data.items() if k in cls.__table__.columns.keys() and k not in exclude}
