import pytest
from .factories import UserFactory
from lynk_up_server.models import User

def test_create_user(db):
  user_fixture = UserFactory.create()

  import ipdb; ipdb.set_trace()
  persisting_user = User.objects.get(id=user_fixture.id)
