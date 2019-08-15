# TodoApp
A django REST API app for creating TODO list with Categories

## Models

1. Category
2. Todo


## CRUD APIs for Category

### Create
* Method POST

```/api/v1/categories/```

params:
```json
{
    "name": ""
}
```

### Retrieve
* Method GET

```/api/v1/categories/```

### Update
* Method PUT

```/api/v1/categories/{primary-key}/```

### Delete
* Method DELETE

```/api/v1/categories/{primary-key}/```

## CRUD APIs for Todo

### Create
* Method POST

```/api/v1/todo/```

params:
```json
{
    "title": "",
    "description": "",
    "assigned_date": null,
    "category": null
}
```

### Retrieve
* Method GET

```/api/v1/todo/```

### Update
* Method PUT

```/api/v1/todo/{primary-key}/```

### Delete
* Method DELETE

```/api/v1/todo/{primary-key}/```

