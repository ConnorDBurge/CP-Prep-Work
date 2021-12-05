from classes.category import Category


class Budget:

    def __init__(self, month):
        self.month = month
        self.categories = list()

    def transaction(self, category_name, name, amount):
        for category in self.categories:
            if category.name == category_name:
                category.transaction(name, amount)
                break
        else:
            new_category = Category(category_name)
            self.categories.append(new_category)
            new_category.transaction(name, amount)

    def get_income(self):
        for category in self.categories:
            if category.name == 'income':
                return category.total

    def get_expenses(self):
        expenses = 0
        for category in self.categories:
            if category.name != 'income':
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
