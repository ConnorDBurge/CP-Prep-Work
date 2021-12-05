from classes.budget import Budget

budget = Budget('December')
budget.transaction('bills', 'Netflix', '4.99')

for transaction in budget.transactions:
    print(transaction.__dict__)

print(str(budget))
