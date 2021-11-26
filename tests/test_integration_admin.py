from fixture import client
from helpers import createJhonDoe, createUser, createJWT
from ms.repositories import userRepo


def test_create(client):
    user = createJhonDoe()
    token = createJWT({'id': user.id})['token']
    headers = {'Authorization': f'Bearer {token}'}
    data = {
        'phone': '1231231232',
        'email': 'jhon.doe.2@example.com',
        'password': 'secret'
    }
    response = client.post('/admin', headers=headers, data=data)
    assert response.status_code == 200

def test_read(client):
    user = createJhonDoe()
    token = createJWT({'id': user.id})['token']
    headers = {'Authorization': f'Bearer {token}'}
    response = client.get(f'/admin/{user.id}', headers=headers)
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
    response = client.put(f'/admin/{user.id}', headers=headers, data=data)
    assert response.status_code == 200

def test_active(client):
    user = createJhonDoe()
    token = createJWT({'id': user.id})['token']
    headers = {'Authorization': f'Bearer {token}'}
    response = client.post(f'/admin/{user.id}/activate', headers=headers)
    assert response.status_code == 204

def test_deactive(client):
    user = createJhonDoe()
    token = createJWT({'id': user.id})['token']
    headers = {'Authorization': f'Bearer {token}'}
    response = client.delete(f'/admin/{user.id}/activate', headers=headers)
    assert response.status_code == 204

def test_softdelete(client):
    user = createJhonDoe()
    token = createJWT({'id': user.id})['token']
    headers = {'Authorization': f'Bearer {token}'}
    response = client.delete(f'/admin/{user.id}', headers=headers)
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
    response = client.post(f'/admin/{new_user.id}/restore', headers=headers)
    assert response.status_code == 204

def test_harddelete(client):
    user = createJhonDoe()
    token = createJWT({'id': user.id})['token']
    headers = {'Authorization': f'Bearer {token}'}
    user_to_delete = createUser({
        'phone': '1231231232',
        'email': 'jhon.doe+01@example.com',
        'password': 'secret',
    })
    userRepo.soft_delete(user_to_delete.id)
    response = client.delete(f'/admin/{user_to_delete.id}/hard', headers=headers)
    assert response.status_code == 204
