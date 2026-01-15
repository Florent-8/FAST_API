# TodoApp

## Overview

TodoApp is a web application built using the FastAPI framework. It provides a platform for users to manage their daily tasks efficiently. The application includes features such as user authentication, task management, and an admin panel for managing users and tasks.

## Features

- User registration and authentication
- Create, read, update, and delete (CRUD) operations for tasks
- Admin panel for managing users and tasks
- Responsive design with static assets (CSS and JavaScript)
- Database integration using SQLAlchemy and Alembic for migrations
- Modular architecture with routers for better code organization
- Unit tests for key functionalities

## Project Structure

```
fastapi/
├── books.py
├── books2.py
├── package.json
├── requirements.txt
├── fastapienv/                # Virtual environment
├── TodoApp/                   # Main application folder
│   ├── __init__.py
│   ├── alembic.ini            # Alembic configuration file
│   ├── database.py            # Database connection and setup
│   ├── main.py                # Application entry point
│   ├── models.py              # Database models
│   ├── routers/               # API routers
│   │   ├── admin.py           # Admin-related routes
│   │   ├── auth.py            # Authentication routes
│   │   ├── todos.py           # Task management routes
│   │   ├── users.py           # User management routes
│   └── alembic/               # Alembic migrations
│       ├── env.py
│       ├── README
│       ├── script.py.mako
│       └── versions/          # Migration scripts
├── static/                    # Static files
│   ├── css/                   # CSS files
│   └── js/                    # JavaScript files
├── templates/                 # HTML templates
│   ├── add-todo.html
│   ├── edit-todo.html
│   ├── home.html
│   ├── layout.html
│   ├── login.html
│   ├── navbar.html
│   └── register.html
└── test/                      # Unit tests
    ├── __init__.py
    ├── test_admin.py
    ├── test_auth.py
    ├── test_example.py
    ├── test_main.py
    ├── test_todos.py
    ├── test_users.py
    └── utils.py
```

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd fastapi
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv fastapienv
   fastapienv\Scripts\activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:

   ```bash
   alembic upgrade head
   ```

5. Run the application:

   ```bash
   uvicorn TodoApp.main:app --reload
   ```

6. Open your browser and navigate to `http://127.0.0.1:8000` to access the application.

## Testing

To run the unit tests, execute the following command:

```bash
pytest test/
```

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your fork.
4. Submit a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Deployment

The application is deployed and can be accessed at the following link:

[Deployment Link](https://fastapi-deploy-y05n.onrender.com)
