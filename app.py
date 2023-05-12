from flask import Flask

from flaskr import create_app
from flask_migrate import Migrate
from flaskr.models.base import db

app = create_app()
migrate = Migrate(app=app, db=db)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    # use idea 在运行配置中开启debug和设置端口
    app.run()
