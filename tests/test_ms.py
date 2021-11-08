from fixture import app, client, db
from helpers import createJhonDoe, createJWT
from ms.repositories import userRepo



def test_index(client):
    response = client.get('/about')
    assert response.status_code == 200
    assert response.content_type == 'application/json'

def test_register(client):
    data = {
        'phone': '1231231231',
        'password': 'secret',
        'email': 'jhon.doe@example.com'
    }
    response = client.post('/register', data=data)
    assert response.status_code == 200
    assert response.content_type == 'application/json'

def test_login(client):
    createJhonDoe()
    data = {
        'username': '1231231231',
        'password': 'secret'
    }
    response = client.post('/login', data=data)
    assert response.status_code == 200

def test_refresh_token(client):
    user = createJhonDoe()
    refresh_token = createJWT({'id': user.id})['refresh_token']
    headers = {'Authorization': f'Bearer {refresh_token}'}
    print(refresh_token, headers)
    response = client.post('/refresh', headers=headers)
    print(response)
    assert response.status_code == 200

def test_check(client):
    user = createJhonDoe()
    token = createJWT({'id': user.id})['token']
    headers = {'Authorization': f'Bearer {token}'}
    response = client.post('/check', headers=headers)
    assert response.status_code == 204

def test_profile(client):
    createJhonDoe()
    data = {
        'username': '1231231231',
        'password': 'secret'
    }
    response = client.post('/login', data=data)
    token = response.json['token']
    headers = {'Authorization': f'Bearer {token}'}
    response = client.get('/profile', headers=headers)
    assert response.status_code == 200

def test_create(client):
    user = createJhonDoe()
    token = createJWT({'id': user.id})['token']
    headers = {'Authorization': f'Bearer {token}'}
    data = {
        'phone': '1231231232',
        'email': 'jhon.doe.2@example.com',
        'password': 'secret'
    }
    response = client.post('/', headers=headers, data=data)
    assert response.status_code == 200

def test_read(client):
    user = createJhonDoe()
    token = createJWT({'id': user.id})['token']
    headers = {'Authorization': f'Bearer {token}'}
    response = client.get(f'/{user.id}', headers=headers)
    assert response.status_code == 200

def test_update(client):
    user = createJhonDoe()
    token = createJWT({'id': user.id})['token']
    headers = {'Authorization': f'Bearer {token}'}
    data = {
        'phone': '1231231232',
        'email': 'jhon.doe.2@example.com',
        'password': 'secret'
    }
    response = client.put(f'/{user.id}', headers=headers, data=data)
    assert response.status_code == 200

def test_softdelete(client):
    user = createJhonDoe()
    token = createJWT({'id': user.id})['token']
    headers = {'Authorization': f'Bearer {token}'}
    response = client.delete(f'/{user.id}', headers=headers)
    assert response.status_code == 204

def test_restore(client):
    user = createJhonDoe()
    token = createJWT({'id': user.id})['token']
    new_user = userRepo.add({
        'phone': '1231231232',
        'email': 'jhon.doe.2@example.com',
        'password': 'secret'
    })
    userRepo.soft_delete(new_user.id)
    headers = {'Authorization': f'Bearer {token}'}
    response = client.post(f'/{new_user.id}/restore', headers=headers)
    assert response.status_code == 200

def test_harddelete(client):
    user = createJhonDoe()
    token = createJWT({'id': user.id})['token']
    headers = {'Authorization': f'Bearer {token}'}
    response = client.delete(f'/{user.id}/hard', headers=headers)
    assert response.status_code == 204
