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
<summary> 
  
### All Endpoints 
</summary>

<details>
<summary>
  
> ### Users
</summary>


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

Errors:

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
PATCH /users/:user_id/
```

<details close>
<summary>  Details </summary>
<br>

Requests: <br>

```json
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

Errors:

| Code | Description |
| :--- | :--- |
| 400 | `BAD REQUEST` |

Response:

```json

{
    "error": [
        "title": "BAD REQUEST",
        "status": "400"
    ]
}
```

</details>

---
</details>


<details>
<summary>
  
> ### Friends
</summary>

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

</details>

---

### Get one Friend for a User

```http
GET /users/:user_id/friends/:friend_id/
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
        "id": 2,
        "type": "user",
        "attributes": {
            "user_name": "otheruser321",
            "phone_number": "555-111-5555",
            "full_name": "Antonio King Hunt",
            "my_events": [],
            "invited_to_events": [],
            "my_groups": [
                {
                    "id": 3,
                    "name": "Brunch",
                    "member_count": 3
                }, etc.
            ],
            "included_in_groups": [
                {
                    "id": 9,
                    "name": "Plein Air Painting",
                    "member_count": 2
                }, etc.
            ]
        }
    }
}
```

Errors:

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

### Create Friend for a User

```http
POST /users/:user_id/friends/
```

<details close>
<summary>  Details </summary>
<br>

Request: <br>
```json
{
    "friend": 5
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
            },
            {
                "user_id": 5,
                "user_name": "dawson123",
                "full_name": "Dawson Timmons",
                "phone_number": "555-000-3333"
            }
        ]
    }
}
```

Errors:

| Code | Description |
| :--- | :--- |
| 400 | `BAD REQUEST` |

Response:

```json

{
    "error": [
        "title": "BAD REQUEST",
        "status": "400"
    ]
}
```

</details>

---

### Delete Friend for a User

```http
DELETE /users/:user_id/friends/:friend_id/
```

<details close>
<summary>  Details </summary>
<br>

Request: <br>
```json
{
    "friend_id": 5,
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
</details>


<details>
<summary>
  
> ### Groups
</summary>

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
            "type": "group",
            "attributes": {
                "group_host_id": 1,
                "group_host_name": "Andra Helton",
                "group_name": "Game Night",
                "group_friends": [
                    {
                        "user_id": 3,
                        "user_name": "joe123",
                        "full_name": "Joe Fogiato",
                        "phone_number": "555-888-1111"
                    }, etc.
                ],
                "group_events": [
                    {
                        "id": 1,
                        "group": 1,
                        "group_name": "Game Night",
                        "title": "Space Catan",
                        "date": "05-20-23",
                        "time": "8:00 PM"
                    }, etc.
                ]
            }
        }, etc.
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
        "type": "group",
        "attributes": {
            "group_host_id": 1,
            "group_host_name": "Andra Helton",
            "group_name": "Game Night",
            "group_friends": [
                {
                    "user_id": 3,
                    "user_name": "joe123",
                    "full_name": "Joe Fogiato",
                    "phone_number": "555-888-1111"
                }, etc.
            ],
            "group_events": [
                {
                    "id": 1,
                    "group": 1,
                    "group_name": "Game Night",
                    "title": "Space Catan",
                    "date": "05-20-23",
                    "time": "8:00 PM"
                }, etc.
            ]
        }
    }
}
```

Errors:

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

### Create a Group

```http
GET /groups/
```

<details close>
<summary>  Details </summary>
<br>

Request: <br>
```json
{
    "user": 1,
    "name": "Plein Air Painting",
    "friends_list": [
        {
            "friend_id": 2
        },
        {
            "friend_id": 4
        }
    ]
}
```
Note: friends_list is an optional param

| Code | Description |
| :--- | :--- |
| 201 | `CREATED` |

Response:

```json

{
    "id": 33,
    "type": "group",
    "attributes": {
        "group_host_id": 1,
        "group_host_name": "Andra Helton",
        "group_name": "Plein Air Painting",
        "group_friends": [
            {
                "user_id": 2,
                "user_name": "otheruser321",
                "full_name": "Antonio King Hunt",
                "phone_number": "555-111-5555"
            },
            {
                "user_id": 4,
                "user_name": "harrison321",
                "full_name": "Harrison Ryan",
                "phone_number": "555-999-0000"
            }
        ],
        "group_events": []
    }
}
```

Errors:

| Code | Description |
| :--- | :--- |
| 400 | `BAD REQUEST` |

Response:

```json

{
    "error": [
        "title": "BAD REQUEST",
        "status": "400"
    ]
}
```

