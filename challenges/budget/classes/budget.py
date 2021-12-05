from classes.component import Category


class Budget:

    def __init__(self, month):
        self.month = month
        self.income = None
        self.expenses = {}

    def increse_transaction(self, category, name, amount):
        if category == 'income':
            if self.income is None:
                self.income = Category(category)
            return self.income.increase(name, amount)

        if category not in self.expenses:
            self.expenses[category] = Category(category)
        self.expenses[category].increase(name, amount)

    def reduce_transaction(self, category, name, amount):
        if category == 'income':
            if self.income is None:
                self.income = Category(category)
            return self.income.reduce(name, amount)

        if category not in self.expenses:
            self.expenses[category] = Category(category)
        self.expenses[category].reduce(name, amount)

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
