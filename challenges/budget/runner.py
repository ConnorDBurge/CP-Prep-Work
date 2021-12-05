from classes.budget import Budget

budget = Budget('December')
budget.new_transaction('bills', 'Netflix', '4')

for transaction in budget.transactions:
    print(transaction.__dict__)

print(str(budget))
