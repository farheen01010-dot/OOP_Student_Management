
from models.person import Person


class Student(Person):

    def __init__(self, student_id, name, age):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = []

    def add_course(self, course):
        for existing_course in self.courses:
            if existing_course.name.lower() == course.name.lower():
                print("Student is already enrolled in this course!")
                return False

        self.courses.append(course)
        return True

    def display_courses(self):
        if not self.courses:
            print(self.name, "is not enrolled in any courses.")
            return

        print(self.name, "is enrolled in:")

        for course in self.courses:
            print(
                "-",
                course.name,
                "| Duration:",
                course.duration
            )

    def introduce(self):
        print("Hi, my name is", self.name)
        print("I am", self.age, "years old.")

    def __str__(self):
        return (
            f"ID: {self.student_id}, "
            f"Name: {self.name}, "
            f"Age: {self.age}"
        )

    def __repr__(self):
        return (
            f"Student(student_id={self.student_id}, "
            f"name='{self.name}', age={self.age})"
        )

    def __len__(self):
        return len(self.courses)

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented

        return self.student_id == other.student_id