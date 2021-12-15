from account import Account
from savings import Savings
from checking import Checking
from random import randint
import os
import csv


class Owner:
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, 'data/owner.csv')
    owners = {}
    owner_ids = []

    def __init__(self, last_name, first_name, street, city, state, id=None):
        self.id = id if id is not None else self._create_id()
        self.last_name = last_name
        self.first_name = first_name
        self.street = street
        self.city = city
        self.state = state
        self.accounts = {}
        Owner.owners[str(self.id)] = self
        Owner.owner_ids.append(self.id)

    def __str__(self):
        string = f'{str(self.id)} - {self.last_name}, {self.first_name}: '
        for account in self.accounts.values():
            string += f'{account.type}: {account.last_five} '
        return string

    def _create_id(self):  # returns 10 digtit owner id
        range_start = 10**(10 - 1)
        range_end = (10**10)-1
        return randint(range_start, range_end)

    def new_account(self, account_info):
        try:
            if int(account_info['balance']) < 0:
                raise ValueError()
            account_info['owner'] = self.id  # attach owner id to account
            if account_info['type'] == 'Savings':
                balance = Savings.validate_balance(
                    int(account_info['balance']))
                account_info['balance'] = balance
                account = Savings(**account_info)
            elif account_info['type'] == 'Checking':
                account = Checking(**account_info)
            # add account to owners dict()
            self.accounts[account.last_five] = account
            return account
        except ValueError:
            print('\nInitial deposit must be positive\n')

    @classmethod
    def load_owners(cls):
        with open(cls.path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['id'] in cls.owner_ids:
                    continue
                Owner(**row)
        cls.load_accounts()
        cls._attach_accounts()
        return Owner.owners

    @classmethod
    def load_accounts(cls):
        with open(Account.account_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['id'] in Account.account_ids:
                    continue
                if row['type'] == 'Savings':
                    Savings(**row)
                elif row['type'] == 'Checking':
                    Checking(**row)

    @classmethod
    def _attach_accounts(cls):
        for owner in Owner.owners.values():
            for account in Account.accounts.values():
                if account.owner == owner.id:
                    if account.last_five not in owner.accounts:
                        owner.accounts[account.last_five] = account
                    else:
                        existing = owner.accounts[account.last_five]
                        print(f'\n{account.type} account ending with {account.last_five} could not be attached to {owner.last_name}, {owner.first_name}.\nAn account labled {account.type} already exist ending with {existing.last_five}\n')

    @classmethod
    def save(cls):
        with open(cls.path, 'w') as f:
            fields = ['id', 'last_name', 'first_name',
                      'street', 'city', 'state']
            writer = csv.DictWriter(f, fields)
            writer.writeheader()
            for owner in cls.owners.values():
                owner_info = {
                    'id': owner.id,
                    'last_name': owner.last_name,
                    'first_name': owner.first_name,
                    'street': owner.street,
                    'city': owner.city,
                    'state': owner.state
                }
                writer.writerow(owner_info)
