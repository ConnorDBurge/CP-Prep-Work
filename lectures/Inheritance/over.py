class Food:
    def __init__(self, name):
        self.name = name


class Donut(Food):
    def __init__(self, name, flavor):
        super().__init__(name)
        self.flavor = flavor


f = Food('Chips')
d = Donut('Donut', 'Lemon')
