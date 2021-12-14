from account import Account
from random import randint


class Owner:

    def __init__(self, last_name='', first_name='', street='', city='', state=''):
        self.id = self._create_id()
        self.last_name = last_name
        self.first_name = first_name
        self.street = street
        self.city = city
        self.state = state
        self.accounts = {}

    def _create_id(self):
        range_start = 10**(10 - 1)
        range_end = (10**10)-1
        return randint(range_start, range_end)

    def new_account(self, account_info):
        try:
            if account_info['balance'] < 0:
                raise ValueError()
            account = Account(**account_info)
            self.accounts[type] = account
            Account.accounts.append(account)
        except ValueError:
            print('Initial deposit must be positive')

    def show_accounts(self):
        print(self.accounts)
