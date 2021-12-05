from classes.budget import Budget

import unittest


class TestBudget(unittest.TestCase):

    def test_return_type(self):
        received = Budget('December')
        self.assertIsInstance(received, Budget)

    def test_month_name(self):
        received = Budget('December')
        self.assertEqual(received.month, 'December')

    def test_return_income_dict(self):
        budget = Budget('December')
        budget.increse_transaction('income', 'Salary 1', '1317')
        budget.increse_transaction('income', 'Salary 2', '1000')
        budget.reduce_transaction('income', 'Salary 1', '317')
        expected = {'Salary 1': 317, 'Salary 2': 1000}
        self.assertEqual(budget.income.dict, expected)

    def test_return_bill_dict(self):
        budget = Budget('December')
        budget.increse_transaction('bills', 'Cox', '178')
        budget.increse_transaction('bills', 'Verizon', '103')
        expected = {'Cox': 178, 'Verizon': 103}
        self.assertEqual(budget.bills.dict, expected)


if __name__ == '__main__':
    unittest.main()
