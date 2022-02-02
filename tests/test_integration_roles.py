from fixture import client
from helpers import createJhonDoe, createUser, createJWT, getRole
from ms.repositories import RoleRepository


def test_create(client):
    user = createJhonDoe()
    token = createJWT({'id': user.id})['token']
    headers = {'Authorization': f'Bearer {token}'}
    data = {'name': 'test'}
    response = client.post('/api/v1/users/admin/roles', headers=headers, data=data)
    assert response.status_code == 200

def test_read(client):
    role = getRole('client')
    user = createJhonDoe()
    token = createJWT({'id': user.id})['token']
    headers = {'Authorization': f'Bearer {token}'}
    response = client.get(f'/api/v1/users/admin/role/{role.id}', headers=headers)
    assert response.status_code == 200

def test_update(client):
    role = getRole('client')
    user = createJhonDoe()
    token = createJWT({'id': user.id})['token']
    headers = {'Authorization': f'Bearer {token}'}
    data = {'name': 'cliente'}
    response = client.put(f'/api/v1/users/admin/role/{role.id}', headers=headers, data=data)
    assert response.status_code == 200

def test_harddelete(client):
    role = getRole('client')
    user = createJhonDoe()
    token = createJWT({'id': user.id})['token']
    headers = {'Authorization': f'Bearer {token}'}
    response = client.delete(f'/api/v1/users/admin/role/{role.id}', headers=headers)
    assert response.status_code == 400

    roleRepo = RoleRepository()
    role_to_delete = roleRepo.add({"name": "test"})
    response = client.delete(f'/api/v1/users/admin/role/{role_to_delete.id}', headers=headers)
    assert response.status_code == 204
