from fixture import app, auth, client
from ms.repositories import RoleRepository
from helpers import getRole


def test_paginate(client, auth, app):
    with app.app_context():
        token = auth.get_token(username='admin@example.com', password='secret')
        headers = {'Authorization': f'Bearer {token}'}
        response = client.get('/api/v1/users/admin/roles', headers=headers)
        assert response.status_code == 200

        token = auth.get_token(username='client@example.com', password='secret')
        headers = {'Authorization': f'Bearer {token}'}
        response = client.get('/api/v1/users/admin/roles', headers=headers)
        assert response.status_code == 403


def test_create(client, auth):
    token = auth.get_token()
    headers = {'Authorization': f'Bearer {token}'}
    data = {'name': 'test'}
    response = client.post('/api/v1/users/admin/roles', headers=headers, data=data)
    assert response.status_code == 200


def test_read(client, auth, app):
    with app.app_context():
        role = getRole('client')
        token = auth.get_token()
        headers = {'Authorization': f'Bearer {token}'}
        response = client.get(f'/api/v1/users/admin/role/{role.id}', headers=headers)
        assert response.status_code == 200


def test_update(client, auth, app):
    with app.app_context():
        role = getRole('client')
        token = auth.get_token()
        headers = {'Authorization': f'Bearer {token}'}
        data = {'name': 'cliente'}
        response = client.put(f'/api/v1/users/admin/role/{role.id}', headers=headers, data=data)
        assert response.status_code == 200


def test_harddelete(client, auth, app):
    with app.app_context():
        role = getRole('client')
        token = auth.get_token()
        headers = {'Authorization': f'Bearer {token}'}
        response = client.delete(f'/api/v1/users/admin/role/{role.id}', headers=headers)
        assert response.status_code == 400

    with app.app_context():
        roleRepo = RoleRepository()
        role_to_delete = roleRepo.add({"name": "test"})
        response = client.delete(f'/api/v1/users/admin/role/{role_to_delete.id}', headers=headers)
        assert response.status_code == 204
