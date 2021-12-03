def print_name(something):
    print(something.name)


class Human:

    def __init__(self, name, ssn):
        self.name = name
        self.ssn = ssn


class Dog:

    def __init__(self, name, fur_color):
        self.name = name
        self.fur_color = fur_color


ankur = Human('Ankur', '888-44-3333')
ottis = Dog('Ottis', 'Grey')

print_name(ankur)
print_name(ottis)
