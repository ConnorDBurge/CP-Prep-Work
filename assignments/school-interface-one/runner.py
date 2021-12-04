from classes.school import School

school = School('Ridgemont High')


while True:
    mode = input("\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit\n")

    if mode == '1':
        school.list_students()

    elif mode == '2':
        student_id = input('\nEnter student id: ')
        student = school.find_student_by_id(student_id)
        print(str(student))

    elif mode == '3':
        # dictionary to hold the student data
        student_data = {'role': 'student'}
        student_data['name'] = input('Enter student name:\n')
        student_data['age'] = input('Enter student age: \n')
        student_data['password'] = input('Enter student password: \n')
        student_data['id'] = input('Enter student school id: \n')

        # pass dictionary to the database
        school.add_student(student_data)

    elif mode == '4':
        student_id = input('Enter student id: \n')
        school.delete_student(student_id)

    elif mode == '5':
        break

    mode = None
