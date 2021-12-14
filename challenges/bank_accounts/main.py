from owner import Owner

owner = Owner('Burge', 'Connor', '931 Dogwood Lane',
              'Peachtree City', 'Georgia')
new_account = {
    'id': 12345678912345678,
    'balance': 600,
    'open_date': '2021-12-14',
    'type': 'Savings'
}
owner.new_account(new_account)
for account in owner.accounts.values():
    print(account.id)
    print(account.last_five)
    print(account.open_date)
    print(account.balance)
    print(account.type)
