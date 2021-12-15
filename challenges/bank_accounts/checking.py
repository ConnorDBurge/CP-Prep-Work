from account import Account
from datetime import datetime


class Checking(Account):

    def __init__(self, type, owner, balance=None, id=None, open_date=None):
        self.id = id if id is not None else self._create_id()
        self.last_five = self._last_five(self.id)
        self.open_date = open_date if open_date is not None else datetime.now().date()
        self.balance = int(
            balance if balance is not None else self.deposit(balance))
        self.owner = owner
        self.type = type
        Account.accounts[self.id] = self
        Account.account_ids.append(self.last_five)

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
