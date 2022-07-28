from fixture import app, auth, client
from ms.repositories import UserRepository
from helpers import getUser

def test_api_register(client):
    data = {
        'phone': '9000000001',
        'email': 'jhon.doe@example.com',
        'password': 'secret',
        'password_confirmation': 'secret',
    }
    res = client.post('/api/v1/users/register', data=data)
    assert res.status_code == 201
    assert res.content_type == 'application/json'
    assert 'token' in res.json
    assert 'refresh_token' in res.json


def test_api_login(client, auth):
    auth.register(email="admin@example.com", password="secret")
    data = {
        'username': 'admin@example.com',
        'password': 'secret'
    }
    res = client.post('/api/v1/users/login', data=data)
    assert res.status_code == 200
    assert 'token' in res.json
    assert 'refresh_token' in res.json

    data['password'] = 'secreto'
    res = client.post('/api/v1/users/login', data=data)
    assert res.status_code == 400


def test_api_refresh_token(client, auth):
    auth.register(email="admin@example.com", password="secret")
    refresh_token = auth.get_refreshtoken()
    headers = {'Authorization': f'Bearer {refresh_token}'}
    res = client.post('/api/v1/users/refresh', headers=headers)
    assert res.status_code == 200
    assert 'token' in res.json
    assert 'refresh_token' in res.json


def test_api_check(client, auth):
    userRepo = UserRepository()

    auth.register(email="admin@example.com", password="secret")
    user = getUser("admin@example.com")
    token = auth.get_token()
    headers = {'Authorization': f'Bearer {token}'}
    res = client.post('/api/v1/users/check', headers=headers)
    assert res.status_code == 204

    userRepo.delete(user.id)
    res = client.post('/api/v1/users/check', headers=headers)
    assert res.status_code == 403

    headers = {}
    res = client.post('/api/v1/users/check', headers=headers)
    assert res.status_code == 403

    headers = {'Authorization': f'Bearer abcde12345'}
    res = client.post('/api/v1/users/check', headers=headers)
    assert res.status_code == 403
