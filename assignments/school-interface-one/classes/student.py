import csv
import os
from classes.person import Person


class Student(Person):

    @classmethod
    def all_students(cls):
        # get path to classes/
        my_path = os.path.abspath(os.path.dirname(__file__))
        # join path to classes/
        path = os.path.join(my_path, "../data/students.csv")
        student_list = list()  # empty list to store all students
        with open(path) as csvfile:
            # create a dictionary for each student
            dict_students = csv.DictReader(csvfile)
            # for each student create Student object
            for student in dict_students:
                new_student = Student(**student)  # pass kwargs
                student_list.append(new_student)  # append Student object
        return student_list  # return list of Student objects

    def __init__(self, name, age, role, school_id, password):
        super().__init__(name, age, role, password)
        self.school_id = school_id
