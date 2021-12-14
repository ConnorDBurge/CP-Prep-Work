from account import Account
from bank import Bank
import unittest


class BankAccountsTest(unittest.TestCase):

    def test_account_creation(self):
        '1. Test Account() creation'
        self.assertIsInstance(Account(), Account)

    def test_bank_creation(self):
        '2. Test Bank() creation'
        self.assertIsInstance(Bank(), Bank)


if __name__ == '__main__':
    unittest.main()
