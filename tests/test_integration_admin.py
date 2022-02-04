from fixture import app, auth, client
from helpers import getRole, getUser
from ms.repositories import UserRepository


def test_paginate(client, auth, app):
    with app.app_context():
        token = auth.get_token()
        headers = {'Authorization': f'Bearer {token}'}
        response = client.get('/api/v1/users/admin', headers=headers)
        assert response.status_code == 200


def test_create(client, auth, app):
    with app.app_context():
        role = getRole('client')
        token = auth.get_token()
        headers = {'Authorization': f'Bearer {token}'}
        data = {
            'phone': '1231231232',
            'email': 'jhon.doe.2@example.com',
            'password': 'secret',
            'role_id': role.id
        }
        response = client.post('/api/v1/users/admin', headers=headers, data=data)
        assert response.status_code == 200


def test_read(client, auth, app):
    with app.app_context():
        user = getUser('client@example.com')
        token = auth.get_token()
        headers = {'Authorization': f'Bearer {token}'}
        response = client.get(f'/api/v1/users/admin/{user.id}', headers=headers)
        assert response.status_code == 200


def test_update(client, auth, app):
    with app.app_context():
        role = getRole('admin')
        user = getUser('client@example.com')
        token = auth.get_token()
        headers = {'Authorization': f'Bearer {token}'}
        data = {
            'phone': '1231231232',
            'email': 'jhon.doe.2@example.com',
            'role_id': role.id
        }
        response = client.put(f'/api/v1/users/admin/{user.id}', headers=headers, data=data)
        assert response.status_code == 200


def test_update_password(client, auth, app):
    with app.app_context():
        user = getUser('client@example.com')
        token = auth.get_token()
        headers = {'Authorization': f'Bearer {token}'}
        data = {
            'password': 'secret',
            'password_confirmation': 'secret'
        }
        response = client.put(f'/api/v1/users/admin/{user.id}/password', headers=headers, data=data)
        assert response.status_code == 204


def test_active(client, auth, app):
    with app.app_context():
        user = getUser('client@example.com')
        token = auth.get_token()
        headers = {'Authorization': f'Bearer {token}'}
        response = client.post(f'/api/v1/users/admin/{user.id}/activate', headers=headers)
        assert response.status_code == 204


def test_deactive(client, auth, app):
    with app.app_context():
        user = getUser('client@example.com')
        token = auth.get_token()
        headers = {'Authorization': f'Bearer {token}'}
        response = client.delete(f'/api/v1/users/admin/{user.id}/activate', headers=headers)
        assert response.status_code == 204


def test_softdelete(client, auth, app):
    with app.app_context():
        user = getUser('client@example.com')
        token = auth.get_token()
        headers = {'Authorization': f'Bearer {token}'}
        response = client.delete(f'/api/v1/users/admin/{user.id}', headers=headers)
        assert response.status_code == 204


def test_restore(client, auth, app):
    with app.app_context():
        token = auth.get_token()

        userRepo = UserRepository()
        role = getRole('client')
        new_user = userRepo.add({
            'phone': '1231231232',
            'email': 'jhon.doe.2@example.com',
            'password': 'secret',
            'role_id': role.id
        })
        userRepo.soft_delete(new_user.id)

        headers = {'Authorization': f'Bearer {token}'}
        response = client.post(f'/api/v1/users/admin/{new_user.id}/restore', headers=headers)
        assert response.status_code == 204


def test_harddelete(client, auth, app):
    with app.app_context():
        token = auth.get_token()

        userRepo = UserRepository()
        role = getRole('client')
        user_to_delete = userRepo.add({
            'phone': '1231231232',
            'email': 'jhon.doe+01@example.com',
            'password': 'secret',
            'role_id': role.id
        })
        userRepo.soft_delete(user_to_delete.id)

        headers = {'Authorization': f'Bearer {token}'}
        response = client.delete(f'/api/v1/users/admin/{user_to_delete.id}/hard', headers=headers)
        assert response.status_code == 204
