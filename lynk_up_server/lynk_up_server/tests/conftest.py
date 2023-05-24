import pytest
import requests

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

@pytest.fixture
def users_response():
  response_data = {
    "data": [
        {
            "id": 1,
            "attributes": {
                "user_name": "Dmtimmons",
                "phone_number": "303-333-3433",
                "full_name": "Dawson Timmons"
            },
            "events": [
                {
                    "id": 1,
                    "group_id": 1,
                    "title": "party downtown",
                    "date": "05-18-2023",
                    "time": "8:00pm",
                    "address": "123 fun st."
                }
            ]
        },
        {
            "id": 2,
            "attributes": {
                "user_name": "c00ldude321",
                "phone_number": "445-332-3324",
                "full_name": "Hulk Hogan"
            },
            "events": []
        }
    ]
  }
  return response_data

@pytest.fixture
def single_user_response():
  response_data = {
    "data": {
        "id": 1,
        "attributes": {
            "user_name": "Dmtimmons",
            "phone_number": "303-333-3433",
            "full_name": "Dawson Timmons"
        },
        "events": [
            {
                "id": 1,
                "group_id": 1,
                "title": "party downtown",
                "date": "05-18-2023",
                "time": "8:00pm",
                "address": "123 fun st."
            }
        ]
    }
  }
  return response_data

@pytest.fixture
def groups_response():
    response_data = {
        "data": {
            "groups": [
                {
                    "id": 1,
                    "name": "Super Fun time",
                    "updated": "2023-05-17T20:33:49.959112Z",
                    "created": "2023-05-17T20:33:49.959162Z",
                    "user": 1,
                    "friends": [
                        1
                    ]
                },
                {
                    "id": 2,
                    "name": "More Fun time",
                    "updated": "2023-05-17T20:33:49.959112Z",
                    "created": "2023-05-17T20:33:49.959162Z",
                    "user": 1,
                    "friends": [
                        1
                    ]
                },
                {
                    "id": 3,
                    "name": "Pushing the limits time",
                    "updated": "2023-05-17T20:33:49.959112Z",
                    "created": "2023-05-17T20:33:49.959162Z",
                    "user": 2,
                    "friends": [
                        1
                    ]
                }
            ]
        }
    }
    return response_data

@pytest.fixture
def single_group_response():
    response_data = {
        "data": {
            "id": 1,
            "name": "Super Fun time",
            "updated": "2023-05-17T20:33:49.959112Z",
            "created": "2023-05-17T20:33:49.959162Z",
            "user": 1,
            "friends": [
                1
            ]
        }
    }
    return response_data

@pytest.fixture
def groups_create_response():
    response_data = {
        "data": {
            "id": 1,
            "name": "Test Group",
            "updated": "2023-05-17T20:33:49.959112Z",
            "created": "2023-05-17T20:33:49.959162Z",
            "user": 1,
            "friends": [
                1,
                2
            ]
        }    
    }
    return response_data

@pytest.fixture
def groups_update_response():
    response_data = {
        "data": {
            "id": 1,
            "name": "Updated Test Group",
            "updated": "2023-05-18T21:33:49.959112Z",
            "created": "2023-05-17T20:33:49.959162Z",
            "user": 1,
            "friends": [
                2,
                3
            ]
        }    
    }
    return response_data

@pytest.fixture
def not_found_response():
  response = requests.Response()
  response.status_code = 404
  return response

@pytest.fixture
def events_response():
  response = {
    "data": [
        {
            "id": 1,
            "group_id": 1,
            "title": "test event",
            "date": "now",
            "time": "now",
            "address": "here"
        },
        {
            "id": 2,
            "group_id": 1,
            "title": "test event2",
            "date": "now",
            "time": "now",
            "address": "here"
        }
      ]
    }
  return response

@pytest.fixture
def single_event_response():
    response = {
        "data": {
            "id": 1,
            "group_id": 1,
            "title": "test event",
            "date": "now",
            "time": "now",
            "address": "here"
        }
    }
    return response

@pytest.fixture
def friends_request():
  response = {
    "data": {
      "friends": [
        {
          "user_name": "Harrison Ryan",
          "user_id": 1
        },
        {
          "user_name": "Joe Fogiato",
          "user_id": 3
        },
        {
          "user_name": "Antonio KH",
          "user_id": 4
        },
        {
          "user_name": "Trevor Fitz",
          "user_id": 5
        }
      ]
    }
  }

