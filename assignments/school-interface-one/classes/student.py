from classes.person import Person


class Student(Person):

    def __init__(self, name, age, role,  password, school_id):
        super().__init__(name, age, role, password)
        self.school_id = school_id

    @classmethod
    def all_students(cls):
        # return list of Student objects
        return Student.create_people('students.csv')
