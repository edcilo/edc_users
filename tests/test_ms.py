from fixture import app, client, db
from helpers import createJhonDoe, createJWT



def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.content_type == 'application/json'

def test_register(client):
    data = {
        'username': 'JhonDoe',
        'password': 'secret',
        'email': 'jhon.doe@example.com'
    }
    response = client.post('/register', data=data)
    assert response.status_code == 200
    assert response.content_type == 'application/json'

def test_login(client):
    createJhonDoe()
    data = {
        'username': 'JhonDoe',
        'password': 'secret123.'
    }
    response = client.post('/login', data=data)
    assert response.status_code == 200

def test_refresh_token(client):
    refresh_token = createJWT()['refresh_token']
    headers = {'Authorization': f'Bearer {refresh_token}'}
    response = client.post('/refresh', headers=headers)
    assert response.status_code == 200

def test_check(client):
    token = createJWT()['token']
    headers = {'Authorization': f'Bearer {token}'}
    response = client.post('/check', headers=headers)
    assert response.status_code == 200

def test_profile(client):
    createJhonDoe()
    data = {
        'username': 'JhonDoe',
        'password': 'secret'
    }
    response = client.post('/login', data=data)
    token = response.json['token']
    headers = {'Authorization': f'Bearer {token}'}
    response = client.get('/profile', headers=headers)
    assert response.status_code == 200
