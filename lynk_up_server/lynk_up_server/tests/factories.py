import factory
from faker import Faker
from lynk_up_server.models import User
fake = Faker()

class UserFactory(factory.Factory):
  class Meta:
    model = User
    abstract = False

  user_name = fake.simple_profile()['username']
  phone_number = fake.phone_number()
  full_name = fake.simple_profile()['name']
