from flask import Flask
from flask import request

def create_app(): 
    app = Flask(__name__)

    METHODS=['GET', 'POST']

    @app.route('/', methods=METHODS)
    @app.route('/<a>', methods=METHODS)
    @app.route('/<a>/<b>', methods=METHODS)
    @app.route('/<a>/<b>/<c>', methods=METHODS)
    def catch_all(**kwargs):
        path = request.path
        data = request.data
        print('')
        print("path", path)
        print("data", data)
        return '123'

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()