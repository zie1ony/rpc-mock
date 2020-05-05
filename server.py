from flask import Flask
from flask import request
import json

def log(value):
    print("[SERVER] %s" % value)

def personal_newAccount():
    return "0x407d73d8a49eeb85d32cf465507dd71d507100c1"

def eth_blockNumber():
    return "0x4b7" # 1207

def eth_getBlockByNumber():
    return {
        "transactions": []
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
        log('New request')
        if not request.data:
            log('No data. Exiting') 
            return 'no data'

        data = request.get_json()
        log('Data:')
        log(data)

        if not data['method']:
            log('No method. Exiting') 
            return 'no method'

        method = data['method']
        log('Method:')
        log(method)

        result = None
        if method == 'personal_newAccount':
            result = personal_newAccount()
        elif method == 'eth_blockNumber':
            result = eth_blockNumber()
        elif method == 'eth_getBlockByNumber':
            result = eth_getBlockByNumber()

        response = {
          "id": 1,
          "jsonrpc": "2.0",
          "result": result
        }

        log('Response')
        log(response)
        return response

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host= '0.0.0.0', port=8000)
