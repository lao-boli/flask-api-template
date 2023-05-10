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

    @classmethod
    def list_users(cls, args):
        query = cls.init_query(args)
        users = query.all()
        return users

    @classmethod
    def init_query(cls, args):
        order_by = args.get('orderBy')
        name = args.get('name')
        username = args.get('username')
        age = args.get('age')
        min_age = args.get('min_age')
        max_age = args.get('max_age')
        query = User.query
        if username:
            query = query.filter_by(username=username)
        if name:
            query = query.filter_by(name=name)
        if age:
            query = query.filter_by(age=age)
        if min_age:
            query = query.filter(User.age >= int(min_age))
        if max_age:
            query = query.filter(User.age <= int(max_age))
        if order_by:  # 如果排序字段不为空，则按该字段排序
            if order_by.startswith('-'):
                # 如果以'-'开头，则按照该列降序排序
                query = query.order_by(getattr(User, order_by[1:]).desc())
            else:
                # 否则按照该列升序排序
                query = query.order_by(getattr(User, order_by).asc())
        return query

    @classmethod
    def page(cls, args):
        page_num = int(args.get('pageNum', 1))
        page_size = int(args.get('pageSize', 10))
        query = cls.init_query(args)
        page = query.paginate(page=page_num, per_page=page_size)
        return page

    @classmethod
    def get_by_id(cls, user_id):
        return cls.query.get(user_id)

    @classmethod
    def get_by_username(cls, username):
        return cls.query.filter_by(username=username).one()

    @classmethod
    def add(cls, data):
        filtered_data = cls.filter_dict(data)
        user = User(**filtered_data)
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()  # 回滚事务
            if 'Duplicate entry' in str(e):
                raise ResultError(message='键冲突')
        return user

    @classmethod
    def update(cls, data: dict):
        user = cls.query.get(data.get('userId'))
        if user is None:
            raise ResultError(message='未找到用户')
        filtered_data = cls.filter_dict(data, exclude=['user_id'])
        # 将过滤后的数据赋值到对应的属性
        for key, value in filtered_data.items():
            setattr(user, key, value)
        db.session.commit()
        return user

    @classmethod
    def delete(cls, user_id):
        user = User.query.get(user_id)
        if user is None:
            raise ResultError(message='未找到用户')
        db.session.delete(user)
        db.session.commit()
        return 'User deleted'
