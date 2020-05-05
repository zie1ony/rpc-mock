from flask import Flask
from flask import request

def personal_newAccount():
    return {
      "id": 1,
      "jsonrpc": "2.0",
      "result": "0x407d73d8a49eeb85d32cf465507dd71d507100c1"
    }

def create_app(): 
    app = Flask(__name__)

    METHODS=['GET', 'POST']

    @app.route('/', methods=METHODS)
    @app.route('/<a>', methods=METHODS)
    @app.route('/<a>/<b>', methods=METHODS)
    @app.route('/<a>/<b>/<c>', methods=METHODS)
    def catch_all(**kwargs):
        print('')
        print("data", request.data)
        if not request.data: 
            return personal_newAccount()

        if request.data.method == 'personal_newAccount':
            return personal_newAccount()
        
        return ''

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host= '0.0.0.0', port=8000)
