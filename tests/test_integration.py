from fixture import client


def test_index(client):
    response = client.get('/api/v1/users/about')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
