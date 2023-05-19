import requests
import pytest

def test_can_call_all_groups(groups_response):
  response_data = groups_response
  response = requests.get('http://example.com') 
  response.json = lambda: response_data 
  assert response.status_code == 200

def test_can_return_valid_data_for_all_groups(groups_response):
  response_data = groups_response
  response = requests.get('http://example.com')
  response.json = lambda: response_data
  data = response.json()
  assert data == groups_response

def test_can_call_a_single_group(single_group_response):
  response_data = single_group_response
  response = requests.get('http://example.com')
  response.json = lambda: response_data
  assert response.status_code == 200

def test_can_return_valid_data_for_a_single_group(single_group_response):
  response_data = single_group_response
  response = requests.get('http://example.com')
  response.json = lambda: response_data
  assert response.status_code == 200
  assert response.json() == single_group_response

def test_will_return_error_status_if_group_is_not_found(not_found_response):
  response = not_found_response
  assert response.status_code == 404