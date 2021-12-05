from classes.budget import Budget

budget = Budget('December')

budget.increse_transaction('income', 'Salary 1', '2000')
budget.increse_transaction('income', 'Salary 2', '1317')

budget.increse_transaction('bills', 'Cox', '178')
budget.increse_transaction('bills', 'Verizon', '103')

print(str(budget))
