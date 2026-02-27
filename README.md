# FastAPI Project

A modern, fast, and easy-to-use API server built with **FastAPI** — a high-performance Python framework based on standard Python type hints.

---

## 🚀 Features

- Built with FastAPI for high performance and async support
- Automatic API documentation with Swagger UI and ReDoc
- Easy to extend with routers, services, and middleware
- Supports environment-based configuration
- Prepared for database migrations (Alembic)

---

## 🛠️ Built With

- **Python 3.x**
- **[FastAPI](https://github.com/fastapi/fastapi)** – API framework for creating fast and scalable HTTP services
- **Uvicorn** – Lightning-fast ASGI server
- **Pydantic** – Data validation and settings management

---

## 📁 Project Structure

````bash
📦 .
├── alembic/                 # Database migration files
├── app/
│   ├── main.py              # FastAPI application instance
│   ├── api/                 # API route definitions
│   ├── models/              # ORMs and schemas
│   ├── services/            # Business logic modules
│   └── database.py          # Database connection setup
├── requirements.txt         # Project dependencies
├── alembic.ini              # Alembic config file
└── README.md




---

## 🧪 Testing the API

You can test the API using:

- Swagger UI → `http://127.0.0.1:8000/docs`
- ReDoc → `http://127.0.0.1:8000/redoc`
- Postman
- curl

---

### 📮 Testing with Postman

1️⃣ Download and install **Postman**
https://www.postman.com/downloads/

2️⃣ Start your FastAPI server:

```bash
uvicorn app.main:app --reload
````
