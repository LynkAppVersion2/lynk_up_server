import requests
import pytest

BASE_ENDPOINT = 'http://127.0.0.1:8000/'
USERS_ENDPOINT = f'{BASE_ENDPOINT}users/'
USER_ENDPOINT_HAPPY = f'{BASE_ENDPOINT}users/303-333-3433'
USER_ENDPOINT_SAD = f'{BASE_ENDPOINT}users/doesnotexist'

@pytest.fixture
def users_instance():
  return {'data': [{'attributes': {'id': 1, 'user_name': 'Dmtimmons', 'phone_number': '303-333-3433', 'full_name': 'Dawson Timmons'}, 'events': [{'id': 1, 'group_id': 1, 'title': 'party downtown', 'date': '05-18-2023', 'time': '8:00pm', 'address': '123 fun st.'}]}]}

@pytest.fixture
def user_instance():
  return {'data': {'attributes': {'id': 1, 'user_name': 'Dmtimmons', 'phone_number': '303-333-3433', 'full_name': 'Dawson Timmons'}, 'events': [{'id': 1, 'group_id': 1, 'title': 'party downtown', 'date': '05-18-2023', 'time': '8:00pm', 'address': '123 fun st.'}]}}


def test_can_call_all_users():
  response = requests.get(USERS_ENDPOINT)
  data = response.json()
  assert response.status_code == 200

def test_can_return_valid_data_for_all_users(users_instance):
  response = users_instance
  assert response == {'data': [{'attributes': {'id': 1, 'user_name': 'Dmtimmons', 'phone_number': '303-333-3433', 'full_name': 'Dawson Timmons'}, 'events': [{'id': 1, 'group_id': 1, 'title': 'party downtown', 'date': '05-18-2023', 'time': '8:00pm', 'address': '123 fun st.'}]}]}

def test_can_call_a_single_user():
  response = requests.get(USER_ENDPOINT_HAPPY)
  data = response.json()
  assert response.status_code == 200

def test_can_return_valid_data_for_a_single_user(user_instance):
  response = user_instance
  assert response == {'data': {'attributes': {'id': 1, 'user_name': 'Dmtimmons', 'phone_number': '303-333-3433', 'full_name': 'Dawson Timmons'}, 'events': [{'id': 1, 'group_id': 1, 'title': 'party downtown', 'date': '05-18-2023', 'time': '8:00pm', 'address': '123 fun st.'}]}}

def test_will_return_error_status_if_user_is_not_found():
  response = requests.get(USER_ENDPOINT_SAD)
  assert response.status_code == 404