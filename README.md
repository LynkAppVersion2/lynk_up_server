## RESTful Endpoints

<details close>


### Get a User


```http
GET /api/v1/users/:id
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
            "first_name": "Kaylah",
            "last_name": "Rose",
            "phone_number": null,
            "email": "kaylahrosem@gmail.com",
            "emergency_contact_name": null,
            "emergency_contact_phone_number": null,
            "google_uid": "12345678901234567890"
        }
    }
}
```

</details>

---
