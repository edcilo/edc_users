import json
from fixture import app, auth, client
from helpers import getPermission, getRole


def test_api_paginate(client, auth, app):
    token = auth.get_token(username="root@example.com", password="secret")
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    response = client.get('/api/v1/users/admin/role', headers=headers)
    assert response.status_code == 200
    assert "data" in response.json
    assert "pagination" in response.json


def test_api_list(client, auth, app):
    token = auth.get_token(username="root@example.com", password="secret")
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    response = client.get('/api/v1/users/admin/role/list', headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_api_create(client, auth, app):
    token = auth.get_token(username="root@example.com", password="secret")
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    data = json.dumps({
        'name': 'foo',
        'fixed': True,
    })
    response = client.post('/api/v1/users/admin/role', headers=headers, data=data)
    assert response.status_code == 201
    assert "id" in response.json


def test_api_detail(client, auth, app):
    token = auth.get_token(username="root@example.com", password="secret")
    role = getRole("user")
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    response = client.get(f'/api/v1/users/admin/role/{role.id}', headers=headers)
    assert response.status_code == 200


def test_api_update(client, auth, app):
    token = auth.get_token(username="root@example.com", password="secret")
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    data = json.dumps({
        'name': 'foo',
        'fixed': False
    })

    role = getRole("root")
    response = client.put(f'/api/v1/users/admin/role/{role.id}', headers=headers, data=data)
    assert response.status_code == 403

    role = getRole("user")
    response = client.put(f'/api/v1/users/admin/role/{role.id}', headers=headers, data=data)
    assert response.status_code == 200


def test_api_syncpermissions(client, auth, app):
    token = auth.get_token(username="root@example.com", password="secret")
    role = getRole("user")
    permission = getPermission("User - list")
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    data = json.dumps({
        'permissions': [permission.id]
    })
    response = client.post(f'/api/v1/users/admin/role/{role.id}/sync-permissions', headers=headers, data=data)
    assert response.status_code == 204


def test_api_delete(client, auth, app):
    token = auth.get_token(username="root@example.com", password="secret")
    role = getRole("user")
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    response = client.delete(f'/api/v1/users/admin/role/{role.id}', headers=headers)
    assert response.status_code == 403

    data = json.dumps({
        'name': 'User - list',
        'fixed': False
    })
    response = client.put(f'/api/v1/users/admin/role/{role.id}', headers=headers, data=data)

    response = client.delete(f'/api/v1/users/admin/role/{role.id}', headers=headers)
    assert response.status_code == 204
