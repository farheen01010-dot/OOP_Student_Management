from abc import ABC, abstractmethod


# =========================
# STUDENT REPORT
# =========================

class StudentReport(ABC):

    @abstractmethod
    def generate(self, student):
        pass


# =========================
# BASIC STUDENT REPORT
# =========================

class BasicStudentReport(StudentReport):

    def generate(self, student):

        return (
            f"Student: {student.name}, "
            f"Age: {student.age}"
        )


# =========================
# COURSE STUDENT REPORT
# =========================

class CourseStudentReport(StudentReport):

    def generate(self, student):

        courses = [
            course.name
            for course in student.courses
        ]

        return (
            f"{student.name} is enrolled in: "
            f"{courses}"
        )