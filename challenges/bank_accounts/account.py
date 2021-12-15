from random import randint
from datetime import datetime
import os
import csv


class Account:
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, 'data/account.csv')
    accounts = {}
    account_ids = []

    def __init__(self, type, owner, balance=None, id=None, open_date=None):
        self.id = id if id is not None else self._create_id()
        self.last_five = self._last_five(self.id)
        self.open_date = open_date if open_date is not None else datetime.now().date()
        self.balance = int(balance if balance is not None else self.deposit(
            balance))
        self.owner = owner
        self.type = type
        Account.accounts[self.id] = self
        Account.account_ids.append(self.last_five)

    def __str__(self):
        return f'{self.owner}-A{self.last_five} {self.type}: ${self.get_balance():,.2f}'

    def __repr__(self):
        return f'{self.owner}-A{self.last_five} {self.type}: ${self.get_balance():,.2f}'

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
        except ValueError:
            return 'Deposit must be positive.'
        return self.get_balance()

    def withdraw(self, amount):
        try:
            if self.get_balance() - amount < 0:
                raise ValueError
            else:
                self.balance -= amount
        except ValueError:
            return 'Insufficient funds to withdraw.'
        return self.get_balance()

    # retrun account balance
    def get_balance(self):
        return self.balance

    @classmethod
    def load_accounts(cls):
        with open(cls.path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['id'] in cls.account_ids:
                    continue
                Account(**row)
