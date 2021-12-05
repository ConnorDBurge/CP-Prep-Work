from classes.component import Category


class Budget:

    def __init__(self, month):
        self.month = month
        self.income = Category('income')
        self.bills = Category('bills')
        self.food = Category('food')
        self.health = Category('health')
        self.lifestyle = Category('lifestyle')
        self.personal = Category('personal')
        self.transportation = Category('transportation')

    def increse_transaction(self, category, name, amount):
        if category == 'income':
            self.income.increase(name, amount)
        elif category == 'bills':
            self.bills.increase(name, amount)
        elif category == 'food':
            self.food.increase(name, amount)
        elif category == 'health':
            self.health.increase(name, amount)
        elif category == 'personal':
            self.personal.increase(name, amount)
        elif category == 'transportation':
            self.transportation.increase(name, amount)

    def reduce_transaction(self, category, name, amount):
        if category == 'income':
            self.income.reduce(name, amount)
        elif category == 'bills':
            self.bills.reduce(name, amount)
        elif category == 'food':
            self.food.reduce(name, amount)
        elif category == 'health':
            self.health.reduce(name, amount)
        elif category == 'personal':
            self.personal.reduce(name, amount)
        elif category == 'transportation':
            self.transportation.reduce(name, amount)

    def total_expenses(self):
        total_expenses = 0
        expenses = [
            self.bills,
            self.food,
            self.health,
            self.lifestyle,
            self.personal,
            self.transportation
        ]
        for expense in expenses:
            total_expenses += expense.total
        return total_expenses

    def get_remaining(self):
        remaining = self.income.total - self.total_expenses()
        return remaining

    def __str__(self):
        expenses = [
            self.bills,
            self.food,
            self.health,
            self.lifestyle,
            self.personal,
            self.transportation
        ]
        string = f'\n{self.month.upper() + " BUDGET":<21}\n--------------------------------\n{"INCOME":<21}$ {self.income.total:,.2f}\n{"EXPENSES":<21}$ {self.total_expenses():,.2f}\n{"INCOME - EXPENSES":<21}$ {self.get_remaining():,.2f}'
        for expense in expenses:
            percent = expense.total / self.income.total
            string += expense.str(percent)
        return string
