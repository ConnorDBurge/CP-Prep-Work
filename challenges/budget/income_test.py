from classes.components.income import Income
import unittest


class IncomeTest(unittest.TestCase):

    def test_return_type(self):
        received = Income()
        self.assertIsInstance(received, Income)

    def test_create_income(self):
        income = Income()
        income.add_new_income('Salary 1', '1317')

    def test_income_dict(self):
        income = Income()
        income.add_new_income('Salary 1', '1317')
        income.add_new_income('Salary 2', '1000')
        expected = {'Salary 1': 1317, 'Salary 2': 1000}
        self.assertEqual(income.income_dict, expected)

    def test_change_income(self):
        income = Income()
        income.add_new_income('Salary 1', '1317')
        income.change_income('Salary 1', '2000')
        expected = {'Salary 1': 2000}
        self.assertEqual(income.income_dict, expected)


if __name__ == '__main__':
    unittest.main()
