from random import randint
import os
import csv


class Account:
    my_path = os.path.abspath(os.path.dirname(__file__))
    account_path = os.path.join(my_path, 'data/account.csv')
    a_o_path = os.path.join(my_path, 'data/account_owners.csv')
    accounts = {}
    account_ids = []

    def __str__(self):
        return f'{self.owner}-{self.type[0]}{self.last_five}: ${self.get_balance():,.2f}'

    # create 17 digit account number
    def _create_id(self):
        range_start = 10**(17 - 1)
        range_end = (10**17)-1
        return randint(range_start, range_end)

    # creates last five of account number reversed
    def _last_five(self, id):
        return str(id)[-5:]  # extract last 5 digits

    def deposit(self, amount):
        try:
            if amount < 0:
                raise ValueError
            if self.balance is None:
                self.balance = amount
            else:
                self.balance += amount
            print(f'\nNew Balance: ${self.get_balance():,.2f}\n')
        except ValueError:
            print('\nDeposit must be positive.')
        return self.get_balance()

    def withdraw(self, amount):
        try:
            if self.get_balance() - amount < 0:
                raise ValueError
            else:
                self.balance -= amount
                print(f'\nNew Balance: ${self.get_balance():,.2f}\n')
        except ValueError:
            print('\nInsufficient funds to withdraw.')
        return self.get_balance()

    # retrun account balance
    def get_balance(self):
        return self.balance

    @classmethod
    def save(cls):
        with open(cls.account_path, 'w') as f:
            fields = ['id', 'owner', 'balance', 'open_date', 'type']
            writer = csv.DictWriter(f, fields)
            writer.writeheader()
            for account in cls.accounts.values():
                account_info = {
                    'id': account.id,
                    'owner': account.owner,
                    'balance': account.balance,
                    'open_date': account.open_date,
                    'type': account.type
                }
                writer.writerow(account_info)
        with open(cls.a_o_path, 'w') as f:
            fields = ['account_id', 'owner_id']
            writer = csv.DictWriter(f, fields)
            writer.writeheader()
            for account in cls.accounts.values():
                account_info = {
                    'account_id': account.id,
                    'owner_id': account.owner
                }
                writer.writerow(account_info)
