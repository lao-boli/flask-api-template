import os

from flask import Flask, jsonify
from .models import *
from .exception import ResultError


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.debug = True
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:root@127.0.0.1:3306/pytest?charset=utf8',
        SQLALCHEMY_POOL_RECYCLE=1800,
        SQLALCHEMY_POOL_TIMEOUT=1500,
        SQLALCHEMY_ENGINE_OPTIONS={'pool_pre_ping': True},
        SQLALCHEMY_ECHO=True,
    )

    # error handlers
    @app.errorhandler(RuntimeError)
    def handle_runtime_error(e):
        app.logger.error('{}'.format(e))
        return jsonify(Result.fail(msg='未知异常'))

    @app.errorhandler(ResultError)
    def handle_result_error(e: ResultError):
        return jsonify(Result.fail_with_error(e))

    # db
    from .models.base import db
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # router
    from .api.user import api
    app.register_blueprint(api)
    return app
