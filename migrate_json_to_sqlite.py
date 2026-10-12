
import json
import sqlite3

from models.student import Student
from models.course import Course
from storage.sqlite_student_storage import SQLiteStudentStorage


def migrate_json_to_sqlite():
    json_path = "data/students.json"
    database_path = "students.db"

    # Check that the original JSON file exists
    try:
        with open(json_path, "r", encoding="utf-8") as file:
            records = json.load(file)

    except FileNotFoundError:
        print("JSON file not found:", json_path)
        return

    except json.JSONDecodeError:
        print("The JSON file contains invalid JSON.")
        return

    if not isinstance(records, list):
        print("Invalid data: Expected a list of student records.")
        return

    # Initialize the database and create its tables
    storage = SQLiteStudentStorage(database_path)

    migrated = 0
    skipped = 0

    try:
        with sqlite3.connect(database_path) as connection:
            connection.execute("PRAGMA foreign_keys = ON")

            for record in records:
                student_id = record.get("student_id")
                name = record.get("name")
                age = record.get("age")

                # Validate the required student fields
                if (
                    not isinstance(student_id, int)
                    or isinstance(student_id, bool)
                    or student_id <= 0
                    or not isinstance(name, str)
                    or not name.strip()
                    or not isinstance(age, int)
                    or isinstance(age, bool)
                    or age <= 0
                ):
                    print("Skipping invalid student record:", record)
                    skipped += 1
                    continue

                # Skip IDs already present in SQLite
                existing = connection.execute(
                    "SELECT 1 FROM students WHERE student_id = ?",
                    (student_id,)
                ).fetchone()

                if existing:
                    print(
                        "Skipping existing student ID:",
                        student_id
                    )
                    skipped += 1
                    continue

                # Insert the student
                connection.execute(
                    """
                    INSERT INTO students (student_id, name, age)
                    VALUES (?, ?, ?)
                    """,
                    (student_id, name.strip(), age)
                )

                # Import courses in either supported JSON format
                courses = record.get("courses", [])

                if not isinstance(courses, list):
                    print(
                        "Ignoring invalid courses for student:",
                        student_id
                    )
                    courses = []

                for course_data in courses:
                    if isinstance(course_data, str):
                        course_name = course_data.strip()
                        duration = "Not specified"

                    elif isinstance(course_data, dict):
                        course_name = course_data.get("name", "")
                        duration = course_data.get(
                            "duration",
                            "Not specified"
                        )

                        if not isinstance(course_name, str):
                            continue

                        if not isinstance(duration, str):
                            duration = str(duration)

                        course_name = course_name.strip()
                        duration = duration.strip()

                    else:
                        continue

                    if not course_name:
                        continue

                    connection.execute(
                        """
                        INSERT OR IGNORE INTO courses
                            (student_id, name, duration)
                        VALUES (?, ?, ?)
                        """,
                        (student_id, course_name, duration)
                    )

                migrated += 1

        print("\nMigration completed!")
        print("Students imported:", migrated)
        print("Records skipped:", skipped)
        print("Original JSON file was not changed.")

    except (sqlite3.Error, OSError) as error:
        print("Migration failed:", error)


if __name__ == "__main__":
    migrate_json_to_sqlite()