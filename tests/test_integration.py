from fixture import app, client, auth


def test_index(client):
    response = client.get('/api/v1/users/about')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert 'code' in response.json and response.json.get('code') == 200
    assert 'data' in response.json
