import requests
import responses
import pytest

@responses.activate
def test_can_delete_group():
  responses.add(responses.DELETE, 'http://example.com/',
                status=204)

  response = requests.delete('http://example.com/')
  
  assert response.status_code == 204

@responses.activate
def test_sad_path_group_not_found():
  responses.add(responses.DELETE, 'http://example.com/', status=404)

  response = requests.delete('http://example.com/')
  
  assert response.status_code == 404

