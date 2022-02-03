from fixture import app, auth, client


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
    data = {
        'username': 'admin@example.com',
        'password': 'secret'
    }
    response = client.post('/api/v1/users/login', data=data)
    assert response.status_code == 200


def test_login_error(client):
    data = {
        'username': 'admin@example.com',
        'password': 'secreto'
    }
    response = client.post('/api/v1/users/login', data=data)
    assert response.status_code == 400


def test_refresh_token(client, auth):
    refresh_token = auth.get_refreshtoken()
    headers = {'Authorization': f'Bearer {refresh_token}'}
    response = client.post('/api/v1/users/refresh', headers=headers)
    assert response.status_code == 200


def test_check(client, auth):
    token = auth.get_token()
    headers = {'Authorization': f'Bearer {token}'}
    response = client.post('/api/v1/users/check', headers=headers)
    assert response.status_code == 204
