from random import randint


class Account:
    accounts = []

    def __init__(self, type='', init_deposit=0):
        self.type = type
        self.account_number = self._create_account_number()
        self.last_five = self._last_five(self.account_number)
        self.balance = None
        self.deposit(init_deposit)

    def __str__(self):
        return f'{self.type}: ${self.get_balance():,.2f}'

    # create 17 digit account number
    def _create_account_number(self):
        range_start = 10**(17 - 1)
        range_end = (10**17)-1
        return randint(range_start, range_end)

    # creates last five of account number reversed
    def _last_five(self, account_number):
        number = str(account_number)[-5:]  # extract last 5 digits
        return int(number[::-1])  # reverse last 5 to retain 0's

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
