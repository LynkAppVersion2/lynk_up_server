import pytest
from rest_framework.test import APIClient
import vcr
from .factories import UserFactory
from lynk_up_server.models import User, Friend

client = APIClient(base_url='localhost:8000')

def get_response_data(response):
  info = {
      'status_code': response.status_code,
      'content': response.content,
      'headers': response.headers,
      'cookies': response.cookies,
      'request': response.request,
  }
  return info

# with vcr.use_cassette('./fixtures/vcr_cassettes/create_friendship.yaml'):
#   def test_can_create_a_friendship(db):
#     user1 = UserFactory.create()
#     user2 = UserFactory.create()

#     response = client.post(f'/users/{user1.id}/friends', data={'friend_id': user2.id})
#     import ipdb; ipdb.set_trace()
#     response_data = get_response_data(response)

with vcr.use_cassette('./fixtures/vcr_cassettes/delete_friendship.yaml'):
  def test_can_delete_a_friendship(db):
    user1 = UserFactory.create()
    user2 = UserFactory.create()
    friendship = Friend.objects.create(user=user1, friend=user2)

    response = client.delete(f'/users/{user1.id}/friends/{user2.id}')
    # import ipdb; ipdb.set_trace()
    response_data = get_response_data(response)