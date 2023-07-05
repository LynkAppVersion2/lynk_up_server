<div id="header" align="center">
  <img src="images/240969217-dc0f4910-32f9-4e3a-a784-4ba67c4497cc.png" width="300px" height="200px"/>
  <hr>
</div>

## Introduction
Welcome to the backend repository of Lynk Up Version 2! Lynk Up is a platform for creating, discovering, and managing events. From small gatherings to large parties, this app provides an intuitive and user-friendly platform to manage social circles and meetups. 

In this latest version, users can seamlessly navigate through features like adding and managing friendships, creating friend groups and events, and even sending SMS updates to invitees with essential event information. The redesigned LynkUp app aims to enhance your social experience and streamline event coordination.

------------------------------------------


## Tech Stack

- Python 3.10.11
- Django 4.2.1
- Django REST Framework 3.14.0
- SQLite3
- Pytest

------------------------------------------
## Getting Started 

To ensure a seamless experience setting up our backend repository, please adhere to the following instructions in sequential order.

<details>
<summary>
  
### Setup Instructions
</summary>

<details>
<summary> 
  
> ### 1. Fork and Clone the repository
</summary>
<br>

```shell
git clone git@github.com:LynkAppVersion2/lynk_up_server.git
```
</details>
<details>
<summary> 

> ### 2. Navigate to the directory
</summary>

```shell
cd lynk_up_server
```
</details>
<details>
<summary>
  
> ### 3. Create Virtual Environment
</summary>

```shell
python3 -m venv .venv
```

```shell
. .venv/bin/activate
```
</details>
<details>
<summary> 

> ### 4. Select Interpreter
</summary>

```shell
cmd + shift + P
```

```shell
Python: Select Interpreter → Select Python 3.10.11 (’.venv’: pipenv) ./.venv/bin/python (recommended)
```
</details>
<details>
<summary>
  
> ### 5. Create Environment for Keys
</summary>

```shell
touch .env
```
<br>

> #### Put the following keys inside .env file:

```shell
DEBUG=True
DJANGO_ENV=development
```
</details>
<details>
<summary>
  
> ### 6. Install Packages
</summary>

```shell
cd lynk_up_server
```

```shell
pip install -r dependencies.txt
```
</details>
<details>
<summary>
  
> ### 7. Generate Secret Key
</summary>

```shell
python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
> #### Copy the output

> #### Add the following to the .env file:

```shell
SECRET_KEY=<YOUR_GENERATED_KEY_HERE>
```
</details>
<details>
<summary>

> ### 8. Run the Migrations
</summary>

```shell
python manage.py migrate
```
</details>
<details>
<summary>
  
> ### 9. Load Fixture Data
</summary>  

```shell
python manage.py loaddata lynk_up_server/fixtures/user.json
```

```shell
python manage.py loaddata lynk_up_server/fixtures/friend.json
```

```shell
python manage.py loaddata lynk_up_server/fixtures/group.json
```

```shell
python manage.py loaddata lynk_up_server/fixtures/event.json
```
</details>
<details>
<summary>
  
> ### 10. Run the Tests
</summary>

```shell
pytest
```
<br>

> ### If everything's green, you're good to go!
</details>
</details>

-----------------------------


## Endpoints

<details close>
<summary> All Endpoints </summary>

### Get all Users

```http
GET /users/
```

<details close>
<summary>  Details </summary>
<br>

Request: <br>
```
No Parameters
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json

