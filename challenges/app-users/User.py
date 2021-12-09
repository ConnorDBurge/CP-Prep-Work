# your User class goes here
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


connor = User('Connor', 'connor.burge@gmail.com', '123456789')
print(User.users)
