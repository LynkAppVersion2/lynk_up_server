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