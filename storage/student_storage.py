from abc import ABC, abstractmethod


# =========================
# STORAGE ABSTRACTION
# =========================

class StudentStorage(ABC):

    @abstractmethod
    def save(self, student):
        pass

    @abstractmethod
    def get_all(self):
        pass


# =========================
# IN-MEMORY STORAGE
# =========================

class InMemoryStudentStorage(StudentStorage):

    def __init__(self):

        self.students = []

    def save(self, student):

        self.students.append(student)

    def get_all(self):

        return self.students