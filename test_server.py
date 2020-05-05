import pytest

from server import create_app

@pytest.fixture
def client():
    app = create_app()
    return app.test_client()


def test_personal_newAccount(client):
    data = {
        "jsonrpc":"2.0",
        "id":1,
        "method":"personal_newAccount",
        "params": ["m*lYNyIC(bx!AsMteR9+d?%jOqSPuTi640$oakhWFZG5w#pLJHEc/fvV@QzBU83\\u0026"]
    }

    resp = client.post('/', json=data)
    print('New Account', resp.data)

def test_eth_blockNumber(client):
    data = {
        "jsonrpc":"2.0",
        "id":1,
        "method":"eth_blockNumber",
        "params": []
    }
    resp = client.post('/', json=data)
    print('Block number', resp.data)
