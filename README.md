# FastAPI To-Do Application

A simple beginner-friendly To-Do API built using **FastAPI**,
**SQLAlchemy**, and **PostgreSQL/SQLite** with a clean production-level
folder structure.

## Features

-   Create a new To-Do
-   Get all To-Dos
-   Get a To-Do by ID
-   Clean project structure (services, schemas, routes, db)
-   Works on Ubuntu

## Project Structure

    fastapi-project/
    │
    ├── app/
    │   ├── main.py
    │   ├── api/
    │   │   └── v1/
    │   │       └── todo_router.py
    │   ├── models/
    │   │   └── todo.py
    │   ├── schemas/
    │   │   └── todo_schema.py
    │   ├── services/
    │   │   └── todo_service.py
    │   ├── db/
    │   │   ├── sessions.py
    │   │   └── base.py
    │   └── core/
    │       └── config.py
    │
    ├── requirements.txt
    ├── README.md
    └── .env

## Ubuntu Setup

### Install Python & Tools

``` bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip python3-venv -y
```

### Create Virtual Environment

``` bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

``` bash
pip install -r requirements.txt
```

## Database Setup

### postgress (local)

No setup needed.

### PostgreSQL (optional)

``` bash
sudo apt install postgresql postgresql-contrib -y
sudo -u postgres psql
CREATE DATABASE todo_db;
\q
```

Add to `.env`:

    DATABASE_URL=postgresql://postgres:yourpassword@localhost/todo_db

## Run the Application

``` bash
uvicorn app.main:app --reload
```

Open API Docs:\
http://127.0.0.1:8000/docs

## API Endpoints

### POST /v1/todo/

``` json
{
  "title": "Buy groceries",
  "is_completed": false,
  "description": "Get milk and eggs"
}
```

### GET /v1/todo/

Returns all todos

### GET /v1/todo/{todo_id}

Returns single todo

## Git Setup (Ubuntu)

``` bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/your-username/fastapi-todo.git
git push -u origin main
```

## Author

Developed by Sankar Senthil while learning FastAPI.