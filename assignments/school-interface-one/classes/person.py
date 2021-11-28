import csv


class Person:

    def __init__(self, name, age, role, password):
        self.name = name
        self.age = age
        self.password = password
        self.role = role

    @classmethod
    def create_people(cls, file_name):
        with open(f"data/{file_name}") as csvfile:
            # create a dictionary for each person
            dict_people = csv.DictReader(csvfile)
            person_list = list()  # empty list to store all people
            # for each person create Person object
            for person in dict_people:
                new_person = cls(**person)  # pass kwargs
                person_list.append(new_person)  # append Person object
            return person_list  # return list of Person objects
