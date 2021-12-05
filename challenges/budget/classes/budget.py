from classes.component import Category
from classes.transaction import Transaction
import csv
import os


class Budget:

    def __init__(self, month):
        self.month = month
        self.income = Category('income')
        self.expenses = {}
        self.transactions = []
        self.read_transaction_file()

    def read_transaction_file(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "data/transactions.csv")
        with open(path) as file:  # open file
            reader = csv.DictReader(file)
            for line in reader:
                self.transaction(**line)

    def transaction(self, category, name, amount):
        transaction = Transaction(category, name, amount)
        self.transactions.append(transaction)

        if category == 'income':
            return self.income.transaction(name, amount)

        else:
            if category not in self.expenses:
                self.expenses[category] = Category(category)
            self.expenses[category].transaction(name, amount)

    def new_transaction(self, category, name, amount):
        transaction = Transaction(category, name, amount)
        self.transactions.append(transaction)

    def total_expenses(self):
        total_expenses = 0
        for category in self.expenses.values():
            total_expenses += category.total
        return total_expenses

    def get_remaining(self):
        remaining = self.income.total - self.total_expenses()
        return remaining

    def __str__(self):
        string = f'\n{self.month.upper() + " BUDGET"}' + f'\n--------------------------------\n{"INCOME":<22}$ {self.income.total:,.2f}\n{"EXPENSES":<22}' + \
            f'$ {self.total_expenses():,.2f}'.rjust(
                10) + f'\n{"INCOME - EXPENSES":<22}' + f'$ {self.get_remaining():,.2f}'.rjust(10)
        for category in self.expenses.values():
            percent = category.total / self.income.total
            string += category.str(percent)
        return string
