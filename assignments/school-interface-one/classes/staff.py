import csv
import os
from classes.person import Person


class Staff(Person):

    @classmethod
    def all_staff(cls):
        # get path to classes/
        my_path = os.path.abspath(os.path.dirname(__file__))
        # join path to classes/
        path = os.path.join(my_path, "../data/staff.csv")
        staff_list = list()  # empty list to store all staff
        with open(path) as csvfile:
            # create a dictionary for each staff
            dict_staff = csv.DictReader(csvfile)
            # for each staff create Staff object
            for staff in dict_staff:
                new_staff = Staff(**staff)  # pass kwargs
                staff_list.append(new_staff)  # append Staff object
        return staff_list  # return list of Staff objects

    def __init__(self, name, age, role, employee_id, password):
        super().__init__(name, age, role, password)
        self.employee_id = employee_id
