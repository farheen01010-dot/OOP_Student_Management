
import sqlite3

from models.student import Student
from models.course import Course
from storage.student_storage import StudentStorage


class SQLiteStudentStorage(StudentStorage):

    def __init__(self, database_path="students.db"):
        self.database_path = database_path

        with self._connect() as connection:
            connection.execute("PRAGMA foreign_keys = ON")

            connection.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    student_id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL
                )
            """)

            connection.execute("""
                CREATE TABLE IF NOT EXISTS courses (
                    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    student_id INTEGER NOT NULL,
                    name TEXT NOT NULL,
                    duration TEXT NOT NULL,
                    FOREIGN KEY (student_id)
                        REFERENCES students(student_id)
                        ON DELETE CASCADE,
                    UNIQUE (student_id, name)
                )
            """)

    def _connect(self):
        return sqlite3.connect(self.database_path)

    def get_all(self):
        with self._connect() as connection:
            connection.execute("PRAGMA foreign_keys = ON")

            student_rows = connection.execute("""
                SELECT student_id, name, age
                FROM students
                ORDER BY student_id
            """).fetchall()

            students = []

            for student_id, name, age in student_rows:
                student = Student(student_id, name, age)

                course_rows = connection.execute("""
                    SELECT name, duration
                    FROM courses
                    WHERE student_id = ?
                    ORDER BY course_id
                """, (student_id,)).fetchall()

                for course_name, duration in course_rows:
                    student.add_course(
                        Course(course_name, duration)
                    )

                students.append(student)

            return students

    def save(self, student):
        with self._connect() as connection:
            connection.execute("PRAGMA foreign_keys = ON")

            connection.execute("""
                INSERT INTO students (student_id, name, age)
                VALUES (?, ?, ?)
            """, (
                student.student_id,
                student.name,
                student.age
            ))

            for course in student.courses:
                connection.execute("""
                    INSERT INTO courses
                        (student_id, name, duration)
                    VALUES (?, ?, ?)
                """, (
                    student.student_id,
                    course.name,
                    course.duration
                ))

    def update_student(self, student):
        with self._connect() as connection:
            connection.execute("PRAGMA foreign_keys = ON")

            cursor = connection.execute("""
                UPDATE students
                SET name = ?, age = ?
                WHERE student_id = ?
            """, (
                student.name,
                student.age,
                student.student_id
            ))

            return cursor.rowcount > 0

    def delete_student(self, student_id):
        with self._connect() as connection:
            connection.execute("PRAGMA foreign_keys = ON")

            cursor = connection.execute("""
                DELETE FROM students
                WHERE student_id = ?
            """, (student_id,))

            return cursor.rowcount > 0

    def update_all(self, students):
        with self._connect() as connection:
            connection.execute("PRAGMA foreign_keys = ON")

            connection.execute("DELETE FROM courses")
            connection.execute("DELETE FROM students")

            for student in students:
                connection.execute("""
                    INSERT INTO students (student_id, name, age)
                    VALUES (?, ?, ?)
                """, (
                    student.student_id,
                    student.name,
                    student.age
                ))

                for course in student.courses:
                    connection.execute("""
                        INSERT INTO courses
                            (student_id, name, duration)
                    VALUES (?, ?, ?)
                    """, (
                        student.student_id,
                        course.name,
                        course.duration
                    ))