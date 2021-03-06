from classes.school import School


class SchoolInterface:

    def __init__(self, school_name):
        self.school = School(school_name)

    def run(self):
        while True:
            self.authenticate_user()
            mode = self.menu()

            if mode == '1':
                self.school.list_students()

            elif mode == '2':
                student_id = input('\nEnter student id: ')
                self.school.find_student_by_id(student_id)

            elif mode == '3':
                student_data = self.school.get_student_info()
                self.school.add_student(student_data)

            elif mode == '4':
                student_id = input('Enter student id: \n')
                self.school.delete_student(student_id)

            elif mode == '5':
                break

    def menu(self):
        return input("\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit\n")

    def authenticate_user(self):
        print(
            f'\nWelcome to {self.school.name}\n-----------------------------------')

        ids = self.school.return_staff_ids()
        attempts = 0
        while True:
            attempts += 1
            id = input('Please enter a valid employee id:\n')
            if id in ids:
                attempts = 0
                break
            elif attempts == 3:
                exit('Attempt limit reached')

        employee = self.school.find_employee_by_id(id)
        while True:
            attempts += 1
            password = input('Please enter a valid password:\n')
            if password == employee.password:
                break
            elif attempts == 3:
                exit('Attempt limit reached')
