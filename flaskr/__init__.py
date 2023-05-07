import os

from flask import Flask
from .models import *
from sqlalchemy import select


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.debug = True
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:root@127.0.0.1:3306/pytest?charset=utf8',
        SQLALCHEMY_ECHO=True
    )

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from .models.base import db
    db.init_app(app)
    with app.app_context():
        db.create_all()

    from .api.user import api
    app.register_blueprint(api)
    return app
