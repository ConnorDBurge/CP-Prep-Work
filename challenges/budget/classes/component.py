class Category:

    def __init__(self, category):
        self.category = category
        self.dict = {}
        self.total = 0

    def transaction(self, name, amount):
        self.dict[name] = int(amount)
        self.total = self.sum()
        return self.total

    def sum(self):
        sum = 0
        for item in self.dict.values():
            sum += item
        return sum

    def str(self, percent):
        string = f'\n--------------------------------\n{self.category.upper() + f" - {percent:.0%}":<22}' + \
            f'$ {self.total:,.2f}'.rjust(10)
        for name, amount in self.dict.items():
            string += f'\n{name:<22}' + f'$ {amount:,.2f}'.rjust(10)
        return string
