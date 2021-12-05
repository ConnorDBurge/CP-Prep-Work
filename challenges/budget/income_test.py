from classes.components.income import Income
import unittest


class IncomeTest(unittest.TestCase):

    def test_return_type(self):
        received = Income()
        self.assertIsInstance(received, Income)

    def test_income_dict(self):
        income = Income()
        income.increase_income('Salary 1', '1317')
        income.increase_income('Salary 2', '1000')
        expected = {'Salary 1': 1317, 'Salary 2': 1000}
        self.assertEqual(income.income_dict, expected)

    def test_increase_income(self):
        income = Income()
        income.increase_income('Salary 1', '1317')
        expected = {'Salary 1': 1317}
        self.assertEqual(income.income_dict, expected)

    def test_reduce_income(self):
        income = Income()
        income.increase_income('Salary 1', '1317')
        income.reduce_income('Salary 1', '317')
        expected = {'Salary 1': 317}
        self.assertEqual(income.income_dict, expected)

    def test_return_total_income(self):
        income = Income()
        income.increase_income('Salary 1', '2000')
        income.reduce_income('Salary 1', '1000')
        expected = 1000
        self.assertEqual(income.total_income, expected)


if __name__ == '__main__':
    unittest.main()
