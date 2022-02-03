from fixture import app, auth, client


def test_profile(client, auth):
    token = auth.get_token()
    headers = {'Authorization': f'Bearer {token}'}
    res = client.get('/api/v1/users/profile', headers=headers)
    assert res.status_code == 200
