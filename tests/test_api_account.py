from fixture import app, auth, client


def test_api_account(app, client, auth):
    with app.app_context():
        auth.register(email="admin@example.com", password="secret")
        token = auth.get_token()
        headers = {'Authorization': f'Bearer {token}'}
        res = client.get('/api/v1/users/profile', headers=headers)
        assert res.status_code == 200
        assert "id" in res.json


def test_api_permissions(app, client, auth):
    with app.app_context():
        auth.register(email="admin@example.com", password="secret")
        token = auth.get_token()
        headers = {'Authorization': f'Bearer {token}'}
        res = client.get('/api/v1/users/profile/permissions', headers=headers)
        assert res.status_code == 200
        assert isinstance(res.json, list)
