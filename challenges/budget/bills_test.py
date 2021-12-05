from classes.components.bills import Bill
import unittest


class BillsTest(unittest.TestCase):

    def test_return_type(self):
        bills = Bill()
        self.assertIsInstance(bills, Bill)

    def test_add_new_bill(self):
        bills = Bill()
        bills.add_new_bill('Cox', '178')
        expected = {'Cox': 178}
        self.assertEqual(bills.bill_dict, expected)

    def test_create_income(self):
        bills = Bill()
        bills.add_new_bill('Cox', '178')
        bills.reduce_bill('Cox', '130')
        expected = {'Cox': 130}
        self.assertEqual(bills.bill_dict, expected)


if __name__ == '__main__':
    unittest.main()
