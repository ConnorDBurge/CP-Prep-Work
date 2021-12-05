from classes.budget import Budget
from classes.components.income import Income
from classes.components.bills import Bill
from classes.components.food import Food
from classes.components.health import Health
from classes.components.lifestyle import Lifestyle
from classes.components.personal import Personal
from classes.components.savings import Savings
from classes.components.transportation import Transportion

import unittest


class TestBudget(unittest.TestCase):

    def test_return_type(self):
        received = Budget('December')
        self.assertIsInstance(received, Budget)

    def test_month_name(self):
        received = Budget('December')
        self.assertEqual(received.month, 'December')

    def test_return_type_income(self):
        received = Budget('December')
        self.assertIsInstance(received.income, Income)

    def test_return_income_dict(self):
        received = Budget('December')
        received.income.increase_income('Salary 1', '1317')
        received.income.reduce_income('Salary 1', 1000)
        expected = {'Salary 1': 1000}
        self.assertEqual(received.income.income_dict, expected)

    def test_return_type_bill(self):
        received = Budget('December')
        self.assertIsInstance(received.bills, Bill)

    def test_return_type_food(self):
        received = Budget('December')
        self.assertIsInstance(received.food, Food)

    def test_return_type_Health(self):
        received = Budget('December')
        self.assertIsInstance(received.health, Health)

    def test_return_type_lifestyle(self):
        received = Budget('December')
        self.assertIsInstance(received.lifestyle, Lifestyle)

    def test_return_type_personal(self):
        received = Budget('December')
        self.assertIsInstance(received.personal, Personal)

    def test_return_type_savings(self):
        received = Budget('December')
        self.assertIsInstance(received.savings, Savings)

    def test_return_type_transportation(self):
        received = Budget('December')
        self.assertIsInstance(received.transportation, Transportion)


if __name__ == '__main__':
    unittest.main()
