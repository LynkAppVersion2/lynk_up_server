import requests
import responses
import pytest

@responses.activate
def test_can_update_group(groups_update_response):
    responses.add(responses.PUT, 'http://example.com/1/update/', json=groups_update_response, status=200)

    data = {
        "user": 1,
        "friends": [2, 3],
        "name": "Updated Test Group"
    }
    response = requests.put('http://example.com/1/update/', json=data)
    
    assert response.status_code == 200
    assert response.json() == groups_update_response

@responses.activate
def test_sad_path_non_existing_group():
    responses.add(responses.PUT, 'http://example.com/9999/update/', status=404)

    data = {
        "user": 1,
        "friends": [2, 3],
        "name": "Updated Test Group"
    }
    response = requests.put('http://example.com/9999/update/', json=data)
    
    assert response.status_code == 404
