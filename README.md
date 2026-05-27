# Flask User Management System

A lightweight User Management application built with **Flask**, **SQLAlchemy ORM**, and **MySQL**. This project demonstrates a clean MVC-like architecture with Blueprints, centralized database configuration, and template rendering.

## 🚀 Features

- **User Registration**: Add new users with roles via a web form.
- **User Directory**: View a list of all registered users.
- **Profile View**: Fetch specific user details by ID.
- **Database Integration**: Automated table creation using SQLAlchemy.
- **Blueprint Architecture**: Modular routing for better scalability.

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Database**: MySQL
- **ORM**: SQLAlchemy
- **Frontend**: Jinja2 Templates, Bootstrap (via templates)

## 📂 Project Structure

```text
Python-Assesment/
├── app.py              # Application entry point & configuration
├── controllers/
│   └── usercontrol.py  # Route handlers and business logic
├── db/
│   └── userdbcontext.py # Database models (User schema)
├── templates/          # HTML files (index, users, newuser, etc.)
├── utils/
│   └── settings.py     # Database engine & connection settings
└── Requirements.txt    # Python dependencies
```

## ⚙️ Setup Instructions

1. **Prerequisites**:
   Ensure you have Python installed and a MySQL server running.

2. **Install Dependencies**:
   ```bash
   pip install flask sqlalchemy pymysql
   ```

3. **Database Configuration**:
   Update the connection string in `utils/settings.py` with your MySQL credentials:
   ```python
   raw_password = "your_password"
   engine = create_engine(f"mysql+pymysql://root:{encoded_password}@localhost:3306/users")
   ```

4. **Run the Application**:
   ```bash
   python app.py
   ```
   The app will start at `http://127.0.0.1:5000`.

## 🗄️ Database Setup (Manual SQL)

To initialize the database environment manually before running the Flask application, the following SQL sequence was used:

1. **Check for existing databases**:
   ```sql
   SHOW DATABASES;
   ```
2. **Create the 'users' database**:
   ```sql
   CREATE DATABASE users;
   ```
3. **Create the 'users' table**:
   ```sql
   CREATE TABLE users (
       id INT PRIMARY KEY AUTO_INCREMENT,
       name VARCHAR(255),
       email VARCHAR(255),
       role VARCHAR(255)
   );
   ```
4. **Seed initial user data**:
   ```sql
   INSERT INTO users (name, email, role) VALUES ('Admin', 'admin@example.com', 'Superuser');
   ```

## 🔗 API Endpoints

All routes are prefixed with `/auth` as defined in `app.py`.

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/` | Home Page |
| GET    | `/hello` | Hello World Message |
| GET    | `/users` | List all users |
| GET    | `/users/<id>` | View specific user |
| GET/POST| `/new_user` | Display form / Submit new user |

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. **Fork** the Project.
2. **Create** your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. **Commit** your Changes (`git commit -m 'Add some AmazingFeature'`).
4. **Push** to the Branch (`git push origin feature/AmazingFeature`).
5. **Open** a Pull Request.

## 🔄 Git Workflow

This project follows a standard feature-branch workflow:

- **Main Branch**: The `main` branch contains stable, production-ready code.
- **Feature Branches**: Use descriptive names for branches (e.g., `feature/user-validation` or `bugfix/connection-leak`).
- **Pull Requests**: All changes must be submitted via Pull Requests. Please provide a clear description of the changes and link any relevant issues.

### Coding Standards
- Follow PEP 8 for Python code style.
- Ensure all database operations are handled within the `SessionLocal` context manager to prevent connection leaks.
- Document any new routes or utility functions added to the project.
