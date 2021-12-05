from .components.income import Income
from .components.bills import Bill
from .components.food import Food
from .components.health import Health
from .components.lifestyle import Lifestyle
from .components.personal import Personal
from .components.savings import Savings
from .components.transportation import Transportion


class Budget:

    def __init__(self, month):
        self.month = month
        self.income = Income()
        self.bills = Bill()
        self.food = Food()
        self.health = Health()
        self.lifestyle = Lifestyle()
        self.personal = Personal()
        self.savings = Savings()
        self.transportation = Transportion()
        self.remaining_balance = 0

    def increase_income(self, name, amount):
        self.income.increase_income(name, amount)
        self.remaining_balance += int(amount)
        return self.income

    def reduce_income(self, name, amount):
        self.income.reduce_income(name, amount)
        self.remaining_balance -= (self.remaining_balance - int(amount))
        return self.income

    def add_new_expense(self, category, name, amount):
        switcher = {
            'bill': self.bill.add_new_expense(name, amount),
            'food': self.food.add_new_expense(name, amount),
            'health': self.health.add_new_expense(name, amount),
            'lifestyle': self.lifestyle.add_new_expense(name, amount),
            'personal': self.personal.add_new_expense(name, amount),
            'savings': self.savings.add_new_expense(name, amount),
            'transportation': self.transportation.add_new_expense(name, amount)
        }
        return switcher.get(category)

    def get_monthly_expenses(self, category=None):
        pass
