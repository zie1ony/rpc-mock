import pytest

from server import create_app

@pytest.fixture
def client():
    app = create_app()
    return app.test_client()


def test_print(client):
    resp = client.post('/logout', follow_redirects=True)

