from classes.budget import Budget
import csv
import os


class Budgets:
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "data/transactions.csv")

    def __init__(self):
        self.budgets = {}  # will hold Budget objects
        self.load_transactions()  # loads file

    def load_transactions(self):
        with open(self.path) as file:
            reader = csv.DictReader(file)
            for line in reader:
                self.transaction(**line)

    def write_to_file(self, transaction):
        fields = ['month', 'category_name', 'name', 'amount']
        with open(self.path, 'a+', newline='') as file:
            writer = csv.DictWriter(file, fields)
            writer.writerow(transaction.__dict__)

    def new_transaction(self, month, category_name, name, amount):
        transaction = self.transaction(month, category_name, name, amount)
        self.write_to_file(transaction)

    def transaction(self, month, category_name, name, amount):
        month = month.upper()
        for budget in self.budgets.values():
            if budget.month == month:
                return budget.transaction(month, category_name, name, amount)

        else:
            new_budget = Budget(month)
            self.budgets[month] = new_budget
            return new_budget.transaction(month, category_name, name, amount)

    def change_transaction_name(self, month, category_name, name, new_name):
        month = month.upper()
        for budget in self.budgets.values():
            if budget.month == month:
                transaction = budget.change_transaction_name(
                    category_name, name, new_name)
        self.write_to_file(transaction)
