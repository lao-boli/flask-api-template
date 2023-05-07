from flask import Flask

from flaskr import create_app

app = create_app()

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