{
    "data": [
        {
            "id": 1,
            "type": "user",
            "attributes": {
                "user_name": "user123",
                "phone_number": "555-555-5555",
                "full_name": "Andra Helton",
                "my_events": [
                    {
                        "id": 1,
                        "group": 1,
                        "group_name": "Game Night",
                        "title": "Space Catan",
                        "date": "05-20-23",
                        "time": "8:00 PM"
                    }, etc.
                ],
                "invited_to_events": [],
                "my_groups": [
                    {
                        "id": 1,
                        "name": "Game Night",
                        "member_count": 4
                    }, etc.
                ],
                "included_in_groups": []
            }
        },
        {
            "id": 2,
            "type": "user",
            "attributes": {
                "user_name": "joe123",
                "phone_number": "555-888-1111",
                "full_name": "Joe Fogiato",
                "my_events": [],
                "invited_to_events": [
                    {
                        "id": 1,
                        "group": 1,
                        "group_name": "Game Night",
                        "title": "Space Catan",
                        "date": "05-20-23",
                        "time": "8:00 PM"
                    }, etc.
                ],
                "my_groups": [],
                "included_in_groups": [
                    {
                        "id": 1,
                        "name": "Game Night",
                        "member_count": 4
                    }, etc.
                ]
            }
        }, etc.
    ]
}
```

</details>

---

### Get a User

```http
GET /users/:user_id/
```

<details close>
<summary>  Details </summary>
<br>

Request: <br>
```
No Parameters
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json

{
    "data": {
        "id": 1,
        "type": "user",
        "attributes": {
            "user_name": "user123",
            "phone_number": "555-555-5555",
            "full_name": "Andra Helton",
            "my_events": [
                {
                    "id": 1,
                    "group": 1,
                    "group_name": "Game Night",
                    "title": "Space Catan",
                    "date": "05-20-23",
                    "time": "8:00 PM"
                }, etc.
            ],
            "invited_to_events": [],
            "my_groups": [
                {
                    "id": 1,
                    "name": "Game Night",
                    "member_count": 4
                }, etc.
            ],
            "included_in_groups": []
        }
    }
}
```

| Code | Description |
| :--- | :--- |
| 404 | `NOT FOUND` |

Response:

```json

{
    "error": [
        "title": "NOT FOUND",
        "status": "404"
    ]
}
```

</details>

---

### Update a User

```http
GET /users/:user_id/
```

<details close>
<summary>  Details </summary>
<br>

Requests: <br>

```
{
    "user_name": "another_username",
    "phone_number": "999-999-9999",
    "full_name": "Different Name"
}
```


| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json

{
    "data": {
        "id": 1,
        "type": "user",
        "attributes": {
            "user_name": "another_username",
            "phone_number": "999-999-9999",
            "full_name": "Different Name",
            "my_events": [
                {
                    "id": 1,
                    "group": 1,
                    "group_name": "Game Night",
                    "title": "Space Catan",
                    "date": "05-20-23",
                    "time": "8:00 PM"
                }, etc.
            ],
            "invited_to_events": [],
            "my_groups": [
                {
                    "id": 1,
                    "name": "Game Night",
                    "member_count": 4
                }, etc.
            ],
            "included_in_groups": []
        }
    }
}
```

| Code | Description |
| :--- | :--- |
| 400 | `BAD REQUEST` |

Response:

```json

{
    "error": [
        "title": "BAD REQUES",
        "status": "400"
    ]
}
```

</details>

---

### Get all Friends for a User

```http
GET /users/:user_id/friends/
```

<details close>
<summary>  Details </summary>
<br>

Request: <br>
```
No Parameters
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json

{
    "data": {
        "friends": [
            {
                "user_id": 2,
                "user_name": "otheruser321",
                "full_name": "Antonio King Hunt",
                "phone_number": "555-111-5555"
            },
            {
                "user_id": 3,
                "user_name": "joe123",
                "full_name": "Joe Fogiato",
                "phone_number": "555-888-1111"
            }, etc.
        ]
    }
}
```

| Code | Description |
| :--- | :--- |
| 404 | `NOT FOUND` |

Response:

```json

{
    "error": [
        "title": "NOT FOUND",
        "status": "404"
    ]
}
```

</details>

---

### Create Friend

```http
POST /users/:user_id/friends/
```

<details close>
<summary>  Details </summary>
<br>

Request: <br>
```json
{
    "friend_id": 1,
    "user_id": 1
}
```

| Code | Description |
| :--- | :--- |
| 201 | `Created` |

Response:

```json

{
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
```

</details>

---

### Delete Friend

```http
POST /users/:user_id/friends/
```

<details close>
<summary>  Details </summary>
<br>

Request: <br>
```json
{
    "friend_id": 1,
}
```

| Code | Description |
| :--- | :--- |
| 204 | `NO CONTENT` |

