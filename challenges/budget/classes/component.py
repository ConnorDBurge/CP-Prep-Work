class Component:

    def __init__(self, category):
        self.category = category
        self.dict = {}
        self.total = 0

    def increase(self, name, amount):
        self.dict[name] = int(amount)
        self.total += int(amount)
        return self.total

    def reduce(self, name, amount):
        self.dict[name] = int(amount)
        self.total -= int(amount)
        return self.total

    def __str__(self):
        string = f'\n--------------------------------\n{self.category.upper():<21}$ {self.total:,.2f}'
        for name, amount in self.dict.items():
            string += f'\n{name:<21}$ {amount:,.2f}'
        return string
