# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple RESTful API using the FastAPI framework in Python. You'll create endpoints, handle requests and responses, and run the API locally using Uvicorn.

## 📝 Tasks

### 🛠️ Implement a Basic REST API

#### Description
Create a small FastAPI application that exposes CRUD-style endpoints for a simple resource (for example, `items` with `id`, `name`, and `description`). Implement at minimum `GET` (list and single), `POST`, and `DELETE` endpoints.

#### Requirements
Completed program should:

- Use FastAPI to define an application and endpoints
- Provide endpoints to list items and retrieve a single item by id
- Allow adding new items via `POST` and deleting items via `DELETE`
- Validate incoming data using Pydantic models
- Return appropriate HTTP status codes (e.g., `201` for created, `404` for not found)
- Include clear docstrings and comments where helpful
- Provide instructions to run the app locally

#### Example endpoints (conceptual)

```
GET  /items        -> list items
GET  /items/{id}   -> get item by id
POST /items        -> create new item
DELETE /items/{id} -> delete item
```

### 🛠️ Optional: Extra Features

#### Description
Add optional improvements to demonstrate deeper understanding.

#### Requirements (optional)

- Add `PUT` or `PATCH` to update items
- Persist items to a simple JSON file for basic persistence
- Add query parameters for filtering or pagination
- Add unit tests for endpoints using `pytest` and `httpx`/`fastapi.testclient`

## Attachments

- `starter-code.py` — minimal FastAPI starter app
- `requirements.txt` — dependencies to install

## How to run

1. Create a virtual environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Run the app with Uvicorn:

```bash
uvicorn starter-code:app --reload
```

3. Open `http://127.0.0.1:8000/docs` to view the interactive API docs.
