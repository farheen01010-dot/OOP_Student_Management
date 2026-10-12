from models.person import Person


class Administrator(Person):

    def __init__(self, name, age, department):

        super().__init__(name, age)

        self.department = department

    def manage(self):

        print(
            self.name,
            "is managing the",
            self.department,
            "department."
        )

    def introduce(self):

        print("Hi, my name is", self.name)
        print("I am", self.age, "years old.")
        print(
            "I manage the",
            self.department,
            "department"
        )