# FastAPI Spring-Style API Example

This is a simple API built with **FastAPI**, structured similarly to a typical **Spring Boot** application.  
It was created for **study and reference purposes**, and includes clear separation of concerns:

- `models.py` → database models (SQLAlchemy)
- `schemas.py` → data validation and serialization (Pydantic)
- `services.py` → business logic
- `routers/` → route definitions (similar to controllers)
- `database.py` → database connection setup
- `main.py` → application entry point

## 🚀 Features

- Create and list users
- SQLite database
- Pydantic for validation
- Separation of layers: model, schema, service, router
- Comments in each file for learning purposes

## 📦 Requirements

- Python 3.10+
- FastAPI
- Uvicorn
- SQLAlchemy

You can install dependencies with:

```bash
pip install fastapi uvicorn sqlalchemy
```


## ▶️ How to run
```bash
uvicorn main:app --reload
```

Then open your browser at:

- http://127.0.0.1:8000/docs
## 📚 About this project
This project was created to help understand how FastAPI works, using a layered structure familiar to Spring Boot developers.
Each part of the code is commented for easier understanding.

Feel free to use it as a boilerplate or study reference.

## 📘 License
This project is for educational purposes. No license is applied.
