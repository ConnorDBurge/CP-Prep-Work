from classes.person import Person


class Staff(Person):

    def __init__(self, name, age, role, password, employee_id,):
        super().__init__(name, age, role, password)
        self.employee_id = employee_id

    @classmethod
    def all_staff(cls):
        # return list of Staff objects
        return Staff.create_people('staff.csv')