</details>

---

### Update a Group

```http
PATCH /groups/:group_id/
```

<details close>
<summary>  Details </summary>
<br>

Request: <br>
```json
{
    "name": "Roller Bladers"
}
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json

{
    "id": 4,
    "type": "group",
    "attributes": {
        "group_host_id": 2,
        "group_host_name": "Antonio King Hunt",
        "group_name": "Roller Bladers",
        "group_friends": [
            {
                "user_id": 6,
                "user_name": "william321",
                "full_name": "William Lampke",
                "phone_number": "555-222-1111"
            }, etc.
        ],
        "group_events": []
    }
}
```

Errors:

| Code | Description |
| :--- | :--- |
| 400 | `BAD REQUEST` |

Response:

```json

{
    "error": [
        "title": "BAD REQUEST",
        "status": "400"
    ]
}
```

</details>

---

### Delete Group

```http
DELETE /groups/:group_id/
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

------------

</details>

<details>
<summary>
  
> ### Events
</summary>

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
            "group_name": "Game Night",
            "host_id": 1,
            "host_name": "Andra Helton",
            "title": "Space Catan",
            "date": "05-20-23",
            "time": "8:00 PM",
            "address": "123 Sesame St.",
            "description": "It's a fun time, just come already",
            "invited": [
                {
                    "user_id": 3,
                    "user_name": "joe123",
                    "full_name": "Joe Fogiato",
                    "phone_number": "555-888-1111"
                }, etc.
            ]
        }, etc.
    ]
}
```

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
        "id": 5,
        "group": 2,
        "group_name": "Friday Night Hangs",
        "host_id": 1,
        "host_name": "Andra Helton",
        "title": "Renaissance Festival Afterparty",
        "date": "06-07-23",
        "time": "6:00 PM",
        "address": "321 Candy Ln.",
        "description": "Come to my place!",
        "invited": [
            {
                "user_id": 7,
                "user_name": "trevor123",
                "full_name": "Trevor Fitzgerald",
                "phone_number": "555-222-3333"
            }, etc.
        ]
    }
}
```

Errors:

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
    "group": 2,
    "title": "Denver Night Hang",
    "date": "06-05-23",
    "time": "8:00 PM",
    "address": "123 Denver Rd.",
    "description": "Having a ball downtown"
}
```

| Code | Description |
| :--- | :--- |
| 201 | `Created` |

Response:

```json

{
    "id": 7,
    "group": 2,
    "group_name": "Friday Night Hangs",
    "host_id": 1,
    "host_name": "Andra Helton",
    "title": "Denver Night Hang",
    "date": "06-05-23",
    "time": "8:00 PM",
    "address": "123 Denver Rd.",
    "description": "Having a ball downtown",
    "invited": [
        {
            "user_id": 7,
            "user_name": "trevor123",
            "full_name": "Trevor Fitzgerald",
            "phone_number": "555-222-3333"
        },
        {
            "user_id": 8,
            "user_name": "gus123",
            "full_name": "Gus Deribeaux",
            "phone_number": "555-222-9999"
        }
    ]
}
```

Errors:

| Code | Description |
| :--- | :--- |
| 400 | `BAD REQUEST` |

Response:

```json

{
    "error": [
        "title": "BAD REQUEST",
        "status": "400"
    ]
}
```

</details>

---

### Update Event

```http
PATCH /events/:event_id/
```

<details close>
<summary>  Details </summary>
<br>

Request: <br>
```json
{
    "title": "Root - A medium length game",
    "date": "08-04-24",
    "time": "9:00 PM",
    "address": "321 another address St.",
    "description": "BYOB - we can also get wings"
}
```

| Code | Description |
| :--- | :--- |
| 201 | `Created` |

Response:

```json

{
    "id": 3,
    "group": 1,
    "group_name": "Game Night",
    "host_id": 1,
    "host_name": "Andra Helton",
    "title": "Root - A medium length game",
    "date": "08-04-24",
    "time": "9:00 PM",
    "address": "321 another address St.",
    "description": "BYOB - we can also get wings",
    "invited": [
        {
            "user_id": 3,
            "user_name": "joe123",
            "full_name": "Joe Fogiato",
            "phone_number": "555-888-1111"
        }, etc.
    ]
}
```

Errors:

| Code | Description |
| :--- | :--- |
| 400 | `BAD REQUEST` |

Response:

```json

{
    "error": [
        "title": "BAD REQUEST",
        "status": "400"
    ]
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
```
No Parameters
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

</details>
</details>

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
