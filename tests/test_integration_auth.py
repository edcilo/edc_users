from fixture import client
from helpers import createJhonDoe, createJWT
from ms.repositories import userRepo


def test_register(client):
    data = {
        'phone': '1231231231',
        'email': 'jhon.doe@example.com',
        'password': 'secret',
        'password_confirmation': 'secret',
    }
    response = client.post('/api/v1/users/register', data=data)
    assert response.status_code == 200
    assert response.content_type == 'application/json'

def test_login(client):
    createJhonDoe()
    data = {
        'username': '1231231231',
        'password': 'secret'
    }
    response = client.post('/api/v1/users/login', data=data)
    assert response.status_code == 200

def test_refresh_token(client):
    user = createJhonDoe()
    refresh_token = createJWT({'id': user.id})['refresh_token']
    headers = {'Authorization': f'Bearer {refresh_token}'}
    print(refresh_token, headers)
    response = client.post('/api/v1/users/refresh', headers=headers)
    print(response)
    assert response.status_code == 200

def test_check(client):
    user = createJhonDoe()
    token = createJWT({'id': user.id})['token']
    headers = {'Authorization': f'Bearer {token}'}
    response = client.post('/api/v1/users/check', headers=headers)
    assert response.status_code == 204
