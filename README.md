<div id="header" align="center">
  <img src="images/3578470E-FAA7-46ED-A5AF-285EDE7AFAC1_4_5005_c.jpeg" width="300px" height="200px"/>
  <hr>
</div>

## Introduction
Welcome to the backend repository of Lynk Up! Lynk Up is a social event management app designed to streamline the organization, attendance, and management of events across different friend groups. This repository houses the codebase for our backend services, intricately crafted using Python and the Django REST framework.

---
## Table of Contents
- [Introduction](#introduction)
- [Table of Contents](#table-of-contents)
- [Directory](#directory)
- [About](#about)
- [Tech Stack](#tech-stack)
- [Key Features](#key-features)
- [Getting Started](#getting-started)
- [RESTful Endpoints](#restful-endpoints)
  - [Get a User](#get-a-user)
  - [Get an Event](#get-an-event)
  - [Create Event](#create-event)
  - [Delete Event](#delete-event)
  - [Get all Events](#get-all-events)
  - [Get a Users' Friends](#get-a-users-friends)
  - [Create Friend](#create-friend)
  - [Delete Friend](#delete-friend)
  - [Get all Groups](#get-all-groups)
  - [Get a Group](#get-a-group)
  - [Delete Group](#delete-group)
- [Team](#team)
- [Contact](#contact)
- [Contribute](#contribute)
- [Licensing](#licensing)
---

## Directory
  [Hosted Website](https://lynk-up-client.vercel.app/dashboard)

  [Hosted Server](https://lynk-up-server.onrender.com/)

  [Client Repository](https://github.com/LYNK-UP-APP/lynk-up-client)
## About
Our backend services are at the heart of the Lynk Up app. They manage data, ensure smooth API integrations, provide secure user authentication, enable efficient event management, and prompt notification services. With Python and Django REST framework, we ensure a fast, reliable, and secure environment for our users.

## Tech Stack
- **Python:** Our primary programming language offering simplicity and versatility.
- **Django REST Framework:** Used for building APIs, ensuring a scalable and secure connection between our frontend and backend services.

## Key Features
1. **Data Management:** Employs Django ORM for seamless database queries and data manipulation.
2. **API Integrations:** Manages and integrates external APIs to augment app functionality.
3. **Event Management:** Handles all CRUD operations related to events, enabling the creation, updates, deletions, and RSVP functionalities.
---
## Getting Started
1. **Clone the Repository:** Get started with Lynk Up Backend by cloning the repository to your local machine.
2. **Install Dependencies:** Navigate into the cloned repository and install necessary dependencies.
3. **Start the Server:** Fire up the Django server.
Note: Please ensure you have Python and pip installed on your machine before running these commands.

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

---
## Contact
For any questions or suggestions, please open an issue in this repository.

## Contribute
We're excited to welcome contributions from everyone, irrespective of their experience level. Your input is crucial in helping us make Lynk Up better. Let's collaborate and build a top-notch social event management app together!

## Licensing

This project is intended to be open source. While a specific license has not been chosen yet, it is our intention to make the code and resources freely available for others to use, modify, and distribute. Until a license is selected, all rights to the code, documentation, and other project resources are reserved. Unauthorized use, distribution, or modification of any part of this project is prohibited.

---

Thank you for being part of our community! Together, let's make Lynk Up the best social event management app on the market.
