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
                print(str(student))
                return student

    def get_student_info(self):
        # dictionary to hold the student data
        student_data = {'role': 'student'}
        student_data['name'] = input('Enter student name:\n')
        student_data['age'] = input('Enter student age: \n')
        student_data['password'] = input('Enter student password: \n')
        student_data['id'] = input('Enter student school id: \n')
        return student_data

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

    def return_staff_ids(self):
        return list(map(lambda staff: staff.id, self.staff))

    def find_employee_by_id(self, id):
        for employee in self.staff:
            if employee.id == id:
                return employee
