import json
from fixture import app, auth, client
from helpers import getPermission, getRole, getUser
from ms.repositories import UserRepository


def test_api_admin_permissions(client, auth, app):
    userRepo = UserRepository()
    auth.register(email="admin@example.com")
    user = getUser("admin@example.com")
    token = auth.get_token(username="admin@example.com", password="secret")
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}

    response = client.get('/api/v1/users/admin', headers=headers)
    assert response.status_code == 403


def test_api_paginate(client, auth, app):
    auth.register()
    token = auth.get_token(username="root@example.com", password="secret")
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    response = client.get('/api/v1/users/admin', headers=headers)
    assert response.status_code == 200
    assert "data" in response.json
    assert "pagination" in response.json


def test_api_trash(client, auth, app):
    auth.register()
    token = auth.get_token(username="root@example.com", password="secret")
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    response = client.get('/api/v1/users/admin/trash', headers=headers)
    assert response.status_code == 200
    assert "data" in response.json
    assert "pagination" in response.json


def test_api_create(client, auth, app):
    role = getRole("user")
    token = auth.get_token(username="root@example.com", password="secret")
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    data = json.dumps({
        'phone': '1231231232',
        'email': 'jhon.doe+00@example.com',
        'password': 'secret',
        'role_id': role.id
    })
    response = client.post('/api/v1/users/admin', headers=headers, data=data)
    assert response.status_code == 201
    assert "id" in response.json


def test_api_detail(client, auth, app):
    auth.register(email="jhon.doe@example.com")
    token = auth.get_token(username="root@example.com", password="secret")
    user = getUser("jhon.doe@example.com")
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    response = client.get(f'/api/v1/users/admin/{user.id}', headers=headers)
    assert response.status_code == 200


def test_api_update(client, auth, app):
    auth.register(email="jhon.doe@example.com")
    token = auth.get_token(username="root@example.com", password="secret")
    role = getRole("user")
    user = getUser("jhon.doe@example.com")
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    data = json.dumps({
        'phone': '1231231232',
        'email': 'jhon.doe.2@example.com',
        'role_id': role.id
    })
    response = client.put(f'/api/v1/users/admin/{user.id}', headers=headers, data=data)
    assert response.status_code == 200


def test_api_update_password(client, auth, app):
    auth.register(email="jhon.doe@example.com")
    token = auth.get_token(username="root@example.com", password="secret")
    user = getUser("jhon.doe@example.com")
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    data = json.dumps({
        'password': 'secret',
        'password_confirmation': 'secret'
    })
    response = client.put(f'/api/v1/users/admin/{user.id}/password', headers=headers, data=data)
    assert response.status_code == 204


def test_api_syncpermissions(client, auth, app):
    auth.register(email="jhon.doe@example.com")
    token = auth.get_token(username="root@example.com", password="secret")
    user = getUser("jhon.doe@example.com")
    permission = getPermission("User - list")
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    data = json.dumps({'permissions': [permission.id]})
    response = client.post(f'/api/v1/users/admin/{user.id}/sync-permissions', headers=headers, data=data)
    assert response.status_code == 204


def test_api_syncroles(client, auth, app):
    auth.register(email="jhon.doe@example.com")
    token = auth.get_token(username="root@example.com", password="secret")
    user = getUser("jhon.doe@example.com")
    role = getRole("root")
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    data = json.dumps({'roles': [role.id]})
    response = client.post(f'/api/v1/users/admin/{user.id}/sync-roles', headers=headers, data=data)
    assert response.status_code == 204


def test_api_active(client, auth, app):
    auth.register(email="jhon.doe@example.com")
    token = auth.get_token(username="root@example.com", password="secret")
    user = getUser("jhon.doe@example.com")
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    response = client.post(f'/api/v1/users/admin/{user.id}/activate', headers=headers)
    assert response.status_code == 204


def test_api_unactive(client, auth, app):
    auth.register(email="jhon.doe@example.com")
    token = auth.get_token(username="root@example.com", password="secret")
    user = getUser("jhon.doe@example.com")
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    response = client.delete(f'/api/v1/users/admin/{user.id}/activate', headers=headers)
    assert response.status_code == 204


def test_api_softdelete(client, auth, app):
    auth.register(email="jhon.doe@example.com")
    token = auth.get_token(username="root@example.com", password="secret")
    user = getUser("jhon.doe@example.com")
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    response = client.delete(f'/api/v1/users/admin/{user.id}', headers=headers)
    assert response.status_code == 204


def test_api_restore(client, auth, app):
    auth.register(email="jhon.doe@example.com")
    token = auth.get_token(username="root@example.com", password="secret")
    user = getUser("jhon.doe@example.com")
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}

    userRepo = UserRepository()
    userRepo.soft_delete(user.id)

    response = client.post(f'/api/v1/users/admin/{user.id}/restore', headers=headers)
    assert response.status_code == 204


def test_api_harddelete(client, auth, app):
    auth.register(email="jhon.doe@example.com")
    token = auth.get_token(username="root@example.com", password="secret")
    user = getUser("jhon.doe@example.com")
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}

    response = client.delete(f'/api/v1/users/admin/{user.id}/hard', headers=headers)
    assert response.status_code == 204
