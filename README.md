<div id="header" align="center">
  <img src="images/240969217-dc0f4910-32f9-4e3a-a784-4ba67c4497cc.png" width="300px" height="200px"/>
  <hr>
</div>

## Introduction
Welcome to the backend repository of Lynk Up Version 2! Lynk Up is a platform for creating, discovering, and managing events. From small gatherings and meetings to large parties, this app provides an intuitive and user-friendly platform to manage social circles and meetups. This version of the LynkUp app is redesigned to allow users to fluidly navigate adding and managing friendships, creating friend groups and events, and sending SMS messages to update invitees with event information.


## Tech Stack
- **Python:** Our primary programming language offering simplicity and versatility.
- **Django REST Framework:** Used for building APIs, ensuring a scalable and secure connection between our frontend and backend services.


## Setup

1. Fork and Clone the repository
```shell
git clone git@github.com:LynkAppVersion2/lynk_up_server.git
```
<br>
<br>

2. Navigate to the directory
```shell
cd lynk_up_server
```
<br>
<br>

3. Create Virtual Environment
```shell
run python3 -m venv .venv
```
<br>
```shell
run . .venv/bin/activate
```
<br>
<br>

4. Select Interpreter
```shell
cmd + shift + P → Python: Select Interpreter → Select Python 3.10.11 (’.venv’: pipenv) ./.venv/bin/python (recommended)
```
<br>
<br>

5. Create Environment for Keys
```shell
run touch .env
```
<br>
Put the following keys inside .env file:
```shell
DEBUG=True
DJANGO_ENV=development
```
<br>
<br>

6. Install Packages
```shell
cd lynk_up_server
```
<br>
```shell
run pip install -r dependencies.txt
```
<br>
<br>

7. Generate Secret Key
```shell
python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
Copy the output
<br>

Add the following to the .env file:
```shell
SECRET_KEY=<YOUR_GENERATED_KEY_HERE>
```
<br>
<br>

8. Run the Migrations
```shell
run python manage.py migrate
```
<br>
<br>

9. Load Fixture Data
```shell
run python manage.py loaddata lynk_up_server/fixtures/user.json
```
<br>

```shell
run python manage.py loaddata lynk_up_server/fixtures/friend.json
```
<br>

```shell
run python manage.py loaddata lynk_up_server/fixtures/group.json
```
<br>

```shell
run python manage.py loaddata lynk_up_server/fixtures/event.json
```
<br>
<br>

10. Run the Tests
```shell
run pytest
```
<br>
If everything's green, you're good to go!

<br>
---


## RESTful Endpoints

Base url to reach the endpoints listed below:
```
https://lynk-up-server.onrender.com
```

<details close>
<summary> All Endpoints </summary>

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
        "id": "1",
        "attributes": {
            "user_name": "Tesseract",
            "phone_number": "888-888-8888",
            "full_name": "Antonio King Hunt",
        },
        "events": [
            {
                "id": 1,
                "group": 1,
                "group_name": "Best Buds",
                "title": "Magic Tournament",
                "date": "05-23-2023",
                "time": "7:00pm",
                "address": "123 fun st.",
                "description": "Fun times with fun people"
            },
            {etc}
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

### Get a Users' Friends

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
                "user_id": 1,
                "user_name": "Joe Fogiato"
            },
            {
                "user_id": 2,
                "user_name": "Dawson T"
            }
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
