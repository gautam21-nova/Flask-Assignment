# Flask Application

A robust REST API / Web Application built using the **Flask** framework, powered by a **MySQL** database, and managed via the **SQLAlchemy** ORM.

---

## 🚀 Features

* **RESTful API / Web Routes:** Clean and structured endpoints for data handling.
* **Object-Relational Mapping (ORM):** Database interactions managed seamlessly via SQLAlchemy.
* **Database Migrations:** Easy schema updates and tracking (Optional: if using Flask-Migrate).
* **Environment Configuration:** Secure handling of database credentials using environment variables.

---

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed on your local machine:

* **Python:** version 3.8 or higher.
* **MySQL Server:** A running MySQL instance (local or hosted).
* **Git:** To clone and manage the repository.

---

## 📦 Getting Started

Follow these steps to get a local copy of the project up and running.

### 1. Clone the Repository
```bash
git clone [https://github.com/gautam21-nova/Flask-Assignment/steptech_assigment](https://github.com/gautam21-nova/steptech_assigment.git)
cd your-repo-name
```

2. Set Up a Virtual Environment
It is highly recommended to use a virtual environment to isolate project dependencies.

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. Install Dependencies
Install all the required Python packages:

```bash
pip install -r requirements.txt
```
Note: Your requirements.txt should include packages like Flask, SQLAlchemy, and PyMySQL or mysqlclient.

4. Configure Environment
Create a .venv file in the root directory of the project to install libraries, creates an isolated workspace for a project, allowing you to install specific package versions without interfering with your global Python installation or other projects:

```bash
python -m venv .venv
```
Activate: This "tricks" your terminal into using the environment's specific Python and pip instead of the global ones.
Windows: 
```bash
.venv\Scripts\activate.bat
```
macOS/Linux:
```bash
source .venv/bin/activate
```

Install: Use pip to install packages only for this project.
Deactivate: Return to your global settings by simply typing (deactivate).
