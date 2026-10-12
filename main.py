
import json

from models.student import Student
from models.course import Course
from services.student_manager import StudentManager
import storage
from storage.sqlite_student_storage import SQLiteStudentStorage


def main():
    storage = SQLiteStudentStorage()
    manager = StudentManager(storage)

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Enroll Student in Course")
        print("7. View Student Courses")
        print("8. Exit")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                student_id = int(input("Enter student ID: "))
                name = input("Enter student name: ").strip()
                age = int(input("Enter student age: "))

                student = Student(student_id, name, age)
                manager.add_student(student)

            elif choice == "2":
                manager.display_students()

            elif choice == "3":
                student_id = int(
                    input("Enter student ID to search: ")
                )
                student = manager.find_student(student_id)

                if student is not None:
                    print("Student found:", student)
                else:
                    print("Student not found.")

            elif choice == "4":
                student_id = int(
                    input("Enter student ID to update: ")
                )
                name = input("Enter the new name: ").strip()
                age = int(input("Enter the new age: "))

                manager.update_student(student_id, name, age)

            elif choice == "5":
                student_id = int(
                    input("Enter student ID to delete: ")
                )
                manager.delete_student(student_id)

            elif choice == "6":
                student_id = int(input("Enter student ID: "))
                course_name = input(
                    "Enter course name: "
                ).strip()
                course_duration = input(
                    "Enter course duration: "
                ).strip()

                if not course_name:
                    print("Error: Course name cannot be empty!")
                    continue

                if not course_duration:
                    print("Error: Course duration cannot be empty!")
                    continue

                course = Course(
                    course_name,
                    course_duration
                )

                manager.enroll_student(student_id, course)

            elif choice == "7":
                student_id = int(
                    input("Enter student ID to view courses: ")
                )
                manager.display_student_courses(student_id)

            elif choice == "8":
                print(
                    "Thank you for using the Student Management System!"
                )
                break

            else:
                print(
                    "Invalid choice. Please enter a number from 1 to 8."
                )

        except ValueError:
            print(
                "Invalid input. Student ID and age must be whole numbers."
            )

        except (OSError, json.JSONDecodeError) as error:
            print("Storage error:", error)


if __name__ == "__main__":
    main()