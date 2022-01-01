from classes.person import Person


class Staff(Person):

    def __init__(self, name, age, role, password, id):
        super().__init__(name, age, role, password, id)
