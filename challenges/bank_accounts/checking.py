from account import Account
from datetime import datetime
from prompts import Prompts
prompt = Prompts()


class Checking(Account):

    def __init__(self, type, owner, balance=None, id=None, open_date=None):
        self.id = id if id is not None else self._create_id()
        self.last_five = self._last_five(self.id)
        self.open_date = open_date if open_date is not None else datetime.now().date()
        self.balance = int(
            balance if balance is not None else self.deposit(balance))
        self.owner = owner
        self.type = type
        self.checks_written = 0
        Account.accounts[self.id] = self
        Account.account_ids.append(self.last_five)

    def withdraw(self, amount):
        amount += 1  # $1.00 dollar fee
        try:
            if self.get_balance() - amount < 0:
                raise ValueError
            else:
                self.balance -= amount
                print(f'\nNew Balance: ${self.get_balance():,.2f}\n')
        except ValueError:
            print('\nInsufficient funds to withdraw.')
        return self.get_balance()

    def withdraw_using_check(self):
        print(f'Check Written: {self.checks_written}\n')
        fee = 0
        if self.checks_written >= 3:
            print('$2.00 fee added.\n')
            fee = 2  # $2.00 dollar fee
        amount = int(prompt.check()) + fee
        self.checks_written += 1
        if self.get_balance() - amount < -10:
            self.balance = -10
        else:
            self.balance -= amount
        print(f'\nNew Balance: ${self.get_balance():,.2f}\n')
        return self.get_balance()

    def reset_checks(self):
        self.checks_written = 0
        return self.checks_written
