## RESTful Endpoints

<details close>


### Get a User


```http
GET /api/v1/users/:phone_number
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
        "type": "user",
        "attributes": {
            "full_name": "Antonio King Hunt",
            "phone_number": "888-888-8888",
            "email": "tesseractcode@gmail.com",
            "events": [
                {
                    "id": 1
                    "title": "Magic Tournament"
                    "date": "05/20/2023"
                    "time": "7:00 PM MST"
                    "address": { 
                                    "street": "1940 Harve. Ave.",
                                    "unit": "Ste. 1-A",
                                    "city": "Missoula",
                                    "state": "MT",
                                    "zip_code": 59801
                    }
                },
                {etc}
            ]
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

<details close>


### Get Events for a User


```http
GET /api/v1/events/:user_id
```

<details close>
<summary>  Details </summary>
<br>
    
Request: <br>
```json
{
    "user_id": 1
}
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json

{
    "data": {
        "events": [
            {
                "id": "1",
                "name": "Party in the park",
                "date": "05/10/2023",
                "time": "7:00 PM MST"
            },
            {
                "id": "4",
                "name": "Another Party in the park",
                "date": "06/10/2023",
                "time": "7:00 PM MST"
            },
            {"etc": ""}
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

<details close>


### Create Event


```http
POST /api/v1/events/
```

<details close>
<summary>  Details </summary>
<br>
    
Request: <br>
```json
{
    "title": "Party at the Park",
    "details": "PARTY IN THE PARK LETS GO",
    "address_1": "123 Main st",
    "address_2": "Unit 3",
    "city": "Fort Collins",
    "state": "CO",
    "zip_code": "80525",
    "date": "01/01/2024",
    "time": "7:00 PM MST",
    "groups": [
        {
            "id": "1"
        },
        {
            "id": "4"
        }
    ]
}
```

| Code | Description |
| :--- | :--- |
| 201 | `Created` |

Response:

```json

{
    "data": {
    "id": "1",
        "title": "Party at the Park",
        "details": "12345 W. East St.",
        "address_1": "Unit 101",
        "address_2": "Fort Collins",
        "city": "Fort Collins",
        "state": "CO",
        "zip_code": "80525",
        "date": "01/01/2024",
        "time": "7:00 PM MST",
        "groups": [
            {
                "name": "Brunch",
                "friends": [
                    {
                        "id": "1",
                        "name": "Andra Helton"
                    },
                    {
                        "id": "4",
                        "name": "Antonio King Hunt"
                    }
                ]
            }
        ]
    }
}
```

</details>

---

<details close>


### Get one Event


```http
GET /api/v1/events/:event_id
```

<details close>
<summary>  Details </summary>
<br>
    
Request: <br>
```json
{
    "id": 1
}
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json

{
    "data": {
        "id": "1",
        "title": "Party at the Park",
        "details": "PARTY",
        "address_1": "123 Main St",
        "address_2": "Unit 101",
        "city": "Fort Collins",
        "state": "CO",
        "zip_code": "80525",
        "date": "01/01/2024",
        "time": "7:00 PM MST",
        "group": {
            "id": "1",
            "name": "Brunch",
            "friends": [
                {
                    "id": "1",
                    "name": "Andra Helton"
                },
                {
                    "id": "4",
                    "name": "Antonio King Hunt"
                }
            ]
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

<details close>


### Get Friends


```http
GET /api/v1/users/:user_id/friends
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

<details close>


### Create Friend


```http
POST /api/v1/users/:user_id/friends
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


<details close>


### Get one Group


```http
GET /api/v1/users/:user_id/groups/:group_id
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
        "user_id": "1"
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
