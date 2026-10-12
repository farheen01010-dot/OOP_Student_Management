
import sqlite3


def view_database():
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    try:
        print("\n===== STUDENTS AND THEIR COURSES =====")

        cursor.execute("""
            SELECT
                students.student_id,
                students.name,
                students.age,
                courses.name,
                courses.duration
            FROM students
            LEFT JOIN courses
                ON students.student_id = courses.student_id
            ORDER BY students.student_id, courses.course_id
        """)

        records = cursor.fetchall()

        if not records:
            print("No students found.")

        for record in records:
            student_id, student_name, age, course_name, duration = record

            if course_name is None:
                course_details = "No courses enrolled"
            else:
                course_details = (
                    f"{course_name} ({duration})"
                )

            print(
                f"ID: {student_id} | "
                f"Name: {student_name} | "
                f"Age: {age} | "
                f"Course: {course_details}"
            )

    finally:
        connection.close()


if __name__ == "__main__":
    view_database()