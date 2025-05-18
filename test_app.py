import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert rv.data == b'Hello, World!'

def test_post_data(client):
    rv = client.post('/data', json={"key": "value"})
    assert rv.status_code == 200
    assert rv.data == b'Received'

def test_post_data_invalid_json(client):
    rv = client.post('/data', data='notjson', content_type='text/plain')
    assert rv.status_code == 400
    assert b'Invalid JSON' in rv.data

def test_demo(client):
    rv = client.get('/Demo')
    assert rv.status_code == 200
    assert rv.data == b'Hello Agent!'
