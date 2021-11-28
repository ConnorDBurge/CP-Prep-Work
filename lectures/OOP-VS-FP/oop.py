# Class - Account
# name
# current_balance
# account_number

# Methods - Account
# withdraw()
# get_balance()
# deposit()
# transfer()
import random


class Account:

    def __init__(self, name, current_balance=0):
        self.name = name
        self.current_balance = current_balance
        self.account_number = random.randint(0, 999)

    def get_balance(self):
        print(f'Balance: ${self.current_balance}')

    def withdraw(self, amount):
        self.current_balance -= amount

    def deposit(self, amount):
        self.current_balance += amount

    def transfer(self, amount, other):
        self.current_balance -= amount
        other.current_balance += amount


tom_account = Account('Connor Burge', 500)
tom_account.get_balance()
tom_account.deposit(60)
tom_account.get_balance()
