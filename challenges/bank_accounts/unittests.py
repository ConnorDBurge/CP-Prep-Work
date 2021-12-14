from account import Account
from owner import Owner
from bank import Bank
import unittest


class AccountsTests(unittest.TestCase):

    def test_account_creation(self):
        '1. Test Account() creation'
        self.assertIsInstance(Account(), Account)

    def test_account_number(self):
        '2. Test Account._create_account_number()'
        account = Account()
        self.assertEqual(len(str(account.id)), 17)

    def test_account_number_last_five(self):
        '3. Test Account._last_five()'
        account = Account()
        last_five = account._last_five(6898552712200517)
        self.assertEqual(last_five, 71500)

    def test_account_balance_1(self):
        '4. Test account.balance()'
        account = Account()
        self.assertEqual(account.get_balance(), 0)

    def test_account_balance_2(self):
        '5. Test account.balance()'
        account = Account('Savings', 10000)
        self.assertEqual(account.get_balance(), 10000)

    def test_account_balance_3(self):
        '6. Test account.balance()'
        account = Account('Savings', 10000)
        account.withdraw(500)
        self.assertEqual(account.get_balance(), 9500)


class OwnerTestCase(unittest.TestCase):

    def test_owner_creation(self):
        '1. Test Owner() creation'
        self.assertIsInstance(Owner(), Owner)

    def test_owner_init_balance_valid(self):
        '2. Test init owner balance'
        owner = Owner()
        owner.new_account('Savings')
        savings_account = owner.accounts['Savings']
        self.assertEqual(savings_account.get_balance(), 0)


class BankTests(unittest.TestCase):
    def test_bank_creation(self):
        '1. Test Bank() creation'
        self.assertIsInstance(Bank(), Bank)


if __name__ == '__main__':
    unittest.main()
