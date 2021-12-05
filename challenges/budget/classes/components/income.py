from .component import Component


class Income(Component):

    def __init__(self):
        self.income_dict = {}

    def add_new_income(self, name, amount):
        self.income_dict[name] = int(amount)

    def change_income(self, name, amount):
        self.income_dict[name] = int(amount)

    def get_income_list(self):
        for name, amount in self.income_dict.items():
            print(f'{name}: {amount}')
        return self.income_dict
