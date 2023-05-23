import pytest
from rest_framework.test import APIClient
import vcr
from .factories import UserFactory
from lynk_up_server.models import User

client = APIClient(base_url='localhost:8000')

@pytest.fixture
def get_response_data(response):
  info = {
      'status_code': response.status_code,
      'content': response.content,
      'headers': response.headers,
      'cookies': response.cookies,
      'request': response.request,
  }
  return info

with vcr.use_cassette('fixtures/vcr_cassettes/create_friendship.yaml'):
  def test_can_create_a_friendship(db):
    user = UserFactory.create()
    response = client.post(f'/users/{user.id}/friends')
    response_data = get_response_data(response)

    assert response_data['status_code'] == 201
