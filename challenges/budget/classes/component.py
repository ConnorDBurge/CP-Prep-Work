class Category:

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

    def str(self, percent):
        string = f'\n--------------------------------\n{self.category.upper() + f" - {percent:.0%}":<22}' + \
            f'$ {self.total:,.2f}'.rjust(10)
        for name, amount in self.dict.items():
            string += f'\n{name:<22}' + f'$ {amount:,.2f}'.rjust(10)
        return string
