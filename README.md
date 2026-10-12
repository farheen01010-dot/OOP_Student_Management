# OOP Student Management System

A Python-based Student Management System built to practice object-oriented programming, modular software design, and database operations using SQLite.

## Features

* Add, view, search, update, and delete student records
* Enroll students in courses and view course details
* Validate student IDs, names, and ages
* Prevent duplicate student IDs and duplicate course enrollment through application validation
* Store student and course information persistently in SQLite
* Use SQL queries to create, retrieve, update, and delete records
* Separate models, business logic, and storage into Python modules
* Support JSON storage and migration of existing JSON records to SQLite

## Technologies Used

* Python
* Object-Oriented Programming (OOP)
* SQLite and SQL
* JSON
* Git and GitHub

## Project Structure

```text
OOP_Student_Management/
├── main.py
├── models/
├── services/
├── storage/
├── reports/
├── data/
├── view_database.py
├── migrate_json_to_sqlite.py
├── add_course_sql.py
├── sqlite_test.py
├── requirements.txt
└── .gitignore
```

## Getting Started

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd OOP_Student_Management
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your repository's actual URL.

### 2. Create a virtual environment

Windows:

```powershell
python -m venv myenv
.\myenv\Scripts\Activate.ps1
```

### 3. Run the application

```bash
python main.py
```

The application creates the SQLite database and required tables when initialized. The database file is stored locally and is not included in the repository.

## Learning Outcomes

This project demonstrates practical experience with Python classes and objects, inheritance, encapsulation, abstraction, polymorphism, CRUD operations, input validation, SQL queries, SQLite persistence, and modular project organization.

## Future Improvements

* Add automated unit tests
* Improve database operations and error handling
* Add a graphical user interface or web interface
* Introduce database migrations and reporting features

## Author

Python and AI/ML enthusiast interested in software development, machine learning, and building practical applications.
