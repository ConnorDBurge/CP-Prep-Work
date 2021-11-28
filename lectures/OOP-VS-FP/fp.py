import random

tom_account = {
    'name': 'Tom',
    'current_balance': 100,
    'account_number': random.randint(0, 999)
}


def get_balance(account):
    return account['current_balance']


def deposit(account, amount):
    account['current_balance'] += amount


def deposit(account, amount):
    account['current_balance'] -= amount


print(get_balance(tom_account))
print(deposit(tom_account, 100))
print(get_balance(tom_account))
