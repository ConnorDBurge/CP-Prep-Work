import csv


class Person:

    def __init__(self, name, age, role, password, id):
        self.name = name
        self.age = age
        self.password = password
        self.role = role
        self.id = id

    @classmethod
    def read_from_file(cls, file_name):
        with open(f"data/{file_name}") as csvfile:
            # create a dictionary for each person
            dict_people = csv.DictReader(csvfile)
            person_list = list()  # empty list to store all people
            # for each person create Person object
            for person in dict_people:
                new_person = cls(**person)  # pass kwargs
                person_list.append(new_person)  # append Person object
            return person_list  # return list of Person objects

    @classmethod
    def write_to_file(cls, file_name, data_list):
        with open(f"data/{file_name}", 'w') as csvfile:
            dict_people = csv.DictWriter(csvfile,
                                         ['name', 'age', 'role', 'id', 'password'])
            dict_people.writeheader()
            for person in data_list:
                dict_people.writerow(person.__dict__)
