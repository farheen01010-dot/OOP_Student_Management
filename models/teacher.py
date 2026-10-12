from models.person import Person


class Teacher(Person):

    def __init__(self, name, age, subject):

        super().__init__(name, age)

        self.subject = subject

    def teach(self):

        print(
            self.name,
            "is teaching",
            self.subject
        )

    def introduce(self):

        print("Hi, my name is", self.name)
        print("I am", self.age, "years old.")
        print("I teach", self.subject)