from .component import Component
from functools import reduce


class Income(Component):

    def __init__(self):
        self.income_dict = {}
        self.total_income = 0

    def increase_income(self, name, amount):
        self.income_dict[name] = int(amount)
        self.total_income += int(amount)

    def reduce_income(self, name, amount):
        self.income_dict[name] = int(amount)
        self.total_income -= int(amount)

    def get_income_list(self):
        for name, amount in self.income_dict.items():
            print(f'{name}: {amount}')
        return self.income_dict
