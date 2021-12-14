from owner import Owner

Owner.load_owners()

for owner in Owner.owners.values():
    print(owner)
print()
for owner in Owner.owners.values():
    for account in owner.accounts.values():
        print(account)
