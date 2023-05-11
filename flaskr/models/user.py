import sqlalchemy
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash
from .base import Base, db
from flaskr.exception import ResultError


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    create_time = Column(DateTime)
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    age = Column(Integer)
    orders = db.relationship('Order', backref='user', lazy='dynamic')
    order_list = []

    def serialize(self):
        s = super().serialize()
        s['order_list'] = self.serialize_list(self.order_list)
        del s['orders']
        return s

    @classmethod
    def get_by_username(cls, username):
        return cls.query.filter_by(username=username).one()

    @classmethod
    def list(cls, params):
        users = super().list(params)
        for user in users:
            # 获取该用户的所有订单
            user.order_list = user.orders.all()
        return users

    @classmethod
    def update(cls, data: dict, key='userId', err_msg='未找到用户'):
        super().update(data, key, err_msg)

    @classmethod
    def delete(cls, model_id, err_msg='未找到用户'):
        super().delete(model_id, err_msg)
