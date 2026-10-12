class Course:

    def __init__(self, name, duration):

        self.name = name
        self.duration = duration

    def display_course(self):

        print("Course:", self.name)
        print("Duration:", self.duration)