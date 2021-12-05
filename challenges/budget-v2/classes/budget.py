from classes.category import Category
import csv
import os


class Budget:
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "data/transactions.csv")

    def __init__(self, month):
        self.month = month
        self.categories = list()
        self.load_transactions()

    def load_transactions(self):
        with open(self.path) as file:
            reader = csv.DictReader(file)
            for line in reader:
                self.transaction(**line)

    def new_transaction(self, category, name, amount):
        transaction = self.transaction(category, name, amount)
        fields = ['category_name', 'name', 'amount']
        with open(self.path, 'a+', newline='') as file:
            writer = csv.DictWriter(file, fields)
            writer.writerow(transaction.__dict__)

    def transaction(self, category_name, name, amount):
        for category in self.categories:
            if category.category_name == category_name:
                return category.transaction(name, amount)

        else:
            new_category = Category(category_name)
            self.categories.append(new_category)
            return new_category.transaction(name, amount)

    def get_income(self):
        for category in self.categories:
            if category.category_name == 'income':
                return category.total

    def get_expenses(self):
        expenses = 0
        for category in self.categories:
            if category.category_name != 'income':
                expenses += category.total
        return expenses

    def get_remaining(self):
        return self.get_income() - self.get_expenses()

    def get_percentage(self, category):
        return category.total / self.get_income()

    def __str__(self):
        string = f'\n{self.month.upper() + " BUDGET"}' + f'\n--------------------------------\n{"INCOME":<22}$ {self.get_income():,.2f}\n{"EXPENSES":<22}' + f'$ {self.get_expenses():,.2f}'.rjust(
            10) + f'\n{"INCOME - EXPENSES":<22}' + f'$ {self.get_remaining():,.2f}'.rjust(10)
        for category in self.categories:
            string += category.str(self.get_percentage(category))
        return string
