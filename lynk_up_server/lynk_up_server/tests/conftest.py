import pytest
import requests

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
def event_creation_response():
    response_data = {
    "group_id": 1,
    "title": "postman event create test2",
    "date": "05/24/2023",
    "time": "4:00pm",
    "address": "123343 test st.",
    "description": "test description2"
    }
    return response_data

@pytest.fixture
def event_update_response():
   response_data = {
    "id": 4,
    "group_id": 1,
    "title": "changed event create test",
    "date": "05/23/2023",
    "time": "3:00pm",
    "address": "123 test st."
    }
   return response_data

@pytest.fixture
def deleted_response():
  response = requests.Response()
  response.status_code = 204
  return response