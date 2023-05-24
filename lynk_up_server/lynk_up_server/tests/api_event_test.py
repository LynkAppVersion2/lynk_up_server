import requests
import pytest
import responses

def test_can_call_all_events(events_response):
  response_data = events_response
  response = requests.get('http://example.com') 
  response.json = lambda: response_data 
  assert response.status_code == 200

def test_can_return_valid_data_for_all_events(events_response):
  response_data = events_response
  response = requests.get('http://example.com')
  response.json = lambda: response_data
  data = response.json()
  assert data == events_response

def test_can_call_a_single_event(single_event_response):
  response_data = single_event_response
  response = requests.get('http://example.com')
  response.json = lambda: response_data
  assert response.status_code == 200

def test_can_return_valid_data_for_a_single_event(single_event_response):
  response_data = single_event_response
  response = requests.get('http://example.com')
  response.json = lambda: response_data
  assert response.status_code == 200
  assert response.json() == single_event_response

@responses.activate
def test_can_create_event(event_creation_response):
  responses.add(responses.POST, 'http://example.com', json=event_creation_response, status=201)
  payload = {
    "group_id": 1,
    "title": "postman event create test3",
    "date": "05/14/2023",
    "time": "5:00pm",
    "address": "143 test st.",
    "description": "test description3"
  }
  response = requests.post('http://example.com', json=payload)
  
  assert response.status_code == 201
  assert response.json() == event_creation_response

@responses.activate
def test_sad_path_missing_fields():
  error_message = {"error": "Missing field: group_id"}
  responses.add(responses.POST, 'http://example.com', json=error_message, status=400)

  data = payload = {
    # "group_id": missing,
    "title": "postman event create test3",
    "date": "05/14/2023",
    "time": "5:00pm",
    "address": "143 test st.",
    "description": "test description3"
  }
  response = requests.post('http://example.com', json=data)
  
  assert response.status_code == 400
  assert response.json() == error_message
  

@responses.activate
def test_update_event(event_update_response):
  responses.add(responses.PUT, 'http://example.com', json=event_update_response, status=200)
  payload = {
    "id": 4,
    "group_id": 1,
    "title": "changed event create test",
    "date": "05/23/2023",
    "time": "3:00pm",
    "address": "123 test st."
    }
  response = requests.put('http://example.com', json=payload)

  assert response.status_code == 200
  assert response.json() == event_update_response

@responses.activate
def test_delete_event(deleted_response):
  responses.add(responses.DELETE, 'http://example.com', status=204)
  response = requests.delete('http://example.com')

  assert response.status_code == 204