Response:

```
No Response
```

Errors:

| Code | Description |
| :--- | :--- |
| 404 | `NOT FOUND` |

</details>

---

### Get an Event

```http
GET /events/:event_id/
```

<details close>
<summary>  Details </summary>
<br>

Request: <br>
```json
{
    "event_id": 1
}
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json

{
    "data": {
        "id": 1,
        "group": 1,
        "group_name": "Best Buds",
        "title": "Magic Tournament",
        "date": "05-23-2023",
        "time": "7:00pm",
        "address": "123 fun st",
        "description": "Fun times with fun people"
    }
}
```

| Code | Description |
| :--- | :--- |
| 404 | `NOT FOUND` |

Response:

```json

{
    "error": [
        "title": "NOT FOUND",
        "status": "404"
    ]
}
```

</details>

---

### Create Event

```http
POST /events/
```

<details close>
<summary>  Details </summary>
<br>

Request: <br>
```json
    {
        "title": "Party at the Park",
        "date": "05-23-2023",
        "time": "6:00pm",
        "address": "6 Paper st",
        "description": "PARTY!",
        "group": 1
    }
```

| Code | Description |
| :--- | :--- |
| 201 | `Created` |

Response:

```json

{
    "id": 2,
    "group": 1,
    "group_name": "Best Buds",
    "title": "Party at the Park",
    "date": "05-23-2023",
    "time": "6:00pm",
    "address": "6 Paper st",
    "description": "PARTY!"
}
```

</details>

---

### Delete Event

```http
POST /events/:event_id/
```

<details close>
<summary>  Details </summary>
<br>

Request: <br>
```json
{
    "event_id": 1,
}
```

| Code | Description |
| :--- | :--- |
| 204 | `NO CONTENT` |

Response:

```
No Response
```

Errors:

| Code | Description |
| :--- | :--- |
| 404 | `NOT FOUND` |

</details>

---

### Get all Events

```http
GET /events/
```

<details close>
<summary>  Details </summary>
<br>

Request: <br>
```
No Parameters
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json

{
    "data": [
        {
            "id": 1,
            "group": 1,
            "group_name": "Best Buds",
            "title": "Magic Tournament",
            "date": "05-23-2023",
            "time": "7:00pm",
            "address": "123 fun st",
            "description": "Fun times with fun people"
        },
        {
            "id": 2,
            "group": 1,
            "group_name": "Best Buds",
            "title": "Party at the Park",
            "date": "05-23-2023",
            "time": "6:00pm",
            "address": "6 Paper 2t",
            "description": "PARTY!"
        },
        {
            "id": 3,
            "group": 2,
            "group_name": "Gal Pals",
            "title": "Galentine's Day",
            "date": "02-13-2024",
            "time": "12:00pm",
            "address": "49th st",
            "description": "Hanging with Leslie, April, Ann, and Donna"
        },
        (etc.)
    ]
}
```

| Code | Description |
| :--- | :--- |
| 404 | `NOT FOUND` |

Response:

```json

{
    "error": [
        "title": "NOT FOUND",
        "status": "404"
    ]
}
```

</details>

---

### Get all Groups

```http
GET /groups/
```

<details close>
<summary>  Details </summary>
<br>

Request: <br>
```
No Parameters
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json

{
    "data": [
        {
            "id": 1,
            "name": "Best Buds",
            "updated": "2023-05-23T23:35:10.294701Z",
            "created": "2023-05-23T23:35:10.294724Z",
            "user": 1,
            "friends": [
                1,
                2,
                (etc,)
            ]
        },
        {
            "id": 2,
            "name": "Gal Pals",
            "updated": "2023-05-24T16:46:29.542505Z",
            "created": "2023-05-24T16:46:29.542545Z",
            "user": 1,
            "friends": [
                1,
                2,
                3,
                (etc,)
            ]
        },
        (etc,)
    ]
}
```

| Code | Description |
| :--- | :--- |
| 404 | `NOT FOUND` |

Response:

```json

{
    "error": [
        "title": "NOT FOUND",
        "status": "404"
    ]
}
```

</details>

---------

### Get a Group

