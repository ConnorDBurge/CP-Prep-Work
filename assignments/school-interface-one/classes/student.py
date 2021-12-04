from classes.person import Person


class Student(Person):

    def __init__(self, name, age, role, password, id):
        super().__init__(name, age, role, password, id)

    def __str__(self):
        return f'\n{self.name.upper()}\n---------------\nage: {self.age}\nid: {self.id}'
