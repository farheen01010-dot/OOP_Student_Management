
class StudentManager:

    def __init__(self, storage):
        self.storage = storage

    # Add a new student
    def add_student(self, student):
        if (
            not isinstance(student.student_id, int)
            or isinstance(student.student_id, bool)
            or student.student_id <= 0
        ):
            print("Error: Student ID must be a positive whole number!")
            return False

        if not student.name.strip():
            print("Error: Student name cannot be empty!")
            return False

        if (
            not isinstance(student.age, int)
            or isinstance(student.age, bool)
            or student.age <= 0
        ):
            print("Error: Age must be a positive whole number!")
            return False

        students = self.storage.get_all()

        for existing_student in students:
            if existing_student.student_id == student.student_id:
                print("Error: Student ID already exists!")
                return False

        self.storage.save(student)
        print("Student added successfully!")
        return True

    # Find a student by ID
    def find_student(self, student_id):
        students = self.storage.get_all()

        for student in students:
            if student.student_id == student_id:
                return student

        return None

    # Update a student's name and age
    def update_student(self, student_id, new_name, new_age):
        if not new_name.strip():
            print("Error: Student name cannot be empty!")
            return False

        if (
            not isinstance(new_age, int)
            or isinstance(new_age, bool)
            or new_age <= 0
        ):
            print("Error: Age must be a positive whole number!")
            return False

        student = self.find_student(student_id)

        if student is None:
            print("Error: Student not found!")
            return False

        student.name = new_name.strip()
        student.age = new_age

        if hasattr(self.storage, "update_student"):
            updated = self.storage.update_student(student)

            if not updated:
                print("Error: Student could not be updated!")
                return False
        else:
            students = self.storage.get_all()
            self.storage.update_all(students)

        print("Student updated successfully!")
        return True

    # Delete a student by ID
    def delete_student(self, student_id):
        student = self.find_student(student_id)

        if student is None:
            print("Error: Student not found!")
            return False

        if hasattr(self.storage, "delete_student"):
            deleted = self.storage.delete_student(student_id)

            if not deleted:
                print("Error: Student could not be deleted!")
                return False
        else:
            students = self.storage.get_all()
            students.remove(student)
            self.storage.update_all(students)

        print("Student deleted successfully!")
        return True

    # Enroll a student in a course
    def enroll_student(self, student_id, course):
        students = self.storage.get_all()

        for student in students:
            if student.student_id == student_id:
                if student.add_course(course):
                    self.storage.update_all(students)
                    print("Student enrolled successfully!")
                    return True

                return False

        print("Error: Student not found!")
        return False

    # Display a student's courses
    def display_student_courses(self, student_id):
        student = self.find_student(student_id)

        if student is None:
            print("Error: Student not found!")
            return False

        student.display_courses()
        return True

    # Display all registered students
    def display_students(self):
        students = self.storage.get_all()

        if not students:
            print("No students registered.")
            return

        print("Registered Students:")

        for student in students:
            print("-", student)