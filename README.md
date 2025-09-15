# Simple FastAPI Todo API

This is a simple Todo API built with FastAPI, SQLAlchemy, and PostgreSQL. This project is a step-by-step guide to creating a robust and scalable API with a database connection.

-----

## Prerequisites

Before you begin, ensure you have the following installed:

  * Python 3.7+
  * PostgreSQL

-----

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/simple-fastapi-todo-api.git
    cd simple-fastapi-todo-api
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**

    Create a file named `requirements.txt` and add the following lines:

    ```
    fastapi
    uvicorn[standard]
    sqlalchemy
    psycopg2-binary
    pydantic-settings
    ```

    Then, install the packages:

    ```bash
    pip install -r requirements.txt
    ```

-----

## Database Configuration

1.  **Create a `.env` file** in the root of the project and add your database URL:

    ```
    DATABASE_URL=postgresql://user:password@host:port/dbname
    ```

    For example:

    ```
    DATABASE_URL=postgresql://postgres:mysecretpassword@localhost:5432/tododb
    ```

2.  **Make sure your PostgreSQL server is running.**

-----

## Project Structure

```
/myproject
├── app
│   ├── api
│   │   ├── deps.py
│   │   └── v1
│   │       └── endpoints
│   │           └── items.py
│   ├── core
│   │   └── config.py
│   ├── db
│   │   └── session.py
│   ├── models
│   │   └── item.py
│   ├── schemas
│   │   └── item.py
│   └── main.py
├── requirements.txt
└── .env
```

-----

## Running the Application

Once you have everything set up, you can run the application with:

```bash
uvicorn app.main:app --reload
```

You can now access the API at [http://127.0.0.1:8000](https://www.google.com/url?sa=E&source=gmail&q=http://127.0.0.1:8000).

-----

## API Endpoints

### Root

  * **GET /**: Returns a welcome message.

      * **Response:**

        ```json
        {
          "status": "ok",
          "message": "Welcome to the Todo API!"
        }
        ```

### Items

  * **POST /**: Creates a new todo item.

      * **Request Body:**

        ```json
        {
          "title": "My first todo",
          "description": "This is my first todo item."
        }
        ```

      * **Response:**

        ```json
        {
          "id": 1,
          "title": "My first todo",
          "description": "This is my first todo item.",
          "completed": false
        }
        ```