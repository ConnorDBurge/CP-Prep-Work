from classes.component import Component


class Budget:

    def __init__(self, month):
        self.month = month
        self.income = Component('income')
        self.bills = Component('bills')
        self.food = Component('food')
        self.health = Component('health')
        self.lifestyle = Component('lifestyle')
        self.personal = Component('personal')
        self.transportation = Component('transportation')

    def increse_transaction(self, category, name, amount):
        if category == 'income':
            self.income.increase(name, amount)
        elif category == 'bills':
            self.bills.increase(name, amount)

    def reduce_transaction(self, category, name, amount):
        if category == 'income':
            self.income.reduce(name, amount)
        elif category == 'bills':
            print('hit')
            self.bills.reduce(name, amount)

    def list_transactions(self, category):
        if category == 'income':
            print(str(self.income))
        elif category == 'bills':
            print(str(self.bills))

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
        string = f'\n{self.month.upper():<21}\n{"INCOME":<21}$ {self.income.total:,.2f}\n{"EXPENSES":<21}$ {self.total_expenses():,.2f}\n{"INCOME - EXPENSES":<21}$ {self.get_remaining():,.2f}'
        for expense in expenses:
            string += str(expense)
        return string
