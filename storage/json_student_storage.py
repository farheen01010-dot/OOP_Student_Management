
import json
import os

from models.student import Student
from models.course import Course
from storage.student_storage import StudentStorage


class JsonStudentStorage(StudentStorage):

    def __init__(self, file_path="data/students.json"):
        self.file_path = file_path

        folder = os.path.dirname(self.file_path)

        if folder:
            os.makedirs(folder, exist_ok=True)

        if not os.path.exists(self.file_path):
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump([], file)

    def get_all(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            records = json.load(file)

        students = []

        for record in records:
            student = Student(
                record["student_id"],
                record["name"],
                record["age"]
            )

            for course_data in record.get("courses", []):

                # Support the old format: "Biotechnology"
                if isinstance(course_data, str):
                    course = Course(
                        course_data,
                        "Not specified"
                    )

                # Support the new format: name + duration
                else:
                    course = Course(
                        course_data["name"],
                        course_data.get(
                            "duration",
                            "Not specified"
                        )
                    )

                student.add_course(course)

            students.append(student)

        return students

    def save(self, student):
        students = self.get_all()
        students.append(student)
        self.update_all(students)

    def update_all(self, students):
        records = []

        for student in students:
            courses = []

            for course in student.courses:
                courses.append({
                    "name": course.name,
                    "duration": course.duration
                })

            records.append({
                "student_id": student.student_id,
                "name": student.name,
                "age": student.age,
                "courses": courses
            })

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(records, file, indent=4)