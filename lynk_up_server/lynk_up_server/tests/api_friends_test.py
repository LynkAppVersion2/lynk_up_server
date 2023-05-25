import pytest, requests,json
from pprint import pprint
from rest_framework.test import APIClient
from vcr import VCR
from .factories import UserFactory
from lynk_up_server.models import *

vcr = VCR()
client = APIClient()

def bytes_to_dict(response, key):
  decoded = response[key][0].decode('utf-8')
  return json.loads(decoded)

@vcr.use_cassette('./fixtures/vcr_cassettes/create_friendship.yaml')
def test_can_create_a_friendship(db):
  user1 = UserFactory.create()
  user2 = UserFactory.create()

  # url = f'/users/{user1.id}/friends/'
  # response = vars(requests.post(url, data={'friend_id': user2.id}))
  payload = dict(
    friend_id=user2.id
  )
  response = vars(client.post(f'/users/{user1.id}/friends/', payload))
  content = bytes_to_dict(response, '_container')
  assert response['status_code'] == 201
  assert 'data' in content
  assert isinstance(content['data'], dict)

  data = content['data']
  assert isinstance(data['friends'], list)
  assert 'user_name' in data['friends'][0]
  assert data['friends'][0]['user_name'] == user2.user_name
  assert 'user_id' in data['friends'][0]
  assert data['friends'][0]['user_id'] == user2.id



# with vcr.use_cassette('./fixtures/vcr_cassettes/get_friends.yaml'):
#   def test_can_get_a_users_friends(db):
#     user1 = UserFactory.create()
#     user2 = UserFactory.create()

#     Friend.objects.create(user=user1, friend=user2)

#     response = client.get(f'/users/{user1.id}/friends')
#     response_data = get_response_data(response)

# with vcr.use_cassette('./fixtures/vcr_cassettes/delete_friendship.yaml'):
#   def test_can_delete_a_friendship(db):
#     user1 = UserFactory.create()
#     user2 = UserFactory.create()
#     friendship = Friend.objects.create(user=user1, friend=user2)

#     response = client.delete(f'/users/{user1.id}/friends/{user2.id}/')
#     # import ipdb; ipdb.set_trace()
#     response_data = get_response_data(response)
#     assert response.status_code == 200
