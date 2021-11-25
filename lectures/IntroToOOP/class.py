class Dog:
    species = 'Canine'  # class attribute
    sound = 'Woof'
    legs = 4
    tail = 4
    mammal = True

    def __init__(self, name, breed):  # constructor
        self.name = name  # instance attribute
        self.breed = breed

    def __str__(self):  # string representation of instance
        return f'I am a dog name {self.name}'

    def species(self):  # instance method
        print(self.sound)

    def __add__(self, other):  # instance + instance
        return self.legs + other.legs

    def __eq__(self, other):  # instance == isinstance
        return self.name == other.name


fido = Dog('Oliver', 'Schnauzer')  # new Dog object
fido.tricks = ['Catcher', 'Rollover']

spot = Dog('Spot', 'Dalmatian')
spot.legs = 3

print(fido + spot)  # invokes __add__
print(fido == spot)  # invokes __eq__
