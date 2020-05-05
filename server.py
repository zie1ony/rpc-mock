from flask import Flask
from flask import request
import json

def log(value):
    print("[SERVER] %s" % value)

def personal_newAccount():
    return {
      "id": 1,
      "jsonrpc": "2.0",
      "result": "0x407d73d8a49eeb85d32cf465507dd71d507100c1"
    }

def eth_blockNumber():
    return {
      "id": 1,
      "jsonrpc": "2.0",
      "result": "0x4b7" # 1207
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

        log('Method:')
        log(data['method'])

        response = None
        if data['method'] == 'personal_newAccount':
            response = personal_newAccount()
        elif data['method'] == 'eth_blockNumber':
            response = eth_blockNumber()
        log('Response')
        log(response)

        return response

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host= '0.0.0.0', port=8000)
