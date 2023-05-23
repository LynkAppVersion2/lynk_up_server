import pytest
from rest_framework.test import APIClient
import vcr
from .factories import UserFactory
from lynk_up_server.models import User

client = APIClient(base_url='localhost:8000')

@pytest.mark.django_db
@pytest.mark.vcr()
def test_can_create_a_friendship(get_response_info()):
  user = UserFactory.create()
  response = client.post(f'api/v1/{user.id}/friends')
  import ipdb; ipdb.set_trace()


  # assert response.status_code == 201
  #created
