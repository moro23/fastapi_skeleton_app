# FastAPI Web Application with SQLAlchemy ORM

## Overview

This is a FastAPI-based web application skeleton that integrates SQLAlchemy ORM for database management. It includes features such as:

- Authentication with JWT
- User management
- Password management
- Role-Based Access Control (RBAC)
- File CRUD operations (local storage, GCS, S3)
- Socket.IO for real-time communication
- Email notifications
- Repository pattern for data management

## Features

- **Authentication**: Secure login and registration using JWT.
- **User Management**: CRUD operations for users with role-based access control.
- **Password Management**: Secure password hashing and verification.
- **File Management**: CRUD operations for files with support for local storage, Google Cloud Storage (GCS), and Amazon S3.
- **Socket.IO**: Real-time communication with WebSocket support.
- **Email Notifications**: Send email notifications using FastAPI Mail.
- **Repository Pattern**: Organized data management with SQLAlchemy.

## Installation

### Prerequisites

- Python 3.8 or later
- A database (e.g., PostgreSQL, SQLite)

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/fastapi_app.git
   cd fastapi_app
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your database:**

   Edit `app/config.py` and set the `DATABASE_URL` to your database connection string.

   ```python
   DATABASE_URL = "sqlite:///./test.db"  # Replace with your DB URL
   ```

5. **Initialize the database:**

   Run the following command to create the database tables:

   ```bash
   python -c "from app.db import Base, engine; Base.metadata.create_all(bind=engine)"
   ```

6. **Run the application:**

   ```bash
   uvicorn app.main:app --reload
   ```

   The application will be accessible at `http://127.0.0.1:8000`.

## API Endpoints

### Authentication

- **POST /auth/login**: Log in a user and receive a JWT token.
- **POST /auth/register**: Register a new user.

### User Management

- **GET /auth/me**: Get details of the currently authenticated user.

### File Management

- **POST /file/upload**: Upload a file.
- **GET /file/{file_id}**: Retrieve a file.
- **DELETE /file/{file_id}**: Delete a file.

### Real-time Communication

- **WebSocket /ws**: Real-time messaging.

## Configuration

- **JWT_SECRET**: The secret key for encoding JWT tokens.
- **DATABASE_URL**: The URL for connecting to your database.
- **EMAIL_CONFIG**: Configuration for sending emails (SMTP settings).

## Testing

Run the tests using pytest:

```bash
pytest
```

## Contributions

Feel free to open issues and submit pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or comments, please reach out to [your.email@example.com](mailto:your.email@example.com).
