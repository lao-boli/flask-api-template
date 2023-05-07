from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Base(db.Model):
    # 忽略基类的主键
    __abstract__ = True
    @classmethod
    def get_db(cls):
        return db
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
