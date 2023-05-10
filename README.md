## RESTful Endpoints

<details close>


### Get a User


```http
GET /api/v1/users/:phone_number
```

<details close>
<summary>  Details </summary>
<br>
    
Parameters: <br>
```
No Parameters
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Example Value:

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

Example Value:

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
