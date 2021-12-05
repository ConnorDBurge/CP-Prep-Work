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

    def add_new_income(self, name, amount):
        self.income.add_new_income(name, amount)
        return self.income

    def add_new_expense(self, category):
        pass

    def get_monthly_expenses(self, category=None):
        pass
