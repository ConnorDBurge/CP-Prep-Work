import csv
import os
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "user.csv")


class User:
    users = {}

    def __init__(self, name, email_address, licence_number):
        self.name = name
        self.email_address = email_address
        self. licence_number = licence_number
        User.users[self.email_address] = {
            'name': self.name,
            'licence_number': self.licence_number
        }

    @classmethod
    def get_all_users(cls):
        with open(path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                User(**row)


User.get_all_users()
for user, v in User.users.items():
    print(user, ": ", v)
