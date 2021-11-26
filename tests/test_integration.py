from fixture import client
from helpers import createJhonDoe, createUser, createJWT
from ms.repositories import userRepo



def test_index(client):
    response = client.get('/about')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
