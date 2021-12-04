from classes.staff import Staff
from classes.student import Student


class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.read_from_file('staff.csv')  # calls Person
        self.students = Student.read_from_file('students.csv')  # calls Person

    def list_students(self):
        for student in self.students:
            print(f'{student.name} {student.id}')

    def find_student_by_id(self, id):
        for student in self.students:
            if student.id == id:
                return student

    def add_student(self, student_data):
        # adds new student to list of student in School object
        self.students.append(Student(**student_data))
        Student.write_to_file('students.csv', self.students)

    def delete_student(self, id):
        # delete student from list of student in School object
        self.students = list(
            filter(lambda student:  # Student object
                   student.id != id,  # filter
                   self.students))  # list to filter
        Student.write_to_file('students.csv', self.students)
