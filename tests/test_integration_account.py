from fixture import app, client
from helpers import createJhonDoe, createJWT
from ms.repositories import userRepo


def test_profile(client):
    user = createJhonDoe()
    token = createJWT({'id': user.id})['token']
    headers = {'Authorization': f'Bearer {token}'}
    res = client.get('/profile', headers=headers)
    assert res.status_code == 200
