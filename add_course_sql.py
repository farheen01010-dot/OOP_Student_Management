
import sqlite3


def add_course():
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    try:
        student_id = int(input("Enter student ID: "))
        course_name = input("Enter course name: ").strip()
        duration = input("Enter course duration: ").strip()

        if student_id <= 0:
            print("Student ID must be positive.")
            return

        if not course_name or not duration:
            print("Course name and duration cannot be empty.")
            return

        # Check whether the student exists
        cursor.execute(
            "SELECT name FROM students WHERE student_id = ?",
            (student_id,)
        )

        student = cursor.fetchone()

        if student is None:
            print("Student not found.")
            return

        # Insert the course
        cursor.execute(
            """
            INSERT INTO courses (student_id, name, duration)
            VALUES (?, ?, ?)
            """,
            (student_id, course_name, duration)
        )

        # Save the transaction
        connection.commit()

        print(
            f"Course '{course_name}' added for {student[0]}!"
        )

    except ValueError:
        connection.rollback()
        print("Student ID must be a whole number.")

    except sqlite3.IntegrityError:
        connection.rollback()
        print("This student is already enrolled in that course.")

    except sqlite3.Error as error:
        connection.rollback()
        print("Database error:", error)

    finally:
        connection.close()


if __name__ == "__main__":
    add_course()