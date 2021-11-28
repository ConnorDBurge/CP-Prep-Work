from classes.staff import Staff
from classes.student import Student


class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.all_staff()
        self.students = Student.all_students()

    def list_students(self):
        for student in self.students:  # for each Student object
            print(f'{student.name} {student.school_id}')

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.school_id == student_id:
                return student