```http
GET /groups/:group_id/
```

<details close>
<summary>  Details </summary>
<br>

Request: <br>
```
No Parameters
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json

{
    "data": {
        "id": 1,
        "name": "Best Buds",
        "updated": "2023-05-23T23:35:10.294701Z",
        "created": "2023-05-23T23:35:10.294724Z",
        "user": 1,
        "friends": [
            1,
            2,
            (etc,)
        ]
    }
}
```

| Code | Description |
| :--- | :--- |
| 404 | `NOT FOUND` |

Response:

```json

{
    "error": [
        "title": "NOT FOUND",
        "status": "404"
    ]
}
```

</details>

---

### Delete Group

```http
POST /groups/:group_id/delete/
```

<details close>
<summary>  Details </summary>
<br>

Request: <br>
```json
{
    "group_id": 1,
}
```

| Code | Description |
| :--- | :--- |
| 204 | `NO CONTENT` |

Response:

```
No Response
```

Errors:

| Code | Description |
| :--- | :--- |
| 404 | `NOT FOUND` |

</details>
</details>



---

## Team
<table>
  <tr>
    <th>Andra Helton</th>
    <th>Antonio King Hunt</th>
    <th>Dawson Timmons</th>
    <th>Harrison Ryan</th>
    <th>William Lampke</th>
  </tr>

<tr>
  <td><img src="https://avatars.githubusercontent.com/u/116662742?v=4" width="135" height="135"></td>
  <td><img src="https://avatars.githubusercontent.com/u/89714398?v=4" width="135" height="135"></td>
  <td><img src="https://avatars.githubusercontent.com/u/117066950?v=4" width="135" height="135"></td>
  <td><img src="https://avatars.githubusercontent.com/u/116698937?v=4" width="135" height="135"></td>
  <td><img src="https://avatars.githubusercontent.com/u/109244868?v=4" width="135" height="135"></td>
</tr>


  <tr>
    <td>
      <a href="https://github.com/ALHelton" rel="nofollow noreferrer">
          <img src="https://i.stack.imgur.com/tskMh.png" alt="github"> Github
        </a><br>
      <a href="https://www.linkedin.com/in/andrahelton/" rel="nofollow noreferrer">
    <img src="https://i.stack.imgur.com/gVE0j.png" alt="linkedin"> LinkedIn
        </a>
    </td>
        <td>
       <a href="https://github.com/4D-Coder" rel="nofollow noreferrer">
            <img src="https://i.stack.imgur.com/tskMh.png" alt="github"> Github
      </a><br>
        <a href="https://www.linkedin.com/in/antoniokinghunt-4d-coder/" rel="nofollow noreferrer">
          <img src="https://i.stack.imgur.com/gVE0j.png" alt="linkedin"> LinkedIn
      </a>
    </td>
        <td>
       <a href="https://github.com/DMTimmons1" rel="nofollow noreferrer">
          <img src="https://i.stack.imgur.com/tskMh.png" alt="github"> Github
      </a><br>
        <a href="https://www.linkedin.com/in/dawson-timmons/" rel="nofollow noreferrer">
          <img src="https://i.stack.imgur.com/gVE0j.png" alt="linkedin"> LinkedIn
      </a>
    </td>
        <td>
       <a href="https://github.com/hwryan12" rel="nofollow noreferrer">
            <img src="https://i.stack.imgur.com/tskMh.png" alt="github"> Github
      </a><br>
        <a href="https://www.linkedin.com/in/harrison-ryan-2b987725a/" rel="nofollow noreferrer">
          <img src="https://i.stack.imgur.com/gVE0j.png" alt="linkedin"> LinkedIn
      </a>
    </td>
        <td>
       <a href="https://github.com/WilliamLampke" rel="nofollow noreferrer">
            <img src="https://i.stack.imgur.com/tskMh.png" alt="github"> Github
      </a><br>
        <a href="https://www.linkedin.com/in/william-lampke-b4a5b5250/" rel="nofollow noreferrer">
          <img src="https://i.stack.imgur.com/gVE0j.png" alt="linkedin"> LinkedIn
      </a>
    </td>
  </tr>
</table>
