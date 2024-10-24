import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello(client):
    """Test the hello route"""
    response = client.get('/')
    assert response.data == b"Hello, World!"
    assert response.status_code == 200
